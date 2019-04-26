from os import system


def initialize():
    system('color 0')

def colorfy(text, color:str='None', backgroundcolor:str='None', bold:bool=False, underline:bool=False,
            warning:bool=False, brightcolor:bool=False, backgroundbrightcolor:bool=False):



    '''
    :param text: Your message

    :param color: None by default
     options: None, red, green, blue, cyan, magenta, yellow, black, white

    :param backgroundcolor: None by default
     options: None, red, green, blue, cyan, magenta, yellow, black, white

    :param bold: False by default

    :param underline: False by default

    :param warning: False by default

    :param brightcolor: False by default

    :param backgroundbrightcolor: False by default

    '''


    if brightcolor == False:
        end = 'm'
    else:
        end = ';1m'

    colors = {
        'None': '',
        'red': '\033[31' + end,
        'green': '\033[32' + end,
        'blue': '\033[34' + end,
        'cyan': '\033[36' + end,
        'magenta': '\033[35' + end,
        'yellow': '\033[33' + end,
        'black': '\033[30' + end,
        'white': '\033[37' + end,
    }

    if backgroundbrightcolor == False:
        bend = 'm'
    else:
        bend = ';1m'

    backgrounds = {
        'None': '',
        'black': '\u001b[40' + bend,
        'red': '\u001b[41' + bend,
        'green': '\u001b[42' + bend,
        'yellow': '\u001b[43' + bend,
        'blue': '\u001b[44' + bend,
        'magenta': '\u001b[45' + bend,
        'cyan': '\u001b[46' + bend,
        'white': '\u001b[47' + bend,
    }


    if bold == False:
        bold = ''
    else:
        bold = '\033[1m'

    if underline == False:
        underline = ''
    else:
        underline = '\033[4m'

    if warning == False:
        warning = ''
    else:
        warning = '\033[93m'


    last = '\033[0m'


    return  (colors[color] + backgrounds[backgroundcolor] + bold + underline + warning + str(text) + last)

