from datetime import datetime
def saludo_por_hora():
    hora = datetime.now().hour
    if hora < 12:
        return "¡Buenos días!"
    elif hora < 18:
        return "¡Buenas tardes!"
    else:
        return "¡Buenas noches!"



respuestas= {
    "hola": saludo_por_hora() ,
    "bien": "Me alegra oír eso :)",
    "mal": "Lo siento mucho espero que te mejores",
    "adiós": "¡Adiós!. Que tengas un buen dia",
    "que estas haciendo": "Esoy aquí para ayudarte",
    "que haces": "Esoy aquí para ayudarte",
    "gracias": "De nada, estoy aquí para ayudarte",
    "cuanto es: ": "La respuesta es: ",
    "print": "El comando 'print' se utiliza para imprimir cosas en la terminal solo tienes que poner: 'print('texto')' ",
    "input": "input(): Puedes preguntarle al usuario una pregunta paar que te reponda",
    "ingredientes de  espaguetis": "Necesitas pasta, tomate, ajo, albahaca y aceite de oliva. ¡Cocina la pasta y mezcla con la salsa de tomate!",
    "ingredientes de ensalada": "Corta lechuga, tomate, pepino, y adereza con aceite de oliva, vinagre y sal.",
    "ingredientes de panqueques": "Mezcla harina, azúcar, leche, huevo y cocina en una sartén caliente.",
    "que hora es": f"La hora actual es: {datetime.now().strftime('%H:%M:%S')}",
    "hora": f"La hora actual es: {datetime.now().strftime('%H:%M:%S')}",
    "que dia es hoy": f"Hoy es {datetime.now().strftime('%A, %d de %B de %Y')}",
    "dia": f"Hoy es {datetime.now().strftime('%A, %d de %B de %Y')}",
    "definicion de python": "Python es un lenguaje de programación interpretado, de alto nivel y orientado a objetos, conocido por su simplicidad y legibilidad.",
    "consejos para estudiar": "Es importante dividir tu tiempo en bloques, tomar descansos regulares y estudiar en un lugar tranquilo. ¡Tú puedes!",
    "cuál es tu color favorito": "No tengo colores favoritos, pero me gustan todos. ¿Y el tuyo?",
    "que pasaría si el sol dejara de brillar": "¡Sería el fin de la vida tal como la conocemos! Pero no te preocupes, el sol seguirá brillando por mucho tiempo más.",
    "como gestionar mi tiempo": "Usa la técnica Pomodoro: trabaja durante 25 minutos, luego toma un descanso de 5 minutos. Esto mejora la concentración y la productividad.",
    "como aprender un nuevo idioma": "Practica todos los días, empieza con frases simples, escucha música y ve películas en el idioma que estás aprendiendo.",
    "que es un algoritmo": "Un algoritmo es una secuencia de pasos o instrucciones que se siguen para resolver un problema o realizar una tarea.",
    "ejercicios para hacer en casa": "Puedes hacer sentadillas, flexiones, abdominales y saltos de tijera. ¡Haz 3 series de 15 repeticiones!",
    "como aprender a programar": "Te recomiendo empezar con Python, es un lenguaje fácil de aprender. Puedes usar sitios como Codecademy o freeCodeCamp.",
    "apps para estudiar": "Puedes probar aplicaciones como Anki para tarjetas de memoria, Quizlet para crear tus propios quizzes, o Evernote para tomar notas.",
    "cuantos metros en kilometro": "1 kilómetro = 1000 metros.",
    "cuantos litros son 1 metro cubico": "1 litro  = 1000000 metros cubicos.",
    "1 metro cubico cuantos litros son": "1 litro  = 1000000 metros cubicos.",




}

while True:
    entrada = input("Tú: ").lower()
    if entrada in respuestas:
        print("Bot: ", respuestas[entrada])
    else:
        print("Bot: No lo he entendido por favor repitalo")
    if entrada == "adiós":
        break
