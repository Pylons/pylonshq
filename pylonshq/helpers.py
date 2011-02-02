"""Helper functions

This module is available as the ``h`` variable in templates, and can also be
imported into handler modules or elsewhere. Put any common functions you want
to access in all templates here.

The WebHelpers package (http://python.org/pypi/WebHelpers) contains some
commonly used helpers for HTML tag creation, text formatting, number
formatting, etc.

The template globals (``h`` et al) are set in
``{{package}}.subscribers.add_renderer_globals()``.
"""

#from webhelpers.html import *
#from webhelpers.html.tags import *

from webhelpers.date import distance_of_time_in_words
from webhelpers.html import HTML, escape, literal, tags

from pylonshq.lib.highlight import code_highlight, langdict

def rst_render(content):
    defaults = {
        'file_insertion_enabled': 0,
        'raw_enabled': 0,
        'input_encoding': 'unicode',
        'halt_level': 7,
    }
    return publish_parts(content, writer_name='html',
                         settings_overrides=defaults)['html_body']