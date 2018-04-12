from org.csstudio.opibuilder.scriptUtil import PVUtil

#Height before
height = PVUtil.getDouble(pvs[0]);
heightRBV = PVUtil.getDouble(pvs[1]);

height_before = height + 0.1;

diff = abs(heightRBV - height_before)

if(diff < 0.1):
    pvs[2].setValue(0);
else:
    pvs[2].setValue(1);

