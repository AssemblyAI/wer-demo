import string
import num2words


def expand_integer_symbols(text):
    tokens = text.split()
    new_tokens = []
    for token in tokens:
        try:
            expanded = num2words.num2words(int(token))
        except (TypeError, ValueError):
            new_tokens.append(token)
        else:
            expanded = expanded.replace('-', ' ')
            new_tokens.append(expanded)
    return ' '.join(new_tokens)


def normalize(text):
    text = text.lower()
    text = text.translate(None, string.punctuation)
    text = expand_integer_symbols(text)
    return text
