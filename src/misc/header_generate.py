import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader as Loader
with open("../../questions.yaml") as question_file:
    questions = yaml.load(question_file, Loader)
    print questions