# searches for substrings between two tags in a given string 
# returns all matching substrings
def substringsBetween(str, open, close):
    if (str == None or open == '' or close == ''):
        return []

    if len(str) == 0:
        return []

    substrings = []
    pos = 0

    while (pos < len(str) - len(close)):
        start = str.find(open,pos)
       
        if start < 0:
            break
        
        start += len(open)
        end = str.find(close,start)
        if end < 0:
            break

        substrings.append(str[start:end])
        pos = end + len(close) 

    if (substrings == []):
        return []
    
    return substrings