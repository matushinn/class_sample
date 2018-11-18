class User:
    def __init__(self,name,age,country):
        #インスタンス変数
        self.name = name
        self.age = age
        self.country = country

    def display_profile(self):
        #display_profile()はUserクラスのインスタンスメソッド
        print(f"私は{self.name}です。国籍{self.country}の{self.age}歳でーーーす")

    def change_nationarity(self,country_name):
        self.country = country_name




if __name__ == '__main__':
    Bob = User("Bob", 15, "America")
    #Userクラスをインスタンス化
    Bob.display_profile()
    Bob.change_nationarity("China")
    Bob.display_profile()


    print(Bob.name)


    Tom = User("Tom", 57, "America")
    Tom.display_profile()
    Tom.change_nationarity("Cambozi-------------------a")
    Tom.display_profile()
    print(Tom.name)

    Ken = User("Ken", 49, "Japan")
    Ken.display_profile()
    Ken.change_nationarity("コロンビーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーア")
    Ken.display_profile()
    print(Ken.name)



