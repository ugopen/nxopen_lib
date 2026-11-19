NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = ".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: CreateArcThru3pts.jar

CreateArcThru3pts.class:
	javac -classpath $(CLASSPATH) CreateArcThru3pts.java

CreateArcThru3pts.jar: CreateArcThru3pts.class
	echo Main-Class: CreateArcThru3pts> manifest.txt
	jar cmf manifest.txt CreateArcThru3pts.jar CreateArcThru3pts.class

run: CreateArcThru3pts.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  CreateArcThru3pts

clean:
	- rm CreateArcThru3pts.prt

clean_all: clean
	- rm *.class
