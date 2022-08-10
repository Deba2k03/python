import datetime
import time
# initial=time.time()
# print(initial)
# k=0
# while(k<20):
#     print("this is deb")
#     time.sleep(2)           #wait the continius loop
#     k+=1
# print(f"while loop run time is: {time.time()-initial} second")
# initial2=time.time()
# for i in range(20):
#     print("this is deb")
# print(f"for loop run time is: {time.time()-initial2} second")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)


# Prints today's date with help
# of datetime library

today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

