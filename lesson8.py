import random


class Loto:
    def __init__(self):
        self.keg_sequence = random.sample(list(range(1, 91)), 90)

    @staticmethod
    def get_card():
        card = []
        numbers = random.sample(list(range(1, 91)), 15)
        for stroka in range(3):
            card.append(numbers[stroka * 5:(stroka + 1) * 5])
            card[stroka].sort()
            for rand_null in range(4):
                null_pos = random.randint(1, 6 + rand_null)
                card[stroka].insert(null_pos, '')
        return card

    @classmethod
    def print_card(cls, card):
        for stroka in range(3):
            print(''.join(str(card[stroka][i]).rjust(3, ' ') for i in range(9)))
        print('-' * 27)

    def get_keg(self):
        keg = self.keg_sequence[len(self.keg_sequence) - 1]
        self.keg_sequence.pop(len(self.keg_sequence) - 1)
        return keg, len(self.keg_sequence)

    @classmethod
    def alter_card(cls, card, n):
        flag_str = 'n'
        flag_num = 0
        for i in range(3):
            for j in range(9):
                if str(card[i][j]) == str(n):
                    flag_str = 'y'
                    flag_num = 1
                    card[i][j] = '-'
        return flag_str, flag_num

    @staticmethod
    def game():
        l = Loto()
        comp_sum = 0
        your_sum = 0
        your_card = l.get_card()
        comp_card = l.get_card()
        print('{:-^27s}'.format('Ваша карточка'))
        l.print_card(your_card)
        print('{:-^27s}'.format('Карточка компьютера'))
        l.print_card(comp_card)
        if input('С каждым новым ходом выпадает новый бочонок.\nЕсли хотите зачеркнуть ячейку - нажмите \'y\'.'
                 ' Если не хотите - нажмите \'n\'. \nНачать игру? (y/n) ').upper() != 'Y':
            print('Игра закончена. У Вас техническое поражение.')
        else:
            while True:
                k, sq_len = l.get_keg()
                print(f"Новый бочонок: {k} (осталось {sq_len})")
                print('{:-^27s}'.format('Ваша карточка'))
                l.print_card(your_card)
                print('{:-^27s}'.format('Карточка компьютера'))
                l.print_card(comp_card)
                comp_answer_str, comp_answer_num = l.alter_card(comp_card, k)
                real_answer_str, real_answer_num = l.alter_card(your_card, k)
                your_answer = input('Зачеркнуть цифру? (y/n) ')
                if your_answer.upper() == real_answer_str.upper():
                    your_sum += real_answer_num
                    comp_sum += comp_answer_num
                    if your_sum == 15 and comp_sum == 15:
                        print('Игра закончена. Ничья.')
                        break
                    elif your_sum == 15:
                        print('Игра закончена. Вы выиграли!')
                        break
                    elif comp_sum == 15:
                        print('Игра закончена. Вы проиграли.')
                        break
                elif your_answer.upper() != 'Y' and your_answer.upper() != 'N':
                    print('Игра закончена. У Вас техническое поражение.')
                    break
                else:
                    print('Игра закончена. Вы проиграли.')
                    break


Loto.game()
