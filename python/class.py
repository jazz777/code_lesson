class Woman:
    def __init__(self):
        """ test """
        self.sex='woman'
        self.kekka=0

    #メソッド　引数なし
    def song(self):
        return("rarara!")

    #メソッド　引数あり
    def set_name(self,name):
        self.name=name

    #メソッド　引数あり
    def cal(self,num):
        self.kekka=num**2
        
##インスタンス作成
nozomi=Woman()

#メソッド実行
print("method run song()")
print(nozomi.song())

#メソッド実行
nozomi.set_name('lion')
print(nozomi.name)

#メソッド実行
nozomi.cal(25)
print(nozomi.kekka)
