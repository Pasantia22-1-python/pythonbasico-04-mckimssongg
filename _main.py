# PASSWORD = '12345'


# def passwordRquired(func):
#     def wrapper():
#         password = input("Dame la contraseña  ")

#         if password == PASSWORD:
#             return func()
#         else: 
#             print("La crontraseña no es correcta")
#     return wrapper

# @passwordRquired
# def needPassword():
#     print('la contraseña es correcta')

# if __name__ == '__main__':
#     needPassword()

def upper(func):
    def wrapper(*args, **kargs):
        result = func(*args, **kargs)
        
        return result.upper()

    return wrapper

@upper
def SayMyName(nombre):
    return ('Hola {}'.format(nombre))

if __name__ == '__main__':
    print(SayMyNAme('Juan'))
