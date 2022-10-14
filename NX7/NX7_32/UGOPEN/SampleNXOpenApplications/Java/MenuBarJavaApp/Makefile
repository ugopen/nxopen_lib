NXOPENJARDIR=$(UGII_ROOT_DIR)
CLASSPATH=".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUI.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: MenuBarJavaApp.jar

MenuBarJavaApp.class:
	javac -classpath $(CLASSPATH) MenuBarJavaApp.java

MenuBarJavaApp.jar: MenuBarJavaApp.class
	echo Main-Class: MenuBarJavaApp> manifest.txt
	jar cmf manifest.txt MenuBarJavaApp.jar MenuBarJavaApp.class

run: MenuBarJavaApp.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  MenuBarJavaApp

clean_all: clean
	- rm *.class 
