; === Keywords ===
["let" "const" "set" "fn" "component" "if" "else" "match" "for" "in" "while" "return" "import" "as"] @keyword

; === Identifiers and Definitions ===
(function_definition name: (_snake_ident) @function.definition)
(function_call name: (_snake_ident) @function)
(node_invocation name: (_pascal_ident) @type)
(component name: (_pascal_ident) @type)

; Properties and keys
(map_pair name: (_snake_ident) @variable.other.member)
(import_list (choice (_snake_ident) (_pascal_ident)) @variable)

; Fallback identifiers
(_snake_ident) @variable
(_pascal_ident) @type

; === Literals ===
(integer) @number
(float) @number
(boolean) @boolean
(null) @constant.builtin
(string) @string
(escape_sequence) @constant.character.escape

; === Structuring Elements ===
(comment) @comment
(spread) @keyword.operator

; === Operators and Punctuation ===
["=" "+=" "-=" "*=" "/="] @keyword.operator
["+" "-" "*" "/" "%" "==" "!=" "<" ">" "<=" ">=" "&&" "||" "!" "=>" ".." "..="] @operator
["." "?."] @punctuation.delimiter
["," "(" ")" "[" "]" "{" "}"] @punctuation.bracket
