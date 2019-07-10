import os
import subprocess

from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ConsoleUtil

from java.lang import Thread, Runnable

class GASSTask(Runnable):
    def run(self):
        element = PVUtil.getString(pvs[1])
        edge = PVUtil.getString(pvs[2])
        vacuum_press = PVUtil.getString(pvs[3])
        default_press = PVUtil.getString(pvs[4])
        wait_purge = PVUtil.getString(pvs[5])
        wait_vacuum = PVUtil.getString(pvs[6])
        argon_order = int(PVUtil.getDouble(pvs[7]))
        helium_order = int(PVUtil.getDouble(pvs[8]))
        nitrogen_order = int(PVUtil.getDouble(pvs[9]))

        ConsoleUtil.writeInfo("Element: " + str(element))
        ConsoleUtil.writeInfo("Edge: " + str(edge))
        ConsoleUtil.writeInfo("Vacuum_press: " + str(vacuum_press))
        ConsoleUtil.writeInfo("Default_press: " + str(default_press))
        ConsoleUtil.writeInfo("Wait_purge: " + str(wait_purge))
        ConsoleUtil.writeInfo("Wait_vacuum: " + str(wait_vacuum))
        ConsoleUtil.writeInfo("Argon_order: " + str(argon_order))
        ConsoleUtil.writeInfo("Helium_order: " + str(helium_order))
        ConsoleUtil.writeInfo("Nitrogen_order: " + str(nitrogen_order))

        command = ['gass', str(element), str(edge), "--pressureVacuum=" + str(vacuum_press), "--pressureWork=" + str(default_press), "--extraTimeManifold=" + str(wait_purge), "--extraTimeManifoldVacuum=" + str(wait_vacuum), "--argonOrder=" + str(argon_order), "--heliumOrder=" + str(helium_order), "--nitrogenOrder=" + str(nitrogen_order)]
        #command = ['python3.4', '/usr/local/bin/gass', '-h']
        #command = ['gass', '-h']

        #command = "gass %s %s" % (str(element), str(edge))

        ConsoleUtil.writeInfo("command: " + str(command))

        #pvs[0].setValue(0)

        subprocess.call(command)
        #os.system(command)


thread = Thread(GASSTask())
thread.start()