   lst = []
def matching_characters(word1,word2):
    print("Common letters:",end=' ')
    for x in word1:
        if x in word2:
            lst.append(x)
    print(','.join(lst))
matching_characters("tissue","materials")       
