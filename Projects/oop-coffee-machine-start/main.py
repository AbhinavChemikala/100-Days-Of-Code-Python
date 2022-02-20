from black import main
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

main_menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

coffee_types = main_menu.get_items()

order_name = input(f"What would you like? ({coffee_types}): ")
order_avail = main_menu.find_drink(order_name)
print(order_avail)
#resource_avail = coffee_machine.is_resource_sufficient(order_name)
#if resource_avail:
    #money_machine.make_payment(order_name)
coffee_machine.make_coffee(order_name)
#else:
print("Sorry, we are out of that coffee.")

print_report = coffee_machine.report()
print(print_report)