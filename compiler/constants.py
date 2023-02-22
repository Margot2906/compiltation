LEXEM_REGEXES = [
    # Comments and whitespaces
    (r"\/\/.*", "COMMENT"),
    (r"[ \t\n]+", None),
    # Special characters
    (r"\(", "L_PAREN"),
    (r"\)", "R_PAREN"),
    (r"\{", "L_CURL_BRACKET"),
    (r"\}", "R_CURL_BRACKET"),
    (r";", "SEMICOLON"),
    # Keywords
    (r"int", "TYPE_INT"),
    (r"main", "KW_MAIN"),
    # Types
    (r"char", "TYPE_CHAR"),
    (r"float", "TYPE_FLOAT"),
    (r"bool", "TYPE_BOOL"),
    # Operators
    (r"\+", "OP_PLUS"),
    (r"\-", "OP_MINUS"),
    (r"\*", "OP_MULT"),
    (r"\/", "OP_DIV"),
    (r"\%", "OP_MOD")
]
