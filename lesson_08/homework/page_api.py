import requests


class YoProApi:

    def __init__(self, url):
        self.url = url

    def create_project(self, name_project, key_auth):
        headers = {
            'Authorization': f'Bearer {key_auth}'
        }
        name_pro = {
            'title': name_project
        }
        body = requests.post(f'{self.url}/projects',
                             json=name_pro, headers=headers)
        return body

    def change_project(self, new_name, key_auth, id_company):
        headers = {
            'Authorization': f'Bearer {key_auth}'
        }
        change_pro = {
            'title': new_name
        }
        body = requests.put(f'{self.url}/projects/{id_company}',
                            json=change_pro, headers=headers)
        return body

    def get_all_project(self, key_auth):
        headers = {
            'Authorization': f'Bearer {key_auth}'
        }
        body = requests.get(f'{self.url}/projects', headers=headers)
        return body

    def get_project_id(self, key_auth, last_id_project):
        headers = {
            'Authorization': f'Bearer {key_auth}'
        }
        body = requests.get(f'{self.url}/projects/{last_id_project}',
                            headers=headers)
        return body
