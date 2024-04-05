list = ["a","b","c","d","e","a"]
found_duplicate = False
for item in list:
    if(list.count(item) > 1):
        print("Duplicate item is",item)
        found_duplicate = True
        break
if not found_duplicate:
    print("No duplicate item in list!")