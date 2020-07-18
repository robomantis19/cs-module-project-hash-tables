# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

commonPercentages = {'a': 8.2, 'b': 1.5, 'c': 2.8, 'd': 4.3,
'e': 12.7, 'f': 2.2, 'g': 2.0, 'h': 6.1, 'i': 7.0, 'j': 0.2, 
'k': 0.8, 'l': 4.0, 'm': 2.4, 'n': 6.7, 'o': 7.5, 'p': 1.9, 
'q': 0.1, 'r': 6.0, 's': 6.3, 't': 9.1, 'u': 2.8, 'v': 1.0, 
'w': 2.4, 'x': 0.2, 'y': 2.0, 'z': 0.1}



file = open('ciphertext.txt', 'r')
arr = []
dictStart={}
for line in file: 
    for i in line: 
        if i not in dictStart: 
            dictStart[i] = 1
        else: 
            count = dictStart[i]
            dictStart[i] = count + 1

print(dictStart)
total = 0
for key1, value1 in dictStart.items():
    total += value1
print('total is: ', total)
for key, value in dictStart.items(): 
    dictStart[key] = round((value/total)*100, 1)

# (key, lambda: x, x[i])
print(dictStart)
sortedDict = {}
sortedArray = []
defaultSA = []
for key3, value3 in dictStart.items():
    
    if key3.isalpha(): 
        if dictStart[key3.upper()] > commonPercentages[key3.lower()]: 
            # diff = dictStart[key3.upper()] - commonPercentages[key3.lower()]
            # sortedDict[key3]= diff
            # print(key3, diff, 'diff')
            # print(key3, value3)
            sortedArray.append(value3)
            print(sortedArray)
            defaultSA.append(commonPercentages[key3.lower()])
sortedDefault = sorted(defaultSA, reverse= True)
sortedArray = sorted(sortedArray, reverse = True)
dictArray =[]
for i in sortedArray: 
    for key, value in dictStart.items(): 
        if dictStart[key] == i: 
            dictArray.append(key)
print('numbers to substitute', dictArray)

dictDefault = []
for i in sortedDefault: 
    for key, value in commonPercentages.items(): 
        if commonPercentages[key] == i: 
            dictDefault.append(key)
print('numbers getting substituted', dictDefault)

substituteDict = {}
count = 0
for i in dictDefault: 
    if count < len(dictArray): 
        substituteDict[i.upper()] = dictArray[count]
    count += 1
print(substituteDict)

file = open('ciphertext.txt', 'r')
string = ""
dictStart={}
for line in file: 
    for i in line: 
        if i not in substituteDict.keys(): 
            string += i
        else: 
            string += substituteDict[i]

print(string)
