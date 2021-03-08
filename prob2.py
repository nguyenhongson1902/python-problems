## Solution 1
# n = int(input("Enter a value: "))
# result = 1
# for i in range(2,n+1):
#     result *= i
# print(str(result))

## Solution 2
# n = int(input("Enter a value: "))
# def factorial(n):
#     assert type(n)==int
#     if (n==0) or (n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(str(factorial(n)))

class Temperature():
    def convertFahrenheit(self, celsius):
        print((celsius*9/5)+32)

    def convertCelsius(self, fahrenheit):
        print((fahrenheit-32)*5/9)

t=Temperature()
t.convertFahrenheit(30)
t.convertCelsius(60)