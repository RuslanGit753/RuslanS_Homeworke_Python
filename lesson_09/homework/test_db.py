from sqlalchemy import create_engine, inspect, text

db_connection_string = (
    "postgresql://postgres:Hhjgh34765@localhost:5432/postgres"
)
engine = create_engine(db_connection_string)


def execute_query(query, params=None):
    with engine.connect() as connection:
        result = connection.execute(text(query), params or {})
        return result.mappings().all()


def test_db_connection():
    inspector = inspect(engine)
    names = inspector.get_table_names()
    assert 'employees' in names


def test_len_row():
    rows = execute_query("SELECT * FROM employees")
    assert len(rows) == 20


def test_create_entity():
    with engine.connect() as connection:
        result = connection.execute(
            text(
                "INSERT INTO employees (first_name, last_name, email, salary) "
                "VALUES (:first_name, :last_name, :email, :salary)"
            ).bindparams(
                first_name='Anna', last_name='Ivanova',
                email='anna.lew@example.com', salary=80000
            )
        )
        connection.commit()
        assert result.rowcount == 1

    rows = execute_query("SELECT * FROM employees")
    assert len(rows) == 21


def test_update_entity():
    with engine.connect() as connection:
        result = connection.execute(
            text(
                "UPDATE employees SET salary = :salary "
                "WHERE first_name = :first_name AND last_name = :last_name"
            ).bindparams(
                first_name='Anna', last_name='Ivanova', salary=90000
            )
        )
        connection.commit()
        assert result.rowcount == 1

    rows = execute_query(
        "SELECT * FROM employees "
        "WHERE first_name = 'Anna' AND last_name = 'Ivanova'"
    )
    updated_row = rows[0]
    assert updated_row['salary'] == 90000


def test_delete_entity():
    with engine.connect() as connection:
        result = connection.execute(
            text(
                "DELETE FROM employees "
                "WHERE first_name = :first_name AND last_name = :last_name"
            ).bindparams(
                first_name='Anna', last_name='Ivanova'
            )
        )
        connection.commit()
        assert result.rowcount == 1

    rows = execute_query(
        "SELECT * FROM employees "
        "WHERE first_name = 'Anna' AND last_name = 'Ivanova'"
    )
    assert len(rows) == 0
