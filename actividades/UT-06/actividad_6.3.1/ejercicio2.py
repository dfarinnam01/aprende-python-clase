def circular(*nombres):
    for nombre in nombres:
        carta=f'''
            Hola {nombre}!
            '''
        print(carta)

circular("paco","lorena","iago")