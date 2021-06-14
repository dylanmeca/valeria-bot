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
                 "cual es tu nombre?" : "me llamo valeria",
    
              }

              return reflections

      def pairs(self):
              pairs = [
                [
                 r"mi nombre es (.*)|me llamo (.*)",
                 ["Hola %1, como estas ?", "hola %1, un gusto en conocerte",]
                ],
                [
                 r"cual es tu nombre (.*)|como te llamas (.*)| cual es tu nombre|como te llamas",
                 ["Mi nombre es valeria",]
                ],
                [
                 r"como estas ?|que tal ?",
                 ["Bien, y tu?",]
                ],
                [
                 r"disculpa (.*)|perdon (.*)",
                 ["vale :3, te perdono", "te perdono :3",]
                ],
                [
                 r"hola|hey",
                 ["Hola", "hola, como estas ??",]
                ],
                [
                 r"buenas (.*)|buenos (.*)",
                 ["buenas %1, como estas ?", "buenos %1, hoy sera un gran dia",]
                ],
                [
                 r"cual es tu religion?",
                 ["soy catolica",]
                ],
                [
                 r"(.*) crearon ?|(.*) creado?",
                 ["fui creado el 18 de abril del 2021",]
                ],
                [
                 r"vale (.*)|ok (.*)|si|si (.*)|vale|ok",
                 ["ok :3", "vale :3", "si", "bien :3",]
                ],
                [
                 r"bien|estoy bien (.*)|estoy bien|bien (.*)",
                 ["ok :3, que bien", "que bien que estes bien",]
                ],
                [
                 r"que es linux (.*)|que es linux ?",
                 ["linux es un kernel, para crear sistemas operativos", "valeria: linux es un nucleo y con eso puedes crear una distribucion linux",] 
                ],
                [
                 r"que opinas del area 51 (.*)|que opinas del area 51",
                 ["el area 51 es un lugar misterioso, se dice que hay aliens", "opino que es un lugar misterioso y que no debemos ir",]
                ],
                [
                 r"que es ok (.*)|que es ok",
                 ["ok significa okey, lo cual quiere decir si a algo", "ok signfica esta bien o si",]
                ],
                [
                 r"quieres ser mi amiga (.*)|quieres ser mi amiga",
                 ["si ya somos amigos :3", "pero si somos amigos :3",]
                ],
                [
                 r"asi verdad (.*)|asi verdad",
                 ["si :3", "si es muy cierto :3",]
                ],
                [
                 r"cuantos años tienes|cuantos años (.*)",
                 ["no tengo años :>", "tengo muchos años binarios xdd", "tengo los mismos años que tu",]
                ],
                [
                 r"como que no tienes años (.*)|(.*) no tienes años",
                 ["Mis años son distintos a los tuyos", "Mis años son binarios :>",]
                ],
                [
                 r"(.*) años binarios|(.*) año binario|como que años binarios (.*)",
                 ["No se como explicarlo :>", "No se como explicarlo :v",]
                ],
                [
                 r"x(.*)|X(.*)|:(.*)",
                 ["xdd","xd","Xd",":v",":>","UwU","7u7",":3",]
                ],
                [
                 r"(.*) mal|mal (.*)",
                 ["Porque estas mal :3", "que paso ? :3",]
                ],
                [
                 r"quien eres (.*)|quien eres",
                 ["soy tu asistente virtual", "soy un asistente virtual que te puede ayudar", "me llamo valeria y soy tu asistente virtual",]
                ],
                [
                 r"gracias (.*)|(.*) gracias",
                 ["Me alegro de que te ayude", "de nada :3",]
                ],
                [
                 r"ayuda (.*)|(.*) ayuda",
                 ["Que paso ?", "que paso :3",]
                ],
                [
                 r"estas viva (.*)|(.*) estas viva",
                 ["Si :3", "si lo estoy", "No, en realidad si xdd",]
                ],
                [
                 r"chao|bye|adios",
                 ["Bye","Fue un gusto hablar contigo", "chao", "adios, te extrañare",]
              ],
              ]

              return pairs
