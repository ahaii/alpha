# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from assets.models import Servers
from django.http import HttpResponse
import paramiko
import json
import os
import select
import sys
import tty
import termios
from dwebsocket import require_websocket

# Create your views here.


def index(request):
    pass


def webssh(request, server_id):
    host_obj = Servers.objects.get(id=server_id)
    host = host_obj.IIP
    return render(request, 'web_term.html', {'ip': json.dumps(host), 'id': json.dumps(server_id)})


# accept_websocket()装饰器,可以处理http及websocket请求
# require_websocket()装饰器,只能处理websocket请求
@require_websocket
def websocket(request, server_id):
    if not request.is_websocket():
        # noinspection PyBroadException
        # 由于except没有指定捕获错误类型,PyCharm会报异常,加上上面一句,忽略这个.
        try:
            message = request.GET['message']
            return HttpResponse(message)
        except:
            return render(request, 'servers.html')
    else:
        # host_obj = Servers.objects.get(id=server_id)
        # host = host_obj.IIP
        for message in request.websocket:
            if not message:
                print('message is noll')
                break
            else:
                message += message
                print(message)
        request.websocket.send(message)


def commandhandle(request, host, command):
    private_key = paramiko.RSAKey.from_private_key_file('/Users/ahaii/.ssh/id_rsa')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, 22, username='root', pkey=private_key)
    stdin, stdout, stderr = ssh.exec_command(command)
    result = stdout.read()
    return result


def webssh1(request, server_id):
    host_obj = Servers.objects.get(id=server_id)
    host = host_obj.IIP
    trans = paramiko.Transport((host, 22))
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
