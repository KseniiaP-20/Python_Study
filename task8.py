# Домашнее задание

# Написать функцию подсчета количества строк, слов и букв в текстовом файле 

def count(f):    

    b = []
    wordcount = 0
    symbolcount = 0

    for line in f:
        b.append(line.split())

    paragraphcount = len(b)
    
    print('\nКоличество абзацев в текстовом файле составляет:', paragraphcount)      
    
    for i in range(len(b)):
        wordcount += len(b[i])
        for j in range(len(b[i])):
            symbolcount += len(b[i][j])
            
    print('\nКоличество слов в текстовом файле составляет:', wordcount)
    print('\nКоличество букв в текстовом файле составляет:', symbolcount)

    f.close()
 
count(open("task8_text.txt", "r"))
