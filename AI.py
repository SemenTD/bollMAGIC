from random import choice

answers = [
    "Шар говорит 'нет'",
    "Шар говорит 'да'",
    "Шар молчит ...",
    "Шар говорит 'возможно'",
    "Шар в замешптельстве",
    "Шар говорит 'Точно да' "
]

def generate_answer():
    return choice(answers)