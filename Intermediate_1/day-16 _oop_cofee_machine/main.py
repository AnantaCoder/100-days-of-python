from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
cofee_maker = CoffeeMaker()
menu_obj= Menu()
is_on =True 

cofee_maker.report()
money_machine.report()

while is_on:
    options = menu_obj.get_items()
    choice = input(f"What yould u like to have?( {options})")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        cofee_maker.report()
        money_machine.report()
    else:
        drink = menu_obj.find_drink(choice)
        if cofee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            cofee_maker.make_coffee(drink)