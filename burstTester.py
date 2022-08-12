import glob
path = '/Users/akifislam/Desktop/QuestionReader/AS  Biology (9700)'
count = 0
for cur_path in glob.glob(path+"/**", recursive = True):
    if(str(cur_path[-18:]).__contains__("ms") and str(cur_path[-18:]).__contains__(".pdf")):
        print(cur_path)
        count+=1

print(count)