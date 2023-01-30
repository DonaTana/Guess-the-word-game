import random
word_list = ['яблоко', 'апельсин', 'ананас', 'грейпфрукт', 'лимон', 'бология', 'география', 'химия', 'астрономия', 'математика', 'гольф', 'регби', 'гандбол', 'биатлон', 'гимнастика', 'крот', 'страус', 'ленивец', 'тюлень', 'дикобраз', 'подсолнух', 'береза', 'пальма', 'баобаб', 'фиалка', 'лазанья', 'шарлотка', 'рассольник', 'ризотто', 'чизкейк']

def get_word():
  word = random.choice(word_list)
  return word()

def display_hangman(tries):
  stages = ['''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
  return stages[tries] 

def is_valid(lit):
  for i in lit:
    if i in 'йцукенгшщзхъфывапролджэячсмитьбю':
      return True
    else:
      return False
      break

def repeat_check(lit, tries, word, word_completion, guessed_letters, guessed_words, flag):
  if len(lit) == 1:
    if lit in guessed_letters:
      print('Вы уже называли эту букву')
      vvod(tries, word, word_completion, guessed_letters, guessed_words, flag)
    else:
      guessed_letters.append(lit)
  else:
    if lit in guessed_words:
      print('Вы уже называли это слово')
      vvod(tries, word, word_completion, guessed_letters, guessed_words, flag)
    else:
      guessed_letters.append(lit)

def hint(word, word_completion):
  ans = 0
  if input('Может быть вам нужна подсказка? да\нет: ') == 'да':
    print('Я могу предложить тебе две подсказки. 1. Я раскрою первую и последнюю буквы слова 2. Я подскажу, к какой категории относится загаданное слово. Что выберешь?')
    ans = int(input())
    if ans == 1:
      print(word[0]+word_completion[1:-1]+word[-1])
    elif ans == 2:
      if word in word_list[:5]:
        print('фрукты')
      elif word in word_list[5:10]:
        print('наука')
      elif word in word_list[10:15]:
        print('спорт')
      elif word in word_list[15:20]:
        print('животный мир')
      elif word in word_list[20:25]:
        print('растительный мир')
  else:
    print('Тогда продолжим)')
      


def vvod(tries, word, word_completion, guessed_letters, guessed_words, flag):
  while flag == 'next':
    lit = input('Ваш ход: ')
    if is_valid(lit) == True:
      repeat_check(lit, tries, word, word_completion, guessed_letters, guessed_words, flag)
      if word == lit:
        print('Слово угадано! Поздравляем!')
        flag = 'end'
      elif lit not in word:
        tries -= 1
        if tries == 0:
          print(display_hangman(tries))
          print('К сожалению, вы проиграли...')
          print('Это было слово', word)
          flag = 'end'
        else:
          print(display_hangman(tries))
          print('Неверно. У вас осталось', tries, 'попыток')
          hint(word, word_completion)
      else:
        print('Вы угадали букву: ', end='')
        for i in range(len(word)):
          if word[i] == lit:
            word_completion = word_completion[:i] + lit + word_completion[i+1:]
        print(word_completion)
        print('Вы можете попробовать угадать слово сразу, если хотите')
    else:
      print('С вашей буквой что-то не так. Попробуйте снова. ')
      vvod(tries, word, word_completion, guessed_letters, guessed_words, flag)
    if word == word_completion:
      print('Слово угадано! Поздравляем!')
      flag = 'end'
  

  
def play():
  word = random.choice(word_list)
  word_completion = '_' * len(word)
  guessed = False
  guessed_letters = []
  guessed_words = []
  tries = 6 
  flag = 'next'
  print('Давайте играть в угадайку слов!')
  print('У вас есть 6 попыток у гадать слово:', word_completion)
  print(display_hangman(tries))
  vvod(tries, word, word_completion, guessed_letters, guessed_words, flag)
      
play()
while input('Хотите сыграть еще раз?) (да/нет): ') == 'да':
  play()
print('Что ж... До скорой встречи!')