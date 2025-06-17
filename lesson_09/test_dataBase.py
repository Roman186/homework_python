import pytest
from CustomersTable import CustomersTable

# Необходимо внести свои данные для подключения
db_connection_string = 'postgresql://myuser:mypassword@localhost:5432/postgres'


@pytest.mark.database
def test_get_tables():
    tables = CustomersTable(db_connection_string)
    all_tables = tables.get_tables()

    assert len(all_tables) == 17
    assert 'customers' in all_tables, \
        "Таблица customers не найдена"


@pytest.mark.database
def test_insert():
    new_subject = CustomersTable(db_connection_string)
    new_subject.insert_in_table(99999, "customer 99999")
    select_from_table = new_subject.select_order_by_desc_id()

    assert select_from_table['customer_id'] == 99999, \
        "Полученный id не соответствует добавленному id"
    assert select_from_table['customer_nm'] == 'customer 99999', \
        "Полученное значение не соответствует добавленному"


@pytest.mark.database
def test_update_subject():
    update_subj = CustomersTable(db_connection_string)
    update_subj.update_subject()
    result = update_subj.select_order_by_desc_id()

    assert result['customer_nm'] == 'changed customer', \
        "Значение не было обновлено"
    assert result['customer_id'] == 99999, \
        "Вернулось не верное значение"


@pytest.mark.database
def test_delete_subject():
    delete_subj = CustomersTable(db_connection_string)
    delete_subj.delete_subject(99999)
    res = delete_subj.select_one_filters(99999)

    assert len(res) == 0, \
        "Объект не удалился"
