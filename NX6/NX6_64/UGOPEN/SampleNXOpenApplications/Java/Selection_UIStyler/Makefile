NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = .;$(NXOPENJARDIR)/NXOpen.jar;$NXOPENJARDIR)/NXOpenRun.jar;$(NXOPENJARDIR)/NXOpenRemote.jar;$(NXOPENJARDIR)/NXOpenUI.jar;$(NXOPENJARDIR)/NXOpenUIRun.jar;$(NXOPENJARDIR)/NXOpenUIRemote.jar;$(NXOPENJARDIR)/NXOpenUF.jar

compile: UIStylerSelectionExample.jar

UIStylerSelectionExample.jar: UIStylerSelectionExample.class
	echo "Main-Class: UIStylerSelectionExample" > manifest.txt
	jar cmf manifest.txt UIStylerSelectionExample.jar UIStylerSelectionExample.class
	

UIStylerSelectionExample.class:
	javac -classpath $(CLASSPATH) UIStylerSelectionExample.java
    
clean:
	- rm -f *.class
	- rm -f UIStylerSelectionExample.jar

run: UIStylerSelectionExample.jar
    	java -classpath $(CLASSPATH)  UIStylerSelectionExample


