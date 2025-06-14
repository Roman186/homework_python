import requests


class ProjectApi:
    def __init__(self, base_url, my_headers):
        self.base_url = base_url
        self.my_headers = my_headers
        # Вставить полученный токен
        self.token = ''

    def ads_project(self, title):
        data = {
            "title": f"{title}",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        resp = requests.post(
            self.base_url, json=data, headers=self.my_headers)
        return resp

    def empty_title_project(self):
        data = {
            "title": "",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        resp = requests.post(
            self.base_url, json=data, headers=self.my_headers)
        return resp

    def xml_headers(self):
        headers = {'Authorization': f'Bearer {self.token}',
                   'Content-Type': 'application/xml'
                   }
        data = {
            "title": "Work 1",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        resp = requests.post(
            self.base_url, json=data, headers=headers)
        return resp

    def title_not_string(self):
        data = {
            "title": 11,
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        resp = requests.post(
            self.base_url, json=data, headers=self.my_headers)
        return resp

    def request_other_method(self):
        data = {
            "title": "job",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        resp = requests.put(
            self.base_url, json=data, headers=self.my_headers)
        return resp

    def wrong_token(self):
        wrng_token = "S3kCv326H5TJIa34UHpsE-bfP0ddrepRhs03tyuihsbTSbEkvtmLstwLrhmRMpy"
        headers = {'Authorization': f'Bearer {wrng_token}',
                   'Content-Type': 'application/json'
                   }
        data = {
            "title": "bad token",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        resp = requests.put(
            self.base_url, json=data, headers=headers)
        return resp

    def empty_token(self):
        empt_token = ""
        headers = {'Authorization': f'Bearer {empt_token}',
                   'Content-Type': 'application/json'
                   }
        data = {
            "title": "empty token",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        resp = requests.put(
            self.base_url, json=data, headers=headers)
        return resp

    def change_project(self, add_project):
        data_change = {
            "deleted": False,
            "title": "Измененный проект",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        id_project = add_project['id']
        resp = requests.put(
            self.base_url + id_project, json=data_change,
            headers=self.my_headers)
        return resp

    def wrong_id(self):
        data_change = {
            "deleted": False,
            "title": "gggg",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        wrong_id = '344bdsf-32'
        resp = requests.put(
            self.base_url + wrong_id, json=data_change,
            headers=self.my_headers)
        return resp

    def empty_id(self):
        data_change = {
            "deleted": False,
            "title": "empty id",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        empty_id = ""
        resp = requests.put(
            self.base_url + empty_id, json=data_change,
            headers=self.my_headers)
        return resp

    def change_project_with_post(self, project):
        data_change = {
            "deleted": False,
            "title": "patch method",
            "users": {
                "05b014a0-01bd-4e2e-bb8d-b0adf40683a1": "admin"
            }
        }
        id_project = project['id']
        resp = requests.post(
            self.base_url + id_project, json=data_change,
            headers=self.my_headers)
        return resp

    def get_project_by_id(self, project):
        searched_id = project['id']
        resp = requests.get(
            self.base_url + searched_id, headers=self.my_headers)
        return resp

    def nonexistent_project(self):
        nonex_id = '1d8b29ff-2af2-47dadf0-a1a6-ba874'
        resp = requests.get(
            self.base_url + nonex_id, headers=self.my_headers)
        return resp
