class PythonFileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as f:
            file_text = f.read()
        return file_text
