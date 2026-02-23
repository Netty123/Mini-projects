# Калькулятор

def calculator():

    while True:

        number_1 = float(input('Введите первое число: '))
        operator = input('Введите оператор для вычисления(+, -, *, /): ')
        number_2 = float(input('Введите второе число: '))

        if operator == '+':
            print(number_1 + number_2)
            break
        elif operator == '-':
            print(number_1 - number_2)
            break
        elif operator == '*':
            print(number_1 * number_2)
            break
        elif operator == '/':
            if number_2 == 0:
                print('Ошибка! На 0 делить нельзя!')
            else:
                print(number_1 / number_2)
            break
        else:
            print('Ошибка! Повторите заново\n')
            

calculator()

