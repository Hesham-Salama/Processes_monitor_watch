import wmi
import pythoncom
import threading
import time


def msToHMSMS(x):
    milliseconds = (x % 1000) / 100
    seconds = (x/1000)%60
    minutes = (x/(1000*60))%60
    hours = (x/(1000*60*60))%24
    timestr = str(hours)+":"+str(minutes)+":"+str(seconds)+"."+str(milliseconds)
    return timestr


def methodA():
    pythoncom.CoInitialize()
    window_manager = wmi.WMI()
    new_process_watcher = window_manager.Win32_Process.watch_for("creation")
    while True:
            # new processes
            new_process = new_process_watcher()
            print '------------------------------------'
            tempStr1 = "New Process created: " + str(new_process.Caption) + "\n" + "Process ID: "+\
                  str(new_process.ProcessId)+"\n"+"Path: "+str(new_process.ExecutablePath) \
                  + "\n" + "User Name of System: "+ str(new_process.CSName)+"\n"+"Time: "+msToHMSMS(int(round(time.time() * 1000)))
            print tempStr1


def methodB():
    pythoncom.CoInitialize()
    window_manager = wmi.WMI()
    stopped_process_watcher = window_manager.Win32_Process.watch_for("deletion")
    while True:
        # stopped processes
        stopped_process = stopped_process_watcher()
        print '------------------------------------'
        tempStr2 = 'Stopped Process: ' + stopped_process.Caption + "\n" + "Process ID: "+str(stopped_process.ProcessId)+"\n"+"Path: "+str(stopped_process.ExecutablePath) \
              + "\n" + "User Name of System: "+ str(stopped_process.CSName)+"\n"+"Time in UTC zone: "+msToHMSMS(int(round(time.time() * 1000)))
        print tempStr2


if __name__ == '__main__':
    thread1 = threading.Thread(target=methodA)
    thread1.start()
    thread2 = threading.Thread(target=methodB)
    thread2.start()
