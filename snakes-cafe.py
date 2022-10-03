
def welcome():
    welcome_message = """
    **********************************************
    *       Welcome to the Snackes Cafe!         *
    *       Please see our manu below.           *
    *                                            *
    *       To quit at any time, type "quit"     *   
    **********************************************
    """
    print(welcome_message)

def print_menu():    
    menu= [
        'Appetizers;Wings;Cookies;Spring Rolls',
        "Entrees ;Salmon;Steak;Meat Tornado;A Literal",
        "Desserts;Ice Cream;Cake;Pie",
        "Drinks;Coffee;Tea;Unicorn Tears"
    ]
    for item in menu:
        line = item.split(';')
        print('\n'+line[0]+ '\n' + "-"*len(line[0]))
        line.pop(0)
        for meal in line:
            print(meal)  

def ask_user() :
    ask="""
**********************************************
what would you like to order?  
**********************************************\n
"""
    print(ask)

def take_order():

    menu = ['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado'
    , 'a literal', 'ice cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']

    orders = [0  for i in range(len(menu))]  

    order = input('>')
    while (order != 'quit'):
        if (order.lower() not in menu):
            print (f'We dont have {order} yet in our menu')
        else:
            index = menu.index(order.lower())  
            orders[index] +=1
            meals = [idx for idx, val in enumerate(orders) if val != 0] 
            if (len(meals) == 1):
                firstIdx = meals[0]
                number = orders[firstIdx]
                meal = menu[firstIdx]
                print( f" { number } of {meal} have been added to your order") 

            if (len(meals) > 1):
                temp = ''
                for idx in meals:
                    number = orders[idx]
                    meal = menu[idx]
                    temp += f" and {number} of {meal}"
                print (f"{temp[4:]} have been added to your order")

        order = input('>')
    meals = [idx for idx, val in enumerate(orders) if val != 0] 
    print('Your final order is:')
    for idx in meals:
        number = orders[idx]
        meal = menu[idx]
        print(f'{number} of {meal}')
        
def init():
    welcome()
    print_menu()
    ask_user()
    take_order()

init()