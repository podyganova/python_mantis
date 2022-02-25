from model.project import Project
import random


def test_delete_project(app):
    old_projects = app.soap.get_project_list()
    if len(old_projects) == 0:
        app.project.create(Project(name="test", description="test"))
        old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.delete(project)
    old_projects.remove(project)
    new_projects = app.soap.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
