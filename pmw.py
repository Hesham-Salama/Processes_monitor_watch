import wmi
import pythoncom
import threading
import time


def msToHMSMS(x):
    milliseconds = (x % 1000) / 100
    seconds = (x/1000)%60
    minutes = (x/(1000*60))%60
    hours = (x/(1000*60*60))%24
    if hours<10:
        hours = "0"+str(hours)
    if minutes<10:
        minutes = "0"+str(minutes)
    if seconds<10:
        seconds = "0"+str(seconds)
    timestr = str(hours)+":"+str(minutes)+":"+str(seconds)+"."+str(milliseconds)
    return timestr


def methodA():
    pythoncom.CoInitialize()
    window_manager = wmi.WMI()
    new_process_watcher = window_manager.Win32_Process.watch_for("creation")
    while True:
        try:
            # new processes
            new_process = new_process_watcher()
            timeCatch = "Time in UTC: " + msToHMSMS(int(round(time.time() * 1000)))
            tempStr1 = "------------------------------------\nCreated Process: " + str(new_process.Caption) + "\n" + "Process ID: "+\
                  str(new_process.ProcessId)+"\n"+"Path: "+str(new_process.ExecutablePath) \
                  + "\n" + "User Name of System: "+ str(new_process.CSName)+"\n"+timeCatch
            print tempStr1
        except Exception:
            print "\n"+'Exception happened in creation processes watch module'


def methodB():
    pythoncom.CoInitialize()
    window_manager = wmi.WMI()
    stopped_process_watcher = window_manager.Win32_Process.watch_for("deletion")
    while True:
        try:
            # stopped processes
            stopped_process = stopped_process_watcher()
            timeCatch2 = "Time in UTC: "+msToHMSMS(int(round(time.time() * 1000)))
            tempStr2 = '------------------------------------\nStopped Process: ' + stopped_process.Caption + "\n" + "Process ID: "+str(stopped_process.ProcessId)+"\n"+"Path: "+str(stopped_process.ExecutablePath) \
                  + "\n" + "User Name of System: "+ str(stopped_process.CSName)+"\n"+timeCatch2
            print tempStr2
        except Exception:
            print 'Exception happened in deletion processes watch module'


if __name__ == '__main__':
    thread1 = threading.Thread(target=methodA)
    thread1.start()
    thread2 = threading.Thread(target=methodB)
    thread2.start()
