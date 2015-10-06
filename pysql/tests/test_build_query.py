# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def test_insert_into(sql, db):
    assert sql.insert(
        into=db('first_name', 'second_name'),
        values=('Mateusz', 'Probachta')
    ) == "insert into test_db(`first_name`, `second_name`) "
    "values('Mateusz', 'Probachta')"
