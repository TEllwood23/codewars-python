def format_duration(seconds):
    # initialise dict. with year, days, hours, second
    # if statement that checks for zero

    unit_times = {}

    if seconds == 0:
        return "now"
    else:
        unit_times["years"] = seconds//31536000
        after_years = seconds%31536000
        unit_times["days"] = after_years//86400
        after_days = after_years%86400
        unit_times["hours"] = after_days//3600
        after_hours = after_days%3600
        unit_times["mins"] = after_hours//60
        unit_times["secs"] = int(after_hours%60)
    # extract no. years from seconds
    # extract no. days from remaining seconds
    # extract no. hours from remaining seconds
    # record remaining seconds
    # format into final string
    final_string = ""

    if unit_times["years"] > 1:
        years = f"{unit_times['years']} years"
    elif unit_times["years"] == 1:
        years = f"{unit_times['years']} year"
    elif unit_times["years"] == 0:
        years = None

    if unit_times["days"] > 1:
        days = f"{unit_times['days']} days"
    elif unit_times["days"] == 1:
        days = f"{unit_times['days']} day"
    elif unit_times["days"] == 0:
        days = None

    if unit_times["hours"] > 1:
        hours = f"{unit_times['hours']} hours"
    elif unit_times["hours"] == 1:
        hours = f"{unit_times['hours']} hour"
    elif unit_times["hours"] == 0:
        hours = None

    if unit_times["mins"] > 1:
        minutes = f"{unit_times['mins']} minutes"
    elif unit_times["mins"] == 1:
        minutes = f"{unit_times['mins']} minute"
    elif unit_times["mins"] == 0:
        minutes = None

    if unit_times["secs"] > 1:
        seconds = f"{unit_times['secs']} seconds"
    elif unit_times["secs"] == 1:
        seconds = f"{unit_times['secs']} second"
    elif unit_times["secs"] == 0:
        seconds = None

    final_string = ""

    last_time = True


    if seconds:
        final_string = f" and {seconds}"
        last_time = False

    if minutes:
        if last_time:
            final_string = f" and {minutes}"
            last_time = False
        else:
            final_string = f", {minutes}" + f"{final_string}"

    if hours:
        if last_time:
            final_string = f" and {hours}"
            last_time = False
        else:
            final_string = f", {hours}" + f"{final_string}"

    if days:
        if last_time:
            final_string = f" and {days}"
            last_time = False
        else:
            final_string = f", {days}" + f"{final_string}"

    if years:
        if last_time:
            final_string = f" and {years}"
            last_time = False
        else:
            final_string = f", {years}" + f"{final_string}"

    final_string=final_string[2:]

    if unit_times["years"] == 0 and unit_times["days"] == 0 and unit_times["hours"] == 0 and unit_times["mins"] == 0 and unit_times["secs"] == 0:
        final_string = "now"

    if unit_times["years"] == 0 and unit_times["days"] == 0 and unit_times["hours"] == 0 and unit_times["mins"] == 0:
        final_string = f"{seconds}"

    if unit_times["years"] == 0 and unit_times["days"] == 0 and unit_times["hours"] == 0 and unit_times["secs"] == 0:
        final_string = f"{minutes}"

    if unit_times["years"] == 0 and unit_times["days"] == 0 and unit_times["mins"] == 0 and unit_times["secs"] == 0:
        final_string = f"{hours}"

    if unit_times["years"] == 0 and unit_times["hours"] == 0 and unit_times["mins"] == 0 and unit_times["secs"] == 0:
        final_string = f"{days}"

    if unit_times["days"] == 0 and unit_times["hours"] == 0 and unit_times["mins"] == 0 and unit_times["secs"] == 0:
        final_string = f"{years}"
    return final_string
    # return final_string, seconds, minutes, days, years

print(f"Test 1 = {format_duration(0)}")
print(f"Test 1 = {format_duration(1)}")
print(f"Test 1 = {format_duration(62)}")
print(f"Test 1 = {format_duration(120)}")
print(f"Test 1 = {format_duration(3600)}")
print(f"Test 1 = {format_duration(3662)}")
print(f"Test 1 = {format_duration(15731080)}")
print(f"Test 1 = {format_duration(132030240)}")
print(f"Test 1 = {format_duration(205851834)}")
print(f"Test 1 = {format_duration(242062374)}")
print(f"Test 1 = {format_duration(101956166)}")
print(f"Test 1 = {format_duration(33243586)}")


    # for each of "year", "day" etc. may need if statement to pluralise unit or not
