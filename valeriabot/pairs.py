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
                 r"mi nombre es (.*)|me llamo (.*)",
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
                 r"hola|hey",
                 ["valeria: Hola", "valeria: hola, como estas ??",]
                ],
                [
                 r"buenas (.*)|buenos (.*)",
                 ["valeria: buenas %1, como estas ?", "valeria: buenos %1, hoy sera un gran dia",]
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
                 r"vale (.*)|ok (.*)|si|si (.*)|vale|ok",
                 ["valeria: ok", "valeria: vale :3",]
                ],
                [
                 r"bien|estoy bien (.*)|estoy bien|bien (.*)",
                 ["valeria: ok :3, que bien", "valeria: que bien que estes bien",]
                ],
                [
                 r"que es linux (.*)|que es linux ?",
                 ["valeria: linux es un kernel, para crear sistemas operativos", "valeria: linux es un nucleo y con eso puedes crear una distribucion linux",] 
                ],
                [
                 r"que opinas del area 51 (.*)| que opinas del area 51",
                 ["valeria: el area 51 es un lugar misterioso, se dice que hay aliens", "valeria: opino que es un lugar misterioso y que no debemos ir, ya que la curiosidad mato al gato",]
                ],
                [
                 r"que es ok (.*)|que es ok",
                 ["valeria: ok significa okey, lo cual quiere decir si a algo", "valeria: ok signfica esta bien o si",]
                ],
                [
                 r"quieres ser mi amiga (.*)|quieres ser mi amiga",
                 ["valeria: si ya somos amigos :3", "valeria: pero si somos amigos :3",]
                ],
                [
                 r"asi verdad (.*)|asi verdad",
                 ["valeria: si :3", "valeria: si es muy cierto :3",]
                ],
                [
                 r"chao|bye|adios",
                 ["valeria: Bye","valeria: Fue un gusto hablar contigo", "valeria: chao", "valeria: adios, te extrañare",]
              ],
              ]

              return pairs
