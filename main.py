import ping3
ping3.EXCEPTIONS = True

import time
import datetime
from pathlib import Path

logfile = Path('ping.log.csv')

if not logfile.exists():
    with open(logfile, 'w', encoding='utf8') as f:
        f.write('date,ping,error\n')

while True:
    pingtime = -1
    pingerror = ''

    try:
        pingtime = ping3.ping("192.5.5.241")  # F root dns / mirror in msk
    except ping3.errors.PingError as e:
        pingerror = str(e)
    except OSError as e:
        pingtime = -2
        pingerror = str(e)

    date = datetime.datetime.now().isoformat()
    with open(logfile, 'a', encoding='utf8') as f:
        f.write(f'{date},{pingtime},"{pingerror}"\n')

    print(date, pingtime, pingerror)

    waittime = 30 # seconds
    if pingtime < 0.:
        waittime = 5

    try:
        time.sleep(waittime)
    except KeyboardInterrupt:
        print('bye')
        break


