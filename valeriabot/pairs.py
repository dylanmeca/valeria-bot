import re

class pairs:

      def __init__(self):
              return

      def reflections(self):
              reflections = {
                 "hola": "hola",
                 "como estas?": "bien",
                 "estoy bien": "que bien",
                 "hey": "que pasa ?",
    
              }

              return reflections

      def pairs(self):
              pairs = [
                [
                 r"mi nombre es (.*)",
                 ["valeria: Hola %1, como estas ?",]
                ],
                [
                 r"cual es tu nombre ?",
                 ["valeria: Mi nombre es valeria",]
                ],
                [
                 r"como estas ?|que tal ?",
                 ["valeria: Bien, y tu?",]
                ],
                [
                 r"disculpa (.*)|perdon (.*)",
                 ["valeria: vale :3, te perdono", "valeria: te perdono :)",]
                ],
                [
                 r"hola|hey|buenas (.*)",
                 ["valeria: Hola", "valeria: hola, como estas ??", "valeria: buenas %1"]
                ],
                [
                 r"cual es tu religion?",
                 ["valeria: soy catolica",]
        
                ],
                [
                 r"(.*) crearon ?|(.*) creado?",
                 ["valeria: fui creado el 18 de abril del 2021",]
                ],
                [
                 r"vale (.*)|ok (.*)",
                 ["valeria: ok", "valeria: vale :3",]
                ],
                [
                 r"chao|bye|adios",
                 ["valeria: Chao","valeria: Fue bueno hablar contigo"]
              ],
              ]
   
              return pairs
