# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def test_insert_into(db):

    assert db.sql.insert(
        into=db('first_name', 'second_name'),
        values=('Mateusz', 'Probachta')
    ).render() ==   'INSERT INTO test_db(`first_name`, `second_name`) ' \
        'VALUES("Mateusz", "Probachta")'
