import json


def read_json_file(file):
    with open(file, 'r') as f:
        return json.load(f)


def search_best_skills(file):
    data = read_json_file(file)
    lang_skills = {}
    lang_person = {}
    my_json_doc = data['people']
    for people in my_json_doc:
        first_name = people['first_name']
        last_name = people['last_name']
        for skills in people['skills']:
            if skills['name'] not in lang_skills.keys() or skills['level'] > lang_skills.get(skills['name']):
                lang_skills[skills['name']] = skills['level']
                lang_person[skills['name']] = '- %s %s' % (first_name, last_name)
    return lang_person


my_data = search_best_skills('data.json')
for key, value in my_data.items():
    print(key, value)
