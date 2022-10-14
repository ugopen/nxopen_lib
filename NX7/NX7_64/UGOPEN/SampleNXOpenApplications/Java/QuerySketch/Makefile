NXOPENJARDIR = $(UGII_ROOT_DIR)
RUN_JAVA=$(UGII_BASE_DIR)/ugopen/run_java
CLASSPATH = .:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUI.jar:$(NXOPENJARDIR)/NXOpenUF.jar

SketchQueryExample.class:
	javac -classpath $(CLASSPATH) SketchQueryExample.java

run: SketchQueryExample.class
	$(RUN_JAVA) -classpath $(CLASSPATH) SketchQueryExample -b

