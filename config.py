from data import traduction, profit, resources
configProfit = profit
configResources = resources

def isResourceSufficient(order, resources):
    """Retorna True se há ingredientes o suficiente e False caso não haja."""
    for item in order:
        if order[item] >= resources[item]:
            print(f'Desculpaê, você não tem {traduction[item]} suficiente.')
            return False
    return True

def processCoins():
    """Processa o dinheiro inserido."""
    print('Por favor, me dê dinheiro...')
    total = int(input('Quantos centavos? (só os centavos, pô) ')) * 0.1
    total += int(input('Agora quantos reais?) '))
    return total

def isTransactionSuccessful(money, cost):
    """Retorna True se a transação foi feita com sucesso e False caso não tenha sido feita."""
    if money < cost:
        print('Vish... parece que você não tem dinheiro suficiente.')
        return False
    change = round(money - cost, 2)
    print(f'Isso custou R${cost}... Agora você tem R${change}')
    global configProfit
    configProfit += cost
    return True

def report():
    """Retorna quanto de cada ingrediente há disponível."""
    print(f"🚰 Água: {configResources['water']}ml")
    print(f"🥛 Leite: {configResources['milk']}ml")
    print(f"☕️ Café: {configResources['coffee']}g")
    print(f"🤑 Dinheiro usado: R${configProfit}")

def makeCoffee(name, order):
    for item in order:
        configResources[item] -= order[item]
    print(f'Aqui está o seu {name}! ☕️')

def restock():
    configResources['water'] = 300
    configResources['milk'] = 200
    configResources['coffee'] = 100
    print('Uia! Cafeteira reabastecida!')
