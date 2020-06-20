class CoffeeMachine:
    def __init__(self):
        self.amtWaterCurrent = 400
        self.amtMilkCurrent = 540
        self.amtCoffeeBeansCurrent = 120
        self.amtMoneyCurrent = 550
        self.amtDisposableCups = 9
        self.recipes = {
            1: {'name': 'espresso', 'amtWater': 250, 'amtMilk': 0, 'amtCoffee': 16, 'price': 4},
            2: {'name': 'latte', 'amtWater': 350, 'amtMilk': 75, 'amtCoffee': 20, 'price': 7},
            3: {'name': 'cappuccino', 'amtWater': 200, 'amtMilk': 100, 'amtCoffee': 12, 'price': 6}
        }

    def buy_coffee(self):
        user_selection = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if user_selection == 'back':
            pass
        else:
            user_selection = int(user_selection)
            self.process_order(user_selection)

    def fill_machine(self):
        new_water = int(input('Write how many ml of water do you want to add:'))
        new_milk = int(input('Write how many ml of milk do you want to add:'))
        new_coffee = int(input('Write how many grams of coffee beans do you want to add:'))
        new_cups = int(input('Write how many disposable cups of coffee do you want to add:'))
        self.amtWaterCurrent += new_water
        self.amtMilkCurrent += new_milk
        self.amtCoffeeBeansCurrent += new_coffee
        self.amtDisposableCups += new_cups

    def take_money(self):
        print(f'I gave you ${self.amtMoneyCurrent}')
        self.amtMoneyCurrent = 0

    def process_order(self, selection):
        order_selected = self.recipes[selection]
        resources_lacking = self.check_resources(order_selected['amtWater'], order_selected['amtMilk'], order_selected['amtCoffee'], 1)
        if len(resources_lacking) == 0:
            print('I have enough resources, making you a coffee!')
            self.amtWaterCurrent -= order_selected['amtWater']
            self.amtMilkCurrent -= order_selected['amtMilk']
            self.amtCoffeeBeansCurrent -= order_selected['amtCoffee']
            self.amtDisposableCups -= 1
            self.amtMoneyCurrent += order_selected['price']
        else:
            print(f'Sorry, not enough {", ".join(resources_lacking)}')

    def print_state(self):
        print(f'The coffee machine has:\n{self.amtWaterCurrent} of water\n{self.amtMilkCurrent} of milk\n{self.amtCoffeeBeansCurrent} of coffee beans\n{self.amtDisposableCups} of disposable cups\n{self.amtMoneyCurrent} of money')

    def check_resources(self, water, milk, coffee, cups):
        # checks all resources, if its missing adds to list of missing.
        resource_lack = []
        if water > self.amtWaterCurrent:
            resource_lack.append('water')
        if milk > self.amtMilkCurrent:
            resource_lack.append('milk')
        if coffee > self.amtCoffeeBeansCurrent:
            resource_lack.append('coffee')
        if cups > self.amtDisposableCups:
            resource_lack.append('cups')
        return resource_lack


myCoffeeMachine = CoffeeMachine()
actions = {
    'buy': myCoffeeMachine.buy_coffee,
    'fill': myCoffeeMachine.fill_machine,
    'take': myCoffeeMachine.take_money,
    'remaining': myCoffeeMachine.print_state,
    'exit': exit
}

while True:
    actions[input('Write action (buy, fill, take, remaining, exit)')]()
