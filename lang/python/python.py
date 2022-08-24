import re

from talon import Context, Module, actions, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: user.python
"""


ctx.lists["user.code_common_function"] = {
    "enumerate": "enumerate",
    "integer": "int",
    "length": "len",
    "list": "list",
    "print": "print",
    "range": "range",
    "set": "set",
    "split": "split",
    "string": "str",
    "update": "update",
}

mod.list("python_packages", desc="Shorthand names for common python packages")

# capture to add . after. <pkg name> <function for package?
# pandas: ['a','b','c'....] Talon will probably not accept multiple vals.
ctx.lists["user.python_packages"] = {
    "ree": "re", #re
    "regex": "regex", #regex
    "flow": "tf", #tensorflow
    "pex": "px", #plotly express
    "dos": "pd", #pandas. tried daas =-> dos
    "plot lib": "plt",
    "plot lee": "plotly",
}

@mod.capture(rule="{user.python_packages}")
def return_txt(m) -> str:
    """Returns a function name"""
    txt = m.python_packages + "."
    return txt


mod.list("pandas_functions", desc="Shorthand names for common python packages")

ctx.lists["user.pandas_functions"] = {
    "frame": "df_",
    "make new": "DataFrame()",
    "named": "['']",
    "multi": "[['','']]",
    "loke": "loc['']",
    "eye loke": "iloc[,]",
    "read comma": "read_csv()",
    "read web": "read_html()",
    "read jason": "read_json()",
    "read clip": "read_clip()",
    "head": "head()",
    "tail": "tail()",
    "describe": "describe()",
    "info": "info()",
    "right comma": "to_csv()",
    "right excel": "to_excel()",
    "right jason": "to_json()",
    "right clip": "to_clip()",
    "find all": "findall",
    "string contains": ".str.contains(r'',regex=True)",
    "num unique": "nunique()",
    "num unique": "nunique()",
    "drop nah rows": "dropna()",
    "drop nah cols": "dropna(axis=1)",
    "is nah": "isna()",
    "fill nah": "fillna()",
    "calls": "columns",
    "replace": "replace(,)",
    "rename": "rename()",
    "set indy": "set_index()",
    "index": "index",
    "sort val": "sort_values()",
    "series": "Series()",
    "apply col": "apply()",
    "apply row": "apply(, axis=1)",
    "append rows": "append()",
    "concat cols": "concat([, ], axis=1)",
    "concat rows": "join(, on=, how='')",
}

@mod.capture(rule="{user.pandas_functions}")
def text(m) -> str:
    """Returns a pandas function"""
    return m.pandas_functions

#* REGEX

mod.list("ree_functions", desc="Functions for the re module in python")

# capture to add . after. <pkg name> <function for package?
# pandas: ['a','b','c'....] Talon will probably not accept multiple vals.
ctx.lists["user.ree_functions"] = {
    "ree": "re", #re
    "regex": "regex", #regex
    "flow": "tf", #tensorflow
    "pex": "px", #plotly express
    "dos": "pd", #pandas. tried daas =-> dos
    "plot lib": "plt",
    "plot lee": "plotly",
}

@mod.capture(rule="{user.ree_functions}")
def text(m) -> str:
    """Returns a function name for re module."""
    return m.ree_functions



"""a set of fields used in python docstrings that will follow the
reStructuredText format"""
docstring_fields = {
    "class": ":class:",
    "function": ":func:",
    "parameter": ":param:",
    "raise": ":raise:",
    "returns": ":return:",
    "type": ":type:",
    "return type": ":rtype:",
    # these are sphinx-specific
    "see also": ".. seealso:: ",
    "notes": ".. notes:: ",
    "warning": ".. warning:: ",
    "todo": ".. todo:: ",
}

mod.list("python_docstring_fields", desc="python docstring fields")
ctx.lists["user.python_docstring_fields"] = docstring_fields

ctx.lists["user.code_type"] = {
    "boolean": "bool",
    "integer": "int",
    "string": "str",
    "none": "None",
    "dick": "Dict",
    "float": "float",
    "any": "Any",
    "tuple": "Tuple",
    "union": "UnionAny",
    "iterable": "Iterable",
    "vector": "Vector",
    "bytes": "bytes",
    "sequence": "Sequence",
    "callable": "Callable",
    "list": "List",
    "no return": "NoReturn",
}

ctx.lists["user.code_keyword"] = {
    "break": "break",
    "continue": "continue",
    "class": "class ",
    "return": "return ",
    "import": "import ",
    "null": "None",
    "none": "None",
    "true": "True",
    "false": "False",
    "yield": "yield ",
    "from": "from ",
}

exception_list = [
    "BaseException",
    "SystemExit",
    "KeyboardInterrupt",
    "GeneratorExit",
    "Exception",
    "StopIteration",
    "StopAsyncIteration",
    "ArithmeticError",
    "FloatingPointError",
    "OverflowError",
    "ZeroDivisionError",
    "AssertionError",
    "AttributeError",
    "BufferError",
    "EOFError",
    "ImportError",
    "ModuleNotFoundError",
    "LookupError",
    "IndexError",
    "KeyError",
    "MemoryError",
    "NameError",
    "UnboundLocalError",
    "OSError",
    "BlockingIOError",
    "ChildProcessError",
    "ConnectionError",
    "BrokenPipeError",
    "ConnectionAbortedError",
    "ConnectionRefusedError",
    "ConnectionResetError",
    "FileExistsError",
    "FileNotFoundError",
    "InterruptedError",
    "IsADirectoryError",
    "NotADirectoryError",
    "PermissionError",
    "ProcessLookupError",
    "TimeoutError",
    "ReferenceError",
    "RuntimeError",
    "NotImplementedError",
    "RecursionError",
    "SyntaxError",
    "IndentationError",
    "TabError",
    "SystemError",
    "TypeError",
    "ValueError",
    "UnicodeError",
    "UnicodeDecodeError",
    "UnicodeEncodeError",
    "UnicodeTranslateError",
    "Warning",
    "DeprecationWarning",
    "PendingDeprecationWarning",
    "RuntimeWarning",
    "SyntaxWarning",
    "UserWarning",
    "FutureWarning",
    "ImportWarning",
    "UnicodeWarning",
    "BytesWarning",
    "ResourceWarning",
]
mod.list("python_exception", desc="python exceptions")
ctx.lists["user.python_exception"] = {
    " ".join(re.findall("[A-Z][^A-Z]*", exception)).lower(): exception
    for exception in exception_list
}

# BELOW ADDED 6/27 TO PREVENT WARNING IN LOG
@mod.action_class
class Actions:
    def code_insert_function(text: str, selection: str):
        """Here's the damn docstring."""
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"
        actions.user.paste(text)
        actions.edit.left()

@ctx.action_class("user")
class UserActions:
    def code_operator_subscript():
        actions.user.insert_between("[", "]")

    def code_operator_assignment():
        actions.auto_insert(" = ")

    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_subtraction_assignment():
        actions.auto_insert(" -= ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_addition_assignment():
        actions.auto_insert(" += ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_multiplication_assignment():
        actions.auto_insert(" *= ")

    def code_operator_exponent():
        actions.auto_insert(" ** ")

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_division_assignment():
        actions.auto_insert(" /= ")

    def code_operator_modulo():
        actions.auto_insert(" % ")

    def code_operator_modulo_assignment():
        actions.auto_insert(" %= ")

    def code_operator_equal():
        actions.auto_insert(" == ")

    def code_operator_not_equal():
        actions.auto_insert(" != ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_and():
        actions.auto_insert(" and ")

    def code_operator_or():
        actions.auto_insert(" or ")

    def code_operator_bitwise_and():
        actions.auto_insert(" & ")

    def code_operator_bitwise_and_assignment():
        actions.auto_insert(" &= ")

    def code_operator_bitwise_or():
        actions.auto_insert(" | ")

    def code_operator_bitwise_or_assignment():
        actions.auto_insert(" |= ")

    def code_operator_bitwise_exclusive_or():
        actions.auto_insert(" ^ ")

    def code_operator_bitwise_exclusive_or_assignment():
        actions.auto_insert(" ^= ")

    def code_operator_bitwise_left_shift():
        actions.auto_insert(" << ")

    def code_operator_bitwise_left_shift_assignment():
        actions.auto_insert(" <<= ")

    def code_operator_bitwise_right_shift():
        actions.auto_insert(" >> ")

    def code_operator_bitwise_right_shift_assignment():
        actions.auto_insert(" >>= ")

    def code_self():
        actions.auto_insert("self")

    def code_operator_object_accessor():
        actions.auto_insert(".")

    def code_insert_null():
        actions.auto_insert("None")

    def code_insert_is_null():
        actions.auto_insert(" is None")

    def code_insert_is_not_null():
        actions.auto_insert(" is not None")

    def code_state_if():
        actions.user.insert_between("if ", ":")

    def code_state_else_if():
        actions.user.insert_between("elif ", ":")

    def code_state_else():
        actions.insert("else:")
        actions.key("enter")

    def code_state_switch():
        actions.user.insert_between("match ", ":")

    def code_state_case():
        actions.user.insert_between("case ", ":")

    def code_state_for():
        actions.auto_insert("for ")

    def code_state_for_each():
        actions.user.insert_between("for ", " in ")

    def code_state_while():
        actions.user.insert_between("while ", ":")

    def code_define_class():
        actions.auto_insert("class ")

    def code_import():
        actions.auto_insert("import ")

    def code_comment_line_prefix():
        actions.auto_insert("# ")

    def code_state_return():
        actions.insert("return ")

    def code_insert_true():
        actions.auto_insert("True")

    def code_insert_false():
        actions.auto_insert("False")

    def code_comment_documentation():
        actions.user.insert_between('"""', '"""')

    def code_insert_function(text: str, selection: str):
        text += f"({selection or ''})"
        actions.user.paste(text)
        actions.edit.left()

    def code_default_function(text: str):
        actions.user.code_public_function(text)

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "def _{}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_public_function(text: str):
        result = "def {}():".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.left()
        actions.edit.left()

    def code_insert_type_annotation(type: str):
        actions.insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.insert(f" -> {type}")
