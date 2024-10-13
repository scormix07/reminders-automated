import argparse
from datetime import datetime
from reminders import schedule_reminders

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description='Automate reminder scheduling in ClickUp.')
    parser.add_argument('-c', '--client', type=str, required=True, help='Client name')
    parser.add_argument('-n', '--case', type=str, required=True, help='Case number')
    parser.add_argument('-a', '--alert', type=str, choices=['low', 'medium', 'high', 'critical'], 
                        required=True, help='Alert severity level (low, medium, high, critical)')
    parser.add_argument('-d', '--date', type=str, required=True, help='Confirmation date and time (YYYY-MM-DD HH:MM)')

    return parser.parse_args()

if __name__ == "__main__":
    # Parse command line arguments
    args = parse_arguments()

    # Convert confirmation date from string to datetime object
    confirmation_date = datetime.strptime(args.date, '%Y-%m-%d %H:%M')

    # Schedule reminders based on the confirmation date and alert type
    schedule_reminders(confirmation_date, args.alert, args.client, args.case)
