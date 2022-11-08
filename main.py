from data import MENU
from config import isResourceSufficient, processCoins, isTransactionSuccessful, report, configResources, makeCoffee, \
    restock

isOn = True

while isOn:
    choice = input('Qual é a boa hoje? (expresso/latte/cappuccino): ')
    if choice == 'off':
        isOn = False
    elif choice == 'diga':
        report()
    elif choice == 'mais':
        restock()
    else:
        drink = MENU[choice]
        if isResourceSufficient(drink['ingredients'], configResources):
            payment = processCoins()
            isTransactionSuccessful(payment, drink['cost'])
            makeCoffee(choice, drink['ingredients'])
