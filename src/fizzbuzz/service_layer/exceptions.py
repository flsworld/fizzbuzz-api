class CannotCompute(Exception):
    def __init__(self, message="'Multiple of' inputs are identical"):
        self.message = message
        super().__init__(self.message)
