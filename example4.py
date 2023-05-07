import threading 
from threading import Condition, Thread
import time
import logging

logging.basicConfig(level=logging.DEBUG,format='(%(threadName)-9s %(message)s',)

def consumer(cv):
	logging.debug('Consumer thread started...')
	with cv:
		logging.debug('Consumer waiting ...')
		cv.wait()
		logging.debug('Consumer consumed the resource')


def producer(cv):
	logging.debug('Producer thread started...')
	with cv:
		logging.debug('Making resources available')
		logging.debug('Notifying to all consumers')
		cv.notify_all()

def main():
	condition=Condition()
	cs1 = Thread(name='consumer1', target=consumer, args=(condition,))
	cs2 = Thread(name='consumer2', target=consumer, args=(condition,))
	pd = Thread(name='producer', target=producer, args=(condition,))

	cs1.start()
	time.sleep(2)
	cs2.start()
	time.sleep(2)
	pd.start()
	time.sleep(2)

main()