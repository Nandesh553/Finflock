###Setting up the SQL SERVER with Java###

##To download the Sql Server Developer Edition, go to the link below:
    [a link](https://www.microsoft.com/en-in/download/details.aspx?id=1695)
    * Run it to start the SQL installer
	* Click Basic in Select an installation type
	* Click Accept after you have read the license terms
	* (Optional) if you need to, you can choose a custom installation location for SQL Server
	* Click Install to proceed with the installation

#Further installation steps.
	*Use Windows username and password.
	*Select 'mixed mode'.
	*Set up a default password.


##Connecting the java appplication to sql server.

#Download the Microsoft JDBC Driver 6.0 for SQL Server
	[a link](https://www.microsoft.com/en-us/download/details.aspx?id=11774)
* Unzip the file and go to sqljdbc_version\enu\auth\x86 or \x64 
* Copy the sqljdbc_auth.dll to C:\Program Files\Java\jre_Version\bin
* Finally restart eclipse.

#Download the Java driver from the following link.
* If downloading by yourself, make sure it is 'sqljdbc4'.
	[a link](http://www.java2s.com/Code/JarDownload/sqljdbc4/sqljdbc4-2.0.jar.zip)
* Add the jar to the respective classpath.

# Use the url for sql server something as mentioned below.
# Make sure to replace the yourDatabaseName in the url:
	'''
	jdbc:sqlserver://localhost;databaseName=yourDataBaseName;
	'''
Now if the port is not set to "1433"
#You need to Go to 
	`Start > Microsoft SQL Server > Configuration Tools > SQL Server Configuration Manager`

#When it opens Go to 

	* SQL Server Configuration Manager > SQL Server Network Configuration > Protocols for SQLExpress 

#Where you'll find the Protocol TCP/IP, if disabled then Enable it Click on TCP/IP, You'll find its properties.

#In this properties REMOVE ALL THE TCP DYNAMIC PORTS AND ADD VALUE OF 1433 TO ALL TCP PORT and restart
	* `SQL Server Services > SQL Server` 
	*And Its Done.

## All the required files are already present in the folder.