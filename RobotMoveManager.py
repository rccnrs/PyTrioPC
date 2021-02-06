# -*- coding: utf-8 -*-

from multiprocessing import Process, Pipe

class RobotMoveManager(Process):

    def initialize(self,id,swpipe,hwpipe):
        #inits
        self.swpipe = swpipe #downstream end of the pipe
        self.hwpipe = hwpipe #upstream end of the pipe 
        self.id = id
        self.stop = False
        
    def ping(self):
        # ping both side
        self.swpipe.send({'command':'PING', 'id':self.id})
        self.hwpipe.send({'command':'PING', 'id':self.id})
        # wait for reply
        swr = self.swpipe.recv()
        hwr = self.hwpipe.recv()
        if swr['command']=='PING' and hwr['command']=='PING':
            return 0
        else:
            return 1


    def run(self):
        
        #repeat until sw 'STOP' command is received
        while not self.stop:
            #receive sw commands
            swr = self.swpipe.recv()
            print(swr)
            self.swpipe.send({'command':'ACK', 'id':self.id})
            #decode commands
            if swr['command']=='STOP':
                self.stop = True
                print('STOP !!')
            elif swr['command']=='MOVE':
            #check move with external lib
            ##not implemented
            #send secure hw command
            ##not implemented
                self.hwpipe.send(swr) #bypass
            else:
                self.swpipe.send({'command':'NACK', 'id':self.id})
        return 0
        
        


#test
if __name__ == '__main__':
    swpipe = Pipe()
    hwpipe = Pipe()
    proc_RMM = RobotMoveManager()
    proc_RMM.initialize('RMM1', swpipe[1], hwpipe[0])
    proc_RMM.start()
    swpipe[0].send({'command':'PING', 'id':'main_producer'})
    swpipe[0].send({'command':'MOVE', 'id':'main_producer'})
    swpipe[0].send({'command':'STOP', 'id':'main_producer'})
    proc_RMM.join(100)