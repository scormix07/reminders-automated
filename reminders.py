import requests
from config import CLICKUP_API_KEY, CLICKUP_LIST_ID, ESCALATION_MATRIX
from datetime import datetime, timedelta

# Function to create a task in ClickUp
def create_clickup_task(task_name, due_date):
    url = f'https://api.clickup.com/api/v2/list/{CLICKUP_LIST_ID}/task'
    headers = {
        'Authorization': CLICKUP_API_KEY,
        'Content-Type': 'application/json'
    }
    
    task_data = {
        'name': task_name,
        'due_date': int(due_date.timestamp() * 1000),  # Convert to milliseconds
        'status': 'open'
    }

    response = requests.post(url, headers=headers, json=task_data)
    
    if response.status_code == 200:
        print(f'Task "{task_name}" created successfully with due date {due_date}.')
    else:
        print(f'Error creating task: {response.status_code} - {response.text}')

# Function to schedule reminders based on escalation matrix
def schedule_reminders(confirmation_date, alert_type, client_name, case_number):
    if alert_type in ESCALATION_MATRIX:
        for time_period, level in ESCALATION_MATRIX[alert_type]:
            # Determine due date based on alert type
            if alert_type == 'critical':
                due_date = confirmation_date + timedelta(hours=time_period)
            else:
                due_date = confirmation_date + timedelta(days=time_period)
            
            task_name = f'{level} for {alert_type.capitalize()} Alert - Client: {client_name}, Case: {case_number}'
            create_clickup_task(task_name, due_date)
    else:
        print(f'Unknown alert type: {alert_type}')
