

------------------------------------READ--ME-------------------------------------------------

Application: DoCSearch
Author	   : LW CS Team 5.0
Description: This is an application to search for RL50 tables among the dump files.
Notes      : Release version - 1.0.0.1	


How to Use:

1. The pre-requsite for this application is to have SearchFile.txt file present in the same folder where the exe file is present.
2. This file should not be empty.
3. Should the above 2 conditions fail, the exe file won't create a Result File.
5. The validation would be prompting properly in the CMD, please take action according to it and you should be able to proceed further.
4. There are 2 ways to execute the application.
	i. 	Open CMD and navigate to the folder where the exe file sits. Type DocSearch.exe (filename) 	
	ii. 	Double click on the DocSearch.exe (executable file) - RECOMMENDED
5. The SearchFile.txt should have the Dump of the RL50 tables which you want to take an extract of.
6. This dump is usually extracted from SQL Database of the Report Builder DB.
7. Query - SELECT Query  FROM ReportDefinitions (in the Odessa RB DB).
8. Paste the result in SearchFile.txt.
9. Run the exe file.
10.A Result file is generated with the name ResultFile.txt


Support : 

In case of any bugs/queries please reach out to the below mentioned support task group :

Dev/ Tech Architech		: devjeet.boipai@odessainc.com
QA/ BA /Requirement Architect 	: priyojit.mitra@odessainc.com