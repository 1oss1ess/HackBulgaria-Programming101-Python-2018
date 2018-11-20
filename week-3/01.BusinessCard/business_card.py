import json

json_file = 'data.json'

with open(json_file, 'r') as f:
    load_json_file = json.load(f)

load_people = load_json_file['people']
user_name = []
user_age = []
user_birth_date = []
user_birth_place = []
user_gender = []
user_avatar = []
user_interests = []
user_skills_name = []
user_skills_level = []

for people in load_people:
    arr_name = []
    arr_level = []
    for skill in people['skills']:
        arr_name.append(skill['name'])
        arr_level.append(skill['level'])
    user_name.append(people['first_name'] + " " + people['last_name'])
    user_age.append(people['age'])
    user_birth_date.append(people['birth_date'])
    user_birth_place.append(people['birth_place'])
    user_gender.append(people['gender'])
    user_avatar.append(people['avatar'])
    user_interests.append(people['interests'])
    user_skills_name.append(arr_name)
    user_skills_level.append(arr_level)

for people in range(len(user_name)):
    with open(str(user_name[people].split()[0]) + '.html', 'w') as myFile:
        myFile.write('<!DOCTYPE html>\n')
        myFile.write('<html>\n')
        myFile.write('<head>\n')
        myFile.write('  <title>')
        myFile.write(user_name[people])
        myFile.write('</title>\n')
        myFile.write('  <link rel="stylesheet" type="text/css" href="styles.css">\n')
        myFile.write('</head>\n')
        myFile.write('<body>\n')
        myFile.write('  <div class="business-card male">\n')
        myFile.write('      <h1 class="full-name">' + user_name[people] + '</h1>\n')
        myFile.write('      <img class="avatar" src="avatars/' + str(user_avatar[people]) + '">\n')
        myFile.write('      <div class="base-info">\n')
        myFile.write('          <p>Age: ' + str(user_age[people]) + '</p>\n')
        myFile.write('          <p>Birth date: ' + user_birth_date[people] + '</p>\n')
        myFile.write('          <p>Birth place: ' + user_birth_place[people] + '</p>\n')
        myFile.write('          <p>Gender: ' + user_gender[people] + '</p>\n')
        myFile.write('      </div>\n')
        myFile.write('      <div class="interests">\n')
        myFile.write('          <h2>Interests:</h2>\n')
        myFile.write('          <ul>\n')
        for index in user_interests[people]:
            myFile.write("              <li>" + index + "</li>\n")
        myFile.write('          </ul>\n')
        myFile.write('      </div>\n')
        myFile.write('      <div class="skills">\n')
        myFile.write('          <h2>Skills:</h2>\n')
        myFile.write('          <ul>\n')
        for index in range(len(user_skills_name[people])):
            myFile.write('              <li>' + str(user_skills_name[people][index]) + ' - ' + str(user_skills_level[people][index]) + '</li>\n')
        myFile.write('          </ul>\n')
        myFile.write('      </div>\n')
        myFile.write('  </div>\n')
        myFile.write('</body>\n')
        myFile.write('</html>')
