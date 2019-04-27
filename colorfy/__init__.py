from os import system, name



def initialize():
    if name == 'nt':
        system('color 0')


def colorfy(text, color:str='None' , backgroundcolor:str='None', rgb:tuple=(-1,-1,-1), backgroundrgb:tuple=(-1,-1,-1), bold:bool=False, underline:bool=False, negative:bool=False):

    ansi ="\u001b["

    choice = 0

    fore = {
        'None': '',
        'black': ansi + f'30m',
        'red': ansi + f'31m',
        'green': ansi + f'32m',
        'yellow': ansi + f'33m',
        'blue': ansi + f'34m',
        'magenta': ansi + f'35m',
        'cyan': ansi + f'36m',
        'white': ansi + f'37m',
    }

    back = {
        'None': '',
        'black': ansi + f'40m',
        'red': ansi + f'41m',
        'green': ansi + f'42m',
        'yellow': ansi + f'43m',
        'blue': ansi + f'44m',
        'magenta': ansi + f'45m',
        'cyan': ansi + f'46m',
        'white': ansi + f'47m',
    }

    fore = (fore[color])

    back = (back[backgroundcolor])

    negative = ansi + '7m' if negative == True else ''

    underline = ansi + '4m' if underline == True else ''

    bold = ansi + '1m' if bold == True else ''

    backgroundrgb = ansi + f'48;2;{backgroundrgb[0]};{backgroundrgb[1]};{backgroundrgb[2]}m' if backgroundrgb != (-1,-1,-1) else ''

    rgb = ansi + f'38;2;{rgb[0]};{rgb[1]};{rgb[2]}m' if rgb != (-1,-1,-1) else ''

    last = ansi + '0m'

    return (negative + underline + bold + rgb + backgroundrgb + fore + back + str(text) + last)
