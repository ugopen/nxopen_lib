NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = .:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUI.jar:$(NXOPENJARDIR)/NXOpenUF.jar

CreateNoteExample.jar: nxexamples/createnote/CreateNoteExample.class nxexamples/utils/DialogOutputStream.class
	echo "Main-Class: nxexamples.createnote.CreateNoteExample"> manifest.txt
	jar cmf manifest.txt CreateNoteExample.jar nxexamples
	

nxexamples/createnote/CreateNoteExample.class: nxexamples/createnote/CreateNoteExample.java nxexamples/createnote/UserSymbolDialog.java
	javac -classpath $(CLASSPATH) nxexamples/createnote/*.java

nxexamples/utils/DialogOutputStream.class: nxexamples/utils/DialogOutputStream.java
	javac nxexamples/utils/DialogOutputStream.java
    
clean:
	- rm -f nxexamples/createnote/*.class
	- rm -f nxexamples/utils/*.class
