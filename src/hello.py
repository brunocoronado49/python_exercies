def hello_world(name):
    return f'Hello {name}'


if __name__ == '__main__':
    name = input('Please, enter your name: ')
    result = hello_world(name=name)
    print(result)