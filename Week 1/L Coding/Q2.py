def del_char(word, char):
    if len(char) > 1:
        return word
        
    n = ""
    for i in range(len(word)):
        if word[i] != char:
            n += word[i]
    return n
    
    
s = input()
c = input()
print(del_char(s,c))