#  Inheritance

class Animal(): #父類別
    def __init__(self):
        self.feet_number=4
    def shout(self):    
        print("Hello! I'm an animal.")

class Dog(Animal): #子類別(Dog)繼承父類別(Animal)
    def shout_detail(self):
        print("Hello! I'm an dog.")
    pass

dog=Dog() #用dog進行Dog的instant object
dog.shout() #直接call class Animal裡面的shout函數，就會印出 Hello......
dog.shout_detail() #call Dog裡面的shout_detail函數
print(dog.feet_number) #call class Animal裡面的feet_number