from org.csstudio.opibuilder.scriptUtil import PVUtil
import org.csstudio.opibuilder.scriptUtil.ConsoleUtil as ConsoleUtil

encoder_mono = PVUtil.getDouble(pvs[0]);
position_monotheta = PVUtil.getDouble(pvs[1]);
encoder_warning = PVUtil.getDouble(pvs[2]);

diff = abs(encoder_mono - position_monotheta);
ConsoleUtil.writeInfo (str(diff))

if(diff > 0.1):
#	pvs[2].setValue("Leitura incorreta do encoder. Faca o procedimento para a busca da posicao de referencia.");
	pvs[2].setValue("Incorrect feedback with the encoder. Do the reference search procedure.");
#	ConsoleUtil.writeInfo ("Leitura incorreta do encoder. Faca o procedimento para a busca da posicao de referencia")
	ConsoleUtil.writeInfo ("Incorrect feedback with the encoder. Do the reference search procedure.")
else:
#	pvs[2].setValue("Leitura correta do encoder - Experimento liberado");
	pvs[2].setValue("Correct feedback with the encoder. Experiment released!");
#	ConsoleUtil.writeInfo ("Leitura correta do encoder - Experimento liberado")
	ConsoleUtil.writeInfo ("Correct feedback with the encoder. Experiment released!")