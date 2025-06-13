import requests
import pytest
from youGile import ProjectApi

base_url = "https://yougile.com/api-v2/projects/"
# Вставить полученный токен
token = ''
my_headers = {'Authorization': f'Bearer {token}',
              'Content-Type': 'application/json'
              }


@pytest.fixture()
def add_project():
    data = {
        "title": "Yaya",
        "users": {
            "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
        }
    }
    resp = requests.post(base_url, json=data, headers=my_headers)
    added_project = resp.json()
    return added_project["id"]


@pytest.mark.positive
def test_positive_add_project():
    main_page = ProjectApi(base_url, my_headers)
    new_project = main_page.ads_project('Homework 22')
    assert new_project.status_code == 201
    assert 'id' in new_project.json(), \
        "В ответе нет id"
    assert len(new_project.json()) == 1, \
        "Ответ должен возвращать только одно значение"
    assert isinstance(new_project.json()['id'], str), \
        "Значение id не является строкой"


@pytest.mark.negative
def test_empty_title_project():
    main_page = ProjectApi(base_url, my_headers)
    empty_title_project = main_page.empty_title_project()
    assert empty_title_project.status_code == 400, \
        "Поле title не может быт пустым"


@pytest.mark.negative
def test_xml_headers():
    main_page = ProjectApi(base_url, my_headers)
    xml_in_project = main_page.xml_headers()
    assert xml_in_project.status_code == 400, \
        "Тело запроса должно быть в формате JSON"


@pytest.mark.negative
def test_title_not_string():
    main_page = ProjectApi(base_url, my_headers)
    project_without_title = main_page.title_not_string()
    assert project_without_title.status_code == 400, \
        "Поле title принимает не string"


@pytest.mark.negative
def test_request_other_method():
    main_page = ProjectApi(base_url, my_headers)
    other_method = main_page.request_other_method()
    assert other_method.status_code == 404, \
        "Запрос отправлен не методом POST"


@pytest.mark.negative
def test_wrong_token():
    main_page = ProjectApi(base_url, my_headers)
    bad_token = main_page.wrong_token()
    assert bad_token.status_code == 401, \
        "Запрос отправлен с неправильным токеном"


@pytest.mark.negative
def test_empty_token():
    main_page = ProjectApi(base_url, my_headers)
    empty_token_project = main_page.empty_token()
    assert empty_token_project.status_code == 401, \
        "Запрос отправлен с пустым токеном"


@pytest.mark.positive
def test_change_project(add_project):
    main_page = ProjectApi(base_url, my_headers)
    changes_project = main_page.change_project(add_project)
    assert changes_project.status_code == 200, \
        "Проект не удалось отредактировать"
    assert changes_project.json()['id'] == add_project, \
        "id измененного проекта != id изменяемого проекта"
    assert isinstance(changes_project.json()['id'], str), \
        "Значение id не является строкой"


@pytest.mark.negative
def test_wrong_id():
    main_page = ProjectApi(base_url, my_headers)
    wrong_id_project = main_page.wrong_id()
    assert wrong_id_project.status_code == 404, \
        f"Ожидаемый статус код: 404, а получили: {wrong_id_project}"


@pytest.mark.negative
def test_empty_id():
    main_page = ProjectApi(base_url, my_headers)
    project_empty_id = main_page.empty_id()
    assert project_empty_id.status_code == 404, \
        f"Ожидаемый статус код: 404, а получили: {project_empty_id}"


@pytest.mark.negative
def test_change_project_with_post(add_project):
    main_page = ProjectApi(base_url, my_headers)
    change_other_method = main_page.change_project_with_post(add_project)
    assert change_other_method.status_code == 404, \
        f"Ожидаемый статус код: 404, а получили: {change_other_method}"


@pytest.mark.positive
def test_get_project_by_id(add_project):
    main_page = ProjectApi(base_url, my_headers)
    getting_project = main_page.get_project_by_id(add_project)
    assert getting_project.status_code == 200, \
        "Проект по id не найден"
    assert 'id' in getting_project.json(), \
        "В ответе не возвращается id"
    assert add_project == getting_project.json()['id'], \
        "id в запросе == id в ответе"
    assert 'title' in getting_project.json(), \
        "В ответе не возвращается title проекта"
    assert 'timestamp' in getting_project.json(), \
        "В ответе не возвращается время создания проекта"
    assert isinstance(getting_project.json()['timestamp'], int), \
        "Значение timestamp не является числом"


@pytest.mark.negative
def test_nonexistent_project():
    main_page = ProjectApi(base_url, my_headers)
    nonex_project = main_page.nonexistent_project()
    assert nonex_project.status_code == 404, \
        f"Ожидаемый статус: 404, а получен: {nonex_project}"
