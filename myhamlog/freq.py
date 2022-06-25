
# input is either a number or string in khz
def freq_to_band(f):
    fi = float(f)
    if fi < 138:
        return '2200'
    elif fi < 480:
        return '630'
    elif fi < 2001:
        return '160'
    elif fi < 4001:
        return '80'
    elif fi < 5415:
        return '60'
    elif fi < 7301:
        return '40'
    elif fi < 10151:
        return '30'
    elif fi < 14351:
        return '20'
    elif fi < 18169:
        return '17'
    elif fi < 21451:
        return '15'
    elif fi < 24991:
        return '12'
    elif fi < 29701:
        return '10'
    elif fi < 54001:
        return '6'
    elif fi < 148001:
        return '2'
    elif fi < 225001:
        return '1.25'
    elif fi < 450001:
        return '70'
    else:
        return ''

def is_2200m(khz):
    return khz >= 137.5 and khz <= 137.8

def is_630m(khz):
    return khz >= 472.0 and khz <= 479.0

def is_160m(khz):
    return khz >= 1800.0 and khz <= 2000.0

def is_80m(khz):
    return khz >= 3500.0 and khz <= 4000.0

def is_60m(khz):
    chan_width = 2.8
    return (khz >= 5330.5 and khz <= 5330.5 + chan_width) or \
        (khz >= 5346.5 and khz <= 5346.5 + chan_width) or \
        (khz >= 5357.0 and khz <= 5357.0 + chan_width) or \
        (khz >= 5371.5 and khz <= 5371.5 + chan_width) or \
        (khz >= 5403.5 and khz <= 5403.5 + chan_width)

def is_40m(khz):
    return khz >= 7000.0 and khz <= 7300.0

def is_30m(khz):
    return khz >= 10100.0 and khz <= 10150.0

def is_20m(khz):
    return khz >= 14000.0 and khz <= 14350.0 

def is_17m(khz):
    return khz >= 18068.0 and khz <= 18168.0

def is_15m(khz):
    return khz >= 21000.0 and khz <= 21450.0

def is_12m(khz):
    return khz >= 24890.0 and khz <= 24990.0

def is_10m(khz):
    return khz >= 28000.0 and khz <= 29700.0

def is_6m(khz):
    return khz >= 50000.0 and khz <= 54000.0

def is_2m(khz):
    return khz >= 144000.0 and khz <= 148000.0

def is_220Mhz(khz):
    return (khz >= 219000.0 and khz <= 220000.0) or \
        (khz >= 222000.0 and khz <= 225000.0)

def is_70cm(khz):
    return khz >= 420000.0 and khz <= 450000.0

def is_valid_freq(f):
    try:
        khz = float(f)
    except ValueError as e:
        return False
    return is_2200m(khz) or is_630m(khz) or is_160m(khz) or \
        is_80m(khz) or is_60m(khz) or is_40m(khz) or \
        is_30m(khz) or is_20m(khz) or is_17m(khz) or \
        is_15m(khz) or is_12m(khz) or is_10m(khz) or \
        is_6m(khz) or is_2m(khz) or is_220Mhz(khz) or \
        is_70cm(khz)
        