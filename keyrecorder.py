import keyboard
keyboard.write ( "ACTIVATED" )
recorded = keyboard.record(until='alt + ctrl + shift + f12')
keyboard.play(recorded, speed_factor=10)