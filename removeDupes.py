lines_seen = set()  # holds lines already seen
#outfile = open("possiblePermsNoDupes.txt", "w")
for line in open("possiblePerms.txt", "r"):
    if line not in lines_seen:  # not a duplicate
        print(line)
        # outfile.write(line)
        lines_seen.add(line)
#outfile.close()
