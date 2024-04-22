from flask import Flask, render_template, request
from your_module_name import db, Workout

app = Flask(__name__)



@app.route('/search', methods=['GET', 'POST'])
def search_exercise():
    if request.method == 'POST':
        # Get the exercise name from the form data
        exercise_name = request.form.get('search')
        
        # Retrieve the exercise from the database by name
        exercise = Workout.query.filter_by(excercise=exercise_name).first()

        return render_template('index.html', exercise=exercise)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)