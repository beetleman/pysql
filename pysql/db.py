# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from .sql import MySqlSQL
from .sql.base import (
    AdhockNode,
    Node
)


class Db(Node):
    _sql_class = type

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_sql(cls):
        return cls._sql_class()

    @property
    def _self_node(self):
        if not hasattr(self, '__self_node'):
            self.__self_node = AdhockNode(
                self.name, upper=False, quote='`'
            )
        return self.__self_node

    def render(self):
        return self.name

    @property
    def sql(self):
        if not hasattr(self, '_sql'):
            self._sql = self.create_sql()
        return self._sql

    def __call__(self, *args):
        return self._self_node(*args)


class MySqlDb(Db):
    _sql_class = MySqlSQL
