# -*- coding: utf-8 -*-
"""
    pygments.styles.stata
    ~~~~~~~~~~~~~~~~~~~~~

    Style inspired by Stata's do-file editor. Note this is not meant
    to be a complete style. It's merely meant to mimic Stata's do file
    editor syntax highlighting.

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Whitespace, Generic, Text


class StataStyle(Style):
    """
    Light mode style inspired by Stata's do-file editor. Dark mode style
    is my preferred mode; invert comments for most normal use. Further
    note this is not meant to be a complete style.
    """

    default_style = ''

    # dark mode
    # ---------
    background_color = "#232629"
    highlight_color = "#49483e"

    styles = {
        Whitespace:            '#bbbbbb',
        Error:                 'bg:#e3d2d2 #a61717',
        # light mode
        # ----------
        # String:                '#7a2424',
        # Number:                '#2c2cff',
        # Operator:              '',
        # Name.Function:         '#2c2cff',
        # Keyword:               'bold #353580',
        # Keyword.Constant:      '',
        # Comment:               'italic #008800',
        # Name.Variable:         'bold #35baba',
        # Name.Variable.Global:  'bold #b5565e',
        # dark mode
        # ---------
        Text:                  '#cccccc',
        String:                '#51cc99',
        Number:                '#4FB8CC',
        Operator:              '',
        Name.Function:         '#6a6aff',
        # Name.Format:           '#be646c',
        Name.Format:           '#e2828e',
        Keyword:               'bold #7686bb',  # #6b88b6
        Keyword.Constant:      '',
        Comment:               'italic #777777',
        Name.Variable:         'bold #7AB4DB',
        Name.Variable.Global:  'bold #BE646C',
        Generic.Prompt:        '#ffffff',
    }
