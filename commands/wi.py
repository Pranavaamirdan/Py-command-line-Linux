# from PyDictionary import PyDictionary

# dictionary=PyDictionary("hotel","ambush","nonchalant","perceptive")
# 'There can be any number of words in the Instance'

# print(dictionary.printMeanings()) '''This print the meanings of all the words'''
# print(dictionary.getMeanings()) '''This will return meanings as dictionaries'''
# print (dictionary.getSynonyms())

# print (dictionary.translateTo("hi")) '''This will translate all words to Hindi'''
# from PyDictionary import PyDictionary

# word = input('The word to be helped with: ')
# print("hello")
# function = input('What type of a thesaurus do you want to apply: ')

# dictionary = PyDictionary()
# meaning = dictionary.meaning(word)
# print()

# from prompt_toolkit import prompt
# from prompt_toolkit.history import FileHistory
# from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
# from prompt_toolkit.completion import Completer, Completion
# import click
# from fuzzyfinder import fuzzyfinder
# from pygments.lexers.sql import SqlLexer

# SQLKeywords = ['select', 'from', 'insert', 'update', 'delete', 'drop']

# class SQLCompleter(Completer):
#     def get_completions(self, document, complete_event):
#         word_before_cursor = document.get_word_before_cursor(WORD=True)
#         matches = fuzzyfinder(word_before_cursor, SQLKeywords)
#         for m in matches:
#             yield Completion(m, start_position=-len(word_before_cursor))

# while 1:
#     user_input = prompt(u'SQL>',
#                         history=FileHistory('history.txt'),
#                         auto_suggest=AutoSuggestFromHistory(),
#                         completer=SQLCompleter(),
#                         lexer=SqlLexer,
#                         )
#     click.echo_via_pager(user_input)

from __future__ import print_function, unicode_literals
from PyInquirer import style_from_dict, Token, prompt, Separator
from PyDictionary import PyDictionary 
dictionary = PyDictionary()

word = input('The word to be helped with: ')

color = {
    "purple" : '\033[95m',
    "cyan" : '\033[96m',
    "darkcyan" : '\033[36m',
    "blue" : '\033[94m',
    "green" : '\033[92m',
    "yellow" : '\033[93m',
    "red" : '\033[91m',
    "end" : '\033[0m',
}

style = {
    "bold" : '\033[1m',
    "underline" : '\033[4m' ,
    "end" : '\033[0m'
} 

style = style_from_dict({
    Token.Separator: '#cc5454',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#cc5454',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#f44336 bold',
    Token.Question: '',
})

questions = [
    {
        'type': 'list',
        'message': 'Select the type of a thesaurus do you want to apply:',
        'name': 'thesaurus',
        'choices': [
            Separator('The Thesaurus Type'),
            {
                'name': 'Meaning'
            },
            {
                'name': 'Synonyms'
            },
            {
                'name': 'Antonyms'
            }
        ],
        'validate': lambda answer: 'You must choose at least one topping.' \
            if len(answer) == 0 else True
    }
]

answers = prompt(questions, style=style)

if answers["thesaurus"] == 'Meaning':
    meanings = dictionary.meaning(word)
    num = 1
    for meaning in meanings["Noun"]:
        # print(style["bold"] + num + style["end"] + color["cyan"] + meaning + color["end"])
        print(f'{num} - {meaning}')
        num += 1

elif answers["thesaurus"] == 'Synonyms':
    synonyms = dictionary.synonym(word)
    print(synonyms)
 