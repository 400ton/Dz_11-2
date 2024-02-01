
def return_string(value):
    """возвращает строку регистром"""
    return value.upper()

def capital_letters(value):
    """делает заглавными первые буквы каждого слова в строке, поступившей на вход"""
    return ' '.join(word.capitalize() for word in value.split())

