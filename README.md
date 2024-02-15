# STC-converter
A python library that converts speak to python commands

## Installation
```bash
git clone https://github.com/SamuelSGSouza/STC-converter.git
```

## Usage
```python
from STC import STC

stc = STC(start_word="computer", language="en")

stc.add_command(function=print, commands=["print", "write",])

stc.run()
```
Now, when you say "computer, write hello world", the program will print "hello world"

## Limitations
- The library is not perfect, so it may not work as expected
- The library will only work with one command at a time


## Dependencies
- SpeechRecognition
- PyAudio
- Nltk

## How to use

### Start Command
The start command is the word that the program will listen to start the command. For example, if you set the start command to "computer", the program will only listen to commands after you say "computer". You must say the start command before every command.
#### Example
```python
from STC import STC

stc = STC(start_word="computer", language="en")

stc.add_command(function=print, commands=["print", "write",])

stc.run()
```
Now, when you say "computer, write hello world", the program will print "hello world". But if you say "write hello world", the program will not do anything.
**Importante:**: The start command must be one word.

### Language
The language is the language that the program will listen to. At the moment, the library only supports English and Portuguese and the default language is English. The language must be set to "en-US" for English and "pt-BR" for Portuguese.

#### Example
```python
from STC import STC

stc = STC(start_word="computer", language="en-US")

stc.add_command(function=print, commands=["print", "write",])

stc.run()
```

### Add Command
The add command method is used to add a command to the program. The function parameter is the function that will be called when the command is said. The commands parameter is a list of words that the program will listen to call the function. The program will not only listen to the exact words in the list, but also to similar words. For example, if you add the command "print" and say "printer", the program will call the function. To define the similarity of the words, the library uses the Levenshtein distance algorithm.

#### Example
```python
from STC import STC

def open_file(file_name):
    with open(file_name, "r") as file:
        print(file.read())

stc = STC(start_word="computer", language="en-US")

stc.add_command(function=open_file, commands=["open", "read", "show", "print"])

stc.run()
```

### Context Definition
As long as you add functions to the program, maybe you need to add functions with the same name but with different contexts. For example, you may want to add a function to print a text and another function to print a number. To do that, you can use the context parameter. The context parameter is a string that will be used to define the context of the command. The context parameter is optional and the default value is "".

When setting the STC object, you can set the context keyword that will be used to define the context of the command. The context keyword is optional and the default value is "using context". That way, when you say the start command, the program will listen to the context keyword to define the context of the command.
#### Example
```python
from STC import STC

class OpenFile:
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        with open(self.file_name, "r") as file:
            print(file.read())

stc = STC(start_word="computer", language="en", context_keyword="use context")

stc.add_command(function=OpenFile.open_file, commands=["open", "read", "show", "print"], context="open file")

```
Now, when you say "computer, use context open file, open file", the program will call the function. But if you say "computer, use context open file, print", the program will not do anything.
**Importante:**: The context keyword can be one or more words, but it must be followed by the context of the command.
