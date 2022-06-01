import enum

class GuessText(enum.Enum):
    G = 'greater'
    L = 'less'

if __name__ == '__main__':
    # get list values
    print([text.value for text in GuessText])

    # get key
    print(GuessText('greater').name)

    # get value
    print(GuessText.G.value)

    # get list keys
    print([GuessText(text.value).name for text in GuessText])