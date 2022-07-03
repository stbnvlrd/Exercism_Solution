def transpose(lines):
    
    lines = lines.split("\n")
    max_len = len(max(lines, key=len))
    transposed = [""]*max_len
    for y in range(len(lines)):
        new_line = lines[y]
        if y + 2 <= len(lines):
            while len(new_line) < len(max(lines[y+1:len(lines)], key=len)):
                new_line = new_line + " "
        for x in range(len(new_line)):
                transposed[x] = transposed[x] + new_line[x]
            
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