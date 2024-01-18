import pandas as pd 

# Read the Excel file as input
df = pd.read_excel('Assignment_Timecard.xlsx')

# Initialize variables
consecutive_days = []
less_than_10_hours = []
more_than_14_hours = []

# Iterate through the data structure and identify employees who meet the following criteria
for i in range(len(df)):
    # Check for 7 consecutive days
    if i + 6 < len(df) and df.iloc[i:i+7]['Employee Name'].nunique() == 1:
        consecutive_days.append((df.iloc[i]['Employee Name'], df.iloc[i]['Position ID']))
    
    # Check for less than 10 hours of time between shifts but greater than 1 hour
    if i > 0 and (df.iloc[i]['Time'] - df.iloc[i-1]['Time Out']).seconds / 3600 < 10 and (df.iloc[i]['Time'] - df.iloc[i-1]['Time Out']).seconds / 3600 > 1:
        less_than_10_hours.append((df.iloc[i]['Employee Name'], df.iloc[i]['Position ID']))
    
    # Check for more than 14 hours in a single shift
    if (df.iloc[i]['Time Out'] - df.iloc[i]['Time']).seconds / 3600 > 14:
        more_than_14_hours.append((df.iloc[i]['Employee Name'], df.iloc[i]['Position ID']))

# Print the name and position of the identified employees to the console
print("Employees who have worked for 7 consecutive days:")
for employee in consecutive_days:
    print(f"{employee[0]} ({employee[1]})")

print("\nEmployees who have less than 10 hours of time between shifts but greater than 1 hour:")
for employee in less_than_10_hours:
    print(f"{employee[0]} ({employee[1]})")

print("\nEmployees who have worked for more than 14 hours in a single shift:")
for employee in more_than_14_hours:
    print(f"{employee[0]} ({employee[1]})")

# Write console output to output.txt in the base folder of the Git repo
with open('output.txt', 'w') as f:
    f.write("Employees who have worked for 7 consecutive days:\n")
    for employee in consecutive_days:
        f.write(f"{employee[0]} ({employee[1]})\n")
    
    f.write("\nEmployees who have less than 10 hours of time between shifts but greater than 1 hour:\n")
    for employee in less_than_10_hours:
        f.write(f"{employee[0]} ({employee[1]})\n")
    
    f.write("\nEmployees who have worked for more than 14 hours in a single shift:\n")
    for employee in more_than_14_hours:
        f.write(f"{employee[0]} ({employee[1]})\n") 
