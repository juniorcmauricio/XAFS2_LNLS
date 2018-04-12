from org.csstudio.opibuilder.scriptUtil import PVUtil
#from org.csstudio.opibuilder.scriptUtil import executeSystemCommand
import org.csstudio.opibuilder.scriptUtil.ConsoleUtil as ConsoleUtil
import math

# Checar se executeSystemCommand funciona e a funcao de wait/sleep

#PVs
#pv0: Ei
#pv1: Ef
#pv2: E_medial
#pv3: height_medial

initial_energy = PVUtil.getDouble(pvs[0]);
final_energy = PVUtil.getDouble(pvs[1]);

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

pvs[2].setValue(energy);
pvs[3].setValue(height);

# moving motors to calculate positions
# energy_theta
ConsoleUtil.writeInfo ("Energia e altura médias calculadas:");
ConsoleUtil.writeInfo ("E = ");
ConsoleUtil.writeInfo (str(energy));
ConsoleUtil.writeInfo ("height = ");
ConsoleUtil.writeInfo (str(height));

