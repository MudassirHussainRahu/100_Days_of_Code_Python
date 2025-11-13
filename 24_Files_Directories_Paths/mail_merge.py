with open("Input/Names/invited_names.txt") as file:
    names = file.read()


print(names)

names = names.split("\n")
print(len(names))

with open("Input/Letters/starting_letter.txt") as file:
    letter_lines = file.readlines()

print(letter_lines)

letter_lines[-1] = "LALO\n"

for name in names:
    n = f" Dear {name},\n"
    letter_lines[0] = n
    letter = " ".join(letter_lines)
    with open(f"letters/{name}_letter.txt", "w") as file:
        file.write(letter)

