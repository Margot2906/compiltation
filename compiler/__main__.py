# -*- encoding: utf-8 -*-

import sys

from compiler.lexer import Lexer

if __name__ == "__main__":
    lexer = Lexer()
    print(lexer.lex_file("examples\example1.c"))
