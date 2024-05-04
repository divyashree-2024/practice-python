#lambda fn

#def double(x):
#    return x*2
#print(double(5))

double=lambda x:x*2
multiply=lambda x,y:x*y
age_check=lambda age:True if age>=18 else False
print(multiply(5,7))
print(age_check(10))