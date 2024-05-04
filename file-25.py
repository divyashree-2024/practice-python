#fns to variable

#def hello():
 #  print("hello")
#print(hello)
#hi=hello
##hi()
#hello()

#say=print
#say("whoa! its works!:o")


#higher order fns

#def loud(text):
  #  return text.upper()
#def quiet(text):
#    return text.lower()
#def hello(func):
 #   text=func("hello")
 #   print(text)
#hello(loud)

def divisor(x):
   def dividend(y):
      return y/x
   return dividend
divide=divisor(2)
print(divide(10))