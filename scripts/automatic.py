from org.csstudio.opibuilder.scriptUtil import PVUtil
import org.csstudio.opibuilder.scriptUtil.ConsoleUtil as ConsoleUtil

import subprocess

from threading import Thread

status_pv = pvs[1];

# Mono Enconder
enconder_mono_pv = pvs[2]
position_monotheta_pv = pvs[3]


# Interlock
interlock_optical_pv = pvs[4];
interlock_experimental_pv = pvs[5];

# Position Mono
initial_energy_pv = pvs[6]
final_energy_pv =  pvs[7]
medium_height_pv = pvs[8]
medium_energy_pv = pvs[9]
actual_height_pv =  pvs[10]
velo_height_pv =  pvs[11]
energy_pv = pvs[12]
height_motor_dmov_pv = pvs[13]

#LEDs
LED1 = pvs[14]
LED2 = pvs[15]
LED3 = pvs[16]
LED4 = pvs[17]


def turn_off_display():
	LED1.setValue(0)
	LED2.setValue(0)
	LED3.setValue(0)
	LED4.setValue(0)
	status_pv.setValue("")

def check_mono_enconder():
	encoder_mono = PVUtil.getDouble(enconder_mono_pv);
	position_monotheta = PVUtil.getDouble(position_monotheta_pv);
	
	diff = abs(encoder_mono - position_monotheta);

	if(diff > 0.1):
		status_pv.setValue("Leitura incorreta do encoder. Faca o procedimento para a busca da posicao de referencia");
		#ConsoleUtil.writeInfo ("Leitura incorreta do encoder. Faca o procedimento para a busca da posicao de referencia")
		raise ValueError("Leitura incorreta do encoder. Faca o procedimento para a busca da posicao de referencia")

	else:
		status_pv.setValue("Leitura correta do encoder - Experimento liberado");
		ConsoleUtil.writeInfo ("Leitura correta do encoder - Experimento liberado")
		
def check_interlock():
	interlock_optical = PVUtil.getDouble(interlock_optical_pv);
	interlock_experimental = PVUtil.getDouble(interlock_experimental_pv);

	
	if(interlock_optical != interlock_experimental):
		status_pv.setValue("Necessitamos de feixe nas estacoes experimentais");
		#ConsoleUtil.writeInfo ("Necessitamos de feixe nas estacoes experimentais")
		raise ValueError("Necessitamos de feixe nas estacoes experimentais")
	elif (interlock_optical == 0):
		status_pv.setValue("Necessitamos de feixe nas estacoes experimentais");
		#ConsoleUtil.writeInfo ("Necessitamos de feixe nas estacoes experimentais")
		raise ValueError("Necessitamos de feixe nas estacoes experimentais")
	else:
		status_pv.setValue("Feixe nas estacoes experimentais - Experimento liberado");
		ConsoleUtil.writeInfo ("Feixe nas estacoes experimentais - Experimento liberado")

def mono_position_height():

	initial_energy = PVUtil.getDouble(initial_energy_pv);
	final_energy = PVUtil.getDouble(final_energy_pv);
	actual_height = PVUtil.getDouble(actual_height_pv);
	velo_height = PVUtil.getDouble(velo_height_pv);
	
	#calculations
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
	
	
	# moving motors to calculated positions
	# energy_theta
	#ConsoleUtil.writeInfo ("Movendo os motores para as posicoes calculadas...");
	#ConsoleUtil.writeInfo ("E = ");
	#ConsoleUtil.writeInfo (str(energy));
	move_motor(energy_pv, energy)
	
	#height second crystal
	height_before = height + 0.1;
	move_motor(actual_height_pv, height_before, height_motor_dmov_pv, True)

	#ConsoleUtil.writeInfo ("height_before = ");
	#ConsoleUtil.writeInfo (str(height_before));
	move_motor(actual_height_pv, height, height_motor_dmov_pv, True)
	#ConsoleUtil.writeInfo ("height = ");
	#ConsoleUtil.writeInfo (str(height));
	#ConsoleUtil.writeInfo ("Feito");

def move_motor(motor_pv, position, motor_dmov_pv = None, wait=False):
	motor_pv.setValue(position)
	if(wait == True):
		while(PVUtil.getDouble(motor_dmov_pv) == 0):
			pass
		

def check_error(cmd, value):
	if(value!=0):
		#ConsoleUtil.writeInfo("error")
		raise ValueError("Command '"+ cmd +"' returned with code: " + str(value))
			
def exec_cmd(cmd):
	e = os.system(cmd)
	check_error(cmd, e)


class Th(Thread):

	def __init__ (self):
		Thread.__init__(self)
		
	def run(self):
		try:
			turn_off_display()
			#check_mono_enconder()
			LED1.setValue(1)
			#check_interlock()
			LED2.setValue(1)
			#mono_position_height()
			LED3.setValue(1)
			#TODO: varredura_motor_pitch
			#TODO: SCAN_ENERGY 
			LED4.setValue(1)

			
		except ValueError as e:
			ConsoleUtil.writeInfo("Error: " + str(e))
			exit()
		except Exception as e:
			ConsoleUtil.writeInfo(e)
			exit()

#a = Th()
#a.start()

print("asdf") 