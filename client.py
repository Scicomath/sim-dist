import socket
import time
import os
while True:
    s = socket.socket()
    # 主服务器信息
    host = '192.168.164.178'
    port = 45979
    # 连接服务器
    s.connect((host, port))
    #data = s.recv(1024)
    #print(data.decode('utf-8'))
    # 请求任务
    s.send(bytes('Request job,' + str(8), 'utf-8'))
    data = s.recv(1024).decode('utf-8')
    data = data.split(',')
    print(data)
    if data[0] == 'Job':
        jobs = [int(data[1]), int(data[2])]
        print('Recive jobs: ', jobs)
    else:
        print('None job')
        s.close()
        break
        
    #time.sleep(10) # 执行任务
    os.system("./test "+str(jobs[0])+' '+str(jobs[1])+' > '+str(jobs[0]).zfill(7)+'_'+str(jobs[1]).zfill(7)+'.dat')
    print('Job done!')

    # 连接服务器
    s = socket.socket()
    s.connect((host, port))
    # 发送完成任务信号
    s.send(bytes('Done job,'+str(jobs[0])+','+str(jobs[1]), 'utf-8'))

    s.close()
