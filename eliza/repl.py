from eval import Eliza
import time
import random
import sys

eliza = Eliza()

def main():
	eliza = Eliza()
	while True:
		input = raw_input('--> ')
		if input == 'exit':
			sys.exit(0)
		
		secs = random.uniform(0.25, 1)
		time.sleep(secs)
		print eliza.send(input)

