from genericpath import exists
from re import S
from textwrap import wrap
import requests
import os
import platform

useLegacyJar = False
current_java17_path = ""
current_java8_path = ""
#Retrieve path to java if already set, if not set those paths
for line in open('current_java17_path.txt'):
    current_java17_path = line.strip()
    break
if current_java17_path == "":
    current_java17_path = input("Please enter the path to the java 17 file : ")
    with open('current_java17_path.txt', 'w') as f:
        f.write(current_java17_path)
check = os.system("\""+current_java17_path+"\" -version")
if check != 0:
    print("Invalid java 17 path, delete the contents of current_java17_path.txt and try again")
    exit()
for line in open('current_java8_path.txt'):
    current_java8_path = line.strip()
    break
if current_java8_path == "":
    current_java8_path = input("Please enter the path to the java 8 file: ")
    with open('current_java8_path.txt', 'w') as f:
        f.write(current_java8_path)
check = os.system("\""+current_java8_path+"\" -version")
if check != 0:
    print("Invalid java 8 path, delete the contents of current_java8_path.txt and try again")
    exit()
#Ask the user for the name of the server
serverName = input("Please enter the name of the server or enter list to list all currently installed servers : ")
os.makedirs("servers", exist_ok=True)
currentServers = os.listdir("servers")
if serverName == "list":
    print("Currently installed servers:")
    print(currentServers)
if serverName in currentServers:
    os.chdir("servers/"+serverName)
    print("Server found, starting server...")
    if platform.system() == "Windows":
        os.system("run.bat")
    else:
        os.system("run.sh")

os.chdir("servers")
os.makedirs(serverName, exist_ok=True)
os.chdir(serverName)

#Ask the user what type of minecraft server they want to use
print("What type of minecraft server do you want to use?")
print("1. Paper Minecraft Server")
print("2. Forge Minecraft Server")
serverType = input(">")

#Ask the user what version of minecraft they want to use
print("What version of minecraft do you want to use?")
print("1. 1.8")
print("2. 1.9")
print("3. 1.10")
print("4. 1.11")
print("5. 1.12")
print("6. 1.13")
print("7. 1.14")
print("8. 1.15")
print("9. 1.16")
print("10. 1.17")
print("11. 1.18")
print("12. 1.19")
print("13. Manual (Recommended if the version you are installing is fairly recent)")
serverVersion = input(">")
url = ""
if serverType == "1":
    if serverVersion == "1" or serverVersion == "1.8":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.8.8/builds/445/downloads/paper-1.8.8-445.jar"
        useLegacyJar = True
    elif serverVersion == "2" or serverVersion == "1.9":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.9.4/builds/775/downloads/paper-1.9.4-775.jar"
        useLegacyJar = True
    elif serverVersion == "3" or serverVersion == "1.10":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.10.2/builds/918/downloads/paper-1.10.2-918.jar"
        useLegacyJar = True
    elif serverVersion == "4" or serverVersion == "1.11":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.11.2/builds/1106/downloads/paper-1.11.2-1106.jar"
        useLegacyJar = True
    elif serverVersion == "5" or serverVersion == "1.12":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar"
        useLegacyJar = True
    elif serverVersion == "6" or serverVersion == "1.13":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar"
        useLegacyJar = True
    elif serverVersion == "7" or serverVersion == "1.14":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar"
        useLegacyJar = True
    elif serverVersion == "8" or serverVersion == "1.15":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar"
        useLegacyJar = True
    elif serverVersion == "9" or serverVersion == "1.16":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar"
        useLegacyJar = True
    elif serverVersion == "10" or serverVersion == "1.17":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar"
    elif serverVersion == "11" or serverVersion == "1.18":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/386/downloads/paper-1.18.2-386.jar"
    elif serverVersion == "12" or serverVersion == "1.19":
        url = "https://api.papermc.io/v2/projects/paper/versions/1.19/builds/36/downloads/paper-1.19-36.jar"
    elif serverVersion == "13" or serverVersion == "Manual":
        url = input("Please enter the url to the server jar: ")
    else:
        print("Invalid version")
        exit()
elif serverType == "2":
    if serverVersion == "1" or serverVersion == "1.8":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.8.9-11.15.1.2318-1.8.9/forge-1.8.9-11.15.1.2318-1.8.9-installer.jar"
        useLegacyJar = True
    elif serverVersion == "2" or serverVersion == "1.9":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.9.4-12.17.0.2317-1.9.4/forge-1.9.4-12.17.0.2317-1.9.4-installer.jar"
        useLegacyJar = True
    elif serverVersion == "3" or serverVersion == "1.10":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.10.2-12.18.3.2511/forge-1.10.2-12.18.3.2511-installer.jar"
        useLegacyJar = True
    elif serverVersion == "4" or serverVersion == "1.11":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.11.2-13.20.1.2588/forge-1.11.2-13.20.1.2588-installer.jar"
        useLegacyJar = True
    elif serverVersion == "5" or serverVersion == "1.12":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.12.2-14.23.5.2860/forge-1.12.2-14.23.5.2860-installer.jar"
        useLegacyJar = True
    elif serverVersion == "6" or serverVersion == "1.13":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.13.2-25.0.223/forge-1.13.2-25.0.223-installer.jar"
        useLegacyJar = True
    elif serverVersion == "7" or serverVersion == "1.14":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.14.4-28.2.26/forge-1.14.4-28.2.26-installer.jar"
        useLegacyJar = True
    elif serverVersion == "8" or serverVersion == "1.15":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.15.2-31.2.57/forge-1.15.2-31.2.57-installer.jar"
        useLegacyJar = True
    elif serverVersion == "9" or serverVersion == "1.16":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.16.5-36.2.35/forge-1.16.5-36.2.35-installer.jar"
        useLegacyJar = True
    elif serverVersion == "10" or serverVersion == "1.17":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.17.1-37.1.1/forge-1.17.1-37.1.1-installer.jar"
    elif serverVersion == "11" or serverVersion == "1.18":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.18.2-40.1.0/forge-1.18.2-40.1.0-installer.jar"
    elif serverVersion == "12" or serverVersion == "1.19":
        url = "https://maven.minecraftforge.net/net/minecraftforge/forge/1.19-41.0.45/forge-1.19-41.0.45-installer.jar"
    elif serverVersion == "13" or serverVersion == "Manual":
        url = input("Please enter the url to the forge installer jar: ")
    else:
        print("Invalid version")
        exit()
if serverType == "1":
    r = requests.get(url, allow_redirects=True)
    open("server.jar", "wb").write(r.content)
    if useLegacyJar:
        g = open("run.bat", "w")
        g.write("@echo off\n")
        g.write("\"" + current_java8_path + "\" -Xmx1024M -Xms1024M -jar server.jar")
        g.close()
        h = open("run.sh", "w")
        h.write("#!/bin/bash\n")
        h.write("java -Xmx1024M -Xms1024M -jar server.jar")
        h.close()
        os.system("chmod +x run.sh")
    else:
        g = open("run.bat", "w")
        g.write("@echo off\n")
        g.write("\"" + current_java8_path + "\" -Xmx1024M -Xms1024M -jar server.jar")
        g.close()
        h = open("run.sh", "w")
        h.write("#!/bin/bash\n")
        h.write("java -Xmx1024M -Xms1024M -jar server.jar")
        h.close()
        os.system("chmod +x run.sh")
elif serverType == "2":
    r = requests.get(url, allow_redirects=True)
    open("forge.jar", "wb").write(r.content)
    if useLegacyJar:
        os.system("\"" + current_java8_path + "\" -jar forge.jar --installServer")
        os.remove("run.bat")
        os.remove("run.sh")
        g = open("run.bat", "w")
        g.write("@echo off\n")
        g.write("\"" + current_java8_path + "\" @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.19-41.0.45/win_args.txt %*")
        g.close()
        h = open("run.sh", "w")
        h.write("#!/bin/bash\n")
        h.write("\"" + current_java8_path + "\" @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.19-41.0.45/linux_args.txt $@")
        h.close()
        os.system("chmod +x run.sh")
    else:
        os.system("\"" + current_java17_path + "\" -jar forge.jar --installServer")
        os.remove("run.bat")
        os.remove("run.sh")
        g = open("run.bat", "w")
        g.write("@echo off\n")
        g.write("\"" + current_java17_path + "\" @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.19-41.0.45/win_args.txt %*")
        g.close()
        h = open("run.sh", "w")
        h.write("#!/bin/bash\n")
        h.write("\"" + current_java8_path + "\" @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.19-41.0.45/linux_args.txt $@")
        h.close()
        os.system("chmod +x run.sh")
#Ask user if they agree to the eula
print("Do you agree to the EULA at https://aka.ms/MinecraftEULA ? (y/n)")
eula = input(">")
if eula.lower() == "y" or eula.lower() == "yes" or eula.lower() == "true" or eula.lower() == "t":
    file = open("eula.txt", "w")
    file.write("eula=true")
    file.close()
    if platform.system() == "Windows":
        os.system("run.bat")
    else:
        os.system("run.sh")

else:
    print("You must agree to the EULA to use this server")
    exit()
