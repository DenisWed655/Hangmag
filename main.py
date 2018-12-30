from random import choice

print('Добро пожаловать в игру "Виселица", введите "stop" - что бы закончить')
hangman = [
    [' _________'],
    ['|    |    '],
    ['|    0    '],
    ['|  -|||-  '],
    ['|    |    '],
    ['|   | |   ']
]

list_words = ['кот', 'эхолот', 'изображение', 'ленинград']

def game():
    random_word = choice(list_words)
    word = list(random_word)
    field_word = ['_'] * len(random_word)
    print(field_word)
    error_count = 0

    while error_count < len(hangman):
        user_char = input('Введите букву: ')

        if user_char in word:
            for i in range(word.count(user_char)):
                field_word[word.index(user_char)] = user_char
                word[word.index(user_char)] = '#'
            print(field_word)
            if '_' not in field_word:
                print('Поздравляю, Вы выиграли, было загадано слово: ', random_word)
                return
        else:
            error_count += 1
            print(field_word)
            for i in range(error_count):
                print(hangman[i])
    print('Вы проиграли, было загадано слово: ', random_word)

while True:
    if input('Начинаем игру?') == 'stop':
        print('Хмм, как жаль что ты уходишь:(')
        break
    game()
