import json
import os

all_cources = json.load(open('./assets/courses/course-list.json', 'r'))
all_cources_names = [course['filename'] for course in all_cources['courses']]
all_json_files = []

for root, dirs, files in os.walk('./assets/courses'):
    for file in files:
        if file.endswith('.json') and file != 'course-list.json':
            all_json_files.append(file)
            
            
for json_file in all_json_files:
    if json_file not in all_cources_names:
        print(f'{json_file} is not in course-list.json')