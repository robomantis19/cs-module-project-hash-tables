def word_count(s):
    # Your code here
    dictionary = {}
    se = s.strip('\"')
    se = se.strip('\.')
    se = se.replace(" ", ",")
    print(se)
    words = se.split(",")
    if len(words) == 1 and words == "":
        
        return dictionary
    for i in range(0, len(words)-2): 
        if words[i] == ",": 
            words.pop(i)
    for word in words: 
        # for key, value in dictionary.items(): 
        word = word.lower()
        if word == '': 
            return dictionary
        if word not in dictionary:
            dictionary[word] =  1
        else:
            dictionary[word] = dictionary[word] + 1
    print(dictionary)
    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))