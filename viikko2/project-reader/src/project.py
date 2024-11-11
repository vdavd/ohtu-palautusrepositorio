class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies


    def _stringify(self, content):
        return "- " + "\n- ".join(content) if len(content) > 0 else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            "\n"
            f"\nAuthors: \n{self._stringify(self.authors)}"
            "\n"
            f"\nDependencies: \n{self._stringify(self.dependencies)}"
            "\n"
            f"\nDevelopment dependencies: \n{self._stringify(self.dev_dependencies)}"
        )
