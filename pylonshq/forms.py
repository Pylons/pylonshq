# -*- coding: utf-8 -*- 
import logging
from formencode import Schema, validators
from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('pylonshq')

log = logging.getLogger(__name__)

class LoginForm(Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    username = validators.UnicodeString(
        not_empty=True,
        messages={
            'empty':_('Please enter your username.')
        }
    )
    password = validators.UnicodeString(
        not_empty=True,
        messages={
            'empty':_('Please enter your password.')
        }
    )
