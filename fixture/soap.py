from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_project_list(self):
        username = self.app.setting["username"]
        password = self.app.setting["password"]
        client = Client(self.app.soap_url)
        try:
            client_list = client.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            return False
        list_projects = []
        for project in client_list:
            list_projects.append(Project(name=project["name"]))
        return (list_projects)

    def can_login(self, username, password):
        client = Client(self.app.soap_url)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

