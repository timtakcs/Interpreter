#Error

class Error:
    def __init__(self, name, details):
        self.details = details
        self.name = name

    def asString(self):
        message = f'{self.name}: {self.details}\n'
        return message

class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__("Illegal Char", details)

class IllegalVariableDeclaration(Error):
    def __init__(self, details):
        super().__init__("Invalid Variable Declaration", details)

class IllegalFloatError(Error):
    def __init__(self, details):
        super().__init__("Illegal Float", details)

class InvalidSyntaxError(Error):
    def __init__(self, message, details):
        super().__init__(message, details)

class InvalidString(Error):
    def __init__(self, details):
        super().__init__("String literal isn't terminated", details)

class MissingVariableError(Error):
    def __init__(self, details):
        super().__init__("Variable has not been declared", details)

class IndexOutOfBoundsError(Error):
    def __init__(self, details):
        super().__init__("Index out of bounds", details)

class InvalidNumOfArgumentsError(Error):
    def __init__(self, details):
        super().__init__("Mismatch of arguments", details)

class DimensionExceededError(Error):
    def __init__(self, details):
        super().__init__("Dimension of array exceeded", details)

class InvalidFunctionCall(Error):
    def __init__(self, details):
        super().__init__("Invalid function call", details)

class MaxRecursionDepthExceeded(Error):
    def __init__(self, details):
        super().__init__("Max Recursion Depth Exceeded", details)




