from threading import Thread, Semaphore
import time

obj=Semaphore(3)

def display(name):
	obj.acquire()
	for i in range(3):
		print("Hello from {}".format(name))
		time.sleep(1)

	obj.release()


def main():
	t1=Thread(target=display, args=("Thread1",))
	t2=Thread(target=display, args=("Thread2",))
	t3=Thread(target=display, args=("Thread3",))
	t4=Thread(target=display, args=("Thread4",))
	t5=Thread(target=display, args=("Thread5",))

	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()

	t1.join()
	t2.join()
	t3.join()
	t4.join()
	t5.join()

main()
