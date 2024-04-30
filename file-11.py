#import random

#import random
#x=random.randint(1,6)
#y=random.random()
#mylist=['rock','paper','scissors']
#z=random.choice(mylist)

#cards=[1,2,3,4,5,6,7,8,"J","K","Q","A"]
#random.shuffle(cards)
#print(cards)



#exception


try:
    numerator=int(input("enter a no:"))
    denominator=int(input("enter a no:"))
    result=numerator/denominator
    print(result)
except ZeroDivisionError:
    print("u cant find:")
except ValueError:
    print("enter only value:")
except Exception:
    print("Something went wrong:(")
else:
    print(result)
finally:
    print("This will always execute")