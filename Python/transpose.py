def transpose(lines):
   
    # lines = lines.split("\n")
    for index in range(len(lines)):
        while len(lines(index)) < len(lines(index + 1)):
            new = lines(index) + " "
            lines(index) = new
    transposed = [""]*len(lines[0])
    for y in range(len(lines)):
    	for x in range(len(lines[y])):
            transposed[x] = transposed[x] + lines[y][x]
            
    print(transposed)
    return "\n".join(transposed)

transpose(["A1"])
transpose(["A", "1"])
transpose(["ABC", "123"])
transpose(["Single line."])
transpose(["The fourth line.", "The fifth line."])
transpose(["The first line.", "The second line."])
transpose(["The longest line.", "A long line.", "A longer line.", "A line."])
transpose(["HEART", "EMBER", "ABUSE", "RESIN", "TREND"])