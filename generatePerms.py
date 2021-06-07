import itertools

firstByteValues = []
middleDwordValues = []
finalByteValues = []

outFile = open("possiblePerms.txt", "w")

firstByteFile = open('firstByte.txt', 'r')
middleDwordFile = open('middleDword.txt', 'r')
finalByteFile = open('finalByte.txt', 'r')

firstByteLines = firstByteFile.readlines()
middleDwordLines = middleDwordFile.readlines()
finalByteLines = finalByteFile.readlines()

for line in firstByteLines:
    firstByteValues.append(line.strip())
for line in middleDwordLines:
    middleDwordValues.append(line.strip())
for line in finalByteLines:
    finalByteValues.append(line.strip())

fullArray = [firstByteValues, middleDwordValues, finalByteValues]
for permutation in list(itertools.product(*fullArray)):
    outFile.write(permutation[0] + " " + permutation[1] + " " +
                  permutation[2] + "\n")

outFile.close()
firstByteFile.close()
middleDwordFile.close()
finalByteFile.close()
