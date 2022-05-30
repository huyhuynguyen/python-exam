import enum

class GuessText(enum.Enum):
    G = 'greater'
    L = 'less'

# if __name__ == '__main__':
#     string = 'G'
#     print(GuessText[string].value)
#     print([text.value for text in GuessText])
#     print(GuessText('greater').name)
#     print(GuessText.G.value)
#     print([GuessText(text.value).name for text in GuessText])