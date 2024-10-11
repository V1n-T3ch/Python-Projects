def convert_minutes_to_hours_minutes(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return hours, minutes

time_in_minutes = 100
hours, minutes = convert_minutes_to_hours_minutes(time_in_minutes)
print(f"{hours} h {minutes} m")