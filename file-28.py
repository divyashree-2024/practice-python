#map()

#store=[("shirt",20.00),
 #       ("pants",25.00),
 #       ("jaclket",50.00),
#        ("socks",10.00)]
#to_rupees=lambda data:(data[0],data[1]*83.38)
#to_dollars=lambda data:(data[0],data[1]/83.38)
#store_dollars=list(map(to_dollars,store))
#for i in store_dollars:
 #  print(i)


#filter

friends=[("Rachel",19),
         ("Monica",19),
         ("Ross",21) ]
age=lambda data:data[1]>=18
drinks_budds=list(filter(age,friends))
for i in drinks_budds:
    print(i)