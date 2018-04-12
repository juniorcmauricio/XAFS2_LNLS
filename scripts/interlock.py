from org.csstudio.opibuilder.scriptUtil import PVUtil
import org.csstudio.opibuilder.scriptUtil.ConsoleUtil as ConsoleUtil

interlock_optical = PVUtil.getDouble(pvs[0]);
interlock_experimental = PVUtil.getDouble(pvs[1]);
interlock_warning = PVUtil.getDouble(pvs[2]);

if(interlock_optical != interlock_experimental):
	pvs[2].setValue("We need beam at experimental stations!");
	ConsoleUtil.writeInfo ("We need beam at experimental stations!")
elif (interlock_optical == 0):
	pvs[2].setValue("We need beam at experimental stations!");
	ConsoleUtil.writeInfo ("We need beam at experimental stations!")
else:
	pvs[2].setValue("Beam at experimental stations! - Experiment released!");
	ConsoleUtil.writeInfo ("Beam at experimental stations! - Experiment released!")