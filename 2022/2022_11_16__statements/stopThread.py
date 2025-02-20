import threading
import ctypes
import time

class thread_with_exception(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name
			 
	def run(self):
		for i in range(10):
			try:
				print(f"n: {i}")
				time.sleep(1)
			except Exception:
				print("Except has caught SystemExit")
				continue
		  
	def get_id(self):
 
		# returns id of the respective thread
		if hasattr(self, '_thread_id'):
			return self._thread_id
		for id, thread in threading._active.items():
			if thread is self:
				return id

	def raise_exception(self):
		thread_id = self.get_id()
		res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread_id),
              ctypes.py_object(SystemExit))
		if res > 1:
			ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
			print('Exception raise failure')

t1 = thread_with_exception('Thread 1')
t1.start()

print("After 3s stop the thread")
for i in range(5):
	time.sleep(1)
	if i == 2:
		print(f"Stopping thread")
		t1.raise_exception()

print("Main thread stopped")
