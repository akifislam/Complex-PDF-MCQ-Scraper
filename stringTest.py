testList = ['A \nB \nC \nD', 'less turgid \nless turgid \nmore turgid \nmore turgid', 'more negative \nless negative \nless negative \nmore negative']
newTestList = []

print(testList)
for item in testList:
    newTestList.append(item.split("\n"))

print(newTestList)