#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    # Vérification des types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Vérification contenu vide
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Pour chaque participant
    for idx, attendee in enumerate(attendees, start=1):
        # Récupération des valeurs ou "N/A"
        name = attendee.get("name", "N/A") or "N/A"
        title = attendee.get("event_title", "N/A") or "N/A"
        date = attendee.get("event_date", "N/A") or "N/A"
        location = attendee.get("event_location", "N/A") or "N/A"

        # Substitution dans le template
        content = (
            template.replace("{name}", str(name))
                    .replace("{event_title}", str(title))
                    .replace("{event_date}", str(date))
                    .replace("{event_location}", str(location))
        )

        # Nom du fichier
        filename = f"output_{idx}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Generated: {filename}")
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
