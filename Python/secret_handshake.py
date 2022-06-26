def commands(binary_str):
    secret_handshake = []
    if binary_str[0] == "0":
        if binary_str[4] == "1":
            secret_handshake.append("wink")
        if binary_str[3] == "1":
            secret_handshake.append("double blink")
        if binary_str[2] == "1":
            secret_handshake.append("close your eyes")
        if binary_str[1] == "1":
            secret_handshake.append("jump")
    else:
        if binary_str[1] == "1":
            secret_handshake.append("jump")
        if binary_str[2] == "1":
            secret_handshake.append("close your eyes")
        if binary_str[3] == "1":
            secret_handshake.append("double blink")
        if binary_str[4] == "1":
            secret_handshake.append("wink")
    return secret_handshake