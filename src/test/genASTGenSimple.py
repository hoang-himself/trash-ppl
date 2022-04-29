from random import randint as ri
from random import choice as c


def rl():
    return chr(ri(ord('a'), ord('z')))


def rL():
    return chr(ri(ord('A'), ord('Z')))


def rd(d):
    return chr(ri(ord(d), ord('9')))


asuite = open('ASTGenSuite.py', 'w')
asuite.write(
    '''import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
'''
)

for cnt in range(100):
    s = ri(10, 20)
    lexeme = c([rl(), rL(), '_'])
    for _ in range(s):
        lexeme += c([rl(), rL(), rd('0'), '_'])
    asuite.write(
        f"""    def test_{cnt}(self):
        line = '''Class {lexeme} {{ }}'''
        expect = '''Program([ClassDecl(Id({lexeme}),[])])'''
        self.assertTrue(TestAST.test(line, expect, {cnt}))

"""
    )

asuite.close()
