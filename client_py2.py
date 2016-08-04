#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import socket
import time
import os
while True:
    s = socket.socket()
    # 主服务器信息
    host = socket.gethostname()
    port = 45979
    # 连接服务器
    s.connect((host, port))
    #data = s.recv(1024)
    #print(data.decode('utf-8'))
    # 请求任务
    s.send(str('Request job,' + str(8)).encode('utf-8'))
    data = s.recv(1024).decode(u'utf-8')
    data = data.split(u',')
    print data
    if data[0] == u'Job':
        jobs = [int(data[1]), int(data[2])]
        print u'Recive jobs: ', jobs
    else:
        print u'None job'
        s.close()
        break
        
    #time.sleep(10) # 执行任务
    os.system(u"./test "+unicode(jobs[0])+u' '+unicode(jobs[1])+u' > '+unicode(jobs[0]).zfill(7)+u'_'+unicode(jobs[1]).zfill(7)+u'.dat')
    print u'Job done!'

    # 连接服务器
    s = socket.socket()
    s.connect((host, port))
    # 发送完成任务信号
    s.send(str('Done job,'+str(jobs[0])+','+str(jobs[1])).encode('utf-8'))

    s.close()
