from starkware.cairo.lang.compiler.ast.code_elements import CodeElementFunction, CodeBlock, CodeElementImport
from starkware.cairo.lang.compiler.ast.visitor import Visitor


class ImportParser(Visitor):

    def __init__(self):
        super().__init__()
        self.extracted_imports = []

    def _visit_default(self, obj):
        # top-level code is not generated
        return obj

    def visit_CodeBlock(self, elm: CodeBlock):
        self.extract_imports(elm)
        return super().visit_CodeBlock(elm)
    
    def extract_imports(self, elm):
        for x in elm.code_elements:
            if isinstance(x.code_elm, CodeElementImport):
                path = x.code_elm.path.name
                path_formatted = path.replace(".", "/") + ".cairo"
                self.extracted_imports.append(path_formatted)
        self.extracted_imports = [*set(self.extracted_imports)]
        return 0
    
    def parse_imports(self, cairo_module):
        self.visit(cairo_module)
        res = self.extracted_imports
        return res