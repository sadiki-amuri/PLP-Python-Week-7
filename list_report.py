
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]


print("--- Numbered Items List ---")
for index in range(len(items)):
    print(f"{index + 1}. {items[index]}")

more_than_four_count = 0
for item in items:
    if len(item) > 4:
        more_than_four_count += 1

print(f"\nNumber of items with more than 4 letters: {more_than_four_count}")

longest_name = items[0]
for item in items:
    if len(item) > len(longest_name):
        longest_name = item

print(f"The longest item name is: {longest_name}")
