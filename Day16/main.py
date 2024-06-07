from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    print("Coffee machine in the OOP world")

    menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()

    turned_off = False

    while not turned_off:

        choice = "nothing"
        while choice not in menu.get_items() and choice != "off" and choice != "report":
            choice = input(f"What would you like? {menu.get_items()}: ").lower()

        if choice == "off":
            turned_off = True
        elif choice == "report":
            coffee_machine.report()
            money_machine.report()
        else:
            # A drink has been selected
            # check for resources availability
            drink = menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(drink):
                # then proceed to payment
                if money_machine.make_payment(drink.cost):
                    # then make the drink
                    coffee_machine.make_coffee(drink)


if __name__ == "__main__":
    main()
