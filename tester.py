x = ['A ', 'high ', 'high ', 'low ', 'low ']

def beautifyOptions(options,hasTable):
    print("Original Options : ",options)
    if hasTable==False:
        return options
    else:
        stringToInsert = ""
        for item in range(1,len(options)-1):
          stringToInsert +=  options[item] + "#"

        stringToInsert+= str(options[-1])

        return stringToInsert

# print(beautifyOptions(x,True))

headers = "  ,centrioles,cilia,mitochondria,vacuole,"
headers = headers.lstrip().lstrip(',')
print(headers)