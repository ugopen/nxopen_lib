NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = ".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: InterOP.jar

InterOP.class:
	javac -classpath $(CLASSPATH) InterOP.java

InterOP.jar: InterOP.class
	echo Main-Class: InterOP> manifest.txt
	jar cmf manifest.txt InterOP.jar InterOP.class

run: InterOP.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  InterOP

clean:
	- rm RenamedArc.prt

clean_all: clean
	- rm *.class
