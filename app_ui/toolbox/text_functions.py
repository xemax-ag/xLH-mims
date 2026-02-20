from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def datetime_to_ui(dt: datetime | None = None, time: bool = True, date: bool = True) -> str:
    if dt is None:
       dt = datetime.now(ZoneInfo('Europe/Berlin'))
        
    if time and date:
        return dt.strftime('%H:%M:%S - %d:%m:%y')
    elif time:
        return dt.strftime('%H:%M:%S')
    elif date:
        return dt.strftime('%d:%m:%y')
    else:
        return dt.strftime('%H:%M:%S - %d:%m:%y')

if __name__ == '__main__':
    print(datetime_to_ui())