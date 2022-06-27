def slices(series, length):
    if series == [] or series == "":
        raise ValueError("series cannot be empty")
    else:
        if length < 0:
            raise ValueError("slice length cannot be negative")
        elif length == 0:
            raise ValueError("slice length cannot be zero")
        elif length > len(series):
            raise ValueError("slice length cannot be greater than series length")
        else:
            slices = [""]*(len(series) - length + 1)
            for index in range(len(slices)):
                slices[index] = series[index:(index+length)]
    return slices
    
