class Calculator:

    def __init__(self, default_number = 345):
        self.number = 12345
        self.default_number = default_number

    def self_function(self):
        return 'hello world'


calculator = Calculator()

print(calculator.number)
print(calculator.default_number)
print(calculator.self_function())

calculator_two = Calculator(default_number=10)
print(calculator_two.number)
print(calculator_two.default_number)
