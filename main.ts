// Created by: Nina Mathew
// Created on: 10/5/20
// This program finds the area and perimeter of a trapezoid
game.splash("Lets calculate the area and perimeter of a trapezoid!")
let A_Base = game.askForNumber("Enter the A Base of the trapezoid")
let B_Base = game.askForNumber("Enter the B Base of the trapezoid")
let C_Base = game.askForNumber("Enter the C Base of the trapezoid")
let D_Base = game.askForNumber("Enter the D Base of the trapezoid")
let perimeter = A_Base + (B_Base + (C_Base + D_Base))
game.splash(convertToText(perimeter))
let height = game.askForNumber("Enter the Height of the trapezoid")
A_Base = game.askForNumber("Enter the A Base of the trapezoid")
B_Base = game.askForNumber("Enter the B Base of the trapezoid")
let Add_Base = A_Base + B_Base
let add_base2 = Add_Base / 2
let area = add_base2 * height
game.splash(convertToText(area))
game.splash("Done")
