from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        self.form_filling(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.projects_cache = None

    def delete(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.projects_cache = None

    def open_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def form_filling(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    projects_cache = None

    def get_project_list(self):
        if self.projects_cache is None:
            wd = self.app.wd
            self.open_projects_page()
            self.projects_cache = []
            for element in wd.find_elements_by_xpath("//tr[starts-with(@class, 'row-')] ")[1:-2]:
                name_text = element.find_element_by_xpath(".//td[1]").text
                status_text = element.find_element_by_xpath(".//td[2]").text
                enabled_text = element.find_element_by_xpath(".//td[3]").text
                description_text = element.find_element_by_xpath(".//td[5]").text
                self.projects_cache.append(Project(name=name_text, status=status_text, enabled=enabled_text,
                                                   description=description_text))
            return list(self.projects_cache)