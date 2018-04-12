from org.csstudio.opibuilder.scriptUtil import PVUtil

#Medium energy
energy_medium = PVUtil.getDouble(pvs[0]);
energyRBV = PVUtil.getDouble(pvs[1]);
mov = PVUtil.getDouble(pvs[3]);
diff = abs(energy_medium - energyRBV)


if (diff < 0.5 & mov == 0) :
    pvs[2].setValue(1);
else:
    pvs[2].setValue(0);

