gvariable = False


class Test:

    def print_variable(self):
        print(gvariable)

    def change_value(self, val):
        global gvariable
        gvariable = val