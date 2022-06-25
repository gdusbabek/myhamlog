import sys
import socket
import time
from . import freq

# 'day,time,freq,call,recv,sent,mode,comment'
def make_n3fjp_message(ll):
    log_message = f'<CMD><IGNORERIGPOLLS><VALUE>TRUE</VALUE></CMD>'
    log_message += f'<CMD><ACTION><VALUE>CLEAR</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYCALL</CONTROL><VALUE>{ll.call}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYDATE</CONTROL><VALUE>{ll.day}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYRSTS</CONTROL><VALUE>{ll.sent}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYRSTR</CONTROL><VALUE>{ll.recv}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYTIMEON</CONTROL><VALUE>{ll.time}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYBAND</CONTROL><VALUE>{freq.freq_to_band(ll.freq)}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYFREQUENCY</CONTROL><VALUE>{ll.freq}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYMODE</CONTROL><VALUE>{ll.mode}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYOTHER1</CONTROL><VALUE></VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYOTHER2</CONTROL><VALUE></VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYCOMMENTS</CONTROL><VALUE>{ll.comment}</VALUE></CMD>'
    log_message += f'<CMD><ACTION><VALUE>CALLTAB</VALUE></CMD>'
    log_message += f'<CMD><ACTION><VALUE>ENTER</VALUE></CMD>'
    log_message += f'<CMD><IGNORERIGPOLLS><VALUE>FALSE</VALUE></CMD>'
    return log_message

def make_n3fjp_pota_message(ll):
    log_message = f'<CMD><IGNORERIGPOLLS><VALUE>TRUE</VALUE></CMD>'
    log_message += f'<CMD><ACTION><VALUE>CLEAR</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYCALL</CONTROL><VALUE>{ll.call}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYDATE</CONTROL><VALUE>{ll.day}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYRSTS</CONTROL><VALUE>{ll.sent}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYRSTR</CONTROL><VALUE>{ll.recv}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYTIMEON</CONTROL><VALUE>{ll.time}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYBAND</CONTROL><VALUE>{freq.freq_to_band(ll.freq)}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYFREQUENCY</CONTROL><VALUE>{ll.freq}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYMODE</CONTROL><VALUE>{ll.mode}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYOTHER1</CONTROL><VALUE>{ll.their_park}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYOTHER2</CONTROL><VALUE>{ll.my_park}</VALUE></CMD>'
    log_message += f'<CMD><UPDATE><CONTROL>TXTENTRYCOMMENTS</CONTROL><VALUE>{ll.comment}</VALUE></CMD>'
    log_message += f'<CMD><ACTION><VALUE>CALLTAB</VALUE></CMD>'
    log_message += f'<CMD><ACTION><VALUE>ENTER</VALUE></CMD>'
    log_message += f'<CMD><IGNORERIGPOLLS><VALUE>FALSE</VALUE></CMD>'
    return log_message

def write_n3fjp(data, host, port, timeout=2):
    data += '\r\n'
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((host, port))
        total_sent = 0
        while total_sent < len(data):
            just_sent = sock.send(data[total_sent:].encode())
            if just_sent == 0:
                raise RuntimeError('problem with socket write')
            total_sent += just_sent
        answer = b''
        sock.setblocking(0)
        time.sleep(0.2)
        begin = time.time()
        while True:
            if time.time() - begin > timeout:
                break
            try:
                chunk = sock.recv(4096)
                if len(chunk) > 0:
                    answer += chunk
                    begin = time.time()
                else:
                    time.sleep(0.1)
            except:
                pass# time.sleep(0.1)
        sock.close()
    except socket.error as err:
        sys.stderr.write(f'[ERROR] {str(err)}')