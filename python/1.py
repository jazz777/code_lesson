
'''
sleep を挟んで、コマンドを順次実行していくような関数のプロトタイプ
引数a は　インスタンスIDを想定。

改善①
インスタンスIDは　ディクショナリにいれて、
{'host0':'i-0000000','host1':'i-0000001'}
のような形式にして、ループさせる

改善②
ディクショナリは、ファイル形式にして保存

改善③
dynamodb から、読み込む。

#print((lambda a:str(a**2+1)+'   nozomi')(10))
#print((lambda a:'nozomi '*a)(10))
'''

import time

def func(a):
    print(a,'を起動しています。')
    time.sleep(1)
    print('........')
    time.sleep(1)
    print('........')
    time.sleep(1)
    print(a,'を起動しました')

func('ec2')
