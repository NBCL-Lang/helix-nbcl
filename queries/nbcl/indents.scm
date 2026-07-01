; Indent content inside bracketed blocks
[
  (block)
  (node_block)
  (match_expr)
  (array)
  (map)
] @indent

; Align matching closing brackets with the opening statement line
"}" @outdent
"]" @outdent
")" @outdent
