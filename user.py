class User:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country


if __name__ == '__main__':
    Bob = User("Bob", 15, "America")
    #Userクラスをインスタンス化

    print(Bob)
    print(Bob.name)
    print(Bob.age)
    print(Bob.country)


    Tom = User("Tom", 57, "America")
    print(Tom)
    print(Tom.name)
    print(Tom.country)

    Ken = User("Ken", 49, "Japan")
    print(Ken)
    print(Ken.name)
    print(Ken.country)



