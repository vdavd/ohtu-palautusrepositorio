from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella

        parsed_toml = toml.loads(content)
        for key, content in parsed_toml.items():
            print(f"{key}: {content}")

        dependencies = [dep for dep in parsed_toml["tool"]["poetry"]["dependencies"].keys()]
        dev_dependencies = [dep for dep in parsed_toml["tool"]["poetry"]["group"]["dev"]["dependencies"].keys()]
        return Project(parsed_toml["tool"]["poetry"]["name"], parsed_toml["tool"]["poetry"]["description"], dependencies, dev_dependencies, 
                       parsed_toml["tool"]["poetry"]["license"], parsed_toml["tool"]["poetry"]["authors"])
