from stc import STC

def open_file(file_name):
    with open(file_name, "r") as file:
        print(file.read())

def printer(text):
    print(text)

stc = STC(start_command="computer", lang="en-US", context_definer="using")

stc.add_command(function=open_file, commands=["open", "read", "show"], context="file")
stc.add_command(function=printer, commands=["print"], context="printer")

stc.run()