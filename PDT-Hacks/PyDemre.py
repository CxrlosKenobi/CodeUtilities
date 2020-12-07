##                          ##
#  Creado por @CxrlosKenobi  #
##     Para ensayos PDT      #

from colorama import init, Fore, Back, Style
import os
import time
import string
import random
import csv
import random
init(autoreset=True)

def cleaner():
    os.system('clear')

def init(sheet):
    user = dict()

    for i in range(1,66):
        user[i] = '-'
        sheet[i] = 'none'
    for i in range(5):
        time.sleep(0.2)
        print(Fore.GREEN + '[ ok ] Loading...' + Fore.WHITE)
    #gnome-terminal --title="Dev Server" --command="bash -c 'python3 test.py; $SHELL'"
    #os.system('gnome-terminal --title="Timer by @kenobi" --command="bash -c 'python3 test.py'"')
    #os.system('gnome-terminal /home/kenobi/GitHub/CodeUtilities/PDT-Hacks/time.command')
    return user

# Full-range variables
sheet = dict()
user = init(sheet)

def Scott(user, i): # Quien recibe de input las respuestas; Mandarlas a un CSV file
    current = i
    key = 'A E B C D E a b c d e' # Para verificación o testeo
    print(Fore.WHITE + '\n\tResponder con [ABCDE] e ingresa R para cambiar una respuesta')
    try:
        ans = input(Fore.WHITE + f'Respuesta ({i})\n> ')
    except KeyboardInterrupt:
        print('')
        exit()
    if (ans == 'R') and (current > 1): # Corregir respuesta
        r = int(input(Fore.YELLOW + '\tCorregir la número\n> '))
        cleaner()
        hoja(user, i)
        r_ans = input(Fore.WHITE + f'Corección ({r})\n> ')
        user[r] = Fore.MAGENTA + r_ans + Fore.WHITE
        print(Fore.GREEN + '[ ok ] Corregido')
        time.sleep(0.4)
    elif ans in key: # Registrar respuesta
        user[i] = ans
        return user
    elif (ans == '' or len(ans) == 0 or len(ans) >= 2):
        user[i] = Fore.YELLOW + '_' + Fore.WHITE
    else:
        user[i] = Fore.YELLOW + '_' + Fore.WHITE

def hoja(user, i):
    print('\n')
    print(Fore.CYAN + f'Progreso: {round((i/65)*100)} %'+ Fore.WHITE + '\n')
    tab = '      ' # Var aux
    for row in range(1,16): # Preguntas de la 1-60
        for j in range(2,21,30):
            print(f'\
            {str(row).zfill(2)}) '+ user[row] +f'{tab}\
            {row+15}) '+ user[row+15] + f'{tab}\
            {row+30}) '+ user[row+30] + f'{tab}\
            {row+45}) '+ user[row+45] + f'{tab}')
    print('')
    for row in range(61, 66): # Preguntas de la 61-65
        print(f'\
            {row}) '+ user[row], end='')
    print('\n')

def sheets(sheet, i):
    print('\n')
    print(Fore.CYAN + f'Progreso: {round((i/65)*100)} %'+ Fore.WHITE + '\n')
    tab = '      ' # Var aux
    for row in range(1,16): # Preguntas de la 1-60
        for j in range(2,21,30):
            print(f'\
            {str(row).zfill(2)}) '+ sheet[row] +f'{tab}\
            {row+15}) '+ sheet[row+15] + f'{tab}\
            {row+30}) '+ sheet[row+30] + f'{tab}\
            {row+45}) '+ sheet[row+45] + f'{tab}')
    print('')
    for row in range(61, 66): # Preguntas de la 61-65
        print(f'\
            {row}) '+ sheet[row], end='')
    print('\n')

def saver(user):
    with open('responses.csv','w') as f:
        w = csv.writer(f)
        w.writerows(user.items())

def init_backup(user):
    with open('responses_backup.csv', 'w') as f:
        w = csv.writer(f)
        w.writerows(user.items())

def end_backup():
    os.system('rm -rf responses_backup.csv')

def verify(sheet):
    cleaner()
    print(Fore.GREEN + '\## PAUTA ##' + Fore.WHITE)
    for i in range(1, 66):
        sheets(sheet, i)
        ans = input('Ans:\n> ')
        sheet[i] = ans
        cleaner()
    with open('sheet.csv', 'w') as f:
        w = csv.writer(f)
        w.writerows(sheet.items())
    buenas = []
    malas = []
    piloto = []
    for i in range(5):
        ran = random.randint(1,66)
        piloto.append(ran)
    for i in range(1, 66):
        if i in piloto:
            pass
        elif user[i] == sheet[i]:
            buenas.append(i)
        elif user[i] != sheet[i]:
            malas.append(i)

    user_checked = user
    os.system('clear')
    print('testing')
    time.sleep(1)
    for i in user_checked:
        print(buenas)


def main():
    #Pantallita de bienvenida; Créditos; Ascii; etc
    cleaner()
    init(sheet)
    for i in range(1,66):
        hoja(user, i)
        Scott(user, i)
        init_backup(user)
        cleaner()
    saver(user)
    end_backup()
    verify(user)

if __name__ == '__main__':
    main()
