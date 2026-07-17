import pytz
from datetime import datetime, time

# Define a function to convert a datetime object between two time zones
def convert_time_zone(dt, from_tz:String , to_tz: String):
    """
    What this Function do?:
    Converts a datetime object from one time zone to another.

    Args:
        dt (datetime): The datetime object to convert.
        from_tz (str): The current time zone of the datetime object.
        to_tz (str): The time zone to convert the datetime object to.

    Returns:
        datetime: The converted datetime object.
    """
    # Create timezone objects
    from_tz_obj = pytz.timezone(from_tz)
    to_tz_obj = pytz.timezone(to_tz)

    # Convert the datetime object to the 'from_tz' timezone (if necessary)
    print(dt.tzinfo)
    print(type(from_tz_obj))
    localized_dt_objt = dt.replace(tzinfo=from_tz_obj)
    print(localized_dt_objt.tzinfo)

    # Convert the datetime object to the 'to_tz' timezone
    converted_dt_obj = localized_dt_objt.astimezone(to_tz_obj)

    return converted_dt_obj


# create date object
current_date = datetime.now()

# create timezone object 
# local_timezone1 = pytz.timezone('America/New_York')
# local_timezone2 = pytz.timezone('Pacific/Honolulu')

print(convert_time_zone(current_date,'America/New_York','Pacific/Honolulu'))


