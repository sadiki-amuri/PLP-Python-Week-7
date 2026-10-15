
fruits = ["Mango", "Banana", "Orange", "Pineapple"]


print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")


fruits.append("Passion")
print(f"List after appending: {fruits}")

fruits.remove("Orange")
print(f"List after removing: {fruits}")

print(f"Number of fruits remaining: {len(fruits)}")
