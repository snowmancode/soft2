class Person:
    
    age = 20

    def greet(self):
        print('Hello')



print(Person.age)


print(Person.greet)

Thomas = Person()
print(Thomas.age)
Thomas.greet()

Bruce_Wayne = Person()
print(Bruce_Wayne.age)
Bruce_Wayne.greet()
