import time
from lru_cache import LRUCache

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# runtime for started code is O(n^2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# runtime for solution code is O(n) 
cache = LRUCache(10000)
# add all names from names_1 file to cache
for name in names_1:
    cache.set(name, name)
# compare each name in cache against the names in names_2 file and append matches
for name in names_2:
    if name in cache.storage:
        duplicates.append(name)

# stretch solution using built in python set()

# set_difference = list(set(names_1) & set(names_2))
# for name in set_difference:
#     duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.




