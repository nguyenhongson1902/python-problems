# ip= input("Enter values:")
# # for example, input '34,67,55,33,12,98'
# result_list = ip.split(',')
# result_tuple = tuple(result_list)

# print(result_list)
# print(result_tuple)
# import datetime


# class Time():
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes=minutes

#     def addTime(t1, t2):
#         t3=Time(0,0)
#         if (t1.minutes+t2.minutes)>=60:
#             t3.hours=(t1.minutes+t2.minutes)//60
#         t3.hours = t3.hours + t1.hours + t2.hours
#         t3.minutes = t1.minutes + t2.minutes - ((t1.minutes+t2.minutes)//60)*60

#         return t3
    
#     def displayTime(self):
#         print('Time:', self.hours,'hours and', self.minutes,'minutes')

#     def displayMinute(self):
#         print("Minutes:", (self.hours*60)+self.minutes)

# a = Time(2,50)
# b = Time(1,20)
# c = Time.addTime(a,b)
# c.displayTime()
# c.displayMinute()

from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

@not_during_the_night
def say_whee():
    print("Whee!")


# say_whee = not_during_the_night(say_whee)
say_whee()
