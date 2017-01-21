
# Draw lines with recursions
def draw_line_vertical(len, symbol='* '):
    if len > 0:
        print(symbol)
        draw_line_vertical(len - 1)


def draw_line_horizontal(len, symbol='* ', line=''):
    if len > 0:
        line += symbol
        print(symbol)
        draw_line_horizontal(len - 1, line=line)
    else:
        print(line)

def draw_line(len, vertical=False, symbol='* ', line=''):
    if vertical:
        if len > 0:
            print(symbol)
            draw_line(len - 1)
    else:
        if len > 0:
            line += symbol
            draw_line(len - 1, line=line)
        else:
            print(line)

#length = int(input('Please, enter the line length: \n'))
#direction = True if input('Please, chose direction:\n') == 'True' else False
#draw_line(length, direction)

## Draw square(5)

def draw_square(side, symbol='*   ', raws=0, column=''):
    def draw_columns(columns=side, column=''):
        if columns > 0:
            column += symbol
            draw_columns(columns - 1, column=column)
        else:
            print(column + '\n')
    if raws < side:
        draw_columns()
        draw_square(side, raws=raws + 1)

#draw_square(5)

#draw_empty_square(5)

def draw_empty_square(side, symbol='*   ', raw=0):
    solid = raw == 0 or raw == side - 1
    def draw_columns(columns=side, column=''):
        if columns > 0:
            column += symbol if solid or (columns == side or columns == 1) else '    '
            draw_columns(columns - 1, column=column)
        else:
            print(column + '\n')
    if raw < side:
        draw_columns()

        draw_empty_square(side, raw=raw + 1)

draw_empty_square(8)






#трикутник прямокутний, трикутник рівнобедренний(зверху вниз)