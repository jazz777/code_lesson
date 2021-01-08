import time
import threading
class T(threading.Thread):
  def run(self):
    print('nozomi.start')
    time.sleep(10)
    print('nozomi.end')

t = T()
t.start() 
t1 = T()
t1.start() 
t2 = T()
t2.start() 
t3 = T()
t3.start() 
t4 = T()
t4.start() 
t5 = T()
t5.start() 