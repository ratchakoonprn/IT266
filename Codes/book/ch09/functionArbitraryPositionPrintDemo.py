def make_icecream(*flavor):
    """Print the list of ice cream flavor"""
    print('\nYour ice cream flavor:')
    for item in flavor:
        print(f'- {item}')

make_icecream('chocolate')
make_icecream('mango','macadamia','espresso','vanilla')
