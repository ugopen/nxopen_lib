//
//      Copyright (c) 2005 UGS Corp.
//         All rights reserved
//          Written by V.A.L.

import java.rmi.*;
import java.rmi.server.UnicastRemoteObject;

import nxopen.*;

/** Implements the NXRemoteServer interface */
public class NXRemoteServerImpl extends UnicastRemoteObject implements NXRemoteServer
{
    private String host;
    private String serverName;
    private Session theSession = null;
    private UFSession theUFSession = null;
    private boolean isShutdownAllowed;
    
    public NXRemoteServerImpl() throws RemoteException
    {
        super();
        host = System.getProperty("nxexamples.remoting.host");
        serverName = System.getProperty("nxexamples.remoting.servername");
        if ( host == null || host.equals(""))
            host = "localhost";
        if ( serverName == null )
            serverName = "NXServer";
        isShutdownAllowed = (System.getProperty("nxexamples.remoting.allowshutdown") != null);
    }
    
    /** Starts the server and binds it with the RMI registry */
    public void startServer() throws Exception
    {
        System.out.println("Starting");
        NXRemotableObject.RemotingProtocol remotingProtocol = NXRemotableObject.RemotingProtocol.create();
        theSession = (Session)SessionFactory.get("Session", remotingProtocol);
        theUFSession = (UFSession)SessionFactory.get("UFSession", remotingProtocol);
        System.out.println("Got Session");
        theSession.listingWindow().open();
        theSession.listingWindow().writeLine("Binding Session");
        Naming.rebind("//" + host + "/" + serverName, this);
        theSession.listingWindow().writeLine("Session bound");
        System.out.println("ready");
    }
    
    public Session session() throws RemoteException, NXException { return theSession; }
    
    public UFSession ufSession() throws RemoteException, NXException { return theUFSession; }
    
    public boolean isShutdownAllowed() throws RemoteException { return isShutdownAllowed; }
    
    private class ShutdownThread extends Thread
    {
        public void run()
        {
            try
            {
                Thread.sleep(250);                
            }
            catch (Exception e)
            {
                throw new RuntimeException(e);
            }
            finally
            {
                System.exit(0);
            }
        }
    }
    
    public void shutdown() throws RemoteException
    {
        if ( !isShutdownAllowed )
            throw new RemoteException("Shutdown not allowed");
        
        try
        {
            Naming.unbind("//" + host + "/" + serverName);
        }
        catch (Exception e)
        {
            throw new RemoteException("Exception during unbind", e);
        }
        finally
        {
            // We need to shut down the server after this method
            // has returned.  If we shut down before this method has
            // returned, the client will receive an exception.
            // So, we create a separate thread that will wait 
            // briefly and then shut down the server.
            (new ShutdownThread()).start();
        }
    }    
    
    public static void main(String[] args) throws Exception
    {
        NXRemoteServerImpl self = new NXRemoteServerImpl();
        self.startServer();
    }
}
