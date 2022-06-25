import socket
from datetime import datetime
from collections import namedtuple
from . import freq

# freq,call,recv,sent,mode,comment (automatically sets date/time)
# day,time,freq,call,recv,sent,mode,comment

# LogLine = namedtuple('LogLine', ['day', 'time', 'frequency', 'call', 'recd', 'sent', 'mode', 'comment'])
LogLine = namedtuple('LogLine', 'day,time,freq,call,recv,sent,mode,comment'.split(','))
ParkLine = namedtuple('ParkLine', 'day,time,freq,call,recv,sent,mode,their_park,my_park,comment'.split(','))

def now():
    dt = datetime.utcnow()
    return (dt.strftime('%Y/%m/%d'), dt.strftime('%H:%M'))

def is_valid_ymd(s):
    try:
        datetime.strptime(s, '%Y/%m/%d')
        return True
    except ValueError as e:
        return False

def is_valid_hhmm(s):
    try:
        datetime.strptime(s, '%H:%M')
        return True
    except ValueError as e:
        return False

def collapse_comments(parts, base_elements):
    while len(parts) > base_elements + 1:
        parts[len(parts) - 2] = parts[len(parts) - 2] + ',' + parts[len(parts) - 1]
        del parts[len(parts) - 1]
    return parts
        
def parse(rawline, base_elements=7):
    parts = rawline.split(',')
    if freq.is_valid_freq(parts[0]):
        # we only have freq,call,recv,sent,mode,comment
        # shift in day and time.
        dt = now()
        parts.insert(0, dt[1])
        parts.insert(0, dt[0])
    
    # if there is no comment, give it one.
    if len(parts) == base_elements:
        parts.append('')
    
    # there could have been a lot of commas in the comments. fix those.
    parts = collapse_comments(parts, base_elements)
    
    # at this point parts should have everything:
    # day,time,freq,call,recv,sent,mode,comment
    if len(parts) != base_elements + 1:
        raise ValueError(f"Wrong number of elements: #{len(parts)}-->{','.join(parts)}")
    
    # now lets validate...
    if not is_valid_ymd(parts[0]):
        raise ValueError(f"Invalid date: {parts[0]}")
    if not is_valid_hhmm(parts[1]):
        raise ValueError(f"Invalid time: {parts[1]}")
    if not freq.is_valid_freq(parts[2]):
        raise ValueError(f"Invalid frequency: {parts[2]}")
    # that's all we're validating.

    return parts

def parse_pota(rawline):
    return parse(rawline, base_elements=9)

def make_line(rawline, pota=False):
    parts = parse_pota(rawline) if pota else parse(rawline)
    line = ParkLine(*parts) if pota else LogLine(*parts)
    return line
