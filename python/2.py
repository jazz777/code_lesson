import time
sleep_time=1

def get_id(name):
    time.sleep(sleep_time)
    '''
name(タグ名）を指定して、インスタンスIDを取得する
    '''
    print('get_id complete!')
    return 'i-00990989'

def detuch_ec2(id):
    time.sleep(sleep_time)
    '''
ec2 detach id
    '''
    print(id,'detuch_ec2 complete!')

def change_boot_def():
    time.sleep(sleep_time)
    '''
    
    '''
    print('change_boot_def complete!')

def reboot_asg():
    time.sleep(sleep_time)
    '''
    
    '''
    print('reboot_asg complete!')

def terminate_detuch():
    time.sleep(sleep_time)
    '''
    
    '''
    print('terminate_detuch complete!')

a_id=get_id('name')
#print(i)


detuch_ec2(a_id)
'''
change_boot_def()
reboot_asg()
terminate_detuch()
'''