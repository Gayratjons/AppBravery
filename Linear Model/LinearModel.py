import pandas as pd
from functools import reduce
import csv
import matplotlib.pyplot as plt


# REQUIRED_COLUMNS = ["revenue_2019","marketcap_2026"]
# MISSING = {"", "nan", "n/a", "na", "null", "none", "-"}



# # Merging
# files = ["inc5000_2019.csv", "companiesmarketcap.csv"]
# dfs = [pd.read_csv(f) for f in files]
# merged = reduce(lambda l, r: pd.merge(l, r, on="name", how="left"), dfs)
# merged.to_csv("merged_companies.csv", index=False)


# # Filtering
# df = pd.read_csv("merged_companies.csv").drop(columns=["rank_x", "profile", "url",
#                                                        "workers", "previous_workers",
#                                                        "rank_y", "industry", "state",
#                                                        "metro", "city", "country"])
# df.to_csv("filtered.csv", index=False)



# # Preparing for the train and test data
# def has_value(cell):
#     return cell is not None and cell.strip().lower() not in MISSING

# def filter_rows(path, out_path):
#     with open(path, newline="", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         missing_cols = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
#         if missing_cols:
#             raise ValueError(f"Column(s) not found: {missing_cols}. "
#                              f"Available: {reader.fieldnames}")
#         fieldnames = reader.fieldnames
#         kept, total = [], 0
#         for row in reader:
#             total += 1
#             if all(has_value(row[c]) for c in REQUIRED_COLUMNS):
#                 kept.append(row)

#     with open(out_path, "w", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(kept)

#     print(f"Kept {len(kept)} of {total} rows, removed {total - len(kept)}.")


# if __name__ == "__main__":
#     filter_rows("filtered.csv", "file.csv")


def to_number(text):
    """'24.4 Million' -> 24400000.0, '3.5 Billion' -> 3500000000.0"""
    value, unit = str(text).split()
    factor = {"thousand": 1e3, "million": 1e6, "billion": 1e9}[unit.lower()]
    return float(value) * factor

#Plotting the final clensed dataset
df = pd.read_csv("final.csv")
df["revenue_2019"] = df["revenue_2019"].apply(to_number)
df.to_csv("final.csv", index=False)

#df["revenue_usd"] = df["revenue_2019"].apply(to_number)
# fig, ax = plt.subplots(figsize=(11, 6.5))
#
# # Thin gray line joining each company's two dots (revenue -> market cap)
# def plotting():
#     for _, r in df.iterrows():
#         ax.plot([r["growth_%"]] * 2, [r["revenue_usd"], r["marketcap_2026"]],
#                 color="lightgray", linewidth=1, zorder=1)
#
#     ax.scatter(df["growth_%"], df["revenue_usd"], color="red", s=60,
#             label="Revenue 2019", zorder=2)
#     ax.scatter(df["growth_%"], df["marketcap_2026"], color="blue", s=60,
#             label="Market cap 2026", zorder=2)
#
#     # Ticker label next to each market cap dot
#     for _, r in df.iterrows():
#         ax.annotate(r["Symbol"], (r["growth_%"], r["marketcap_2026"]),
#                     textcoords="offset points", xytext=(6, 4), fontsize=8)
#
#     ax.set_xscale("log")
#     ax.set_yscale("log")
#     ax.set_xlabel("Inc. 5000 revenue growth % (log scale)")
#     ax.set_ylabel("USD (log scale)")
#     ax.set_title("2019 revenue vs 2026 market cap, by 2019 growth rate")
#     ax.grid(True, which="both", alpha=0.3)
#     ax.legend()
#
#     plt.tight_layout()
#     plt.savefig("graph.png", dpi=150)
#     plt.show()
#
# plotting()
#
#