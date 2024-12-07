class Car:
    category = "motor vehicle"
    model = "Toyota"
    color = "red"

    def __init__(self,model,color):
        self.model = model
        self.color = color

    def dispaly(self):
        print(self.model)
        print(self.color)

    def update_model(self,new_model,new_color):
        self.model = new_model
        self.color = new_color

# new_car =  Car()
# print(new_car.category)
# print(new_car.dispaly())

# car = Car("Toyota","red")
# car.dispaly()
# car.update_model("Honda","black")
# car.dispaly()
# print(car.category)

# cretae a class named BanckAccount with the attribute account holder to sotre the name and a attribute balence to store the amount in the acc balence and add the following methods to the class
# 1. deposit(amount) - add the given amount to the balance
# 2. withdraw(amount) - subtract the given amount from the balance if sufficient funds are available,other wise pprint an errr messsage
# 3. display() - display the current balance
# write the small script to demonstrate,
# 1. create an object of the class
# 2. perform some deposits and withdrawls
# 3. display the balance after each operation

# class BankAccount:
#     account_holder = ""
#     balance = 0

#     def __init__(self,account_holder,amount):
#         self.account_holder = account_holder
#         self.balance = amount
    
#     def deposit(self,amount):
#         self.balance = self.balance + amount
#         return self.balance
    
#     def withdraw(self,amount):
#         if self.balance >= amount:
#             self.balance = self.balance - amount
#             print("Withdraw Amount",amount)
#             return self.balance
#         else:
#             print("Withdraw Amount",amount)
#             return "Insufficient funds Because Your Accout Balance is",self.balance
        
#     def display(self):
#         print("Account Holder Name:",self.account_holder)
#         if self.balance == 0 | self.balance < 0:
#             print("Balence Must Be a Posutive Number")
#         else:
#             print("Total Amount In Your Account",self.balance)
    

# account1 = BankAccount("Dasun Nirmal",1000)
# print("Depost Amount",account1.deposit(1000))
# print("After Withdraw, Total Amount",account1.withdraw(500))
# account1.display()

# print()

# account2 = BankAccount("Rosel",1000)
# print("Depost Amount",account2.deposit(1000))
# print("After Withdraw, Total Amount",account2.withdraw(500))
# account2.display()

# Inheritance

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal): # inherits the animal classs
    def __init__(self,name,color):
        self.color = color
        super().__init__(name)
        
    def speak(self):
        print(self.name,"Says Bark")
        print(self.name,"is",self.color)

class Cat(Animal): # inherits the animal classs
    def __init__(self,name,color):
        self.color = color
        super().__init__(name)

    def speak(self):
        print(self.name,"Says Meow")
        print(self.name,"is",self.color)

# dog = Dog("Tommy","black")
# dog.speak()
# cat = Cat("Kitty","white")
# cat.speak()

# Creatting a basic libery system using a inheritance 
# 1. Base Class - LibraryItem

# Attributes                       Methods
# title:String                     display_info()
# author:String                    
# publication_year:int             

# 2. Derived Class - Book
# inherit from libraryItem

# Attributes                       Methods
# genre:String                     over ride the display_info() and print the genre and isbn 
# isbn:int

# 3. Derived Class - Magazine
# inherit from libraryItem

# Attributes                       Methods
# issue:String                     the issue number or the date of the magazine

# over ride the display_info() and print details and the issue number                      

# Tsck
# 1. Create Instances of the Book and Magazine classes with appropriate values
# 2. Call the display_info() method for each instance to test inheritance and method over riding


# class LibraryItem:
#     title = ""
#     author = ""
#     publication_year = 0

#     def __init__(self,title,author,publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
    
#     def display_info(self):
#         print("Title:",self.title)
#         print("Author:",self.author)
#         print("Publication Year:",self.publication_year)

# class Book(LibraryItem):
#     genre = ""
#     isbn = ""

#     def __init__(self,title,author,publication_year,genre,isbn):
#         self.genre = genre
#         self.isbn = isbn
#         super().__init__(title,author,publication_year)

#     def diplay_info(self):
#         super().display_info()
#         print("Genre:",self.genre)
#         print("ISBN:",self.isbn)

# class Magazine(LibraryItem):
#     issue = ""

#     def __init__(self,title,author,publication_year,issue):
#         self.issue = issue
#         super().__init__(title,author,publication_year)

#     def display_info(self):
#         super().display_info()
#         print("Issue:",self.issue)

# book = Book("Python Programming","Dasun Nirmal",2024,"Programming","123456")
# book.diplay_info()

# print()

# magazine = Magazine("Python Magazine","Dasun Nirmal",2024,"Issue 1")
# magazine.display_info()


# Encapsulation

# Attributes with a single underscore are protected and those with double underscore are private

# class MyClass:
#     _test1 = "protected"
#     __test2 = "private"

#     def __init__(self):
#         print("Protected:",self._test1)
#         print("Private:",self.__test2)

#     def _display(self):
#         print("Protected Method")

#     def __display(self):
#         print("Private Method")
    
# my_obj = MyClass()
# print(my_obj._test1) # Can access the protected attribute but not recommended
# print(my_obj.__test2) # AttributeError: 'MyClass' object has no attribute '__test2'

# my_obj._display() # Can access the protected method but not recommended
# my_obj.__display() # AttributeError: 'MyClass' object has

class MyClassTwo:

    def __init__(self):
        self.__data = "private data"

    def get_value(self):
        print("Value is",self.__data)

    def set_value(self,value):
        self.__data = value

my_2 = MyClassTwo()
my_2.get_value()
my_2.set_value("New Value")

# Write a python program to create a class named "Quadratic Equation" that represents a quadratic equation of the form ax^2 + bx + c = 0. 
# The class should have the private attributes a, b, and c to store the coefficients of the quadratic equation.
# Create a constructor that takes the values of a, b, and c and initializes the attributes.
# A private method named __discriminant() that calculates the discriminant of the quadratic equation.
# A public method find_roots() that returns the roots of the quadratic equation using the formula x = (-b ± √(b^2 - 4ac)) / 2a
# return the roots of the Quadratic Equation.
# if D = 0; one real root
# if D > 0; two destincs roots
# if D < 0; two complex roots