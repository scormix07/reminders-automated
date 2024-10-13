# CLI for Automated Reminder Scheduling in ClickUp

## Overview
This project automates the scheduling of reminders in ClickUp based on the confirmation sent date, alert severity, and a preset escalation matrix for different alert types.

### Files:
- `main.py`: Main script that handles command line inputs and triggers reminder scheduling.
- `config.py`: Configuration file holding ClickUp API settings and escalation matrices.
- `reminders.py`: Contains functions to add reminders in ClickUp.

### How to Run:
1. Set the required environment variables:
   - `CLICKUP_API_KEY`: Your ClickUp API key.

2. Change the `CLICKUP_LIST_ID` in `config.py` to your ClickUp list ID.

3. Open a terminal and run the following command:
   ```bash
   python main.py -c "<client_name>" -n "<case_number>" -a "<alert_severity>" -d "<confirmation_date>"
