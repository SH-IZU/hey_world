# def say_hi():
#     print('hi inside function')
#     return 10

# x= say_hi()
# print(type(x))
# print(say_hi())

# #%%
# def add_numbers(a, b, c=0, d=0, e=0, f=0, g=0):
#     return a+b+c+d+e+f+g
# print(add_numbers(1,2))
# print(add_numbers(1,2,3))
# print(add_numbers(1,2,3,4))
# print(add_numbers(1,2,3,4,5))
# print(add_numbers(1,2,3,4,5,6))
# %%
#


# x = add_numbers(1,2)
# print(x) 
# print(add_numbers(1,2,3))
# print(add_numbers(1,2,3,4))
# print(add_numbers(1,2,3,4,5))
# print(add_numbers(1,2,3,4,5,6,7,8,9))

# #%%
# def student_detail(name, age, **kwargs):
#     print(f'[details of{age} years of old student: {name}]')
#     for key, value in kwargs.items():
#        print(f'the {key} is {value}')


# student_detail("sadhana",19)

# def test(*args, **kwargs):
#     print(args)
#     print(kwargs)

# test(1,2,3,'hello')
# #%%
#

# def fibonacci(n):
#     print(f'value of n:',)
#     if n > 1:
#         return(fibonacci(n-1) + fibonacci(n-2))
#     return

# def fibonacci(n):
#     fib_sequence = [0, 1]
#     for i in range(2, n):
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
#     return fib_sequence

# # Print the first 20 Fibonacci numbers
# fibonacci_sequence = fibonacci(20)
# for num in fibonacci_sequence:
#     print(num)






# # %%
# a = 10
# b = 0
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("cannot divide by 0") 
# except TypeError as e:
#     print('multiple types cannot be mixed')   
#     print(f'{e}')

# except   Exception as e:
#     print("exception")
#     print(f'{e}')
# finally:
#     print("finally success")

# take input a and b from user
# a and b is integer
# loop the user input until you get the dorrect value
# while True:
#     try:
#         a = int(input("Enter the value for 'a': "))
#         b = int(input("Enter the value for 'b': "))
#         break  # Break the loop if both inputs are valid integers
#     except ValueError:
#         print("Please enter valid integers for both 'a' and 'b'.")

# print("You entered 'a' as", a, "and 'b' as", b)

# while True:
#     try:
#         a = float(input("Enter the value for 'a': "))
#         b = float(input("Enter the value for 'b': "))
#         break  # Break the loop if both inputs are valid integers
#     except ValueError:
#         print(" enter  integers for both 'a' and 'b'.")

# print("You entered 'a' as", a, "and 'b' as", b)


class LengthError(Exception):
    def __init__(self,value : int, *args : object)-> None:
        self.value = value
        super().__init__(*args)
    def __str__(self):
        return(f'Length can\'t be negative')
class Length:
    def __init__(self,value):
        if value < 0:
            raise LengthError(value)
        self.value = value
l1 = Length(1)
l2 = Length(-6)