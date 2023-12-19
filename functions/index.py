# netlify/functions/index.py
from datetime import datetime, timedelta
import json

def next_weekday(d, weekday):
    # ... [same as before] ...

def weekday_name(day):
    # ... [same as before] ...

def generate_cleaning_rota(num_weeks):
    # ... [same as before] ...

def handler(event, context):
    # Extract 'num_weeks' from the query string parameters
    num_weeks = event.get('queryStringParameters', {}).get('num_weeks', '1')

    try:
        num_weeks = int(num_weeks)
        rota = generate_cleaning_rota(num_weeks)
        body = json.dumps({"rota": rota})
        return {"statusCode": 200, "body": body}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
