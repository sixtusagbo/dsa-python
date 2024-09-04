# Use list functions to make this better
numbers = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    try:
        value = float(inp)
        numbers.append(value)
    except ValueError:
        print("Input must be a number")

average = sum(numbers) / len(numbers)

print("Average:", average)
