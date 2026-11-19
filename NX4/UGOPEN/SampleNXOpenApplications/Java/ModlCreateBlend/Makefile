NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = ".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: ModlCreateBlend.jar

ModlCreateBlend.class:
	javac -classpath $(CLASSPATH) ModlCreateBlend.java

ModlCreateBlend.jar: ModlCreateBlend.class
	echo Main-Class: ModlCreateBlend> manifest.txt
	jar cmf manifest.txt ModlCreateBlend.jar ModlCreateBlend.class

run: ModlCreateBlend.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  ModlCreateBlend

clean:
	- rm ModlCreateBlend.prt

clean_all: clean
	- rm *.class
