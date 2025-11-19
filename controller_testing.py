import pygame
import time

# --- Init pygame & joystick system ---
pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("❌ No controller detected. Plug one in and try again.")
    quit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"✅ Detected controller: {joystick.get_name()}")
print(f"   Axes: {joystick.get_numaxes()}")
print(f"   Buttons: {joystick.get_numbuttons()}")
print(f"   Hats (D-pads): {joystick.get_numhats()}")
print("\nMove sticks / press buttons. Press Ctrl+C to quit.\n")

try:
    while True:
        # Process internal pygame events
        pygame.event.pump()

        # Read all axes (analog sticks / triggers)
        axes = [round(joystick.get_axis(i), 3)
                for i in range(joystick.get_numaxes())]

        # Read all buttons (0 or 1)
        buttons = [joystick.get_button(i)
                   for i in range(joystick.get_numbuttons())]

        # Read all hats (D-pad)
        hats = [joystick.get_hat(i)
                for i in range(joystick.get_numhats())]

        # Print on one line so it just updates in place
        print(f"Axes: {axes}  Buttons: {buttons}  Hats: {hats}    ",
              end="\r", flush=True)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nExiting.")
finally:
    joystick.quit()
    pygame.joystick.quit()
    pygame.quit()
# how to use: in terminal, navigate to the directory where this script is saved and run:
# python controller_testing.py