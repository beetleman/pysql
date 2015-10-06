# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import

from .base import (
    SQL,
    TplNode,
    AdhockNode
)


class MySqlSQL(SQL):

    def insert(self, into, values):
        tpl = 'INSERT INTO {db} {values}'
        return TplNode(tpl)(db=into, values=AdhockNode('values')(*values))
