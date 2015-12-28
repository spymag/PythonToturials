def remove_duplicates(numbers):
    newNumbers=[]
    for item in numbers:
        if item not in newNumbers:
            newNumbers.append(item)
    print newNumbers
    return newNumbers

remove_duplicates([1,1,3,3])    
