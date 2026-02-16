import os


class DataHandler:
    def __init__(self, directory) -> None:
        self.directory = directory

    def read(self):
        return os.listdir()

    def write(self, filename, data):
        file_path = os.path.join(self.directory, filename)

        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(data)
        except Exception as e:
            print(f"Error: {e}")

    def read_file(self, filename) -> str:
        try:
            file_path = os.path.join(self.directory, filename)

            with open(file_path, "r") as f:
                return f.read()

        except Exception as e:
            print(e)

        return ""
