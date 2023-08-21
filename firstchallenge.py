def time_conversion(hour,duration,minute,):
    if duration == "am":
        if hour == 12:
            hour = 0
    else:
        if hour != 12:
            hour += 12
    
    return f"{hour:02d}{minute:02d}"


print(time_conversion())
print(time_conversion())