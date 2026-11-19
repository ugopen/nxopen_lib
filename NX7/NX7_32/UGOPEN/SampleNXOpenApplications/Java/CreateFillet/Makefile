NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = ".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: CreateFillet.jar

CreateFillet.class:
	javac -classpath $(CLASSPATH) CreateFillet.java

CreateFillet.jar: CreateFillet.class
	echo Main-Class: CreateFillet> manifest.txt
	jar cmf manifest.txt CreateFillet.jar CreateFillet.class

run: CreateFillet.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  CreateFillet

clean:
	- rm CreateFillet.prt

clean_all: clean
	- rm *.class
