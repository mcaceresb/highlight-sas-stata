# -*- coding: utf-8 -*-
"""
    pygments.lexers.stata
    ~~~~~~~~~~~~~~~~~~~~~

    Lexer for Stata

    :copyright: Copyright 2006-2017 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

import re
from pygments.lexer import RegexLexer, include, words
from pygments.token import Comment, Keyword, Name, Number, \
    String, Text, Operator

from pygments.lexers._stata_builtins import builtins_base, builtins_functions

__all__ = ['StataLexer']


class StataLexer(RegexLexer):
    """
    For `Stata <http://www.stata.com/>`_ do files.

    .. versionadded:: 2.2
    """
    # Syntax based on
    # - http://fmwww.bc.edu/RePEc/bocode/s/synlightlist.ado
    # - http://github.com/isagalaev/highlight.js/blob/master/src/languages/stata.js
    # - http://github.com/jpitblado/vim-stata/blob/master/syntax/stata.vim

    name      = 'Stata'
    aliases   = ['stata', 'do']
    filenames = ['*.do', '*.ado']
    mimetypes = ['text/x-stata', 'text/stata', 'application/x-stata']
    flags = re.MULTILINE | re.DOTALL

    tokens = {
        'root': [
            include('comments'),
            include('strings'),
            include('operators'),
            include('macros'),
            include('numbers'),
            include('keywords'),
            include('format'),
            (r'.', Text),
        ],
        'comments': [
            (r'(^//|(?<=\s)//)(?!/)', Comment.Single, 'comments-double-slash'),
            (r'^\s*\*', Comment.Single, 'comments-star'),
            (r'/\*', Comment.Multiline, 'comments-block'),
            (r'(^///|(?<=\s)///)', Comment.Special, 'comments-triple-slash')
        ],
        'comments-block': [
            (r'/\*', Comment.Multiline, '#push'),
            # this ends and restarts a comment block. but need to catch this so
            # that it doesn\'t start _another_ level of comment blocks
            (r'\*/\*', Comment.Multiline),
            (r'(\*/\s+\*(?!/)[^\n]*)|(\*/)', Comment.Multiline, '#pop'),
            # Match anything else as a character inside the comment
            (r'.', Comment.Multiline),
        ],
        'comments-star': [
            (r'///.*?\n', Comment.Single,
                ('#pop', 'comments-triple-slash')),
            (r'(^//|(?<=\s)//)(?!/)', Comment.Single,
                ('#pop', 'comments-double-slash')),
            (r'/\*', Comment.Multiline, 'comments-block'),
            (r'.(?=\n)', Comment.Single, '#pop'),
            (r'.', Comment.Single),
        ],
        'comments-triple-slash': [
            (r'\n', Comment.Special, '#pop'),
            # A // breaks out of a comment for the rest of the line
            (r'//.*?(?=\n)', Comment.Single, '#pop'),
            (r'.', Comment.Special),
        ],
        'comments-double-slash': [
            (r'\n', Text, '#pop'),
            (r'.', Comment.Single),
        ],
        'macros': [
            (r'\$\{', Name.Variable.Global, 'macro-global-braces'),
            (r'\$', Name.Variable.Global, 'macro-global'),
            (r'`', Name.Variable, 'macro-local'),
        ],
        'macro-global-braces': [
            (r'\$\{', Name.Variable.Global, '#push'),
            (r'}', Name.Variable.Global, '#pop'),
            (r'.', Name.Variable.Global),
        ],
        'macro-global': [
            (r'}', Name.Variable.Global, '#pop'),
            (r'\w(?![\w}])', Name.Variable.Global, '#pop'),
            (r'.', Name.Variable.Global),
        ],
        'macro-local': [
            (r'`', Name.Variable, '#push'),
            (r"'", Name.Variable, '#pop'),
            (r'.', Name.Variable),
        ],
        'strings': [
            # `"compound string"'
            (r'`"', String, 'string-compound'),
            # "string"
            (r'(?<!`)"', String, 'string-regular'),
        ],
        'string-compound': [
            (r'`"', String, '#push'),
            (r'"\'', String, '#pop'),
            include('macros'),
            (r'\\\\|\\"|\\\n', String.Escape),
            (r'.', String)
        ],
        'string-regular': [
            (r'(")(?!\')|(?=\n)', String, '#pop'),
            include('macros'),
            (r'\\\\|\\"|\\\n', String.Escape),
            (r'.', String)
        ],
        # Built in functions and statements
        'keywords': [
            (words(builtins_functions, prefix = r'\b', suffix = r'(?=\()'),
             Name.Function),
            (words(builtins_base, prefix = r'(^\s*|\s)', suffix = r'\b'),
             Keyword),
        ],
        # http://www.stata.com/help.cgi?operators
        'operators': [
            (r'-|==|<=|>=|<|>|&|!=', Operator),
            (r'\*|\+|\^|/|!|~|==|~=', Operator)
        ],
        # Stata numbers
        'numbers': [
            # decimal number
            (r'\b[+-]?([0-9]+(\.[0-9]+)?|\.[0-9]+|\.)([eE][+-]?[0-9]+)?[i]?\b',
             Number),
        ],
        # Stata formats
        'format': [
            (r'%-?\d{1,2}(\.\d{1,2})?[gfe]c?', Name.Variable),
            (r'%(21x|16H|16L|8H|8L)', Name.Variable),
            (r'%-?(tc|tC|td|tw|tm|tq|th|ty|tg).{0,32}', Name.Variable),
            (r'%[-~]?\d{1,4}s', Name.Variable),
        ]
    }
