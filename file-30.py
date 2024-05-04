#dictionary comprehension

#cities_in_F={'New york':34,'Boston':56,'Los angeles':100}
#cities_in_C={key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
#print(cities_in_C)

#weather={'New york':"snowing",'Boston':"sunny",'Los angeles':"cloudy"}
#sunny_weather={key: value for (key,value) in weather.items() if value=="sunny"}
#print(sunny_weather)

cities={'New york':34,'Boston':56,'Los angeles':100}
desk_cities={key: ("WARM" if value>=50 else "COLD") for (key,value) in cities.items()}
print(desk_cities)