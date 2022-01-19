import actions
import pyfiglet

result = pyfiglet.figlet_format("Password Manager")

while True:
    actions.clean_screen()
    
    print(result)

    req = input('''\n\n
Press 1 : Add new credentials
Press 2 : Fetch password
Press e : to exit
Enter : ''')
    print()
    if req == '1':
        actions.credentials_feeder()
    elif req == '2':
        actions.pass_fetcher()
    elif req == 'e':
        print('exiting....')
        break
    else:
        print('\nInvalid Input...!!')
    
    cont = input('wanna continue [y/n] : ')
    if cont == 'n':
        print('\nexiting....')
        break
    
    
    
