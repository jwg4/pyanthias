JSON_DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"

def format_datetime(dt):
    """
    Format a datetime object into a string that Screenly can understand.
        >>> from datetime import datetime
        >>> format_datetime(datetime(2026, 4, 6, 2, 7, 41, 139000, tzinfo=timezone(timedelta(hours=1))))
        '2026-04-06T02:07:41.139000+01:00'
    """
    return dt.strftime(JSON_DATETIME_FORMAT)