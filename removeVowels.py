def anti_vowel(text):
    st= text
    vowelCheck="aeiouAEIOU"
    toprint=''
    #itterate through the vowelcheck
    for item in range(len(st)):
        a = 1
        for check in range(len(vowelCheck)):
            if vowelCheck[check] == st[item]:
                print "vowel found ", st[item]
                a = 0
                break
        if a == 1:
             toprint +=st[item]
    print(toprint)
    return(toprint)

anti_vowel("Hey look Words!")
