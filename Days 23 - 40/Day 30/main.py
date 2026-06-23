try:
    file = open("data.txt")
    dictionary = {"key": "value"}
    print(dictionary["key1"])
except FileNotFoundError:
    file = open("data.txt", "w")
    file.write("Hi mate")
except KeyError:
    print("Wrong key mate!")