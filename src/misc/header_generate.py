import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader as Loader
def _load_questions(path):
    with open("../../questions.yaml") as question_file:
        questions = yaml.load(question_file, Loader)
        return questions

def _generate(questions,
              language,
              src_dir,
              chapter_range):
    def _get_fname(title):
        return title+'.py'
    
    def _comment(line):
        return "# " + line + '\n'
    
    def _function_header(name):
        return "def %s():\n" % name.lower().replace(" ", "_")
    
    def _default_content():
        return '\tpass\n'
    for chp_num in chapter_range:
        chapter_dic = questions[chp_num]
        title = chapter_dic.keys()[0]
        chp_questions = chapter_dic[title]
        src_file_path = src_dir+language+'/'+_get_fname(title)
        print src_file_path
        with open(src_file_path, "w") as src_file:
            for question in chp_questions:
                questitle = question.keys()[0]                
                content = question[questitle]
                code = _comment(questitle)
                code += _comment(content[0]) # discription
                code += _comment("example input/output:")
                code += _comment("in: "+str(content[1]))
                code += _comment("out: "+str(content[2]))
                code += _function_header(questitle)
                code += _default_content()
                code += '\n'
                src_file.write(code)
        pass
    pass

def _main():
    question_path = "../../questions.yaml"
    language = "python"
    src_dir = "../../src/"
    chapter_range = range(1)
    questions = _load_questions(question_path)
    _generate(questions, language, src_dir, chapter_range)


if __name__ == "__main__":
    _main()