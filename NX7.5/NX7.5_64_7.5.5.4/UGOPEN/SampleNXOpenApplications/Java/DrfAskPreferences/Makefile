NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = ".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: DrfAskPreferences.jar

DrfAskPreferences.class:
	javac -classpath $(CLASSPATH) DrfAskPreferences.java

DrfAskPreferences.jar: DrfAskPreferences.class
	echo Main-Class: DrfAskPreferences> manifest.txt
	jar cmf manifest.txt DrfAskPreferences.jar DrfAskPreferences.class

run: DrfAskPreferences.class
	$(UGII_BASE_DIR)/ugopen/run_java -classpath $(CLASSPATH)  DrfAskPreferences

clean:
	- rm DirPath.prt

clean_all: clean
	- rm *.class
