print(''' Help
start - to start the car
stop - to stop the car
quit - to exit''')
command = ''
started = False
while True:
    command = input('What do you want to do with the car now? ').lower()
    if command == 'start':
        if started:
            print('Car is already started, you dumb fuck!')
        else:
            started = True
            print('Car has started!')
    elif command == 'stop':
        if started:
            print('Car stopped!')
            started = False
        else:
            print('Car has already stopped!')
    elif command == 'quit':
        print('You left the car. Good bye!')
        break
    else:
        print("I don't understand that, please try again!")