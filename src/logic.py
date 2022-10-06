import traceback
from typing import Dict, List
import click
import toml
import os
from starkware.cairo.lang.compiler.ast.module import CairoModule
from starkware.cairo.lang.compiler.parser import parse_file

from cairo_dependencies_graph.import_parser import ImportParser


def cairo_parser(code, filename): return parse_file(
    code=code, filename=filename)


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 0.1.0')
    ctx.exit()


def generate_graph(directory: str):
    # visit all files in subdirs
    graph = {}
    for root, subdirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".cairo"):
                # Visit file
                file_path = os.path.join(root, file)
                dependencies = visit_file(file_path)
                graph[file_path] = dependencies

    write_graphviz_file(graph)


def write_graphviz_file(graph: Dict):
    # TODO remove this hardcoded values
    graph = {'tests/main.cairo': ['a', 'b'], 'tests/test_main.cairo': [
        'a'], 'tests/recursive_folder/main_l2.cairo': ['c', 'd', 'e']}
    graphviz_file = open("graph.gv", "w")
    graphviz_file.write("digraph G {\n")
    for file, dependencies in graph.items():
        graphviz_file.write(
            f"""{{"{file}"}} -> {{{','.join(f'''"{value}"''' for value in dependencies)}}}\n""")
    graphviz_file.write("}")
    graphviz_file.close()


def visit_file(file_path: str):
    with open(file_path, "r") as file:
        code = file.read()
        cairo_ast = cairo_parser(code, file_path)
        cairo_module = CairoModule(
            cairo_ast, module_name=file_path,
        )
        # Create a class that inherits from Visitor and implement the visit methods for codeBlocks.
        # This method should parse all the imports and return a list of all the import paths.
        # dependencies: List[str] = ImportParser().parse_imports(cairo_module)
        # return dependencies
