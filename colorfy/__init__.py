from os import system, name

ansi = "\u001b["

class colors:
    class fore:
        black = ansi + '30m'
        red = ansi + '31m'
        green = ansi + '32m'
        yellow = ansi + '33m'
        blue = ansi + '34m'
        magenta = ansi + '35m'
        cyan = ansi + '36m'
        white = ansi + '37m'
    class back:
        black = ansi + '40m'
        red = ansi + '41m'
        green = ansi + '42m'
        yellow = ansi + '43m'
        blue = ansi + '44m'
        magenta = ansi + '45m'
        cyan = ansi + '46m'
        white = ansi + '47m'




def initialize():
    if name == 'nt':
        system('color 0')


def colorfy(text, color=None, back=None, forergb:tuple=(-1, -1, -1), backrgb:tuple=(-1, -1, -1), bold:bool=False, underline:bool=False, negative:bool=False):



    fore = color if color != None else ''

    backg = back if back != None else ''

    negative = ansi + '7m' if negative == True else ''

    underline = ansi + '4m' if underline == True else ''

    bold = ansi + '1m' if bold == True else ''

    backrgb = ansi + f'48;2;{backrgb[0]};{backrgb[1]};{backrgb[2]}m' if backrgb != (-1,-1,-1) else ''

    forergb = ansi + f'38;2;{forergb[0]};{forergbrgb[1]};{forergb[2]}m' if forergb != (-1,-1,-1) else ''

    last = ansi + '0m'

    return (negative + underline + bold + forergb + backrgb + fore + backg + (text) + last)
