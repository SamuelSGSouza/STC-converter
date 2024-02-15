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
stc = STC(start_word="computer", language="en")
```
**Importante:**: The start command must be one word.

### Language
The language is the language that the program will listen to. At the moment, the library only supports English and Portuguese and the default language is English. The language must be set to "en-US" for English and "pt-BR" for Portuguese.

#### Example
```python
stc = STC(start_word="computer", language="pt-BR")
```

### Add Command
The add command method is used to add a command to the program. The function parameter is the function that will be called when the command is said. The commands parameter is a list of words that the program will listen to call the function. The program will not only listen to the exact words in the list, but also to similar words. For example, if you add the command "print" and say "printer", the program will call the function. To define the similarity of the words, the library uses the Levenshtein distance algorithm.

#### Example
```python
stc.add_command(function=print, commands=["print", "write",])
```

### Context Definition
As long as you add functions to the program, maybe you need to add functions with the same name but with different contexts. For example, you may want to add a function to print a text and another function to print a number. To do that, you can use the context parameter. The context parameter is a string that will be used to define the context of the command. The context parameter is optional and the default value is "".