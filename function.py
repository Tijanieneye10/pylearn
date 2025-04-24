def greeting(name) -> str:
    return 'Hello! {person}'.format(person=name)

# default param
def default_param(name = 'Usman') -> str:
    return f'Hello! {name}'


# argument
def get_args(*param):
    return param

def user_profile(**kwargs):
    return kwargs

profile = user_profile(name = 'Usman', age = 18)

print(profile['age'])

print(greeting('Tijani'))
print(default_param())
print(get_args(1,2,3,4,'name'))