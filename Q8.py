def integer_to_time(x:int):
    if x<60 and x!=1:
        print(x//60,"hours",x%60,"minutes")
    elif x>=120 and x%60!=1:
        print(x//60,"hours",x%60,"minutes") 
    elif x>=60 and x<120 and x%60!=1:
        print(x//60,"hour",x%60,"minutes")    
    else :
        print(x//60,"hours",x%60,"minute")     
integer_to_time(78)          