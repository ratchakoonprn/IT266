def build_profile(**user_info):
    """Print user profile"""
    print('\nUser Profile:')
    for key, value in user_info.items():
        print(f'{key} = {value}')

build_profile(name='ratchakoon')
build_profile(name='ratchakoon',city='bangkok')
build_profile(name='ratchakoon',city='bangkok',country='Thailand')


