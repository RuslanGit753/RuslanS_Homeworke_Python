from page_api import YoProApi
import pytest


api = YoProApi('https://ru.yougile.com/api-v2')
key_auth = 'P92YEbiSLfh3ha2GzZI48oZZssvkq3so4m8CQ9cEO8FefsXrLzAUiX6geeGzfZge'


@pytest.mark.positive_test
def test_create_project_positive():
    name_project = 'Новый проект создан'
    response = api.create_project(name_project, key_auth)

    assert response.json() != ''
    assert response.status_code == 201


@pytest.mark.negative_test
def test_create_project_negative():
    name_project = ''
    response = api.create_project(name_project, key_auth)

    assert response.status_code == 400


@pytest.mark.positive_test
def test_change_project_positive():
    name_project = 'Проект по захвату Земли'
    response = api.create_project(name_project, key_auth)
    id_company = response.json()['id']

    new_name = 'Проект по захвату Вселенной'
    resp_new = api.change_project(new_name, key_auth, id_company)

    assert resp_new.json() != ''
    assert resp_new.status_code == 200


@pytest.mark.negative_test
def test_change_project_negative():
    name_project = 'Проект по захвату Земли'
    response = api.create_project(name_project, key_auth)
    id_company = response.json()['id']

    new_name = ''
    resp_new = api.change_project(new_name, key_auth, id_company)

    assert resp_new.status_code == 400


@pytest.mark.positive_test
def test_get_project_id_positive():
    response = api.get_all_project(key_auth)
    last_id_project = response.json()['content'][-1]['id']

    get_id_project = api.get_project_id(key_auth, last_id_project)
    get_title_project = get_id_project.json()['title']
    assert get_title_project == 'Проект по захвату Земли'


@pytest.mark.negative_test
def test_get_project_id_negative():
    response = api.get_all_project(key_auth)
    last_id_project = response.json()['content'][-1]['id'][:-1]

    get_id_project = api.get_project_id(key_auth, last_id_project)
    assert get_id_project.status_code == 404
