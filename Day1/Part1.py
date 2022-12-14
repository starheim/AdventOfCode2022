fileReader = open("Day1/Input.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

caloriesCurrentElf = 0
caloriesPerElf = []

for line in textLines:
    calories = line.rstrip()
    if calories == '':
        caloriesPerElf.append(caloriesCurrentElf)
        caloriesCurrentElf = 0
    else:
        caloriesCurrentElf += int(calories)

print("HIghest calorie count: %d" % max(caloriesPerElf))
