import os


class DataHandler:
    def __init__(self, directory) -> None:
        self.directory = directory

    def read(self):
        return os.listdir()

    def write(self, filename, data):
        file_path = os.path.join(self.directory, filename + ".txt")

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("Empty\n")
        except Exception as e:
            print(f"Error: {e}")
