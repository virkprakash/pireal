# -*- coding: utf-8 -*-
#
# Copyright 2015-2016 - Gabriel Acosta <acostadariogabriel@gmail.com>
#
# This file is part of Pireal.
#
# Pireal is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# Pireal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pireal; If not, see <http://www.gnu.org/licenses/>.

ID = 'IDENTIFIER'
CONSTANT = 'CONSTANT'
ASSIGNMENT = 'ASSIGNMENT'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
INTEGER = 'INTEGER'
REAL = 'REAL'
STRING = 'STRING'
DATE = 'DATE'
TIME = 'TIME'
SEMI = 'SEMI'
SEMICOLON = 'SEMICOLON'
LESS = 'LESS'
GREATER = 'GREATER'
LEQUAL = 'LEQUAL'
GEQUAL = 'GEQUAL'
EQUAL = 'EQUAL'
NOTEQUAL = 'NOTEQUAL'
SELECT = 'SELECT'
PROJECT = 'PROJECT'
NJOIN = 'NJOIN'
LEFT_OUTER_JOIN = 'LOUTER'
RIGHT_OUTER_JOIN = 'ROUTER'
FULL_OUTER_JOIN = 'FOUTER'
PRODUCT = 'PRODUCT'
INTERSECT = 'INTERSECT'
UNION = 'UNION'
DIFFERENCE = 'DIFFERENCE'
AND = 'AND'
OR = 'OR'
KEYWORD = 'KEYWORD'
EOF = 'EOF'
BINARYOP = (
    NJOIN,
    LEFT_OUTER_JOIN,
    RIGHT_OUTER_JOIN,
    FULL_OUTER_JOIN,
    PRODUCT,
    INTERSECT,
    DIFFERENCE,
    UNION
)

KEYWORDS = {
    'select': SELECT,
    'project': PROJECT,
    'njoin': NJOIN,
    'louter': LEFT_OUTER_JOIN,
    'router': RIGHT_OUTER_JOIN,
    'fouter': FULL_OUTER_JOIN,
    'product': PRODUCT,
    'intersect': INTERSECT,
    'union': UNION,
    'difference': DIFFERENCE,
    'and': AND,
    'or': OR
}
