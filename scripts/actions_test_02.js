importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

ConsoleUtil.writeInfo("Optimizing the ion chambers...")
ScriptUtil.executeSystemCommand("ic_tune", 10)