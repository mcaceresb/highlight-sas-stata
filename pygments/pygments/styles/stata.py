# -*- coding: utf-8 -*-
"""
    pygments.styles.stata
    ~~~~~~~~~~~~~~~~~~~~~

    Style inspired by Stata's do-file editor

    :copyright: Copyright 2006-2016 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Whitespace


class StataStyle(Style):
    """
    Style inspired by Stata's do-file editor
    """

    default_style = ''

    styles = {
        Whitespace:            '#bbbbbb',
        Comment:               'italic #008800',
        # Comment:               'italic #898989',
        String:                '#7a2424',
        Number:                '#2c2cff',
        Operator:              '',
        Keyword:               'bold #353580',
        Keyword.Constant:      '',
        Name.Function:         '#2c2cff',
        Name.Variable:         'bold #35baba',
        Name.Variable.Global:  'bold #b5565e',
        # Name.Variable:         'bold #7EC0EE',
        # Name.Variable.Global:  'bold #BE646C',
        Error:                 'bg:#e3d2d2 #a61717'
    }
