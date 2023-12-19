from flask import Flask, render_template, request
from datetime import datetime, timedelta
app = Flask(__name__)

def next_weekday(d, weekday):
    """Find the next specific weekday from a given date."""
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return d + timedelta(days_ahead)

def weekday_name(day):
    """Return the weekday name for a given date."""
    return day.strftime("%A")

def generate_cleaning_rota(num_weeks):
    flatmates = ['Seann', 'Charlie', 'Nikhil']
    tasks = ['Kitchen', 'Kitchen', 'Bathroom']
    rota = []

    # Find the next Wednesday from today
    start_date = next_weekday(datetime.now(), 2)  # 2 is for Wednesday

    for week in range(num_weeks):
        week_beginning = start_date + timedelta(weeks=week)
        rota.append(f"Week beginning {week_beginning.strftime('%Y-%m-%d')}:")

        for i, task in enumerate(tasks):
            # Calculate the date for each task
            if i == 0:  # First kitchen shift
                task_date = start_date + timedelta(weeks=week)
            elif i == 1:  # Second kitchen shift, 3 days after the first
                task_date = start_date + timedelta(weeks=week, days=3)
            else:  # Bathroom shift, 4 days after the first
                task_date = start_date + timedelta(weeks=week, days=4)

            weekday = weekday_name(task_date)
            flatmate = flatmates[(week + i) % len(flatmates)]
            rota.append(f"  {weekday}: {task} - {flatmate}")

    return rota

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_weeks = request.form.get('num_weeks')
        try:
            num_weeks = int(num_weeks)
            rota = generate_cleaning_rota(num_weeks)
        except Exception as e:
            print("Error:", e)
            rota = []
        return render_template('rota.html', rota=rota)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)