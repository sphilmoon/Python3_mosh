print('Enter "menu" for help')
command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start": 
        if started:
            print("The car is already revving!")
        else:
            started = True
            print("The car is revving")
    elif command == "stop":
        if not started:
            print("The car is already stopped!")
        else:
            started = False
        print("The car is stopped")
    elif command == "menu":
        print('''
Enter "start" to start the car.
Enter "stop" to stop the car.
Enter "quit" to exit the game.
        ''')
    elif command == "quit":
        break
    else:
        print("I don't understand that.")