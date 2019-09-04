

# converts a timestring from hh:mm:ss format to minutes
def Runtime(timestring):
    '''take a timestring in hh:mm:ss format and convert it to minutes
    input:
    timestring     :     string in hh:mm:ss format
    '''
    timelist = list(map(int, timestring.split(':')))
    return round((timelist[0]*60) + (timelist[1]) + (timelist[2]/60), 2)

#example:
timestring = '02:45:25'

print(Runtime(timestring))

def string_cleaner(dirty_string, swap_dict):
    '''take a string and clean it by replacing parts as directed by the swap_dict dictionary.  This function
        was intended to be mapped or applied over a series or list-like object of strings.
    input:
    dirty_string      :      string that may have substrings to be replaced.
    swap_dict         :      dictionary made of key/value pairs that map unwanted/replacement substrings respectively'''
    for key, value in swap_dict.items():
        dirty_string = dirty_string.lower().replace(key,value).strip()
    return dirty_string



