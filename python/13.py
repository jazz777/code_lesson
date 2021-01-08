'''
なんでもいいのでクラスを定義しクラス変数、メソッドがの使い方を使えるサンプルを示す
'''
class Myclas:
    pass

class Myclas2:
    def __init__(self):
        print('インスタンスが作成されました')
        self.a=1
        print('インスタンス変数aが定義されました')
        self.b=2
        print('インスタンス変数bが定義されました')
        self.c=3
        print('インスタンス変数cが定義されました')



fujiwara=Myclas2()
print('a= ',fujiwara.a)
print('b= ',fujiwara.b)
print('c= ',fujiwara.c)