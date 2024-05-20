"""
Software for a coffee machine
3 flavours: espresso, latte, cappuccino
Program requirements:
1. Check report
2. Check if resources are sufficient
3. Process coins
4. Check transaction successful
5. Make coffee - deduct resources
"""
import data


def print_report(resources: dict) -> None:
    """
    Prints the available resources in the coffee machine
    :param resources: a dictionary representing the current resources in the machine
    :return: None
    """
    print(f"{data.WATER} = {resources[data.WATER]}ml")
    print(f"{data.MILK} = {resources[data.MILK]}ml")
    print(f"{data.COFFEE} = {resources[data.COFFEE]}g")
    print(f"{data.MONEY} = ${resources[data.MONEY]}")


def resources_enough(required_water: int, required_milk: int, required_coffee: int, resources: dict) -> bool:
    """
    Checks if the machine has the required amount of resources to make the coffee
    :param required_water: an integer for the amount of water needed in ml
    :param required_milk: an integer for the amount of milk needed in ml
    :param required_coffee: an integer for the amount of coffee needed in g
    :param resources: a dict for the amount of currently available resources
    :return: True if sufficient resources are available, False otherwise
    """
    enough_water = True
    enough_milk = True
    enough_coffee = True
    if resources[data.WATER] < required_water:
        print(f"Sorry not enough water!")
        enough_water = False
    if resources[data.MILK] < required_milk:
        print(f"Sorry not enough milk!")
        enough_milk = False
    if resources[data.COFFEE] < required_coffee:
        print(f"Sorry not enough coffee!")
        enough_coffee = False
    return enough_water and enough_milk and enough_coffee


def use_resources(required_water: int, required_milk: int, required_coffee: int, resources: dict) -> dict:
    resources[data.WATER] -= required_water
    resources[data.MILK] -= required_milk
    resources[data.COFFEE] -= required_coffee
    return resources


def collect_money(money_owed: float) -> float:
    total = 0
    quarters = int(input("How many quarters (25 cents)?: "))
    total += quarters * data.QUARTER
    if total >= money_owed:
        return round(total, 2)
    dimes = int(input("How many dimes (10 cents)?: "))
    total += dimes * data.DIME
    if total >= money_owed:
        return round(total, 2)
    nickels = int(input("How many nickels (5 cents)?: "))
    total += nickels * data.NICKEL
    if total >= money_owed:
        return round(total, 2)
    pennies = int(input("How many pennies (1 cent)?: "))
    total += pennies * data.PENNY
    return round(total, 2)


def calculate_refund(provided: float, cost: float) -> float:
    return round(provided - cost, 2)


def main():
    resources = data.INITIAL_RESOURCES
    turned_off = False

    while not turned_off:

        choice = ""
        while (choice != data.ESPRESSO and choice != data.LATTE and choice != data.CAPPUCCINO and choice != data.OFF
               and choice != data.REPORT):
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == data.OFF:
            turned_off = True
        elif choice == data.REPORT:
            print_report(resources=resources)
        else:
            # a coffee type has been chosen
            required_water = data.MENU[choice][data.INGREDIENTS][data.WATER]
            required_milk = data.MENU[choice][data.INGREDIENTS][data.MILK]
            required_coffee = data.MENU[choice][data.INGREDIENTS][data.COFFEE]
            if resources_enough(required_water=required_water, required_milk=required_milk,
                                required_coffee=required_coffee, resources=resources):
                # request money
                print(f"For an {choice}, your total will be ${data.MENU[choice][data.COST]}")
                money_provided = collect_money(money_owed=data.MENU[choice][data.COST])
                print(f"Money acquired = ${money_provided}")
                if money_provided < data.MENU[choice][data.COST]:
                    print("Insufficient amount. Money refunded.")
                else:
                    print("Thank you!")
                    refund = calculate_refund(provided=money_provided, cost=data.MENU[choice][data.COST])
                    print(f"Money refunded = ${refund}")
                    # add money to machine
                    resources[data.MONEY] += data.MENU[choice][data.COST]
                    # Now make the coffee
                    resources = use_resources(required_water=required_water, required_milk=required_milk,
                                              required_coffee=required_coffee, resources=resources)
                    print(f"Here is your {choice} ☕. Enjoy!")

    print("Coffee machine turned off. Replenishing milk, water and coffee resources . . .")
    print("Collecting the money inside the coffee machine . . .")
    print("Will be available shortly.")


if __name__ == "__main__":
    main()
