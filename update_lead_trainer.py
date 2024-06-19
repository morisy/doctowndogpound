import random

# List of possible Lead Trainer names
lead_trainers = [
    "Waggy Tailson",
    "Barky Barker",
    "Fido McFurry",
    "Rover Canine",
    "Scooby Doo",
    "Spotty Spots"
]

# Select a random Lead Trainer name
new_lead_trainer = random.choice(lead_trainers)

# Read the staff.html file
with open("staff.html", "r") as file:
    content = file.read()

# Replace the Lead Trainer name
new_content = content.replace(
    "Lead Trainer: Waggy Tailson",
    f"Lead Trainer: {new_lead_trainer}"
)

# Write the updated content back to the staff.html file
with open("staff.html", "w") as file:
    file.write(new_content)
