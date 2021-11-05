"""from math import floor, ceil, trunc
x = float(input('Digite um valor: '))
print(f'O valor digitado foi {x} e a sua porção inteira é {floor(x)}')
print(f'O valor digitado foi {x} e a sua porção inteira é {x//1:.0f}')
print(f'O valor digitado foi {x} e a sua porção inteira é {ceil(x-1)}')
print(f'O valor digitado foi {x} e a sua porção inteira é {trunc(x)}')
print(f'O valor digitado foi {x} e a sua porção inteira é {int(x)})"""

import math
x = float(input('Digite um valor: '))
print(f'O valor digitado foi {x} e a sua porção inteira é {math.floor(x)}')
print(f'O valor digitado foi {x} e a sua porção inteira é {x//1:.0f}')
print(f'O valor digitado foi {x} e a sua porção inteira é {math.ceil(x-1)}')
print(f'O valor digitado foi {x} e a sua porção inteira é {math.trunc(x)}')
print(f'O valor digitado foi {x} e a sua porção inteira é {int(x)}')
