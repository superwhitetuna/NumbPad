import msvcrt
import random 
import time

x = random.randint(1000000000,9999999999)
print(x)

input("Press Enter to Begin:\n")


def time_convert(sec):
  sec = sec % 60
  print("Time Lapsed = {0}".format(sec))


start_time = time.time()

User_Input = ""

n = 0
while n < 10:
    
    if msvcrt.kbhit():
        key = msvcrt.getch()
        User_Input += key.decode("utf-8")
        n += 1
        print(User_Input, end="\r")

end_time = time.time()

time_lapsed = end_time - start_time
time_convert(time_lapsed)

if int(User_Input) == x:
    print("Nice one!")
else:
    print("Go fuck yourself!")
