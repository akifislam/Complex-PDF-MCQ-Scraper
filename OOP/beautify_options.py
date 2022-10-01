def beautifyOptions(options,hasTable):
    tick = '(cid:1)'
    cross='(cid:2)'

    # print("Original Options : ",options)
    if hasTable==False:
        return options
    else:
        stringToInsert = ""
        for item in range(1,len(options)-1):
            if(str(options[item]).__contains__(tick)):
                stringToInsert += "Right " + "#"
            elif(str(options[item]).__contains__(cross)):
                stringToInsert += "Cross " + "#"
            else:
                stringToInsert += options[item] + "#"

        #Again:
        if (str(options[-1]).__contains__(tick)):
            stringToInsert += "Right"
        elif (str(options[-1]).__contains__(cross)):
            stringToInsert += "Cross"
        else:
            stringToInsert+= str(options[-1])
        # print("Value to Insert : ",stringToInsert)
        return stringToInsert
