from model.project import Project
import random
import string


def random_string(prefix, maxlen):
  symbols = string.ascii_letters + string.digits
  return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    project = Project(name=random_string('name', 10), description=random_string('test', 10))
    old_projects = app.soap.get_project_list()
    app.project.create(project)
    old_projects.append(project)
    new_projects = app.soap.get_project_list()
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
