# Perform an action based on a key press.
# Copied from https://www.geeksforgeeks.org/how-to-detect-if-a-specific-key-pressed-using-python/

import keyboard
 
while True:
   
    print(keyboard.read_key())
    if keyboard.read_key() == "a":
        break
