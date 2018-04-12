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
var saveAs = display.getWidget("TextInput_SaveAs2").getPropertyValue("text");
var output = filePath + "/" + saveAs

var args = ""
var tableEdge = display.getWidget("Table").getTable()
var edge = tableEdge.getCellText(0,0)
var value_edge = tableEdge.getCellText(0,1)

 
if (ok){
    //ScriptUtil.executeSystemCommand("scanLine -c " + counter + " --partial " + partial + " --count "+ count + " -o " + output + " energy " + args, 10)
    ScriptUtil.executeSystemCommand("scanLineTrigger -c " + counter + " --partial " + partial + " --count "+ count + " -o " + output + " energy " + args, 10)
}
else{
    ConsoleUtil.writeInfo("Error: check input parameters")
}




