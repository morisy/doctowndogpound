import random
import re

# List of possible Lead Trainer names
lead_trainers = [
    "Waggy Tailson",
    "Barky Barker",
    "Fido McFurry",
    "Rover Canine",
    "Scooby Doo",
    "Spotty Spots"
]

# Read the staff.html file
with open("staff.html", "r") as file:
    content = file.read()

# Find the current Lead Trainer name
current_trainer = re.search(r"Lead Trainer: (\w+(?:\s+\w+){0,2})", content).group(1)

# Select a new Lead Trainer name that is different from the current one
new_lead_trainer = random.choice([name for name in lead_trainers if name != current_trainer])

# Replace the Lead Trainer name
new_content = re.sub(
    r"Lead Trainer: \w+(?:\s+\w+){0,2}",
    f"Lead Trainer: {new_lead_trainer}",
    content
)

# Write the updated content back to the staff.html file
with open("staff.html", "w") as file:
    file.write(new_content)
