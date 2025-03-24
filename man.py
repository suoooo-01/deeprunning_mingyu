class Man:
    def __init__(self, name): # 생성자
        self.name = name
        print("Initilized!")

    def hello(self): # 매서드 1
        print("Hello "+self.name+"!")

    def goodbye(self): # 매서드 2
        print("Goodbye "+self.name+"!")

m=Man("David")
m.hello()
m.goodbye()
