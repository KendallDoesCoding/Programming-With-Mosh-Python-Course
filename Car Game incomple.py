command = ""
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        print('The car has started and it is ready to go tp your destination')
elif command =="stop":
            print('The car has stopped because it needs gas or you have reached your destination') 
            elif command == "help:":
                print(''"""
                start - to start the car
                stop - to stop the car
                quit - To quit the game
                """')
else:
    print("Sorry my programmer has not made me understand this feature.")
                
            
