#scope

#name="divya"
#def display_name():
    #name="div"
    #print(name)
#display_name()
#print(name)


#*args

def add(*div):
    sum=0
    div=list(div)
    div[0]=0
    for i in div:
        sum+=i
    return sum
print(add(1,2,3,4,5))