# クラス定義
class Life:
    def __init__(self):
        self.a = 3
        print('Life is short!!')
    
    def mix(self):
        return 5

nozomi = Life()
print('nozomi',nozomi.a)
print(nozomi.mix())