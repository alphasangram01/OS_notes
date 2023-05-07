from threading import Thread, Lock
class FizzBuzz(object):
	def __init__(self,n):
		self.n=n
		self.count=0
		self.Lock=Lock()

	def fizz(self):
		if self.count<=self.n:
			self.Lock.acquire()
			if self.count%3==0 and self.count%5!=0:
				print("Fizz")
				self.count+=1
			self.Lock.release()

	def buzz(self):
		if self.count<=self.n:
			self.Lock.acquire()
			if self.count%3!=0 and self.count%5==0:
				print("Buzz")
				self.count+=1
			self.Lock.release()

	def fizzbuzz(self):
		if self.count<=self.n:
			self.Lock.acquire()
			if self.count%3==0 and self.count%5==0:
				print("FizzBuzz")
				self.count+=1
			self.Lock.release()

	def number(self):
		if self.count<=self.n:
			self.Lock.acquire()
			if self.count%3!=0 and self.count%5!=0:
				print(self.count)
				self.count+=1
			self.Lock.release()

	Lock
	count=0
	n=100


n=100
def main():
	x=FizzBuzz(n)
	for i in range(n):
		thread1= Thread(target= x.fizz() , args=())
		thread2= Thread(target= x.buzz(), args=()) 
		thread3= Thread(target= x.fizzbuzz(), args=()) 
		thread4= Thread(target= x.number(), args=())

		thread1.start()
		thread2.start()
		thread3.start()
		thread4.start()

		thread1.join()
		thread2.join()
		thread3.join()
		thread4.join()

main()