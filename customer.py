class Customer:
    def __init__(self,first_name,family_name,age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):

       return self.first_name + self.family_name

 if __name__ == "__main__":
    tom = Customer("Tom","Ford",57)
    print(tom.full_name())

    ken = Customer("Ken", "Yokoyama", 49)
    print(tom.full_name())