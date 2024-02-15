from STC import STC

class OpenFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        with open(self.file_name, "r") as file:
            print(file.read())

stc = STC(start_word="computer", language="en", context_keyword="use context")

stc.add_command(function=OpenFile.open_file, commands=["open", "read", "show", "print"], context="open")