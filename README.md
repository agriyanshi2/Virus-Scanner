indows Module:
1) A "Virus Scanner.exe" file is attached named as Virus Scanner.
2) Run the Virus Scanner.exe program, go to options menu in menu bar. Then first download the virus signature database file by clicking on "Download Database" option.
3) Click on browse option and select file to scan.

See check the source code: Windows Module->Virus_Project->Virus_Project-> Form1.cs

To change the design of project, Open Visual Studio and open the Windows Module->Virus_project->Virus_Project.sln file
This is Windows form application devloped in Visual Studio 2019.

Linux Module: 
1)[Prerequisites] Open the respective directory and run command: "pip -r requirements.txt" or "pip install hashlib"
                  database.txt file should be in the same directory as of main.py file.
2) Enter Command: python main.py {file_to_be_scanned} 
    Eg. python main.py abcd
3) This will calculate the MD5 hash of file and will match the signature from the virus database file(database.txt)
4) It will show file is infected or clean.
