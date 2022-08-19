def beautifyQTABLE(table):
    cur_table_str = ""
    for row in range(0,len(table)-1):
        for each_column in range (0,len(table[row])):
            temp_t = table[row]
            if(each_column!=len(table[row])-1):
                modified_str = temp_t[each_column].replace("\n"," ")
                cur_table_str+=modified_str + "#"
            else:
                modified_str = temp_t[each_column].replace("\n", " ")
                if(row!=len(table)):
                    cur_table_str+=modified_str+"@@\n"
                else:
                    cur_table_str+=modified_str

    #Processing Last Row of QTABLE
    lastRow = table[-1]
    new_temp_options = []
    for item in lastRow:
        new_temp_options.append(item.split("\n"))

    lastRow = new_temp_options
    # print(lastRow)

    for i in range (0,len(lastRow[0])):
        for j in range(0,len(lastRow)):
            if(j==len(lastRow)-1):
                cur_table_str += lastRow[j][i]
                continue
            cur_table_str+=lastRow[j][i]+"#"
        if i!=len(lastRow[0])-1:
            cur_table_str+="@@\n"


    return(cur_table_str)