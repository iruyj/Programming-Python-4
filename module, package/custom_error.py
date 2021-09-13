class InvalidLengthError(Exception):
    def __init__(self, message):
        super.__init__(message)     #super-> Exception 생성자에 넣는다

