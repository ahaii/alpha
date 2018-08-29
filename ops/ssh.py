#!/usr/bin/python

import paramiko
import os
import select
import sys
import tty
import termios

trans = paramiko.Transport(('10.123.52.7', 22))
trans.start_client()
default_key_file = os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
prikey = paramiko.RSAKey.from_private_key_file(default_key_file)
trans.auth_publickey(username='root', key=prikey)

channel = trans.open_session()
channel.get_pty()
channel.invoke_shell()
oldtty = termios.tcgetattr(sys.stdin)

try:
    tty.setraw(sys.stdin)
    channel.settimeout(0)
    while True:
        readlist, writelist, errlist = select.select([channel, sys.stdin, ], [], [])
        if sys.stdin in readlist:
            input_cmd = sys.stdin.read(1)
            channel.sendall(input_cmd)

        if channel in readlist:
            result = channel.recv(1024)
            if len(result) == 0:
                print("\r\n****Over**** \r\n")
                break
            sys.stdout.write(result.decode())
            sys.stdout.flush()
finally:
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty)
channel.close()
trans.close()
