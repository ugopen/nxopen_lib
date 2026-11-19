NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = ".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: ModlCreate.jar

ModlCreate.class:
	javac -classpath $(CLASSPATH) ModlCreate.java

ModlCreate.jar: ModlCreate.class
	echo Main-Class: ModlCreate> manifest.txt
	jar cmf manifest.txt ModlCreate.jar ModlCreate.class

run: ModlCreate.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  ModlCreate

clean:
	- rm RenamedArc.prt

clean_all: clean
	- rm *.class
