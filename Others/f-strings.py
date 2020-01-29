if __name__ == '__main__':
    # multiline f-string
    intro = (
        f'f-string also known as formatted string literals was introduced in python 3.6'
        f'evaluated during runtime'
    )
    intro = f'f-string also known as formatted string literals was introduced in python 3.6' \
            f'evaluated during runtime'

    print(intro)

    first_name = 'Brent Jeffson'
    middle_name = 'Flores'
    last_name = 'Florendo'

    name = f'{first_name} {middle_name} {last_name}'
    name = F'{first_name} {middle_name} {last_name}'
    print(name)

    addition = f'{1 + 1}'
    print(addition)

    # never use the same quotation marks used for the string inside the expressions
    name = {'fn': 'Brent Jeffson', 'ln': 'Florendo'}
    using_quotation_marks = f"{name['fn']} {name['ln']}"
    print(using_quotation_marks)




