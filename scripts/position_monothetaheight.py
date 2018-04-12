from org.csstudio.opibuilder.scriptUtil import PVUtil
#from org.csstudio.opibuilder.scriptUtil import executeSystemCommand
import org.csstudio.opibuilder.scriptUtil.ConsoleUtil as ConsoleUtil
import math
from time import *

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
                ConsoleUtil.writeInfo("begin")
                #self.exec_cmd("ic_tune")
                #ConsoleUtil.writeInfo("turn led on")
                #pvs[0].setValue(1)
                #self.exec_cmd("gedit")
                #ConsoleUtil.writeInfo("turn led off")
                #pvs[0].setValue(0)
                #self.exec_cmd("gedit")
                #ConsoleUtil.writeInfo("end")
                
                # Checar se executeSystemCommand funciona e a funcao de wait/sleep

                #PVs
                #pv0: Ei
                #pv1: Ef
                #pv2: XAFS2:Energy
                #pv3: XAFS2:DMC5:m1.RBV
                #pv4 XAFS2:DMC5:m1.VAL
                #pv5: XAFS2:DMC5:m1.VELO
                
                
                initial_energy = PVUtil.getDouble(pvs[0]);
                final_energy = PVUtil.getDouble(pvs[1]);
                actual_height = PVUtil.getDouble(pvs[3]);
                velo_height = PVUtil.getDouble(pvs[5]);
                actual_theta = PVUtil.getDouble(pvs[7]);
                velo_theta = PVUtil.getDouble(pvs[8]);
                
                #calcs
                
                offset = 18.0; #offset_DCM
                h = 6.62606896E-34;
                ev = 1.602176565E-19;
                c = 299792458;
                d = 3.13542;
                hcort_c = h/ev*c/1E-10;
                
                initial_theta = math.asin(1.2398E4/(2*initial_energy*math.pi));
                final_theta = math.asin(1.2398E4/(2*final_energy*math.pi));
                
                initial_height = offset*math.sin(initial_theta)/math.sin(2*initial_theta);
                final_height = offset*math.sin(final_theta)/math.sin(2*final_theta);
                
                height = (initial_height + final_height)/2;
                theta_calc = math.acos(offset/(2*height));
                energy = hcort_c/(2*d*math.sin(theta_calc));
                
                
                # moving motors to calculate positions
                # energy_theta
                ConsoleUtil.writeInfo ("Movendo os motores para as posicoes calculadas...");
                ConsoleUtil.writeInfo ("E = ");
                ConsoleUtil.writeInfo (str(energy));
                self.exec_cmd("caput XAFS2:Energy " + str(energy))
                theta_calc_degree = 180*theta_calc/math.pi;
                time_target = (abs(theta_calc_degree - actual_theta)/velo_theta);
                
                
                #height second crystal
                height_before = height + 0.1;
                self.exec_cmd("caput XAFS2:DMC5:m1 " +str(height_before))
                ConsoleUtil.writeInfo ("height_before = ");
                ConsoleUtil.writeInfo (str(height_before));             
                self.exec_cmd("caput XAFS2:DMC5:m1 " + str(height));
                ConsoleUtil.writeInfo ("height = ");
                ConsoleUtil.writeInfo (str(height));
                ConsoleUtil.writeInfo ("time_target = ");
                ConsoleUtil.writeInfo (str(time_target));
                sleep(time_target);
                ConsoleUtil.writeInfo ("Feito");
                #end_var = True


a = Th()
a.start()