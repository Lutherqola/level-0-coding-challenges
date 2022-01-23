def matching_characters(word1,word2):
    print("common letters")
    for x in word1:
        if x in word2:
            print(x)
matching_characters("tissue","materials")            