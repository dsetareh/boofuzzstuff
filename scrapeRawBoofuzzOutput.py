import re

with open('boofuzzoutput.txt', 'r') as file:
    fileStr = file.read().replace('\n', '')

outFile = open("bytes.txt", "w")

byteRegex = r'Transmitted 6 bytes: (\w{2}\s\w{2}\s\w{2}\s\w{2}\s\w{2}\s\w{2})'
byteRead = re.search(byteRegex, fileStr).group(1)
for match in re.finditer(byteRegex, fileStr):
    outFile.write(match.group(1) + "\n")
    print(match.group(1))
outFile.close()