class Calculator:
    def __init__(self):
        self.expression = ''

    def input(self, char):
        if char == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
            except Exception:
                self.expression = 'Error'
        else:
            self.expression += char

    def reset(self):
        self.expression = ''