%import common.ESCAPED_STRING   -> STRING
%import common.SIGNED_NUMBER    -> NUMBER
%import common.WS
%ignore WS




    COLON: ":"

    token: NAME | COLON

    COMMENT: "#[\n+]"
%ignore COMMENT
        
    LPAREN: "("
        
    RPAREN: ")"
   

    start: stmt+

    stmt: def_stmt | print_stmt | pass_stmt | COMMENT

    arglist: NAME | arglist "," NAME

    function_body: stmt+

    def_stmt: "def" NAME LPAREN arglist RPAREN COLON function_body

    print_stmt: "print" LPAREN arglist RPAREN

    pass_stmt: "pass"
 
    %import common.CNAME -> NAME
