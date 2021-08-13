def greet(name):
    return 'Hello ' + name


greet('Xhanti')


def greet_in_lang(lang, name):
    if lang == 'es':
        return 'Hola ' + name
    elif lang == 'fr':
        return 'Bonjour ' + name
    else:
        return 'Hello'


greet_in_lang('es', 'Andre')
