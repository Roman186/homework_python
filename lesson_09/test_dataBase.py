import pytest
from SubjectTable import SubjectTable

# Необходимо внести свои данные для подключения
db_connection_string = 'postgresql://myuser:mypassword@localhost:5432/postgres'


@pytest.mark.database
def test_get_table():
    tables = SubjectTable(db_connection_string)
    all_tables = tables.get_tables()

    assert 'subject' in all_tables, \
        "Таблица subject не найдена"


@pytest.mark.database
def test_insert():
    new_subject = SubjectTable(db_connection_string)
    new_subject.insert_in_table(99999, "New language")
    select_from_table = new_subject.select_order_by_desc_id()

    assert select_from_table['subject_id'] == 99999, \
        "Полученный id не соответствует добавленному id"
    assert select_from_table['subject_title'] == 'New language', \
        "Полученное значение не соответствует добавленному"


@pytest.mark.database
def test_update_subject():
    update_subj = SubjectTable(db_connection_string)
    update_subj.update_subject()
    result = update_subj.select_order_by_desc_id()

    assert result['subject_title'] == 'Update language', \
        "Значение не было обновлено"
    assert result['subject_id'] == 99999, \
        "Вернулось не верное значение"


@pytest.mark.database
def test_delete_subject():
    delete_subj = SubjectTable(db_connection_string)
    delete_subj.delete_subject(99999)
    res = delete_subj.select_one_filters(99999)

    assert len(res) == 0, \
        "Объект не удалился"
