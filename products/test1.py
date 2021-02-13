class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        print(f'{self.name} {self.age}')


class Male(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.education = True
        self.__wallet = 0

    def description(self):
        print(self.__wallet)
        print(f'{self.name} {self.age} {self.education}')


class Female(Human):
    def __init__(self, name, age):
        super().__init__(name, age)


male1 = Male(name='ruslan', age=15)
male1.description()
print(male1.name)
