NXOPENJARDIR=$(UGII_ROOT_DIR)
CLASSPATH=".:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar"

compile: JavaApp.jar

JavaApp.class:
	javac -classpath $(CLASSPATH) JavaApp.java
	
JavaApp.h:
	javah -classpath $(CLASSPATH) -jni JavaApp


JavaApp.jar: JavaApp.class JavaApp.h
	echo Main-Class: JavaApp> manifest.txt
	jar cmf manifest.txt JavaApp.jar JavaApp.class


