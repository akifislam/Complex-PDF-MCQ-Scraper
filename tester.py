x = [['', 'biological \nmolecule', 'presence of carboxyl \n(COOH) groups', 'presence of two or more \nhydroxyl (OH) groups'], ['1 \n2 \n3 \n4', 'amino acid \nŒ≤-glucose \nglycerol \nfatty acid', 'yes \nno \nno \nyes', 'no \nyes \nno \nno']]
y = [['type of \nbacteria', 'diameter of zone/mm', None, None, None, None], [None, 'week 1', 'week 2', 'week 3', 'week 4', 'week 5'], ['1 \n2 \n3 \n4 \n5', '24.10 \n18.60 \n17.90 \n19.40 \n22.00', '21.90 \n15.40 \n12.80 \n15.30 \n21.00', '19.00 \n12.20 \n12.40 \n13.20 \n20.50', '17.60 \n9.00 \n11.10 \n8.10 \n20.40', '14.30 \n0.00 \n10.90 \n0.00 \n20.40']]
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
    print(lastRow)

    for i in range (0,len(lastRow[0])):
        for j in range(0,len(lastRow)):
            if(j==len(lastRow)-1):
                cur_table_str += lastRow[j][i]
                continue
            cur_table_str+=lastRow[j][i]+"#"
        if i!=len(lastRow[0])-1:
            cur_table_str+="@@\n"


    return(cur_table_str)
#37
#10
print(beautifyQTABLE(x))

# if(len(cur_options)==1):
#             new_temp_options = []
#             for item in cur_options[0]:
#                 new_temp_options.append(item.split("\n"))
#             # print("New : ", new_temp_options)
#             cur_options = new_temp_options
#
#             new_temp_options = []
#             for ii in range (0,4):
#                 newlist = []
#                 for j in range(0,len(cur_options)):
#                     newlist.append(cur_options[j][ii])
#                 new_temp_options.append(newlist)
#             cur_options = new_temp_options