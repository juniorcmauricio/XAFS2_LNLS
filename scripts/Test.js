importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var tableEdge = display.getWidget("Table").getTable()
var edge = tableEdge.getCellText(0,0)
var value_edge = tableEdge.getCellText(0,1)

ConsoleUtil.writeInfo("edge = "+edge + "       value_edge = "+value_edge)




