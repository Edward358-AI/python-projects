print("""
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")

print('Write how many cups of coffee you will need:')
cups = int(input())
print('For ', cups, ' cups of coffee you will need:')
print(cups * 200, ' ml of water')
print(cups * 50, ' ml of milk')
print(cups * 15, ' g of coffee beans')

print("Write how many ml of water the coffee machine has:")
water = int(input())
print("Write how many ml of milk the coffee machine has:")
milk = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
coffee_beans = int(input())
print("Write how many cups of coffee you will need:")
cups_coffee = int(input())


water = water // 200
milk = milk // 50
coffee_beans = coffee_beans // 15

if water <= milk and water <= coffee_beans:
    coffee = water
elif milk <= water and milk <= coffee_beans:
    coffee = milk
else:
    coffee = coffee_beans

if coffee > cups_coffee:
    extra = coffee - cups_coffee
    print('Yes, I can make that amount of coffee', '(and even', extra, 'more than that)')
elif coffee == cups_coffee:
    print('Yes, I can make that amount of coffee')
else:
    print('No, I can make only', coffee, 'cups of coffee')

wa = 400
mi = 540
cb = 120
dc = 9
mo = 550
action = 0
while action != exit:
    print("Write action (buy, fill, take, remaining, shutdown):")
    action = input()
    if action == 'buy':
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        answer = input()
        if answer == '1':
            if wa >= 250 and cb >= 16 and dc >= 1:
                print('I have enough resources, making you a coffee!')
                wa = wa - 250
                cb = cb - 16
                dc = dc - 1
                mo = mo + 4
            elif wa < 250:
                print('Sorry, not enough water.')
            elif cb < 16:
                print('Sorry, not enough coffee beans.')
            elif dc < 1:
                print('Sorry, not enough disposable cups.')
        elif answer == '2':
            if wa >= 350 and mi >= 75 and cb >= 20 and dc >= 1:
                print('I have enough resources, making you a latte!')
                wa = wa - 350
                mi = mi - 75
                cb = cb - 20
                dc = dc - 1
                mo = mo + 7
            elif wa < 350:
                print('Sorry, not enough water.')
            elif mi < 75:
                print('Sorry, not enough milk.')
            elif cb < 20:
                print('Sorry, not enough coffee beans.')
            elif dc < 1:
                print('Sorry, not enough disposable cups.')
        elif answer == '3':
            if wa >= 200 and mi >= 100 and cb >= 12 and dc >= 1:
                print('I have enough resources, making you a cappuccino!')
                wa = wa - 200
                mi = mi - 100
                cb = cb - 12
                dc = dc - 1
                mo = mo + 6
            elif wa < 200:
                print('Sorry, not enough water.')
            elif mi < 100:
                print('Sorry, not enough milk.')
            elif cb < 12:
                print('Sorry, not enough coffee beans.')
            elif dc < 1:
                print('Sorry, not enough disposable cups.')
        elif answer == 'back':
            continue

        print("Write how many ml of water do you want to add:")
        w = int(input())
        wa = wa + w
        print("Write how many ml of milk do you want to add:")
        m = int(input())
        mi = m + mi
        print("Write how many grams of coffee beans do you want to add:")
        b = int(input())
        cb = cb + b
        print("Write how many disposable cups do you want to add:")
        c = int(input())
        dc = c + dc

    elif action == 'take':
        print('I gave you', '$' + str(mo))
        mo = mo - mo
    elif action == 'remaining':
        print("The coffee machine has:")
        print(wa, "of water")
        print(mi, "of milk")
        print(cb, "of coffee beans")
        print(dc, "of disposable cups")
        print('$' + str(mo), "of money")
    elif action == 'shutdown' or 'shut down':
        break
