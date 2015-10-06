import pytest


@pytest.fixture
def db():
    from pysql import MySqlDb
    return MySqlDb('test_db')
