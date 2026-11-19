NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = ".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: CreateExtruded.jar

CreateExtruded.class:
	javac -classpath $(CLASSPATH) CreateExtruded.java

CreateExtruded.jar: CreateExtruded.class
	echo Main-Class: CreateExtruded> manifest.txt
	jar cmf manifest.txt CreateExtruded.jar CreateExtruded.class

run: CreateExtruded.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  CreateExtruded

clean:
	- rm CreateExtruded.prt

clean_all: clean
	- rm *.class
