# -*- coding: utf-8 -*-

from multiprocessing import Process, Pipe
import win32com.client


# Interface with OCX component
class RobotDriverOCX():
    def __init__(self, B32_64):
        #print("init RobotDriverOCX class")
        self.B32_64 = B32_64
        self.trio = None
        self.connected=0
        self.Type=2
        self.PortMode=0
        self.trioPC_device_addr="192.168.0.250"
        self.XlimitAlarm = False
        self.YlimitAlarm = False
        self.ZlimitAlarm = False
        self.ClimitAlarm = False
        self.Xreal = -999
        self.Yreal = -999
        self.Zreal = -999
        self.Creal = -999
        self.Xprog = -999
        self.Yprog = -999
        self.Zprog = -999
        self.Cprog = -999
        
    def connect(self):
        if self.connected==0:
            try:
                if self.B32_64 == '32b':
                     self.trio = win32com.client.Dispatch("TrioPC.TrioPCCtrl.1")
                elif self.B32_64 == '64b':
                     self.trio = win32com.client.Dispatch("TrioPC64.TrioPCCtrl.1")
                
                if self.trio == None:
                    return 0, "trioPC_eth: socket not connected"
                else:
                    self.trio.SetHost(self.trioPC_device_addr)
                    status = self.trio.Open(2,0)
                    if status:
                        self.connected=1
                return status, "trioPC_eth: socket ok"
            except:
                return 0, "trioPC_eth: socket not connected"
        else:    
            return 1, "trioPC_eth: socket already connected"
    def close(self):
        self.trio.Close()
        self.connected=0
        return 1
    
    def write(self,data):
        return 0, "not implemented"
    
    def read_nl(self):
        return 0, "not implemented"
    
    def GetAxeId(self,Axe):
        if Axe=='X':
            return 0
        elif Axe=='Y':
            return 1
        elif Axe=='Z':
            return 3
        elif Axe=='C':
            return 2



    def SetLimitAlarm(self,Axe):
        if Axe=='X':
            self.XlimitAlarm=True
        elif Axe=='Y':
            self.YlimitAlarm=True
        elif Axe=='Z':
            self.ZlimitAlarm=True
        elif Axe=='C':
            self.ClimitAlarm=True
        return 0

    def UnSetLimitAlarm(self,Axe):
        if Axe=='X':
            self.XlimitAlarm=False
        elif Axe=='Y':
            self.YlimitAlarm=False
        elif Axe=='Z':
            self.ZlimitAlarm=False
        elif Axe=='C':
            self.ClimitAlarm=False
        return 0

    def SetPosProg(self,Axe, Position):
        if Axe=='X':
            self.Xprog=Position
        elif Axe=='Y':
            self.Yprog=Position
        elif Axe=='Z':
            self.Zprog=Position
        elif Axe=='C':
            self.Cprog=Position
        return 0

    def GetPosProg(self,Axe):
        if Axe=='X':
            return self.Xprog
        elif Axe=='Y':
            return self.Yprog
        elif Axe=='Z':
            return self.Zprog
        elif Axe=='C':
            return self.Cprog
        return 0


    def SetPosReal(self):
        #self.Xreal = ???
        #self.Yreal = ???
        #self.Zreal = ???
        #self.Creal = ???
        return 0


    def GetPosReal(self,Axe):
        if Axe=='X':
            return self.Xreal
        elif Axe=='Y':
            return self.Yreal
        elif Axe=='Z':
            return self.Zreal
        elif Axe=='C':
            return self.Creal
        return 0




    def In(self,i1,i2):
        if self.connected:
            try:
                status = self.trio.In(int(i1),int(i2),value)
            except Exception as ex:
                #print(ex)
                return "X", "trioOCX_eth: IN failed"
            return value, "trioPC_eth: IN ok"
        else:
            return "X", "trioOCX_eth : not connected"


    def IN(self,i1,i2):
	    return self.In(i1,i2)




    # do_execute('OP(1,0)',0.200)
    def do_execute(self,command,delay):
        if self.connected:
            try:
                status = self.trio.Execute(command)
            except:
                return "X", "trioPC_eth: do_execute failed"
            return status, "trioPC_eth : do_execute OK"
        else:
            return "X", "trioOCX_eth : not connected"


    def Execute(self,command):
        do_execute(command)



    def IsOpen(self):
        try:
            status = self.trio.IsOpen(self.PortMode)
        except Exception as ex:
	    #print(ex)
            return "X", "trioPC_eth: IsOpen failed"
        return status, "trioPC_eth: IsOpen ok"

	
    def Open(self):
        try:
            status = self.trio.Open(self.Type,self.PortMode)
        except Exception as ex:
	    #print(ex)
            return "X", "trioPC_eth: Open failed"
        return status, "trioPC_eth: Open ok"


    def SetHost(self):
        try:
            status = self.trio.SetHost(self.trioPC_device_addr)
        except Exception as ex:
	    #print(ex)
            return "X", "trioPC_eth: SetHost failed"
        return status, "trioPC_eth: SetHost ok"



    def HostAddress(self):
            return self.SetHost()




    def MoveABS(self,Axe,Position,Axis):
        print('OCX MOVEABS',Axe, Position, Axis)
        if self.connected:
            try:
                status = self.trio.MoveAbs(1,int(Position),int(Axis))
            except Exception as ex:
           #print(ex)
               return "X", "trioPC_eth: MoveABS failed"
            return status, "trioPC_eth: MoveABS ok"
        else:
            return "X", "trioOCX_eth : not connected"
	


    def Op(self,p1,p2):
        try:
            status = 0
        except Exception as ex:
	    #print(ex)
            return "X", "trioPC_eth: Op failed"
        return status, "trioPC_eth: Op ok"


    def Base(self,p1,p2):
        try:
            status = self.trio.Base(p1,p2)
        except Exception as ex:
	    #print(ex)
            return "X", "trioPC_eth: Base failed"
        return status, "trioPC_eth: Base ok"


    # SetVariable("0","1",0.250)
    def SetVariable(self,p1,p2,delay):
        try:
            status = self.trio.SetVariable(p1,p2)
        except Exception as ex:
	    #print(ex)
            return "X", "trioPC_eth: SetVariable failed"
        return status, "trioPC_eth: SetVariable ok"





#######################################################################
class RobotDriverEMULATE(RobotDriverOCX):
    
    def connect(self):
        self.connected=1
        return 1, "trioPC_eth: socket ok"

    def close(self):
        self.connected=0
        return 1
        
    def In(self,i1,i2):
        if self.connected:
            return 0, "trioPC_eth: IN ok"
        else:
            return "X", "trioOCX_eth : not connected"

    # do_execute('OP(1,0)',0.200)
    def do_execute(self,command,delay):
        if self.connected:
            return 0, "trioPC_eth : do_execute OK"
        else:
            return "X", "trioOCX_eth : not connected"

    def IsOpen(self):
        return 0, "trioPC_eth: IsOpen ok"

    def Open(self):
         return 0, "trioPC_eth: Open ok"

    def SetHost(self):
        return 0, "trioPC_eth: SetHost ok"

    def MoveABS(self,Axe,Position,Axis):
        print('OCX MOVEABS',Axe, Position, Axis)
        if self.connected:
            return 0, "trioPC_eth: MoveABS ok"
        else:
            return "X", "trioOCX_eth : not connected"

    def Op(self,p1,p2):
        return 0, "trioPC_eth: Op ok"

    def Base(self,p1,p2):
        return 0, "trioPC_eth: Base ok"

    # SetVariable("0","1",0.250)
    def SetVariable(self,p1,p2,delay):
        return 0, "trioPC_eth: SetVariable ok"




####################################################################################
#for multiprocessing
class RobotDriverProc(Process):

    def initialize(self, id, B32_64, runmode, swpipe):
        #inits
        self.connected = False
        self.hwinterface = None
        self.swpipe = swpipe #downstream end of the pipe
        self.id = id
        self.stop = False
        self.B32_64 = B32_64 #trioPC 32b or 64b version
        self.runmode = runmode #'EMULATE' or 'HW'


        
    def ping(self):
        # ping both side
        self.swpipe.send({'command':'PING', 'id':self.id})
        # wait for reply
        swr = self.swpipe.recv()
        if swr['command']=='PING':
            return 0
        else:
            return 1


    def run(self):
        
        #repeat until sw 'STOP' command is received
        while not self.stop:
            #receive sw commands
            try:
                swr = self.swpipe.recv()
            except:
                continue
            print(swr)
            self.swpipe.send({'command':'ACK', 'id':self.id})
            #decode commands
            if swr['command']=='STOP':
                self.stop = True
                print('STOP !!')
                if self.connected:
                    self.hwinterface.close()
                    self.connected = False
            elif swr['command']=='TRIO CONNECT':
                if self.connected:
                    print("TRIO CONNECT")
                    #do nothing
                else:
                    if self.runmode=='HW':
                        self.hwinterface = RobotDriverOCX(self.B32_64)
                    elif self.runmode=='EMULATE':
                        self.hwinterface = RobotDriverEMULATE(self.B32_64)
                    else:
                        #log exception
                        self.hwinterface.connect()
                        self.connected = self.hwinterface.connected
            else:
                if self.connected:
                    #decode HW commands
                    if   swr['command'] == 'HW IN':
                        status, msg = self.hwinterface.In(swr['channel1'],swr['channel2'])
                    elif swr['command'] == 'HW DO EXECUTE':
                        status, msg = self.hwinterface.do_execute(swr['commandstring'],swr['delay'])
                    elif swr['command'] == 'HW IS OPEN':
                        status, msg = self.hwinterface.IsOpen()
                    elif swr['command'] == 'HW MOVE ABS':
                        status, msg = self.hwinterface.MoveABS(swr['axe'],swr['position'], swr['axis'])
                    elif swr['command'] == 'HW BASE':
                        status, msg = self.hwinterface.Base(swr['p1'],swr['p2'])
                    elif swr['command'] == 'HW SET VARIABLE':
                        status, msg = self.hwinterface.SetVariable(swr['p1'], swr['p2'], swr['delay'])
                    else:
                        #unknown command, send NACK
                        self.swpipe.send({'command':'NACK', 'id':self.id})
                else:
                    #not connected or unknown command, send NACK
                    self.swpipe.send({'command':'NACK', 'id':self.id})
        return 0
        
        


#test
if __name__ == '__main__':
    swpipe = Pipe()
    proc_RD = RobotDriver()
    proc_RD.initialize('RD1', '64b', 'EMULATE', swpipe[1])
    proc_RD.start()
    swpipe[0].send({'command':'PING', 'id':'main_producer'})
    swpipe[0].send({'command':'MOVE', 'id':'main_producer'})
    swpipe[0].send({'command':'STOP', 'id':'main_producer'})
    proc_RD.join(100)