from eval import Eliza

def main():
	eliza = Eliza()
	while True:
		input = raw_input('--> ')
		print eliza.send(input)

