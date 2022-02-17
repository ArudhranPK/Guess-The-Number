import random
strike = 4

while strike == 4:
    a = 0
    b = 0
    c = 0
    d = 0
    
    while a > 6 or b > 6 or c > 6 or d > 6 or a == b or a == c or a == d or b == c or b == d or c == d or a == 0 or b == 0 or c == 0 or d == 0:
        computer_number = random.randint(1234, 6543)
    
        d = computer_number % 10
        c = (computer_number % 100 - d) // 10
        b = (computer_number % 1000 - d - (c * 10)) // 100
        a = (computer_number % 10000 - d - (c * 10) - (b * 100)) // 1000
    
    print(a, b, c, d)
    chance = 1

    player_input = int(input(f'Enter the number. (Chance No.{chance}):'))

    strike = 0
    spare = 0

    while chance < 7:

        strike = 0
        spare = 0
    
        chance = chance + 1
    
        z = player_input % 10
        y = (player_input % 100 - z) // 10
        x = (player_input % 1000 - z - (y * 10)) // 100
        w = (player_input % 10000 - z - (y * 10) - (x * 100)) // 1000
                
        if w == a:
            strike = strike + 1
        
        if x == b:
            strike = strike + 1
        
        if y == c:
            strike = strike + 1
        
        if z == d:
            strike = strike + 1
        
        if w == b or w == c or w == d:
            spare = spare + 1
        
        if x == a or x == c or x == d:
            spare = spare + 1
        
        if y == a or y == b or y == d:
            spare = spare + 1
        
        if z == a or z == b or z == c:
            spare = spare + 1
        
        if chance == 7:
            print('You have lost the game!!!')
            break
        
        if strike == 4:
            print('You have won the game!!!')
            break
        
        print(f'Strike = {strike}')
        print(f'Spare = {spare}')
        
        player_input = int(input(f'Enter the number. (Chance No.{chance}):'))
        
    player_answer = str(input('Do you want to continue the game? (y/n):')).lower()
    player_answer_boolean = True

    while player_answer_boolean:

        if player_answer == 'n':
            print('Goodbye!')
            strike = 0
            player_answer_boolean = False
            break

        elif player_answer == 'y':
            print('Okay!')
            player_answer_boolean = False
            strike = 4
            
        else:
            print('Invalid input!')
            player_answer = str(input('Do you want to continue the game? (y/n):')).lower()