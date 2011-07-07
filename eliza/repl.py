from eval import Eliza
import time
import random

eliza = Eliza()

def main():
	eliza = Eliza()
	while True:
		input = raw_input('--> ')
		secs = random.randint(1, 3)
		time.sleep(secs)
		print eliza.send(input)

