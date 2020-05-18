def add(a, b):
    ret = a + b
    return ret


ans = add(5, 10)
print(ans)


class Hero:
    def __init__(self, hp, mp):
        self.hp = hp
        self.mp = mp
    def attack(self):
        print("こうげき")
h = Hero(400,30)
h.attack()


ls = [1,5,3,2,10,9]
ls.sort(reverse=True)
print(ls)