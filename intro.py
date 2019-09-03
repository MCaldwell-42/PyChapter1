# list

my_list = ["I", "you", "we", "uns", "wir", "du", "ich", "you", "you"]

your_list = ["snap","crackle","pop"]

me = list(["arg", "klarg"]) 
# seems dumb

# dictionary
my_pairs = {
  "name": "Fred",
  "age": 46
}

name = my_pairs["name"]

my_pairs["last"] = "Jones"
# print(my_pairs)
my_pairs["address"] = {"street": "123 Sesame St", "zip": 40503}
# print(my_pairs["address"]["zip"])
# accessing nested shiz

# print("items", my_pairs.items())
#bundles up key-pairs and puts them in a list
# print("values", my_pairs.values())
# only gives the right side values


# print(set(my_pairs))
# gives a list of keys



# for key,value in my_pairs.items():
  # print(f"This came from my_pairs: {value}")
# prints all values as strings

# print(f"Hell, my name is {my_pairs['name']}")

my_set = {"fred", 3, 12, True, "Jones", 3}
# print("set", my_set)
my_list = set()
# only way to make an empty set


my_dupes = [1,2,3,2,4,5,1]
my_dupes = set(my_dupes)
# print(list(my_dupes))


# TUPLES

my_tup = ("1", 1, 3, "Hello", True, 3)
print(my_tup)
# tuples act as "vaults" that cannot be edited only passed

name = "Stebe"
if name is not "Steve":
    print("I feel good")
elif name is "Joe":
    print("Joe is the Kind of the World")
else:
     print("I have a cold")

# Comprehensions
stuff = ["dumb", "shit", "list", "stuff"]

for foo in stuff:
    print(foo.capitalize())

cap_stuff = list(map(lambda foo: foo.capitalize, stuff))

cap_stuff = [ foo.capitalize() for foo in stuff ]

print(cap_stuff)

profile = {
    "name": "Fred",
    "age": 34,
    "address": "123 Sesame St"
}

# for (key, value) in profile.items():
#     print(f"The key is {key}, the value is {value}")

profile_string = [f"The key is {key}. The value is {value}" for key, value in profile.items()]
print(profile_string)