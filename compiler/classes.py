class Statement :
    def __init__(self, type_, value) :
        self.type_ = type_
        self.value = value


class If_statement (Statement) :
    def __init__(self, condition, body, else_) :
        self.condition = condition
        self.body = body
        self.else_ = else_

class Declaration :
    def __init__(self, type_, indentifiers, integer) :
        self.type_ = type_
        self.indentifiers = indentifiers
        self.integer = integer

class Type :
    def __init__(self, type_) :
        self.type_ = int or float or bool or str

class Program :
    def __init__(self, statements, declarations) :
        self.statements = statements
        self.declarations = declarations


class Expression :
    def __init__(self, type_, value) :
        self.type_ = type_
        self.value = value

class Assigment :
    def __init__(self, id_, expression) :
        self.id_ = id_
        self.expression = expression


class Equip :
    def __init__(self, type_, value) :
        self.type_ = type_
        self.value = value

class While_statement (Statement) :
    def __init__(self, condition, body) :
        self.condition = condition
        self.body = body

class For_statement (Statement) :
    def __init__(self, condition, body) :
        self.condition = condition
        self.body = body

class Function :
    def __init__(self, type_, name, args, body) :
        self.type_ = type_
        self.name = name
        self.args = args
        self.body = body

class Return_statement (Statement) :
    def __init__(self, expression) :
        self.expression = expression

class Print_statement (Statement) :
    def __init__(self, expression) :
        self.expression = expression
