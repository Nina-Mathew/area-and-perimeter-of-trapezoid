# Created by: Nina Mathew
# Created on: 10/5/20
# This program finds the area and perimeter of a trapezoid
game.splash("Lets calculate the area and perimeter of a trapezoid!")
A_Base = game.ask_for_number("Enter the A Base of the trapezoid")
B_Base = game.ask_for_number("Enter the B Base of the trapezoid")
C_Base = game.ask_for_number("Enter the C Base of the trapezoid")
D_Base = game.ask_for_number("Enter the D Base of the trapezoid")
perimeter = A_Base + (B_Base + (C_Base + D_Base))
game.splash(convert_to_text(perimeter))
height = game.ask_for_number("Enter the Height of the trapezoid")
A_Base = game.ask_for_number("Enter the A Base of the trapezoid")
B_Base = game.ask_for_number("Enter the B Base of the trapezoid")
Add_Base = A_Base + B_Base
add_base2 = Add_Base / 2
area = add_base2 * height
game.splash(convert_to_text(area))
game.splash("Done")