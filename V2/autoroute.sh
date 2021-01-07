#!/bin/sh
#sudo port install openjdk15
#JAVA_HOME=/Library/Java/JavaVirtualMachines/openjdk15/Contents/Home java -jar ~/Downloads/Kicad/freerouting-1.4.4-executable.jar -di . -de Greaseweazle_F7_Plus_V2.dsn -do Greaseweazle_F7_Plus_V2.ses -dr Greaseweazle_F7_Plus_V2.rules
JAVA_HOME=/Library/Java/JavaVirtualMachines/openjdk15/Contents/Home nice -n 20 java -XX:ActiveProcessorCount=4 -jar ~/Downloads/Kicad/freerouting-1.4.4-executable.jar -di . -de Greaseweazle_F7_Plus_V2.dsn -do Greaseweazle_F7_Plus_V2.ses -dr Greaseweazle_F7_Plus_V2.rules
