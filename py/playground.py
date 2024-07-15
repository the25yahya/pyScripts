class ConsoleLogger():
    def __init__(self,message) :
        self.message = message
    def log(self):
        print(f"console print({self.message})")


class ErrorLoger():
    def __init__(self,error) :
        self.message = error
    def log(self):
        print(f"console error : ({self.error})")


class APP():
    def __init__(self,message,error) :
        self.console_logger = ConsoleLogger(message)
        self.error_logger = ErrorLoger(error)
    def log_error(self):
        self.console_logger.log()
    def log_error(self):
        self.error_logger.log()
