def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return f'{n}'
        except (ValueError, TypeError):
            print ('\033[01:31mErro! O valor digitado não é válido!\033[m')
        except (KeyboardInterrupt):
            print ('\033[01:33mO usuário preferiu não digitar!\033[m')
            return 0

def leiaFloat(msg1):
    while True:
        try:
            r = float(input(msg1))
            return f'{r}'
        except (ValueError, TypeError):
            print('\033[01:31mErro! O valor digitado não é válido!\033[m')
        except (KeyboardInterrupt):
            print ('\033[01:33mO usuário preferiu não digitar!\033[m')
            return 0


n = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O número inteiro digitado foi o {n} e o real foi o {r}.')
