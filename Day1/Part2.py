from xml.etree.ElementTree import QName


fileReader = open("Day1/Input.txt", "r")
textLines = fileReader.readlines()
fileReader.close()

caloriesCurrentElf = 0
caloriesPerElf = []
sumOfTopThree = 0

for line in textLines:
    calories = line.rstrip()
    if calories == '':
        caloriesPerElf.append(caloriesCurrentElf)
        caloriesCurrentElf = 0
    else:
        caloriesCurrentElf += int(calories)

for i in range(3):
    mostCalories = max(caloriesPerElf)
    sumOfTopThree += mostCalories
    caloriesPerElf.remove(mostCalories)


print("Sum of the three elves with the most calories: %d" % sumOfTopThree)
