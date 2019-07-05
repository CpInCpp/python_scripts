

# converts a timestring from hh:mm:ss format to minutes
def Runtime(timestring):

    timelist = list(map(int, timestring.split(':')))
    return round((timelist[0]*60) + (timelist[1]) + (timelist[2]/60), 2)

#example:
timestring = '02:45:25'

print(Runtime(timestring))





