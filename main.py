dialogInteraction = ['Добрый день! Здесь Вы можете рассчитать сумму, которую должны откладывать, чтобы накопить на цель.',
                    'Пожалуйста, выберите один из пунктов, который подходит вам:\n1. Накопления по месяцам\n2. Накопления по дням',
                    'Теперь введите сумму в рублях, которую вам необходимо накопить']

userMainChoose = 0
userMoneyInput = 'a'

print(dialogInteraction[0])
print(dialogInteraction[1])

while (userMainChoose != '1' and userMainChoose != '2'):
    userMainChoose = input()
    if (userMainChoose != '1' and userMainChoose != '2'):
        print('Такого пункта нет, попробуйте ещё раз.')
        print(userMainChoose)

print(dialogInteraction[2])

while (userMoneyInput.isdigit):
    userMoneyInput = input()
    if (userMoneyInput.isdigit):
        print('Вы ввели неправильное число, попробуйте ещё раз')

