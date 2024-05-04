#time module

import time
#print(time.ctime(100000000))
#print(time.time())
#print(time.ctime(time()))
#time_object=time.localtime()
#time_object=time.gmtime()
#print(time_object)
#local_time=time.strftime("%B %d %H %w %Y:%M:%S",time_object)
#print(local_time)

#time_string="April 20,2020"
#time_object=time.strptime(time_string,"%B %d, %Y")
#print(time_object)

time_tuple=(2020,4,13,5,20,0,0,0,0)
time_string=time.asctime(time_tuple)
print(time_string)

time_tuple=(2020,4,13,5,20,0,0,0,0)
time_string=time.mktime(time_tuple)
print(time_string)