import os

# ClickUp API Configuration
CLICKUP_API_KEY = os.getenv('CLICKUP_API_KEY')  # Store ClickUp API key in environment variables
CLICKUP_LIST_ID = 'your_clickup_list_id'  # Replace with your ClickUp list ID

# Escalation Matrix (in days for low to high, and hours for critical)
ESCALATION_MATRIX = {
    'low': [(3, 'L1 Reminder'), (5, 'L2 Reminder')],
    'medium': [(2, 'L1 Reminder'), (4, 'L2 Reminder')],
    'high': [(1, 'L1 Reminder'), (2, 'L2 Reminder')],
    'critical': [(0.5, 'L1 Reminder'), (1, 'L2 Reminder')]
}
