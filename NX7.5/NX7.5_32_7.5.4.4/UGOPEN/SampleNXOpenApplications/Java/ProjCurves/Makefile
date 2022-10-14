NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = ".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: ProjCurves.jar

ProjCurves.class:
	javac -classpath $(CLASSPATH) ProjCurves.java

ProjCurves.jar: ProjCurves.class
	echo Main-Class: ProjCurves> manifest.txt
	jar cmf manifest.txt ProjCurves.jar ProjCurves.class

run: ProjCurves.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  ProjCurves

clean:
	- rm ProjCurves.prt

clean_all: clean
	- rm *.class
