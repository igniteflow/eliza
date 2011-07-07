import time
import random


TIMES_UP = [
    "That's very interesting, but I'm afraid our time is up. Same time next week?",
    "Sorry, you have to leave, my next client is waiting.",
    "I really have to ask you to leave now.",
    "The session is over, please go.",
    "Very well, you leave me no option but to call security."
]

GO_ON = [
    "Please, go on",
    "Uh-huh...",
    "I see.",
    "How appropriate. You fight like a cow.",
]

class Eliza(object):

    TIME_ALLOWED = 30

    def __init__(self):
        self.start = time.time()

    def send(self, message):
        if time.time() - self.start > self.TIME_ALLOWED:
            self.do_timeout()
        return random.choice(GO_ON)

    def do_timeout(self):
        try:
            return TIMES_UP.pop(0)
        except IndexError:
            raise IOError("Connection closed.")
            

def test_eliza():
    e = Eliza()
    while True:
        print e.send('Hello')
        time.sleep(0.5)


if __name__ == '__main__':
    test_eliza()
