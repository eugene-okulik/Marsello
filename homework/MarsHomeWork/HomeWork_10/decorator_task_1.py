def universal(func):
    def wrapper(*args):
        func(*args)
        print('finished')

    return wrapper


@universal
def text(*args):
    print(*args)


text('hfgh', 123123123, 'ffkghjdfk;')
