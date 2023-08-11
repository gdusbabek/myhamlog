import sys
from . import freq
from . import line_parser

"""
USING THIS
FIRST - find the line where you type in the name or IP address of the host running N3FJP.
THEN:
python n3fjp_logger.py /path/to/your/file.log
YOUR LOG FILE
* lines starting with # are a comment.
# set up a few constants. You can change these at any time in the file just by adding a new line.
# this is very handy if you end up changing frquency.
freq: 14325
date: YYYY/MM/DD
park: X-XXXX
county: YOUR_COUNTY
state: XX
grid: XXXXxx
mode: ssb
# then, each log entry is formatted like this:
HHMM,THEIR_CALL,SENT,RECVD,COMMENT
# the comment is optional.
# If you want to log a P2P, leave their park number as the only part of the comment.
# Here are some examples:
freq: 14325
1328,xx1xxx,56,57,chuck in detroit
1331,xx2xxxx,53,59,k-3873
1332,xx3xx,59,54
# had to qsy...
freq: 14330
1334,x4xx,56,56,pa
"""

# We want to yield one of these:
# freq,call,recv,sent,mode,comment (automatically sets date/time)
def process_log(input_path):
    my_park = None
    freqs = None
    freqf = None
    band = None
    mode = 'ssb'
    dates = None
    county = None
    state = None
    grid = None

    with open(input_path, 'r') as reader:
        line = reader.readline()
        while line:
            line = line.strip().upper()
            # print(line)
            if len(line) == 0:
                pass
            elif line.startswith('#'):
                pass
            elif line.startswith('FREQ:'):
                freqs = line.split(':')[1].strip()
                band = freq.freq_to_band(freqs)
                freqf = float(freqs) / 1000.0
            elif line.startswith('MODE: '):
                mode = line.split(':')[1].strip()
            elif line.startswith('DATE:'):
                dates = line.split(':')[1].strip()
            elif line.startswith('PARK:'):
                my_park = line.split(':')[1].strip()
            elif line.startswith('COUNTY:'):
                county = line.split(':')[1].strip()
            elif line.startswith('STATE:'):
                state = line.split(':')[1].strip()
            elif line.startswith('GRID:'):
                grid = line.split(':')[1].strip()
            else:
                # processing line entry.
                # print(f'date:{dates}, freq:{freq}, park:{my_park}, state:{state}, county:{county}, grid:{grid}  {line}')
                try:
                    parts = line.split(',')
                    times = parts[0][0:2] + ':' + parts[0][2:]
                    call = parts[1]
                    their_rst = parts[2]
                    my_rst = parts[3]
                    if len(parts) > 4:
                        comment = ''.join(parts[4:])
                    else:
                        comment = ''
                    if comment.lower().startswith('k-') or \
                    comment.lower().startswith('ve-') or \
                    comment.lower().startswith('hi-'):
                        their_park = comment
                        comment = ''
                    else:
                        their_park = ''
                    
                    # day,time,freq,call,recv,sent,mode,their_park,my_park,comment
                    yield line_parser.ParkLine(dates, times, freqs, call, their_rst, my_rst, mode, their_park, my_park, comment)
                    # yield f"{dates},{times},{freqs},{call},{their_rst},{my_rst},{mode},{their_park},{my_park},{comment}"
                except IndexError:
                    print(f"Bad Line: {line}")
                    sys.exit(0)
            # read the next line.
            line = reader.readline()
