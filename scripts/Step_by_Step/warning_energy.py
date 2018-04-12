from org.csstudio.opibuilder.scriptUtil import PVUtil
import org.csstudio.opibuilder.scriptUtil.ConsoleUtil as ConsoleUtil

energy = PVUtil.getDouble(pvs[0]);
energy_target = PVUtil.getDouble(pvs[1]);
ConsoleUtil.writeInfo (str(energy));
ConsoleUtil.writeInfo (str(energy_target));

if (energy == energy_target):
    pvs[2].setValue("OK");
    ConsoleUtil.writeInfo ("Atingida a energia alvo. Por favor, continue.")
else:
    pvs[2].setValue("Pressione Go");
    ConsoleUtil.writeInfo ("Energia alvo não atingida. Por favor, aguarde.")
