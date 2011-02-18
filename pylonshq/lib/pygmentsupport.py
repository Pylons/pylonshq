# -*- coding: utf-8 -*- 
import docutils.parsers.rst
from pygments import highlight
from pygments.lexers import get_lexer_by_name, get_all_lexers
from pygments.formatters import HtmlFormatter

def code_block( name, arguments, options, content, lineno,
             content_offset, block_text, state, state_machine ):
    """
    The code-block directive provides syntax highlighting for blocks
    of code.  It is used with the the following syntax::

    .. code-block:: Python
 
        class Test(object):
            pass
    
    The code will be highlighted with the pygments syntax highlighter. It's
    recommended that you include the appropriate stylesheets when using this
    highlighter.
    """

    try:
        language = arguments[0]
    except IndexError:
        language = options.get('language', '')
    try:
        linenos = arguments[1]
    except IndexError:
        linenos = options.get('linenos', False)

    language = language.lower()
    if language == 'hypertext':
        language = 'html'
    if language == 'pasteini':
        language = 'ini'
    content = '\n'.join(content)
    if not language:
        if content.strip().startswith('>>>'):
            language = 'pycon'
        else:
            language = 'python'
    lexer = get_lexer_by_name(language, stripall=True)
    formatter = HtmlFormatter(linenos=linenos, cssclass="syntax", encoding='utf-8')
    html = highlight(unicode(content), lexer, formatter).decode('utf-8')
    raw = docutils.nodes.raw('',html, format = 'html')
    return [raw]

#code_block.arguments = (1,0,0)
code_block.arguments = (1,0,0)
code_block.options = {'linenos':docutils.parsers.rst.directives, 
                      'language':docutils.parsers.rst.directives.unchanged}
code_block.content = 1
  
# Simply importing this module will make the directive available.
docutils.parsers.rst.directives.register_directive( 'code-block', code_block )
