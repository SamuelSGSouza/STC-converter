from stc import STC

stc = STC(start_command="computer", lang="en-US")
stc.add_command("", lambda: print("Hello World"), ["hello", "hi", "hey"])



if __name__ == "__main__":
    stc.run()