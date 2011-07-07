from eval import Eliza

def main():
	while True:
		input = raw_input('--> ')
		eliza = Eliza()
		print eliza.send(input)

