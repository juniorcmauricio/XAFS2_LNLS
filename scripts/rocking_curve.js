importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

function monthName(n) {
    if (n == 0)  { return "January";   }
    if (n == 1)  { return "February";  }
    if (n == 2)  { return "March";     }
    if (n == 3)  { return "April";     }
    if (n == 4)  { return "May";       }
    if (n == 5)  { return "June";      }
    if (n == 6)  { return "July";      } 
    if (n == 7)  { return "August";    }
    if (n == 8)  { return "September"; }
    if (n == 9)  { return "October";   }
    if (n == 10) { return "November";  }
    if (n == 11) { return "December";  }
}

var filePath = "/storage/"
var dateObj = new Date();
var year = dateObj.getFullYear();
var month = dateObj.getMonth();
var user = display.getWidget("TextInput_User").getPropertyValue("text");
filePath += year + "/" + monthName(month) + "/" + user 
ScriptUtil.executeSystemCommand("mkdir -p "+ filePath, 10)
//var saveAs = display.getWidget("TextInput_SaveAs").getPropertyValue("text");
var saveAs = "Rocking_curve";
var output = filePath + "/" + saveAs

//ScriptUtil.executeSystemCommand(caput(XAFS2:DMC5:m2.SET, 1), 10)
//ScriptUtil.executeSystemCommand(caput(XAFS2:DMC5:m2.VAL, 0), 10)
//ScriptUtil.executeSystemCommand(caput(XAFS2:DMC5:m2.SET, 0), 10)

//ConsoleUtil.writeInfo("Scaning motor pitch...")
//ScriptUtil.executeSystemCommand("scan -o " + output + " -c " + c + " " + optimumStr + " -- " + motor1 + args + " " + t, 10)
//ScriptUtil.executeSystemCommand("scan -o " + output + " -c " + I0 + " " + --optimum xafs2i0 + " -- " + MonoPitch + -0.04 0.04 0.001 + " " + 1, 10)
ConsoleUtil.writeInfo("Optimizing the ion chambers...")
//ScriptUtil.executeSystemCommand("ic_tune; sleep(45); scan -o " + output + " -c I0 --optimum xafs2i0 Goniometro -1 1 0.5 1", 10)
ScriptUtil.executeSystemCommand("ic_tune", 10)
ConsoleUtil.writeInfo("Testing the scan with goniometer motor.")
ScriptUtil.executeSystemCommand("scan -o " + output + " -c I0 --optimum xafs2i0 Goniometro -1 1 0.5 1", 10)

//ScriptUtil.executeSystemCommand("scan -o /storage/2017/May/Junior/Rocking_Curve_test_gonio -c I0 --optimum xafs2i0 Goniometro -10 10 1 1", 10)


