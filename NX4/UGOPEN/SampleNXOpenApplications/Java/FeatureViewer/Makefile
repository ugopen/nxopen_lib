NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = .:$(NXOPENJARDIR)/NXOpen.jar:

compile: FeatureViewer.jar

nxopen/examples/FeatureViewer.class: nxopen/examples/FeatureViewer.java
	javac -classpath $(CLASSPATH) nxopen/examples/FeatureViewer.java

FeatureViewer.jar: nxopen/examples/FeatureViewer.class
	echo "Main-Class: nxopen.examples.FeatureViewer"> manifest.txt
	jar cmf manifest.txt FeatureViewer.jar nxopen
