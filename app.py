import os 

restaurants = [{'name':'Pizza Hut', 'category':'Pizzeria', 'activation':True},
               {'name':'Outback', 'category':'Autralian', 'activation':False},
               {'name':'Super Grill', 'category':'Buffet', 'activation':True},
               {'name':'Hazaki Sushi', 'category':'Japanese', 'activation':True},
               {'name':'KFC', 'category':'Fried Chicken', 'activation':False},
               {'name':'McDonalds', 'category':'Fast Food', 'activation':True},
               {'name':'Burguer King', 'category':'Fast Food', 'activation':False}
]

def show_program_name():
    print('𝚝𝚊𝚜𝚝𝚎 𝚎𝚡𝚙𝚛𝚎𝚜𝚜\n')

def show_options():
    print('1. Register restaurant')
    print('2. List restaurant')
    print('3. Activate restaurant')
    print('4. Exit\n')

def invalid_option():
    show_subtittle('Invalid option')
    return_to_menu()

def end_app():
    show_subtittle('Closing app...')

def show_subtittle(text):
    os.system('cls')
    print(text)
    print()

def return_to_menu():
    input('\nPress any key to return to menu ')
    main()

def register_new_restaurant():
    show_subtittle('New restaurant register')
    restaurant_name = input('Type the restaurant name that you want to register: ')
    category = input(f'Type the {restaurant_name} category: ')
    restaurant_data = {'name':restaurant_name, 'category':category, 'activation':False}
    restaurants.append(restaurant_data)
    print(f'\nThe restaurant {restaurant_name} has been registered successfully!\n')
    return_to_menu()
    
def list_restaurants():
    show_subtittle('Listing restaurants')
    for restaurant in restaurants:
        restaurant_name = restaurant['name']
        restaurant_category = restaurant['category']
        restaurant_activation = restaurant['activation']
        print(f'- {restaurant_name} | {restaurant_category} | {restaurant_activation}')
    return_to_menu()
    
def chose_options():
    try:
        choosen_option = int(input('Choose one option: '))
        if choosen_option == 1:
            register_new_restaurant()
        elif choosen_option == 2:
            list_restaurants()
        elif choosen_option == 3:
            print('Activate restaurant')
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