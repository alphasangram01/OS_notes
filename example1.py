##this is an example of an intermediate program, it has race conditions
import threading

COUNT = 0

def calculate_count(arg):
	print("{}:begin".format(arg))
	global COUNT
	for _ in range(1000000):
		COUNT = COUNT + 1
	print("{}:ends".format(arg))

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
