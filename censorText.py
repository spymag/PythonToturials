def censor(text,word):
    splitText = text.split()
    print "1: ",splitText
    for index,item in enumerate(splitText):
        if item == word:
            item = "*" * len(item)
            splitText[index]= item
            #i+=1
            print "2: ", item
            
    mergedText = " ".join(splitText)
    print "3: ",mergedText
    return mergedText
    
    
    
censor("this hack is wack hack","hack")  
