import ast  
  
ErrorType = tuple[int, int, str]  
T100 = (  
     "T100 Index must be created concurrently, add 'postgresql_concurrently=True'"
)  
  
  
class Visitor(ast.NodeVisitor):
    def __init__(self) -> None:  
        self.errors: list[ErrorType] = []

    def __visit_call_keywords(self, node: ast.Call) -> bool:
        return any(self.__visit_call_keyword(keyword) for keyword in node.keywords)

    def __visit_call_keyword(self, keyword: ast.keyword) -> bool:
        match keyword:
            case ast.keyword(arg='postgresql_concurrently', value=ast.Constant(value=True)):
                return True
        return False

    def visit_Call(self, node: ast.Call) -> None:
        match node:
            case ast.Call(func=ast.Attribute(value=ast.Name(id='op'), attr='create_index')):
                if not self.__visit_call_keywords(node):
                    self.errors.append((node.lineno, node.col_offset, T100))

        self.generic_visit(node)  
