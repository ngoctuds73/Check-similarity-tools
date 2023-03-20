class ProgrammingLanguage:
    def __init__(self, name, file_extension):
        self.name = name
        self.file_extension = file_extension

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_file_extension(self):
        return self.file_extension

    def set_file_extension(self, file_extension):
        self.file_extension = file_extension

    def __str__(self):
        return f"{self.name}.{self.file_extension}"


class ProgrammingLanguageChecker:
    def __init__(self, filename):
        self.filename = filename

    def get_file_extension(self):
        return self.filename

    def check_language(self):
        ext = self.get_file_extension()
        if ext == "py":
            return ProgrammingLanguage("Python", ext)
        elif ext == "js":
            return ProgrammingLanguage("JavaScript", ext)
        elif ext == "java":
            return ProgrammingLanguage("Java", ext)
        elif ext == "cpp" or ext == "cc" or ext == "cxx":
            return ProgrammingLanguage("C++", ext)
        elif ext == "c":
            return ProgrammingLanguage("C", ext)
        else:
            return None
