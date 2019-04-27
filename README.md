# colorfy
Easy colored terminal

![Screenshot](screenshot.png)

# Usage
```python
from colorfy import *

#initialize()    If you're using Windows

print(colorfy('This is pink', rgb=(255, 0, 255)))
print(colorfy('Hello, green!', color='green', bold=True))
```

# Instalation
```
pip install https://github.com/x8ss/colorfy/archive/master.zip
```
# Params
* :param text: Your message

* :param color: None by default
    - options: black, red, green, yellow, blue, magenta, cyan, white

* :param backgroundcolor: None by default
    - options: black, red, green, yellow, blue, magenta, cyan, white

* :param rgb: (r, g, b)
    - Does not support bold

* :param backgroundrgb: (r, g, b)
    - Does not support bold

* :param bold: False by default

* :param underline: False by default

* :param negative: False by default
