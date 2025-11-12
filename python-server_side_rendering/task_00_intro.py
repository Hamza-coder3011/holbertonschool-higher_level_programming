import os

def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a given template and list of attendees.
    Each invitation is saved as output_X.txt (starting from 1).
    """

    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        name = attendee.get("name", "N/A") or "N/A"
        event_title = attendee.get("event_title", "N/A") or "N/A"
        event_date = attendee.get("event_date", "N/A") or "N/A"
        event_location = attendee.get("event_location", "N/A") or "N/A"

        invitation_text = template.replace("{name}", name)\
            .replace("{event_title}", event_title)\
            .replace("{event_date}", event_date)\
            .replace("{event_location}", event_location)

        output_filename = f"output_{i}.txt"

        try:
            with open(output_filename, 'w', encoding='utf-8') as file:
                file.write(invitation_text)
            print(f"File '{output_filename}' created successfully.")
        except Exception as e:
            print(f"Error writing file '{output_filename}': {e}")
