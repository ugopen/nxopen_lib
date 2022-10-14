NXOPENJARDIR = $(UGII_ROOT_DIR)
CLASSPATH = .:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenUF.jar
CLASSPATHRUN = .:$(NXOPENJARDIR)/NXOpen.jar:$(NXOPENJARDIR)/NXOpenRemote.jar:$(NXOPENJARDIR)/NXOpenUF.jar:$(NXOPENJARDIR)/NXOpenUFRemote.jar
RUN_JAVA = $(UGII_BASE_DIR)/ugopen/run_java

compile: NXClient.class NXRemoteServerImpl_Stub.class

NXClient.class:
	javac -classpath $(CLASSPATH) NXClient.java

NXRemoteServerImpl.class:
	javac -classpath $(CLASSPATH) NXRemoteServerImpl.java

NXRemoteServerImpl_Stub.class: NXRemoteServerImpl.class
	rmic -d . -classpath $(CLASSPATH) NXRemoteServerImpl

run_rmiregistry: NXRemoteServerImpl_Stub.class
	rmiregistry -J-Djava.class.path=$(CLASSPATHRUN) &

run_server: NXRemoteServerImpl_Stub.class
	$(RUN_JAVA)  -classpath $(CLASSPATHRUN) -Dnxexamples.remoting.allowshutdown NXRemoteServerImpl &

run_client: NXClient.class
	java -classpath $(CLASSPATHRUN) -Dnxexamples.remoting.rmilookuptimeout=500000 -Dnxexamples.remoting.host="$(HOST)" NXClient

run: clean run_rmiregistry run_server run_client

clean:
	- rm wwwz.prt CreateArcUsingRemoting.prt

clean_all: clean
	- rm *.class
