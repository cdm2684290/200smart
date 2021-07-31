
import read
import interface
import threading
t1=threading.Thread(target=interface.bi)
#t2=threading.Thread(target=read.ri)
t1.start()
#t2.start()