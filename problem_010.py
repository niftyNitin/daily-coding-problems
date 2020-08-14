import time
def schedular(f, n):
	time.sleep(n)
	f()

def hello_world():
	print("Hello World")

schedular(hello_world, 2)