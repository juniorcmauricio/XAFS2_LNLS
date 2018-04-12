from org.csstudio.opibuilder.scriptUtil import PVUtil
from java.lang import Thread
import org.csstudio.opibuilder.scriptUtil.ConsoleUtil as ConsoleUtil

import time
import os

ConsoleUtil.writeInfo(str(time.clock()))

end_var = False


from threading import Thread

class Th(Thread):



        def __init__ (self):
                Thread.__init__(self)

        def check_error(self, value):
                if(value!=0):
                        ConsoleUtil.writeInfo("error")
                        exit()
        def exec_cmd(self, cmd):
                a = os.system(cmd)
                self.check_error(a)

        def run(self):
                global end_var
                ConsoleUtil.writeInfo("Rocking curve")
                self.exec_cmd("ic_tune")
                #ConsoleUtil.writeInfo("turn led on")
                #pvs[0].setValue(1)
                self.exec_cmd("scan -o /storage/2017/May/Junior/Rocking_Curve_test_gonio -c I0 --optimum xafs2i0 MonoPitch -0.05 0.05 0.001 1")
                #ConsoleUtil.writeInfo("turn led off")
                #pvs[0].setValue(0)
                #self.exec_cmd("gedit")
                ConsoleUtil.writeInfo("end")
                #end_var = True


a = Th()
a.start()
