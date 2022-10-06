import imp
from turtle import speed
from unittest import TestResult
import speedtest
import csv
from datetime import datetime




def Test_speed():
    speed_Test = speedtest.Speedtest()
    speed_Test.get_best_server()

    #Download Speed
    downspeed = speed_Test.download()
    DownloadSpeedMBs = round(downspeed / (10**6),2)

    #Upload Speed
    UploadSpeed = speed_Test.upload()
    UploadSpeedMBs = round(UploadSpeed / (10**6),2)
    #Ping load
    ping = speed_Test.results.ping

    return(ping ,UploadSpeedMBs, DownloadSpeedMBs)


def CsvWrite(TestResult):
    date_today = datetime.today().strftime("%m/%d/%Y")
    with open('internetTestResult.csv','a',newline='') as file:
        
        writ_tercsv = csv.writer(file)
        
        writ_tercsv.writerow([date_today,TestResult[0],TestResult[1],TestResult[2]])


csv_write = Test_speed()

CsvWrite(csv_write)