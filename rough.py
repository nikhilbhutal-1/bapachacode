# def greet(name):
#     return f"hello , {name}"
# def square(x):
#     return x*x 
# def outer():
#     def inner():
#         return "hello"
#     return inner()

# # print(greet("nikhil"))
# # print(square(7))  # Output: 
# print(outer())
# def greet(name = "stranger"):
#     return f"Hello, {name}"
# print(greet())  
list = []
first_value =input("enter values:")
second_value = input("enter values:")
third_value = input("enter values:")
list = [first_value,second_value,third_value]
copy_list = list.copy()
copy_list.reverse() 
if list == copy_list:
    print(" Palindrome ")  # Output: list is equal
else:
    print(" not palindrome")  # Output: list is not equal