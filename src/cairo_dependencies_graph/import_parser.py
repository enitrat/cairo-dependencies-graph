from starkware.cairo.lang.compiler.ast.code_elements import CodeElementFunction, CodeBlock
from starkware.cairo.lang.compiler.ast.visitor import Visitor


class ImportParser(Visitor):

    def __init__(self):
        super().__init__()

    def _visit_default(self, obj):
        # top-level code is not generated
        return obj

    def visit_CodeElementFunction(self, elm: CodeElementFunction):
        return super().visit_CodeElementFunction(elm)

    def visit_CodeBlock(self, elm: CodeBlock):
        return super().visit_CodeBlock(elm)
