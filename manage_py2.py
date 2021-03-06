#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import socket

N = 25 # 任务数量
undo = [1,N] # 待接受任务集合
doing = [] # 正在执行任务集合
done = [] # 已完成任务集合

s = socket.socket()
host = socket.gethostname()
port = 45979
s.bind((host, port))

s.listen(5)
print u'Wating for connection...'
while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 握手阶段
    #print('Got connection from', addr)
    #sock.send(b'Connection success!')
    # 接受请求
    data = sock.recv(1024).decode(u'utf-8')
    data = data.split(u',')
    if data[0] == u'Request job': # 请求任务
        #print('Request', data[1], 'jobs')
        reqNum = int(data[1])
        # 分配任务
        distriJob = []
        if not undo: # 若待接受任务为空，则将正在做的任务重新发出去
            for tmpjobs in doing:
                if (tmpjobs[1]-tmpjobs[0])<=reqNum:
                    distriJob = tmpjobs[:]
                    break
        else:
            maxN = undo[0]+reqNum-1
            if maxN < undo[1]: # 若请求任务数小于待接受任务数
                distriJob = [undo[0], maxN]
                undo = [maxN+1, undo[1]]
            else: # 否则将剩下的任务都分配出去
                distriJob = undo[:]
                undo = [];
            doing.append(distriJob)
        if distriJob: # 若有任务分配
            sock.send(str('Job,'+str(distriJob[0])+','+str(distriJob[1])).encode('utf-8'))
            print u'Distribute jobs:', distriJob, u'to', addr
        else: # 若没有任务分配
            sock.send('None job')
    elif data[0] == u'Done job': # 完成任务
        doneJob = [int(data[1]),int(data[2])]
        doing.remove(doneJob)
        done.append(doneJob)
        print u'Job:', doneJob, u'done by', addr
    else:
        print u'Command not defined:',data[0]
    print u'undo:', undo, u'doing', doing
    if (not undo) and (not doing):
        break
        
        
    sock.close()


