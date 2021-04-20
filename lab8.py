from pprint import pprint

courses = [{'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False},
           {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True},
           {'name': 'andbiz3', 'field': 'android', 'attendee': 15, 'remote': False}]
pprint(courses)
courses[0]['name'] = 'Poop'
pprint(courses)
courses2 = [{'name': 'poop', 'field': 'python', 'attendee': 10, 'remote': False},
           {'name': 'bdpy', 'field': 'python', 'attendee': 15, 'remote': True},
           {'name': 'andbiz3', 'field': 'android', 'attendeen': 15, 'remote': False}]
pprint(courses2)
print(courses2[2]['attendee'])