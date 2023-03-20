class ProgrammingLanguage:
    class ProgrammingLanguage:
        def __init__(self, name):
            self.name = name

        def get_file_extension(self):
            pass


class PythonLanguage(ProgrammingLanguage):
    def __init__(self):
        super().__init__('Python')

    @staticmethod
    def get_file_extension():
        return '.py'


class JavaLanguage(ProgrammingLanguage):
    def __init__(self):
        super().__init__('Java')

    @staticmethod
    def get_file_extension():
        return '.java'


class CLanguage(ProgrammingLanguage):
    def __init__(self):
        super().__init__('C')

    @staticmethod
    def get_file_extension():
        return '.c'


class CppLanguage(ProgrammingLanguage):
    def __init__(self):
        super().__init__('C++')

    @staticmethod
    def get_file_extension():
        return '.cpp'
