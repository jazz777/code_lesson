'''
なんでもいいのでクラスを定義しクラス変数、メソッドがの使い方を使えるサンプルを示す
'''

class Myclas3:
    def __init__(self):
        self.a=1
        self.b=2
    def hello(self):
        print('Hello Every One!!')

fujiwara=Myclas3()
print('a= ',fujiwara.a)
print('b= ',fujiwara.b)

fujiwara.hello()  #クラスの関数を呼び出す場合は()をつけましょう。

print(type(fujiwara))  #__main__.Myclass3型であることが確認できます。
print(type(1))



