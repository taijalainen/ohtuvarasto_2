import toml
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = toml.loads(content)
        #print(data)

        return Project(data['tool']['poetry']['name'],
        data['tool']['poetry']['description'],
        data['tool']['poetry']['dependencies'],
        data['tool']['poetry']['group']['dev']['dependencies'])
        #return Project("Test name", "Test description", [], [])
