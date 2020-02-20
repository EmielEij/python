import os
dir_path=os.getcwd()
print("wat voor projeckt wilt u maken?")
print("[0]=Exit")
print("[1]= C program")
print("[2]= C++ program")
returnnumber =input("kies een getal")
if returnnumber == "0":
    print("Closing program")
elif returnnumber == "1":
    projecktname=input("naam van het projeckt=")
    os.chdir('c:/Users/Emiel Eij/Desktop/automated projeckts')
    os.mkdir(projecktname) 
    os.chdir('c:/Users/Emiel Eij/Desktop/automated projeckts/'+projecktname)
    aplestroph='"'
    f = open(projecktname+".c", "a")
    f.write("#include <stdio.h>")
    f.write("\n")
    f.write("\n")
    f.write("#include "+aplestroph+projecktname+".h"+aplestroph)
    f.write("\n")
    f.write("\n")
    f.write("int main() {")
    f.write("\n")
    f.write("\n")
    f.write("printf(\"hello world\");")
    f.write("\n")
    f.write("\n")
    f.write("return 0;")
    f.write("\n")
    f.write("\n")
    f.write("}")
    f.write("\n")
    f.write("\n")
    f.close()
    
    f = open(projecktname+".h", "a")
    f.write("#ifndef HEADER_FILE")
    f.write("\n")
    f.write("\n")
    f.write("#define HEADER_FILE")
    f.write("\n")
    f.write("\n")
    f.write("#endif")
    f.write("\n")
    f.write("\n")
    f.close()

    f = open(projecktname+"RunCfileTest"+".bat", "a")
    f.write("@echo off")
    f.write("\n")
    f.write("cd /d \"C:/Users/Emiel Eij/Desktop/automated projeckts/"+projecktname+"\"")
    f.write("\n")
    f.write("cmd /c gcc "+projecktname+".c")
    f.write("\n")
    f.write("echo [Begin]")
    f.write("\n")
    f.write("echo _")
    f.write("\n")
    f.write("cmd /c a")
    f.write("\n")
    f.write("echo _[End]")
    f.write("\n")
    f.write("pause")
    f.write("\n")
    f.write("del *.exe")
    f.close()

    f = open("Compile_"+projecktname+".bat", "a")
    f.write("@echo off")
    f.write("\n")
    f.write("cd /d \"C:/Users/Emiel Eij/Desktop/automated projeckts/"+projecktname+"\"")
    f.write("\n")
    f.write("del *.exe")
    f.write("\n")
    f.write("cmd /c gcc -o "+projecktname+"Execute "+projecktname+".c")
    f.write("\n")
    f.write("pause")
    f.write("\n")
    f.close()
    from shutil import copyfile
    
    print(dir_path)
    input("Press a key to continue...")
    copyfile(dir_path+"\GenerateHeader.py", "c:/Users/Emiel Eij/Desktop/automated projeckts/"+projecktname+"/GenerateHeader.py")



elif returnnumber == "2":
    print("creating c++ projeckt")

      



  



