import subprocess
import os
import re
import datetime



def msg(log):
    logofile = open('./log.txt', 'a+')
    otime = datetime.datetime.now()
    logofile.write(otime.strftime('%Y-%m-%d %H:%M:%S') + "\n")
    logofile.write(log + "\n")
    logofile.close()


msg("Getting balance...")
print("Getting balance...")
b = subprocess.run('./ironfish accounts:balance',
                   shell=True,
                   stdout=subprocess.PIPE)
if b.returncode != 0:
    os._exit(0)
bsth = b.stdout
pattern = 'Amount available to spend: \$IRON ([\d\.]+)'
balance = re.findall(pattern=pattern, string=str(bsth, encoding="utf-8"))
if len(balance) == 0:
    os._exit(0)
available = balance[0]
print("Available to spend: %s" % float(available))
msg("Available to spend: %s" % float(available))
if float(available) < 0.10000001:
    os._exit(0)
print("Trying to make deposit...")
msg("Trying to make deposit...")
c = subprocess.run(
    './ironfish deposit --confirm',
    shell=True,
    stdout=subprocess.PIPE)
if c.returncode == 0:
    print(c.stdout)
    print("Deposit made")
    msg(str(c.stdout, encoding="utf-8"))
    msg("Deposit made")
else:
    os._exit(0)