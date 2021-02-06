# -*- coding: utf-8 -*-

#https://medium.com/swlh/dashboards-in-python-for-beginners-and-everyone-else-using-dash-f0a045a86644

import dash
from dash.dependencies import Input, Output, State

import time

import multiprocessing as mp

# import dash app for robot control GUI
from RobotGUI_dash import app as controlgui
from RobotGUI_dash import guiconnect as pipecontrolgui
from RobotMoveManager import RobotMoveManager as RMM
from RobotDriver import RobotDriverProc as HW

def guireceiver(pipe):
    ecount=0
    while True:
        try:
            time.sleep(0.5)
            msg = pipe[1].recv()
            print("MAIN RECEIVED :", msg)
        except Exception as e:
            print("EXECEPTION {}".format(e))
            ecount=ecount+1
            if ecount<20:
                pass
            else:
                return




# launch modules
if __name__ == '__main__':
    Test=True
    ### HW interface
    proc_HW = HW()
    proc_HW.initialize('RD1', '64b', 'EMULATE', hwpipe[1])
    proc_HW.start()
    
    ### move manager
    swpipe = mp.Pipe()
    hwpipe = mp.Pipe()
    proc_RMM = RMM()
    proc_RMM.initialize('RMM1', swpipe[1], hwpipe[0])
    proc_RMM.start()
    if Test:
        swpipe[0].send({'command':'PING', 'id':'main_producer'})
        swpipe[0].send({'command':'MOVE', 'id':'main_producer'})
        swpipe[0].send({'command':'STOP', 'id':'main_producer'})
    
    ###controler
    p=mp.Process(target=guireceiver, args=(pipecontrolgui,))
    p.start()
    
    ###gui dash
    controlgui.run_server(debug=True)
    
    proc_RMM.join(100)
    p.join()