class InputOutputString:
    def __init__(self):
        self.sequence_input=''
    def getString(self):
        self.sequence_input = input("Enter values: ")

    def printString(self):
        print(self.sequence_input.upper())

A = InputOutputString()
A.getString()
A.printString()
