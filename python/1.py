#print((lambda a:str(a**2+1)+'   nozomi')(10))


#print((lambda a:'nozomi '*a)(10))
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


