# -*- coding: utf-8 -*-
from docutils.parsers import rst
from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter

from pylonshq.lib.pygmentsupport import code_block

__all__ = ['code_highlight']

langdict = {}
for lang in get_all_lexers():
    if lang[1]:
        langdict[lang[1][0]] = lang[0]

formatter = HtmlFormatter(linenos=True, cssclass="syntax", encoding='utf-8')

def code_highlight(code, truncate_lines=None):
    # Ensure that code-block is regged properly
    rst.directives.register_directive('code-block', code_block)
    source = code.code
    if truncate_lines:
        split_source = source.split('\n')
        if len(split_source) > truncate_lines:
            source = split_source[:truncate_lines-1]
            source.append('...')
            source = ''.join(source)
    lexer = get_lexer_by_name(code.language, stripall=True)

    return highlight(source, lexer, formatter).decode('utf-8')
