def remove_dups(x):
  return list(dict.fromkeys(x))

mylist = remove_dups(["a", "b", "a", "c", "c"])

print(mylist)