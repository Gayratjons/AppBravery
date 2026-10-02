# # Success Classifier -- Linear Regression + Classification
# 
# Trains on `final.csv` (companies with known 2019 revenue, 2026 marketcap, and actual growth %),
# then predicts success tiers for `startup.csv` (companies with only `raised` and `marketcap` --
# **no actual growth is available or invented for these, since we are predicting, not evaluating them**).
# 
# Place `final.csv` and `startup.csv` in the same folder as this notebook before running.
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def to_number(val):
    """Turn '30.3 Million', '$1.2B', '45,000' etc. into a float."""
    if pd.isna(val):
        return np.nan
    if isinstance(val, (int, float)):
        return float(val)
    s = str(val).strip().lower().replace("$", "").replace(",", "").replace("%", "")
    mult = {"k": 1e3, "m": 1e6, "million": 1e6, "b": 1e9, "billion": 1e9, "t": 1e12}
    m = re.match(r"^(-?\d+\.?\d*)\s*([a-z]*)$", s)
    if not m:
        return np.nan
    num, unit = m.groups()
    return float(num) * mult.get(unit, 1)


# ## 1. Load and clean `final.csv`
df = pd.read_csv("final.csv", on_bad_lines="warn", engine="python")
df["revenue_2019"] = df["revenue_2019"].apply(to_number)
df["marketcap_2026"] = df["marketcap_2026"].apply(to_number)
df["growth_%"] = df["growth_%"].apply(to_number).clip(lower=0)
df = df.dropna(subset=["revenue_2019", "marketcap_2026", "growth_%"]).reset_index(drop=True)

df["log_revenue"] = np.log1p(df["revenue_2019"])
df["log_marketcap"] = np.log1p(df["marketcap_2026"])
df["log_growth"] = np.log1p(df["growth_%"])

print(df.shape)
print(df.head())


# ## 2. Linear regression: expected growth % from revenue + marketcap
# 
# Both inputs and the target are heavily right-skewed (companies span orders of magnitude),
# so everything is fit in `log1p` space. `reg.predict(...)` then gets inverted with `np.expm1`
# to turn it back into a plain growth percentage.
reg = LinearRegression()
reg.fit(df[["log_revenue", "log_marketcap"]], df["log_growth"])

pred_log_growth = reg.predict(df[["log_revenue", "log_marketcap"]])
df["expected_growth_%"] = np.expm1(pred_log_growth)
df["growth_fulfillment"] = df["log_growth"] - pred_log_growth       # actual - expected, in log space
df["raw_success_score"] = df["log_marketcap"] - df["log_revenue"]   # marketcap built per $ of revenue

print("R^2:", reg.score(df[["log_revenue", "log_marketcap"]], df["log_growth"]))


# ## 3. Rule-based success tier
# 
# A simple 2x2 grid on the medians of the two scores above:
# raw size (`raw_success_score`) x whether growth beat expectation (`growth_fulfillment`).
raw_med = df["raw_success_score"].median()
fulfill_med = df["growth_fulfillment"].median()

def tier(raw, fulfill):
    if raw >= raw_med and fulfill >= fulfill_med:
        return "Star"
    if raw >= raw_med:
        return "Coasting"
    if fulfill >= fulfill_med:
        return "Rising"
    return "Underperformer"

df["success_tier"] = [tier(r, f) for r, f in zip(df["raw_success_score"], df["growth_fulfillment"])]
print(df["success_tier"].value_counts())


# ## 4. Classifier
# 
# Trained on `log_revenue` and `log_marketcap` only (deliberately **not** on growth) --
# that's the only feature set `startup.csv` can also supply, since it has no actual
# growth number to give the model.
X, y = df[["log_revenue", "log_marketcap"]], df["success_tier"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

clf = RandomForestClassifier(n_estimators=200, max_depth=4, random_state=42)
clf.fit(X_train, y_train)
print("Held-out accuracy:", clf.score(X_test, y_test))

clf.fit(X, y)  # refit on all of final.csv for the version we'll actually use
df.to_csv("final_classified.csv", index=False)


# ## 5. Apply to `startup.csv` -- prediction only, no actual growth
# 
# `raised` stands in for `revenue_2019`, `marketcap` stands in for `marketcap_2026`.
# `expected_growth_%` here is purely the model's output given those two numbers --
# there is no "actual" growth for a startup to compare it against, so no
# fulfillment/residual is computed for this dataset, and none is faked.
startup = pd.read_csv("startup_2025.csv")
startup["raised"] = startup["raised"].apply(to_number)
startup["marketcap"] = startup["marketcap"].apply(to_number)
startup = startup.dropna(subset=["raised", "marketcap"]).reset_index(drop=True)

startup["log_revenue"] = np.log1p(startup["raised"])
startup["log_marketcap"] = np.log1p(startup["marketcap"])

startup["expected_growth_%"] = np.expm1(reg.predict(startup[["log_revenue", "log_marketcap"]]))
startup["raw_success_score"] = startup["log_marketcap"] - startup["log_revenue"]
startup["predicted_success_tier"] = clf.predict(startup[["log_revenue", "log_marketcap"]])

startup.to_csv("startup_classified.csv", index=False)
print(startup[["name", "raised", "marketcap", "expected_growth_%", "predicted_success_tier"]])


# ## 6. Plot 1 -- `final.csv` classification output -> `final_graph-2.png`
TIER_COLORS = {"Star": "#2ca02c", "Coasting": "#ff7f0e", "Rising": "#1f77b4", "Underperformer": "#d62728"}

fig, ax = plt.subplots(figsize=(11, 6.5))

for _, r in df.iterrows():
    ax.plot([r["growth_%"]] * 2, [r["revenue_2019"], r["marketcap_2026"]],
            color="lightgray", linewidth=1, zorder=1)

for t, c in TIER_COLORS.items():
    sub = df[df["success_tier"] == t]
    if len(sub):
        ax.scatter(sub["growth_%"], sub["marketcap_2026"], color=c, s=60, label=t, zorder=2)

if "Symbol" in df.columns:
    for _, r in df.iterrows():
        if pd.notna(r.get("Symbol")):
            ax.annotate(r["Symbol"], (r["growth_%"], r["marketcap_2026"]),
                        textcoords="offset points", xytext=(6, 4), fontsize=8)

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Growth % (log scale)")
ax.set_ylabel("USD (log scale)")
ax.set_title("final.csv -- classification output")
ax.grid(True, which="both", alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig("final_graph-2.png", dpi=150)
plt.show()


# ## 7. Plot 2 -- `startup.csv` classification output -> `startup_graph-2.png`
# 
# Saved as its own separate file. X-axis is the model's **predicted** growth %
# (there's no actual growth % for startups to plot instead).
x_plot = startup["expected_growth_%"].clip(lower=0.01)  # keep strictly positive for the log axis

fig, ax = plt.subplots(figsize=(11, 6.5))

for idx, r in startup.iterrows():
    ax.plot([x_plot[idx]] * 2, [r["raised"], r["marketcap"]],
            color="lightgray", linewidth=1, zorder=1)

for t, c in TIER_COLORS.items():
    sub = startup[startup["predicted_success_tier"] == t]
    if len(sub):
        ax.scatter(x_plot.loc[sub.index], sub["marketcap"], color=c, s=90,
                   marker="*", edgecolor="black", label=t, zorder=2)

for idx, r in startup.iterrows():
    ax.annotate(r["name"], (x_plot[idx], r["marketcap"]),
                textcoords="offset points", xytext=(6, 4), fontsize=8, style="italic")

ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlabel("Model-expected growth % (log scale)")
ax.set_ylabel("USD (log scale)")
ax.set_title("startup.csv -- classification output (predicted only, no actual growth)")
ax.grid(True, which="both", alpha=0.3)
ax.legend()
plt.tight_layout()
plt.savefig("startup_graph-2.png", dpi=150)
plt.show()