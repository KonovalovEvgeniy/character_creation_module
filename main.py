def attack(char_name: str, char_class: str) -> str:
    """Формируется атака."""
    ...


def defence(char_name: str, char_class: str) -> str:
    """Формируется защита."""
    ...


def special(char_name: str, char_class: str) -> str:
    """Формируются характеристики."""
    ...


def start_training(char_name: str, char_class: str) -> str:
    """Генерируются характеристики тренировки."""
    ...


def choice_char_class() -> str:
    """Выброр класса персонажа."""
    ...


def main():
    """Запуск программы."""
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
