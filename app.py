import os 

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
    input('Press any key to return to menu')
    main()

def end_app():
    os.system('cls')
    print('Closing app...')
    print()
    
def chose_options():
    try:
        choosen_option = int(input('Choose one option: '))
        if choosen_option == 1:
            print('Register restaurant')
        elif choosen_option == 2:
            print('List restaurant')
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