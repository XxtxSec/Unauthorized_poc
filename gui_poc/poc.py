import socket

import time
import pymongo
from PyQt5.QtCore import QThread, pyqtSignal
import re
from pymongo.errors import ServerSelectionTimeoutError


class work_poc(QThread):
    mysignal=pyqtSignal(str)
    ProgressBar_signal = pyqtSignal(int)
    check_input=pyqtSignal(str)
    def __init__(self):
        super(work_poc, self).__init__()
    def write_txt(self,mode,ip,port):
        f=open('../res.txt', 'a+')
        f.write('存在'+'{}'.format(mode)+'  '+str(ip)+':'+str(port)+'\n')
        f.close()

    def poc_redis(self,mode,ip,port):
        try:
            A = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            A.settimeout(2)

            A.connect((ip, int(port)))
            A.send("info\r\n".encode("utf-8"))
            res = A.recv(1024)
            B = str(res, 'utf-8')
            if "Server" in B:
                self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip) + ":" + str(port) + "  登录成功存在redis未授权漏洞")
                self.write_txt(mode,ip,port)
            elif "Clients" in B:

                self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip) + ":" + str(port) + "  登录成功存在redis未授权漏洞")
                self.write_txt(mode,ip,port)
            elif "Memory" in B:

                 self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip) + ":" + str(port) + "  登录成功存在redis未授权漏洞")
                 self.write_txt(mode,ip, port)
            else:

                self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+'{}{}{}'.format(ip,':',port)+'   不存在redis未授权漏洞')
        except ConnectionRefusedError:
            self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+'{}{}{}'.format(ip,':',port)+"   不存在redis未授权漏洞")
        except socket.timeout:
            self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+':'+str(port)+"   连接超时,不存在redis未授权")

    def poc_ftp(self,mode,ip,port):
        try:
          Socket = socket.socket()
          Socket.settimeout(2)
          Socket.connect((str(ip), int(port)))
          A = Socket.recv(1024)
          Socket.send("USER anonymous\r\n".encode('utf-8'))
          B = Socket.recv(1024)
          Socket.send("PASS 1234567@qq.com\r\n".encode('utf-8'))
          C = str(Socket.recv(1024))
          if 'successful' in C:
                 self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+"  登录成功存在FTP匿名登陆")

                 self.write_txt(mode,ip,port)
          else:
              self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+"  不存在FTP匿名登录漏洞漏洞")
        except socket.timeout:
            self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip) + ':' + str(port) + "  连接超时，不存在FTP匿名登录漏洞漏洞")
        except:
            self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+"  无法连接，不存在FTP匿名登录漏洞漏洞")
    def poc_MongoDB(self,mode,ip,port):
        try:
            DB_connect = pymongo.MongoClient(ip, int(port), serverSelectionTimeoutMS=3000,socketTimeoutMS=3000)
            DB_name = DB_connect.list_database_names()
            if DB_name:
                self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+'存在Mongodb未授权漏洞，数据库名称为：' + str(DB_name))
                self.write_txt(mode, ip, port)
        except   ServerSelectionTimeoutError:

            self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+"   连接超时,不存在MongoDB未授权漏洞")
        except :
            self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+"   连接超时,不存在MongoDB未授权漏洞")

    def poc_zookeeper(self,mode,ip, port):
        try:
            connect = socket.socket()
            connect.settimeout(3)
            connect.connect((ip, int(port)))
            connect.send('envi'.encode())
            res = connect.recv(1024).decode()

            if "Environment" in res:
                self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+'  存在Zookeeper未授权漏洞')
                self.write_txt(mode, ip, port)
            elif "whitelist" in res:
                self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+'  已设置访问白名单,不存在Zookeeper未授权漏洞')
            else:
                self.mysignal.emit('[' + str(time.strftime("%H:%M:%S", time.localtime())) + '] [info]  ' + str(ip) + ":" + str(port) + '  不存在Zookeeper未授权漏洞')

        except ConnectionRefusedError:
            self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+'  无法连接不存在Zookeeper未授权漏洞')
        except :
            self.mysignal.emit('['+str(time.strftime("%H:%M:%S", time.localtime()) )+'] [info]  '+str(ip)+":"+str(port)+'  无法连接不存在Zookeeper未授权漏洞')
    def  checkip(self,ip_port):

        A = re.findall(r'([0-9]+):', ip_port)  # ip最后一位是否小于255
        B = re.findall(r'([0-9]+)\.', ip_port)  # ip前三位是否小于255
        C = re.findall(r':([0-9]+)', ip_port)  # 端口是否小于65535
        D = re.findall(r':', ip_port)  # 是否存在中文的:

        if len(D) !=1:
            self.check_input.emit('请输入英文:')
            return 'invalid'

        elif len([x for x in A if int(x) >= 0 and int(x) <= 65535]) != 1 or len([x for x in B if int(x) >= 0 and int(x) <= 255]) != 3:
            self.check_input.emit('ip输入错误')
            return 'invalid'

        elif len([x for x in C if int(x)>=0 and int(x)<=65535])!=1:
            self.check_input.emit('端口输入错误')
            return 'invalid'

    def run(self):
        poc_number=4
        if self.mode == 'redis未授权':
            self.poc_redis(self.mode, self.ip, self.port)
            self.ProgressBar_signal.emit(100)
            time.sleep(1)
            self.ProgressBar_signal.emit(0)
        if self.mode == 'FTP匿名访问':
            self.poc_ftp(self.mode, self.ip, self.port)
            self.ProgressBar_signal.emit(100)
            time.sleep(1)
            self.ProgressBar_signal.emit(0)
        if self.mode=='MongoDB未授权':
            self.poc_MongoDB(self.mode,self.ip,self.port)
            self.ProgressBar_signal.emit(100)
            time.sleep(1)
            self.ProgressBar_signal.emit(0)
        if self.mode=='Zookeeper未授权':
            self.poc_zookeeper(self.mode,self.ip,self.port)
            self.ProgressBar_signal.emit(100)
            time.sleep(1)
            self.ProgressBar_signal.emit(0)
        if self.mode == '全量检测':
            self.poc_redis("redis未授权", self.ip, self.port)
            self.ProgressBar_signal.emit((1/poc_number)*100)
            self.poc_ftp("FTP未授权", self.ip, self.port)
            self.ProgressBar_signal.emit((2/poc_number)*100)
            self.poc_MongoDB("MongoDB未授权", self.ip, self.port)
            self.ProgressBar_signal.emit((3 / poc_number) * 100)
            self.poc_zookeeper("Zookeeper未授权", self.ip, self.port)
            self.ProgressBar_signal.emit((4 / poc_number) * 100)
            self.mysignal.emit("结果已存在当前目录下的res.txt中")




class many_run(work_poc):
    def __init__(self,mode,ip_port):
        super(many_run, self).__init__()
        self.mode=mode
        self.ip_port=ip_port
    def run(self):
      try:
        ip_number=len(self.ip_port)
        poc_number=4
        run_count = 0
        for x in self.ip_port:

            run_count=run_count+1
            index = x.index(':')
            ip = x[:index]
            port = x[index + 1:]
            # print(port)
            if self.mode == 'redis未授权':
                self.poc_redis(self.mode, ip, port)
                self.ProgressBar_signal.emit((run_count/ip_number)*100)
            if self.mode == 'FTP匿名访问':
                self.poc_ftp(self.mode, ip, port)
                self.ProgressBar_signal.emit((run_count/ip_number)*100)
            if self.mode == 'MongoDB未授权':
                self.poc_MongoDB(self.mode, ip, port)
                self.ProgressBar_signal.emit((run_count/ip_number)*100)
            if self.mode == 'Zookeeper未授权':
                self.poc_zookeeper(self.mode, ip, port)
                self.ProgressBar_signal.emit((run_count/ip_number)*100)
            if self.mode == '全量检测':
                self.poc_redis("redis未授权",ip, port)
                self.poc_ftp("FTP未授权", ip, port)
                self.poc_zookeeper("Zookeeper未授权",ip,port)
                self.poc_MongoDB("MongoDB未授权", ip, port)
                self.ProgressBar_signal.emit(run_count/(ip_number)*100)
        self.mysignal.emit("运行完毕已将运行结果存储到当前目录下的res.txt文件中")
      except ValueError:
            self.mysignal.emit("输入错误，请重新输入")
      except :
          self.mysignal.emit("读取文件出现错误")



