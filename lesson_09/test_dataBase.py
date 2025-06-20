import pytest
from SubjectTable import SubjectTable

# Необходимо внести свои данные для подключения
db_connection_string = 'postgresql://myuser:mypassword@localhost:5432/mydatabase'


@pytest.mark.database
def test_get_table():
    tables = SubjectTable(db_connection_string)
    all_tables = tables.get_tables()

    assert 'subject' in all_tables, \
        "Таблица subject не найдена"


@pytest.mark.database
def test_insert():
    new_subject = SubjectTable(db_connection_string)
    max_id = new_subject.get_max_subject_id()
    new_subject.insert_in_table(max_id + 1, "New Language")
    select_from_table = new_subject.select_one_filters(max_id + 1)[0]

    assert select_from_table['subject_title'] == 'New Language'

    # Очистка после проверки
    new_subject.delete_subject(max_id + 1)


@pytest.mark.database
def test_update_subject():
    update_subj = SubjectTable(db_connection_string)
    max_id = update_subj.get_max_subject_id()
    # Сначала добавить тестовые данные
    update_subj.insert_in_table(max_id+1, "Old Language")
    # Затем обновить
    update_subj.update_subject(max_id + 1, 'Update Language')
    result = update_subj.select_one_filters(max_id + 1)[0]

    assert result['subject_title'] == 'Update Language', \
        "Значение не было обновлено"

    # Очистка после проверки
    update_subj.delete_subject(max_id + 1)


@pytest.mark.database
def test_delete_subject():
    delete_subj = SubjectTable(db_connection_string)
    max_id = delete_subj.get_max_subject_id()
    delete_subj.insert_in_table(max_id+1, "Delete language")
    delete_subj.delete_subject(max_id+1)
    res = delete_subj.select_one_filters(max_id + 1)

    assert len(res) == 0, \
        "Объект не удалился"
