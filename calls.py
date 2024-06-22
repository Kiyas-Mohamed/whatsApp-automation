import pyautogui
import time
import os

# Ensure the script directory is the same as where the images are stored
script_dir = os.path.dirname(os.path.abspath(__file__))

def make_whatsapp_call():
    try:
        # Path to the call button image
        call_button_path = os.path.join(script_dir, 'call_button.png')
        if not os.path.exists(call_button_path):
            raise FileNotFoundError(f"Image not found: {call_button_path}")
        
        # Locate the Call button and click it
        call_button_location = pyautogui.locateCenterOnScreen(call_button_path)
        if call_button_location:
            pyautogui.click(call_button_location)
            print("Making a call...")
            return True
        else:
            print("Call button not found on the screen!")
            return False
    except Exception as e:
        print(f"Exception in make_whatsapp_call: {e}")
        return False

def end_whatsapp_call():
    try:
        # Path to the end call button image
        end_call_button_path = os.path.join(script_dir, 'end_call_button.png')
        if not os.path.exists(end_call_button_path):
            raise FileNotFoundError(f"Image not found: {end_call_button_path}")
        
        # Locate the End Call button and click it
        end_call_button_location = pyautogui.locateCenterOnScreen(end_call_button_path)
        if end_call_button_location:
            pyautogui.click(end_call_button_location)
            print("Ending the call...")
            return True
        else:
            print("End call button not found on the screen!")
            return False
    except Exception as e:
        print(f"Exception in end_whatsapp_call: {e}")
        return False

# Main loop
while True:
    call_made = make_whatsapp_call()
    if call_made:
        # Wait for the call to end. Adjust the duration as needed.
        call_duration = 10  # in seconds
        time.sleep(call_duration)
        
        call_ended = end_whatsapp_call()
        if call_ended:
            # Wait before making the next call
            wait_time_between_calls = 5  # in seconds
            time.sleep(wait_time_between_calls)
        else:
            # If the end call button is not found, break the loop
            break
    else:
        # If the call button is not found, break the loop
        break
