NXOPENJARDIR=$(UGII_ROOT_DIR)
CLASSPATH=".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: CreateArc.jar

CreateArc.class:
	javac -classpath $(CLASSPATH) CreateArc.java

CreateArc.jar: CreateArc.class
	echo Main-Class: CreateArc> manifest.txt
	jar cmf manifest.txt CreateArc.jar CreateArc.class

run: CreateArc.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  CreateArc

clean:
	- rm CreateArc.prt

clean_all: clean
	- rm *.class 
