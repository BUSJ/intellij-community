class c1:
    def foo(self, a):
        pass

class c2(c1):
    def foo(self, *a):
        pass

class c3(c1):
    def foo<warning descr="Method signature does not match signature of base method">(self)</warning>:
        pass

class c4(c1):
    def foo(self, **a):
        pass

class c5(c1):
    def foo(self, a):
        pass

class c6:
    pass

class c7(c6):
    def foo(self):
        pass

class c8:
    def __init__(self):
        pass

    def __new__(self):
        pass

    def foo(self, a):
        pass


class c9(c8):
    def __init__(self, a): # different but ok because __init__ is special
        pass

    def __new__(self, p, q): # different but ok because __new__ is special
        pass

    def foo<warning descr="Method signature does not match signature of base method">(self, s, t)</warning>:
        pass

class c10:
    def foo(self, a, b):
        pass

class c11(c10):
    def foo(self, *b):
        pass

class c12(c4):
    def foo(self):
        pass

class c13:
    def foo(self, *args):
        pass

class c14(c13):
    def foo(self):
        pass

class c15:                                    # PY-1083
    def foo(self, x = 1):
        pass

class c16:
    def foo(self, **kwargs):
        pass


# PY-6700
class c17:
    def foo(self, **kwargs):
        pass

class c18(c17):
    def foo(self, arg1=None, **kwargs): # pass
        pass

class c19:
    def foo(self, *args, **kwargs):
        raise NotImplementedError()

class c20(c19):
    def foo(self): # pass
        pass

class c21(c19):
    def foo(self, arg1): # pass
        pass

class c22:
    def foo(self, arg1, *args, **kwargs):
        raise NotImplementedError()

class c23(c22):
    def foo<warning descr="Method signature does not match signature of base method">(self, arg1, arg2=None)</warning>: # fail
        pass


# PY-7157
class c24:
    def foo(self, arg1):
        pass

class c25(c24):
    def foo(self, arg1, arg2=None): #pass
        pass


# PY-7162
class c26:
    def foo(self, arg1, arg2=None):
        pass

class c27(c26):
    def foo<warning descr="Method signature does not match signature of base method">(self, arg1=None)</warning>: #fail
        pass


