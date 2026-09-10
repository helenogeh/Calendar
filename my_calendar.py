
# Import the built-in calendar module
import calendar

# Ask the user to enter the year
year = int(input("Enter the year (e.g., 2026): "))

# Display the entire 12-month calendar for that year
print("\nHere is your 12-month calendar:")
print(calendar.calendar(year))
