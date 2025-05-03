try:
    type_cast = int('10')
    raise Exception('error occurred')
except ValueError as e:
    print(f'this error occurs {e}')