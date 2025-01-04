import datetime

def get_day_from_date_in_hindi(date_string):
    # Convert the date string from "dd.mm.yyyy" to a datetime object
    date_obj = datetime.datetime.strptime(date_string, "%d.%m.%Y")
    
    # Get the day of the week (0 = Monday, 6 = Sunday)
    day_of_week = date_obj.strftime("%A")
    
    # Map the English day to Hindi
    days_in_hindi = {
        "Monday": "सोमवार",
        "Tuesday": "मंगलवार",
        "Wednesday": "बुधवार",
        "Thursday": "गुरुवार",
        "Friday": "शुक्रवार",
        "Saturday": "शनिवार",
        "Sunday": "रविवार"
    }
    
    # Return the day in Hindi
    return days_in_hindi.get(day_of_week, "Invalid day")

# Example date in "dd.mm.yyyy" format
date_input = "04.01.2025"  # Input date in "DD.MM.YYYY" format
day = get_day_from_date_in_hindi(date_input)
print(f"The day for {date_input} in Hindi is: {day}")
