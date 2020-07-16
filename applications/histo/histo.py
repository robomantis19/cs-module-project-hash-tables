# Your code here

file = open('robin.txt', 'r')
string = []
dictStart={}
for line in file:  
    value = ', '.join(line.split(" "))
    string.append(value)
        

words = string 
# .split(" \'")
words

print(words)
# count = 0
# for i in words: 
#     if count == 0: 
#         print(i)
#     count += 1
