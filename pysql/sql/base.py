# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):

    def __init__(self, sql_text):
        self._sql_text = sql_text

    def render(self):
        return self._sql_text

    def __unicode__(self):
        return self.render()

    def __str__(self):
        return self.__unicode__()


class TplNode(Node):

    def render(self):
        NotImplementedError()

    @classmethod
    def quote(cls, arg, quote='"'):
        if isinstance(arg, Node):
            return arg.render()
        if isinstance(arg, (int, float)):
            return arg

        arg = str(arg)
        if arg.isdigit():
            return int(arg)
        try:
            return float(arg)
        except ValueError:
            return arg.join([quote, quote])

    @classmethod
    def args_to_str(cls, args, kwargs, seperator=', ', quote='"'):
        args_str = [cls.quote(a, quote=quote) for a in args]
        for k, v in kwargs.items():
            args_str.append('{0}={1}'.format(
                cls.quote(k, quote=quote),
                cls.quote(v, quote=quote),
            ))
        return seperator.join(args_str)

    def __call__(self, *args, **kwargs):
        return Node(self._sql_text.format(*args, **kwargs))


class AdhockNode(TplNode):

    def __init__(self, name, upper=True, seperator=', ', quote='"'):
        if upper:
            name = name.upper()
        self.name = name
        self.seperator = seperator
        self.quote = quote
        super(AdhockNode, self).__init__('{f}({args})')

    def render(self):
        return self.name

    def __call__(self, *args, **kwargs):
        return super(AdhockNode, self).__call__(
            f=self.name,
            args=self.args_to_str(
                args, kwargs,
                seperator=self.seperator,
                quote=self.quote
            )
        )


class SQL(object):

    def __getattr__(self, key):
        return AdhockNode(key)
