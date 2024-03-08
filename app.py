import os 

restaurants = [{'name':'PIZZA HUT', 'category':'PIZZERIA', 'activation':True},
               {'name':'OUTBACK', 'category':'AUSTRALIAN', 'activation':False},
               {'name':'SUPER GRILL', 'category':'BUFFET', 'activation':True},
               {'name':'HAZAKI SUSHI', 'category':'JAPANESE', 'activation':True},
               {'name':'KFC', 'category':'FRIED CHICKEN', 'activation':False},
               {'name':'MCDONALDS', 'category':'FAST FOOD', 'activation':True},
               {'name':'BURGUER KING', 'category':'FAST FOOD', 'activation':False}
]

def show_program_name():
    print('𝚝𝚊𝚜𝚝𝚎 𝚎𝚡𝚙𝚛𝚎𝚜𝚜\n')

def show_options():
    print('1. Register restaurant')
    print('2. List restaurant')
    print('3. Toggle restaurant activation')
    print('4. Exit\n')

def invalid_option():
    show_subtittle('Invalid option')
    return_to_menu()

def end_app():
    show_subtittle('Closing app...')

def show_subtittle(text):
    os.system('cls')
    line = '-' * (len(text))
    print(line)
    print(text)
    print(line)
    print()

def return_to_menu():
    input('\nPress any key to return to menu ')
    main()

def register_new_restaurant():
    show_subtittle('New restaurant register')
    
    restaurant_name = input('Type the restaurant name that you want to register: ').upper()
    category = input(f'Type the {restaurant_name} category: ').upper()
    restaurant_data = {'name':restaurant_name, 'category':category, 'activation':False}
    restaurants.append(restaurant_data)
    print(f'\nThe restaurant {restaurant_name} has been registered successfully!\n')
    
    return_to_menu()
    
def list_restaurants():
    show_subtittle('Listing restaurants')

    header = f'| {'Restaurant name'.ljust(20)} | {'Category'.ljust(20)} | {'Status'.ljust(20)} |'
    line = '-' * (len(header))
    print(line)
    print(header)
    print(line)
    
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_activation = 'activated' if restaurant['activation'] else 'deactivated'
        
        print(f'| {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_activation.ljust(20)} |')    
    print(line)   
     
    return_to_menu()
    
def toggle_activation():
    show_subtittle('Toogle restaurant activation')
    
    restaurant_name = input('Type the name of the restaurant that you want to toggle the activation: ').upper()
    restaurant_found = False
    
    for restaurant in restaurants:
        if restaurant_name == restaurant['name']:
            restaurant_found = True
            restaurant['activation'] = not restaurant['activation']
            mesage = f'\nThe restaurant {restaurant_name} has been successfully activated'  if restaurant['activation'] else f'The restaurant {restaurant_name} has been successfully deactivated'
            print(mesage)
    if not restaurant_found:
        print('The restaurant was not found')
        
    return_to_menu()
    
def chose_options():
    try:
        choosen_option = int(input('Choose one option: '))
        if choosen_option == 1:
            register_new_restaurant()
        elif choosen_option == 2:
            list_restaurants()
        elif choosen_option == 3:
            toggle_activation()
        elif choosen_option == 4:
            end_app()
        else:
            invalid_option()
    except:
        invalid_option()

def main():
    os.system('cls')
    show_program_name()
    show_options()
    chose_options()
    
if __name__ == '__main__':
    main()