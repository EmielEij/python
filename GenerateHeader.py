import os
print("wat wilt u maken?")
print("[0]=Exit")
print("[1]= Header")
print("[2]= unit test")
returnnumber =input("Maak een keuze")
if returnnumber == "0":
    print("Closing program")
elif returnnumber == "1":
    headerName=input("Naam van de header=")
    dir_path=os.getcwd()
    os.chdir(dir_path)
    f = open(headerName+".c", "a")
    f.write("\n")
    f.write("#include \""+headerName+".h\" ")
    f.close()

    f = open(headerName+".h", "a")
    f.write("#ifndef HEADER_FILE")
    f.write("\n")
    f.write("#define HEADER_FILE")
    f.write("\n")
    f.write("\n")
    f.write("#endif")
    f.close()
    print("paste in main to include to projeckt[#include \""+headerName+".c\"]")
    input("Press a key to continue...")
    
elif returnnumber == "2":
    print("creating unit test")        