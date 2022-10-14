NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = ".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: CreateBSurface.jar

CreateBSurface.class:
	javac -classpath $(CLASSPATH) CreateBSurface.java

CreateBSurface.jar: CreateBSurface.class
	echo Main-Class: CreateBSurface> manifest.txt
	jar cmf manifest.txt CreateBSurface.jar CreateBSurface.class

run: CreateBSurface.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  CreateBSurface

clean:
	- rm CreateBSurface.prt

clean_all: clean
	- rm *.class
