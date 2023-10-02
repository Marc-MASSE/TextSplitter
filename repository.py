class Repository:
    def __init__(self, path):
        self.path = path

    def text_reader(self):
        try:
            with open(self.path, 'r', encoding='utf-8') as file:
                # To read all lines from the file and store them in a list
                lines = file.readlines()
                # To concatenate all lines into a single string
                text = ''.join(lines)
                return text

        except FileNotFoundError:
            print(f"The file '{self.path}' was not found.")
            return None


