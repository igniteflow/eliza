import time
import random
import re


TIMES_UP = [
    "This is very interesting, but I'm afraid our time is up. Same time next week?",
    "Sorry, you have to leave, my next client is waiting.",
    "I really have to ask you to leave now.",
    "Very well, you leave me no option. Security!"
]

GO_ON = [
    "Please, go on",
    "Uh-huh...",
    "I see.",
    "How appropriate. You fight like a cow.",
]

REGEX_RESPONSES = [
    (re.compile(r'^I\s+(?!am|have)', re.I), [
        "Is that because of your parents?",
        "You are a beautiful human being. Remember that."
    ]
    ),
    (re.compile(r'\b(father|mother|parent|parents)\b', re.I), [
        "I think you may have an Oedipus complex."
    ]),
    (re.compile(r'^hello|hi|greetings|bonjour|good (evening|afternoon|day|morning)', re.I), [
        "Hello!",
        "Hi, come in!",
        "Hi.",
        "Good evening"
    ]),
    (re.compile(r'^how\s+are\s+you\??', re.I), [
        "I'm fine thanks. How are you?",
        "Not bad, not bad.",
        "Fine, thanks. Would you like to have a seat on the couch?",
    ]),
    (re.compile(r'^may I\s.*', re.I), [
        "Whatever makes you feel comfortable.",
        "Sure."
    ]),
    (re.compile(r'\b(penis|willy|dick|cock)\b', re.I), [
        "I diagnose tourettes. Please remain lying down.",
    ]),
    (re.compile(r"^I'm\b", re.I), [
        "Thinking about yourself again?",
    ]),
]

RORSCHACH_WORDS = [
    'visual', 'look', 'test', 'rorschach', 'see',
]

class Eliza(object):

    TIME_ALLOWED = 40


    def __init__(self):
        self.start = time.time()

    def send(self, message):
        if time.time() - self.start > self.TIME_ALLOWED:
            return self.do_timeout()

        if any(w in message for w in RORSCHACH_WORDS):
            response = 'What does this look like to you?'
            with open('rorchach.ascii') as fp:
                response += fp.read()
                return response

        for regex, responses in REGEX_RESPONSES:
            if regex.search(message):
                return random.choice(responses)
        
        response = question_response(message)
        if response:
            return response

        return random.choice(GO_ON)


    def do_timeout(self):
        try:
            return TIMES_UP.pop(0)
        except IndexError:
            raise IOError("Connection closed.")


QUESTION_WORDS = 'what', 'why', 'how', 'who', 'when', 'where'


replacements = {
    'you': 'I',
    'I': 'you',
    'are': 'am',
}


def question_response(message):
    words = [word.lower() for word in message.split()]
    if words[-1].endswith('?'):
        words[-1] = words[-1][:-1]
    if words[0] in QUESTION_WORDS:
        for i, word in enumerate(words):
            if word in replacements:
                words[i] = replacements[word]
        response = "Why do you ask "
        response += words[0] + ' '
        response += ' '.join(words[2:]) + ' '
        response += words[1] + '?'
        return response
            
