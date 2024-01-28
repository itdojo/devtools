from os import get_terminal_size


def draw_line(linetype=1):
    terminal_size = get_terminal_size()
    match linetype:
        case 1:
            print('─' * terminal_size.columns)
        case 2:
            print('∙' * terminal_size.columns)
        case 3:
            print('⌶' * terminal_size.columns)
        case 4:
            print('☆' * terminal_size.columns)
        case 5:
            print('⏥' * terminal_size.columns)
        case _:
            print('─' * terminal_size.columns)
    return True