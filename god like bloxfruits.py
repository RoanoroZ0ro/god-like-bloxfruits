import pyautogui
from pynput.keyboard import Key, Listener
import time

pause = True  # Starts paused
running = True  # Script running
auto_click = False  # Auto-click toggle

hold_v_until = 0  # Timestamp to release 'v'
hold_c_until = 0  # Timestamp to release 'c'

def on_press(key):
    global pause, running, auto_click, hold_v_until, hold_c_until

    if key == Key.esc:  
        running = False  # Stop everything
        print("[Exit]")
        return False  

    elif key == Key.f12:  
        pause = not pause  # Toggle pause
        print("[Paused]" if pause else "[Resumed]")

def hold_v():
    """Automatically hold 'v' for 6 seconds once the script starts."""
    global hold_v_until
    pyautogui.keyDown('v')
    if hold_v_until == 0:
        hold_v_until = time.time() + 6 # Hold for 6 sec
        print("Holding 'v' for 6 seconds...")

def hold_c():
    """Manually hold 'c' for 3 seconds."""
    global hold_c_until
    pyautogui.keyDown('c')
    hold_c_until = time.time() + 3  # Hold for 3 sec
    print("Holding 'c' for 3 seconds...")

def main():
    global hold_v_until, hold_c_until

    print("Press [F12] to pause/resume, [ESC] to quit.")
    print("Press 'v' (6 sec), 'c' (3 sec), and 'a' for auto-click.")

    with Listener(on_press=on_press) as listener:
        while running:
            if not pause:
                # if hold_v_until == 0:
                hold_v()
                if time.time() >= hold_v_until:
                    pyautogui.keyUp('v')
                    hold_v_until = 0
                    print('key v press up...')
                    pyautogui.press('enter')
                    time.sleep(2)
                    
                    

                time.sleep(0.1)  # Small delay to prevent excessive CPU usage

        listener.stop()

if __name__ == "__main__":
    main()

