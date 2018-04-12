from org.csstudio.opibuilder.scriptUtil import PVUtil

#Height before
height = PVUtil.getDouble(pvs[0]);
heightRBV = PVUtil.getDouble(pvs[1]);

diff = abs(heightRBV - height)

if(diff < 0.05):
    pvs[2].setValue(1);
else:
    pvs[2].setValue(0);

