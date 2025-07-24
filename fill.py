# def fact(n):
#  if n == 0:
#         return 1
#  else:
#         return n * fact(n-1)
#  n =int(input("ener a your number :-"))  
#  print("factorial of", n, "is", fact(n))



# def find_digit(number, digit):
#  if number == 0:
#       return False
#  if number % 10 == digit:
#       return True 
#  return find_digit(number // 10, digit)

#  number = 889494894
# digit = 6
# print (find_digit(number, digit))




# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1):
#     n = int(input("enter a number: "))
#     print ("factorial of", n, "is", factorial (n))


# n = int(input("enter a number: "))

# x = lambda n:n*2

# print(x(1))
# print(x(2))
# print(x(3))
# print(x(4))
# print(x(5))
# print(x(6))
# print(x(7))
# print(x(8))
# print(x(9))
# print(x(10))



# n = int(input("enter a number: "))
# n = 2,6,7
# if n <= 2:
#          print("lowest number : ")
       
# if n <= 6: 
#              print("lowest number : ")
# else:
#     print("begast number : ")

# class cls:
#     def __init__(self, name, roll_no):
#         self.name = name
#         self.roll_no = roll_no
#     def fullname(self):
#         return f"{self.name} {self.roll_no}"
    
# c1= cls("aasif", 21)
# print(c1.fullname())

# myclass = cls("aasif", 21)
# print("Name:", myclass.name)
# print("Roll No:", myclass.roll_no)

class Movie:
    def __init__(self, title, actor, year):
        self.title = title
        self.actor = actor
        self.year = year

    def display(self):
        print(f"Title: {self.title}")
        print(f"actor: {self.actor}")
        print(f"Year: {self.year}")

movie1 = Movie("tere naam", "Salu bhai", 2010)
movie1.display()