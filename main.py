import datetime
import hashlib

def logger(file_path=None):
    def decorator(old_function):
        def new_function(*args, **kwargs):
            name_f = old_function.__name__
            time_enter = str(datetime.datetime.now())
            arg_1 = ', '.join(args)
            arg_2 = []
            for key, value in kwargs:
                arg_2 += key, value
            arg_named = ', '.join(arg_2)
            something = old_function(*args, **kwargs)
            with open(file_path, 'a+', encoding='utf8') as f:
                f.write(f'{name_f} - {time_enter}, аргументы = {arg_1};{arg_named}; значение = {something.hexdigest()};' + '\n')
            return something
        return new_function
    return decorator

@logger(file_path='log.txt')
def hash_function(text):
    hash_obj = hashlib.md5(text.encode())
    return hash_obj

if __name__ == '__main__':
    print(hash_function('Захэшированный текст').hexdigest())