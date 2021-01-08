try:
    '''
raise BaseException
    '''
    '1'+'nana'

except TypeError:
    print('nozomi')

except ZeroDivisionError:
    print('arukuma')
else:
    print('No Error')

finally:
    print('ore')
