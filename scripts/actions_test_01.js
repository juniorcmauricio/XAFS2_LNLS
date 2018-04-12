importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

ConsoleUtil.writeInfo("Moving the motor...")
ScriptUtil.executeSystemCommand("caput XAFS2:DMC2:m8.VAL 5", 10)