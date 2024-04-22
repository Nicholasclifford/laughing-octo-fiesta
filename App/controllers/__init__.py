from .user import *
from .auth import *

'''
def initialize_db():
  db.drop_all()
  db.create_all()
with open('excercises.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
      workout = Workout(id=row['id'],
                        Name=row['Name'],
                        exercise_type=row['exercise_type'],
                        Targeted_body_part=row['Targeted_body_part'],
                        Video_Link=row['Video_Link'])
      db.session.add(workout)
    db.session.commit() 
    '''