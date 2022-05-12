from turtle import  *
def t_c(do, val):
    do = do.upper()
    if do == 'F':
        forward(val)
    elif do == 'B':
        backward(val)
    elif do == 'R':
        right(val)
    elif do == 'L':
        left(val)
    elif do == 'U':
        penup()
    elif do == 'D':
        pendown()
    elif do == 'N':
        reset()
    else:
        print('Я не знаю такой команды')

def s_a(program):
    cmd_list = program.split('-')
    for command in cmd_list:
        cmd_len = len(command)
        if cmd_len == 0:
            continue
        cmd_type = command[0]
        num = 0
        if cmd_len > 1:
            num_string = command[1:]
            num = int(num_string)
        print(command, ':', cmd_type, num)
        t_c(cmd_type, num)
instructions = ''' Напиши программу для черепашки:
к примеру N-F100-R45-U-F100-L45-D-F100-R90-B50
- = разделитель
U/D = поднять/опустить перо
F100 = вперёд 100
B50 = назад 50
R90 = вправо 90
L45 = влево 45'''
screen = getscreen()
while True:
    t_program = screen.textinput('Чертёжный автомат', instructions)
    print(t_program)
    if t_program == None or t_program.upper() == 'END':
        break
    s_a(t_program)












































