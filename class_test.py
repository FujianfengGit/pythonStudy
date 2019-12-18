#类的使用
class Player():
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def print(self):
        print(' %s 的hp是 %s' %(self.name,self.hp))


user1 = Player('tom',100)
user2 = Player('jim',50)
user1.print()
user2.print()
