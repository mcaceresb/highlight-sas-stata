# -*- coding: utf-8 -*-
"""
    pygments.styles.sas
    ~~~~~~~~~~~~~~~~~~~

    Style inspired by SAS' enhanced program editor

    :copyright: Copyright 2006-2016 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Other, Whitespace, Generic


class SasStyle(Style):
    """
    Style inspired by SAS' enhanced program editor
    """

    default_style = ''

    styles = {
        Whitespace:            '#bbbbbb',
        Comment:               'italic #008800',
        # Comment:               'italic #898989',
        String:                '#800080',
        Number:                'bold #2e8b57',
        Other:                 'bg:#ffffe0',
        Keyword:               '#2c2cff',
        Keyword.Reserved:      'bold #353580',
        Keyword.Constant:      'bold',
        Name.Builtin:          '#2c2cff',
        Name.Function:         'bold italic',
        Name.Variable:         'bold #2c2cff',
        Generic:               '#2c2cff',
        Generic.Emph:          '#008800',
        Generic.Error:         '#d30202',
        Error:                 'bg:#e3d2d2 #a61717'
    }
