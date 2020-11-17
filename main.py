from objective import Objective

dialog_interaction = ['Добрый день! Здесь Вы можете рассчитать сумму, которую должны откладывать, чтобы накопить на цель.',
                    'Пожалуйста, выберите один из пунктов, который подходит вам:\n1. Накопления по месяцам\n2. Накопления по дням',
                    'Вам нужно выбрать название для вашей цели накопления.', 'Теперь введите сумму в рублях, которую вам необходимо накопить.']

user_main_choose = 0
user_amount_input = ''
user_name_input = ''
objectives = []
obj_id = 0

print(dialog_interaction[0])

while (True):

    print(dialog_interaction[1])

    while (True):
        user_main_choose = input()
        if (user_main_choose != '1' and user_main_choose != '2'):
            print('Такого пункта нет, попробуйте ещё раз.')
        else:
            break

    print(dialog_interaction[2])
    
    user_name_input = input()

    print(dialog_interaction[3])

    while (True):
        user_amount_input = input()
        if (not user_amount_input.isdigit()):
            print('Вы ввели неправильное число, попробуйте ещё раз')
        else:
            break

    obj = Objective(obj_id, user_name_input, user_amount_input)
    objectives.append(obj)
    obj_id += 1
    for i in objectives:
        print(i)