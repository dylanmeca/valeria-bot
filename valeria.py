import re
import random

class Chatbot(object):
    def __init__(self, pairs, reflections={}):
        self._pairs = [(re.compile(x, re.IGNORECASE), y) for (x, y) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()

    def _compile_reflections(self):
        sorted_refl = sorted(self._reflections, key=len, reverse=True)
        return re.compile(
            r"\b({0})\b".format("|".join(map(re.escape, sorted_refl))), re.IGNORECASE
        )

    def _substitute(self, str):
        return self._regex.sub(
            lambda mo: self._reflections[mo.string[mo.start() : mo.end()]], str.lower()
        )

    def _wildcards(self, response, match):
        pos = response.find("%")
        while pos >= 0:
            num = int(response[pos + 1 : pos + 2])
            response = (
                response[:pos]
                + self._substitute(match.group(num))
                + response[pos + 2 :]
            )
            pos = response.find("%")
        return response

    def respond(self, str):
        for (pattern, response) in self._pairs:
            match = pattern.match(str)

            if match:
                resp = random.choice(response)  
                resp = self._wildcards(resp, match)  

                if resp[-2:] == "?.":
                    resp = resp[:-2] + "."
                if resp[-2:] == "??":
                    resp = resp[:-2] + "?"
                return resp

    def converse(self, quit="chao"):
        user_input = ""
        while user_input != quit:
            user_input = quit
            try:
                user_input = input("tu: ")
            except EOFError:
                print(user_input)
            if user_input:
                while user_input[-1] in "!.":
                    user_input = user_input[:-1]
                print(self.respond(user_input))

reflections = {
    "hola": "hola",
    "como estas?": "bien",
    "estoy bien": "que bien",
    "hey": "que pasa ?",
    
}

pairs = [
    [
        r"mi nombre es (.*)",
        ["valeria: Hola %1, como estas ?",]
    ],
     [
        r"cual es tu nombre ?",
        ["valeria: Mi nombre es valeria ?",]
    ],
    [
        r"como estas ?",
        ["valeria: Bien, y tu?",]
    ],
    [
        r"disculpa (.*)|perdon (.*)",
        ["valeria: No pasa nada", "valeria: te perdono :)",]
    ],
    [
        r"hola|hey|buenas",
        ["valeria: Hola", "valeria: hola, como estas ??",]
    ],
    [
        r"que (.*) quieres ?",
        ["valeria: Nada gracias",]
        
    ],
    [
        r"(.*) crearon ?|(.*) creado?",
        ["valeria: fui creado el 18 de abril del 2021",]
    ],
    [
        r"chao|bye|adios",
        ["valeria: Chao","valeria: Fue bueno hablar contigo"]
],
]

def start():
    chatbot = Chatbot(pairs, reflections)
    chatbot.converse()

if __name__ == "__main__":
    start()
