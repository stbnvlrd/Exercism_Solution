def encode(message, rails):
    lines = [""]*rails
    for index in range(len(message)):
        line_pos = index
        while line_pos >= 2*rails-2:
            line_pos = line_pos - (2*rails - 2)
        if line_pos < rails:
            lines[line_pos] = lines[line_pos] + message[index]
        else:
            lines[rails - line_pos - 2] = lines[rails - line_pos - 2] + message[index]
    return "".join(lines)    


def decode(encoded_message, rails):
    lines = [""]*rails
    # line_length = [0]*rails
    line_repeats = len(encoded_message)//((2*rails) - 2)
    line_length = [line_repeats*2]*rails
    line_length[0] = line_repeats
    line_length[-1] = line_repeats
    line_rest = len(encoded_message)%(2*rails) - 2)
    for index in range(line_rest):
        line_length[index] = line_length[index] + 1
        
    for index in range(len(line_length)):
        if index == 0:
            lines[index] = Encoded_message[0:line_length[index]]
        if index > 0:
            lines[index] = Encoded_message[:line_length[index]]
            line_length[index] = line_length[index] + line_length[index - 1]
            lines[index] = Encoded_message[line_length[index-1]:line_length[index]]
            
    for index in range(len(line_length)):
        lines[index] = Encoded_message[:line_length[index]]
        while line_pos >= 2*rails-2:
            line_pos = line_pos - (2*rails - 2)
        if line_pos < rails - 1:
            lines[line_pos] = lines[line_pos] + encoded_message[index]
        else:
            lines[rails - line_pos - 1] = lines[rails - line_pos - 1] + encoded_message[index]
    return "".join(lines)