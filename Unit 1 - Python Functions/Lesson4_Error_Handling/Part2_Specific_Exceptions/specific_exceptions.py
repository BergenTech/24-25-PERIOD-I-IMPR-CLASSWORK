# Some specific exception examples
import math
# print('test')
try:
    # pass
    #1 ArithmeticError Example
    # result = math.exp(1000) # Cause an overflow error
    #2 Name Error Example
    # print(non_existent_variable)
    #3 Type Error Example
    # result = '10' + 5
    #4 Value Error Example
    number  = int(input('Enter a number:'))
except ArithmeticError as e:
    print(f"An Arithmetic Error occured {e}")
except NameError as e:
    print(f'A NameError occured {e}')
except TypeError as e:
    print(f'A TypeError occured {e}')
except ValueError as e:
    print(f'A ValueError occured {e}')
except Exception as e:
    print(f'An unexpected error occured {e}')