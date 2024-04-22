from App.database import db

routine_workout_association = db.Table('routine_workout_association',
    db.Column('routine_id', db.Integer, db.ForeignKey('routine.id'), primary_key=True),
    db.Column('workout_id', db.Integer, db.ForeignKey('workout.id'), primary_key=True)
)

class Routine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref='routines')
    workouts = db.relationship('Workout', secondary=routine_workout_association, backref='routines')

    def __init__(self, name, description, user_id):
        self.name = name
        self.description = description
        self.user_id = user_id

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'user_id': self.user_id,
            'workouts': [workout.get_json() for workout in self.workouts]
        }