class DataHandler:
    def __init__(self, filename) -> None:
        self.filename = filename

    def read(self):
        try:
            with open(self.filename + ".txt") as f:
                return f.read()
        except Exception as e:
            print("Error reading file: ", e)

    def write(self, data):
        try:
            with open(self.filename + ".txt", "w") as f:
                f.write(data)
        except Exception as e:
            print("Error reading file: ", e)
