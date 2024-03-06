import os 

restaurants = ['Pizza Hut', 'Outback', 'Super Grill', 'Hazaki Sushi', 'KFC', 'McDonalds', 'Burguer King']

def show_program_name():
    print('𝚝𝚊𝚜𝚝𝚎 𝚎𝚡𝚙𝚛𝚎𝚜𝚜\n')

def show_options():
    print('1. Register restaurant')
    print('2. List restaurant')
    print('3. Activate restaurant')
    print('4. Exit\n')

def invalid_option():
    os.system('cls')
    print('Invalid option\n')
    return_to_menu()

def end_app():
    os.system('cls')
    print('Closing app...')
    print()

def return_to_menu():
    input('\nPress any key to return to menu ')
    main()

def register_new_restaurant():
    os.system('cls')
    print('New restaurant register\n')
    restaurant_name = input('Type the restaurant name that you want to register: ')
    restaurants.append(restaurant_name)
    print(f'\nThe restaurant {restaurant_name} has been registered successfully!\n')
    return_to_menu()
    
def list_restaurants():
    os.system('cls')
    print('Listing restaurants\n')
    for restaurant in restaurants:
        print(f'.{restaurant}')
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