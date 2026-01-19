"""
Modified on Wed Jan  7 16:21:23 2026
@author: melvinmage

Le script de Mr. Habachi posait un problème, toutes les horraires étaient décalées de deux heures à cause de la timezone.
C'est pour cela que j'ai modifié l'ancien script en changeant seulement 2-3 choses mais qui font la différence.
"""

import sys
from datetime import datetime
from icalendar import Calendar
import csv
import pytz

ICS_FILE_LOCATION = sys.argv[1]
CSV_FILE_LOCATION = sys.argv[2]

class Convert2CSV():
    def __init__(self):
        self.csv_data = []
        self.paris_tz = pytz.timezone('Europe/Paris')

    def read_ical(self, ical_file_location):
        with open(ical_file_location, 'r', encoding='utf-8') as ical_file:
            data = ical_file.read()
        self.cal = Calendar.from_ical(data)
        return self.cal

    def make_csv(self):
        for event in self.cal.subcomponents:
            if event.name != 'VEVENT':
                continue
            
            dt_start = event.get('DTSTART').dt
            dt_end = event.get('DTEND').dt

            if isinstance(dt_start, datetime):
                dt_start = dt_start.astimezone(self.paris_tz)
            
            if isinstance(dt_end, datetime):
                dt_end = dt_end.astimezone(self.paris_tz)

            row = [
                dt_start.strftime("%Y-%m-%d"),
                dt_start.strftime("%H:%M:%S"),
                dt_end.strftime("%H:%M:%S"),
                ' : '.join(str(event.get('SUMMARY')).splitlines()),
                str(event.get('LOCATION')),
                ' : '.join(str(event.get('DESCRIPTION')).splitlines()),
            ]
            row = [x.strip() if x else "" for x in row]
            self.csv_data.append(row)

    def save_csv(self, csv_location):
        schema = ["Date", "HStart", "HEnd", "Summary", "Location", "Description"]
        with open(csv_location, 'w', encoding='utf-8', newline='') as csv_handle:
            writer = csv.writer(csv_handle)
            writer.writerow([h for h in schema])
            for row in self.csv_data:
                writer.writerow([r for r in row])

converter = Convert2CSV()
converter.read_ical(ICS_FILE_LOCATION)
converter.make_csv()
converter.save_csv(CSV_FILE_LOCATION)