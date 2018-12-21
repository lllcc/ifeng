class Cat:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def ss(self):
        print("my name is %s, i am a %s" % (self.name, self.sex))


c = Cat("jenny", "girl")
c.ss()
