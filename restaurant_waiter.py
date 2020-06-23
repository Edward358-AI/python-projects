print("Welcome to Edward's Serve-Anything Cafe! What would you like to order?")
print("We have: our specials, salad, pizza, chinese food, burgers")
print("Please choose an option from the menu above.")

our_favorites = "sushi, dumplings, buttermilk pancakes, buttermilk waffles, lasagna, fried rice, barbeque ribs, barbeque chicken wings, spaghetti and meatballs, macaroni and cheese, crossiant, steak dinner, lamb chop kebab" 
pizza = "Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy, Pepperoni, Cheese, Three-meat, Sausage, Hawaiian, barbeque pizza"
salad = "Caesar salad, Green salad, Tuna salad, Fruit salad, Chicken salad, potato salad"
Chinese_food = "Dumplings, stir-fried noodles, Roasted duck, Gyoza, Soy sauce braised pork, soy sauce braised fish, duck soup, chicken soup, spicy fish, dim sum, spare ribs, ramen noodle soup, noodle soup, beef udon, soup dumpling"
dessert = "Ice cream, Sundae, chocolate cake, vanilla cake, cold ice cream drink, moon cakes, banana split, macaroons, s'mores, lava cakes, slushies, fortune cookies"
drinks = "soft drink, water, coffee, tea, hot cocoa, apple juice, orange juice, boba tea, pinapple juice, root beer, wine, beer, lemonade, strawberry lemonade"
burgers = "cheeseburger, double-double, 3*3, hamburger, veggie, 4*4, 5*5, 6*6, double cheese, triple cheese, mix n' match"
sides = "french fries, fruit cup, cup of corn, chips, onion rings, chicken strips, animal fries, hash brown"
a = input()

if a == 'our specials' or a == 'specials':
    print(our_favorites)
    if input() in our_favorites:
        print("Ok.")
    else:
        print("Sorry, we don't have that in our specials")

if a == 'pizza':
    print(pizza)
    if input() in pizza:
        print("Ok.")
    else:
        print("Sorry, we don't have that kind of pizza")

if a == 'salad':
    print(salad)
    if input() in salad:
        print("Ok.")
    else:
        print("Sorry, we don't have that kind of salad")

if a == 'chinese food':
    print(Chinese_food)
    if input() in Chinese_food:
        print("Ok.")
    else:
        print("Sorry, we don't have that kind of Chinese food")

if a == 'burgers':
    print(burgers)
    if input() in burgers:
        print("Ok.")
    else:
        print("Sorry, we don't have that kind of burger")

print("Do you want any sides to go with that?")
        
if input() == 'yes':
    print(sides)
    if input() in sides:
        print("Ok.")
    else:
        print("Sorry, we don't have that.")
        
print("Would you like any drinks?")

if input() == "yes":
    print(drinks)
    if input() in drinks:
        print("Ok.")
    else:
        print("Sorry, we don't have that drink")

print("Would you also like any dessert?")

if input() == 'yes':
    print(dessert)
    if input() in dessert:
        print("Ok.")
    else:
        print("Sorry, we don't have that kind of dessert")

print("Can I get anything else for you? Please choose one from the list below. If you don't want anything else, just say no.")
print("We have salad, pizza, chinese food, burgers, sides, dessert, or drinks")
b = input()

if b == 'pizza':
    print(pizza)
    if input() in pizza:
        print("Ok. Your order is placed.")
    else:
        print("Sorry, we don't have that.")
elif b == 'salad':
    print(salad)
    if input() in salad:
        print("Ok. Your order is placed.")
    else:
        print("Sorry, we don't have that kind of salad")
elif b == 'chinese food':
    print(Chinese_food)
    if input() in Chinese_food:
        print("Ok. Your order is placed.")
    else:
        print("Sorry, we don't have that kind of Chinese food")
elif b == 'burgers':
    print(burgers)
    if input() in burgers:
        print("Ok. Your order is placed.")
    else:
        print("Sorry, we don't have that kind of burger")
elif b == 'sides':
    print(sides)
    if input() in sides:
        print("Ok. Your order is placed.")
    else:
        print("Sorry, we don't have that.")
elif b == 'drinks':
    print(drinks)
    if input() in drinks:
        print("Ok. Your order is placed.")
    else:
        print("Sorry, we don't have that drink")
elif b == 'no':
    print("Ok. Your order is placed! Thank you!")

