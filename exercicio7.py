def to_seconds(hour,minute,second):
    seconds = second
    seconds+= hour * 3600
    seconds+= minute * 60
    return seconds



print(to_seconds(2,40,10))