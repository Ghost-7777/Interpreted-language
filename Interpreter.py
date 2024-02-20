class SimpleScriptInterpreter:
    def __init__(self):
        self.variables = {}

    def run(self, code):
        lines = code.split("\n")
        for line in lines:
            line = line.strip()
            if line.startswith("print"):
                self.handle_print(line)
            elif line.startswith("input"):
                self.handle_input(line)
            elif "=" in line:
                self.handle_assignment(line)

    def handle_assignment(self, line):
        var_name, value = line.split("=")
        var_name = var_name.strip()
        value = value.strip()
        self.variables[var_name] = value

    def handle_print(self, line):
        parts = line.split(" ", 1)
        to_print = parts[1].strip()
        if to_print[0] == '"' and to_print[-1] == '"':
            print(to_print[1:-1])
        elif to_print in self.variables:
            print(self.variables[to_print])
        else:
            try:
                print(eval(to_print, self.variables))
            except (NameError, SyntaxError):
                print("Invalid expression:", to_print)

    def handle_input(self, line):
        var_name = line.split(" ", 1)[1].strip()
        user_input = input()
        self.variables[var_name] = user_input


if __name__ == "__main__":
    interpreter = SimpleScriptInterpreter()

    helloworld = """
    print "Hello, world!"
    """

    multiply = """
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    result = num1 + num2
    print ("Result:", result)
    """

    repeater = """
    char = input("Enter a character: ")
    times = input("Enter number of times to repeat: ")
    print char * int(times)
    """

    programs = {
        "helloworld": helloworld,
        "multiply": multiply,
    }

    selected_program = input("Enter the name of the program you want to run: ")

    if selected_program in programs:
        interpreter.run(programs[selected_program])
    else:
        print("Program not found.")
