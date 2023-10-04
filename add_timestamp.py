import datetime

# Get current time
now = datetime.datetime.now()

# Open readme file in append mode and add current timestamp
with open('README.md', 'a') as readme_file:
    readme_file.write(f"\n\nLast updated: {now}")
