##this is an example of an mutex demonstration.
import threading
from threading import Lock
COUNT = 0
LOCK=Lock()

def calculate_count(arg):
	LOCK.acquire()
	print("{}:begin".format(arg))
	global COUNT
	for _ in range(1000000):
		COUNT = COUNT + 1
	print("{}:ends".format(arg))
	LOCK.release()

def print_args(x):
	print(x)

def main():
	print("main begin: COUNT = {}".format(COUNT))
	t1=threading.Thread(target=calculate_count, args=("t1",))
	t2=threading.Thread(target=calculate_count, args=("t2",))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("main done : COUNT = {}".format(COUNT))


main()

