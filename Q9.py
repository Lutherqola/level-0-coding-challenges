lst =[]
def vowel_finder(word:str):
    print("Vowels:",end=' ')
    for x in word:
       if x in ["a","A","e","E","i","I","o","O","u","U"]:
           lst.append(x)
    print(','.join(lst))
              
vowel_finder("PersuAsion")  
              
