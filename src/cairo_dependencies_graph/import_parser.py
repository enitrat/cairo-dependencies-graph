from starkware.cairo.lang.compiler.ast.code_elements import CodeElementFunction, CodeBlock, CodeElementImport
from starkware.cairo.lang.compiler.ast.visitor import Visitor


class ImportParser(Visitor):

    def __init__(self):
        super().__init__()

    def _visit_default(self, obj):
        # top-level code is not generated
        return obj

    def visit_CodeBlock(self, elm: CodeBlock):
        return self.extract_imports(elm)
    
    def extract_imports(self, elm):
        res = []
        for x in elm.code_elements:
            if isinstance(x.code_elm, CodeElementImport):
                path = x.code_elm.path.name
                path_formatted = path.replace(".", "/") + ".cairo"
                res.append(path_formatted)
                res = [*set(res)]
        return res
    
    def parse_imports(self, cairo_module):
        res = self.visit(cairo_module).cairo_file.code_block
        return res