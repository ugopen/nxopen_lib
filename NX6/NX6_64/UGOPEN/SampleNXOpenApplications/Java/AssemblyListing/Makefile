NXOPENJARDIR = $(UGII_ROOT_DIR)
RUN_JAVA=$(UGII_BASE_DIR)/ugopen/run_java
CLASSPATH = .:$(NXOPENJARDIR)/NXOpen.jar:

compile: AssemblyListing.jar

nxopen/examples/assemblies/AssemblyListing.class:
	javac -classpath $(CLASSPATH) nxopen/examples/assemblies/AssemblyListing.java

AssemblyListing.jar: nxopen/examples/assemblies/AssemblyListing.class
	echo "Main-Class: nxopen.examples.assemblies.AssemblyListing"> manifest.txt
	jar cmf manifest.txt AssemblyListing.jar nxopen utils

run: compile
	$(RUN_JAVA) -classpath $(CLASSPATH):AssemblyListing.jar nxopen.examples.assemblies.AssemblyListing -p ../parts/toycar_assy.prt

