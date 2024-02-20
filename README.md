Instruction	Description
bowl Push 0 onto the stack
tournament	Duplicate the top value of the stack
pin	Add 1 to the top value of the stack
foul	Pops A and then B from the stack and pushes B - A to the stack
pull	Takes one character of input and pushes it's ascii code to the stack
spare	Pop the top value of the stack and print it as an ascii character
strike	Pop the top value of the stack and print it as an integer
check FEET n	Pop the top of the stack. If it is zero, jump to the nth line
points home	Pop the top of the stack and push it to the bottom
points travel	Remove the bottom value of the stack and push it to the top
fry	Terminate program execution
