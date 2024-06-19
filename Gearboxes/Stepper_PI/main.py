#-------------------------------------- Library Import ---------------------------------------------
from DRV8825 import DRV8825
import sys
import time

dir_pin_M1 = 13
step_pin_M1 = 19
enable_pin_M1 = 12
speed = 150

def main():
    # Vérifie que deux arguments ont été fournis (en plus du nom du script)
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <number> <string>")
        sys.exit(1)

    # Récupère les arguments
    steps = sys.argv[1]
    dir = sys.argv[2]
    
    # Affiche les arguments
    print(f"Stepper rotation of {steps} steps")
    print(f"Rotating : {dir}")
    
    Motor1 = DRV8825(dir_pin=dir_pin_M1, step_pin=step_pin_M1, enable_pin=enable_pin_M1)
    time.sleep(1)

    
    # Motor1.MoveTo(steps=2000, speedRPM=speed)
    Motor1.TurnStep(dir, int(steps), speed)
    

if __name__ == "__main__":
    main()
