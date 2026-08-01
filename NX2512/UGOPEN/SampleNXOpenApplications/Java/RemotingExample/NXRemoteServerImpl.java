/*=============================================================================

                    Copyright (c) 2012 Siemens PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: Sample NX/Open Application
===============================================================================

=============================================================================
*/

import java.rmi.*;
import java.rmi.server.UnicastRemoteObject;

import nxopen.*;

/** Implements the NXRemoteServer interface */
public class NXRemoteServerImpl extends UnicastRemoteObject implements NXRemoteServer
{
    private static String host;
    private static String serverName;
    private static Session theSession = null;
    private static UFSession theUFSession = null;
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
                //If the server is run inside of NX, executing exit
                // will cause NX to shut down as well
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

    public static int getUnloadOption() 
    {
        return  BaseSession.LibraryUnloadOption.EXPLICITLY;
    }

    public static void onUnload() 
    {

        try
        {
            theSession.listingWindow().open();
            theSession.listingWindow().writeLine("UnBinding Session");
            try
            {
                Naming.unbind("//" + host + "/" + serverName);
                theSession.listingWindow().writeLine("Session unbound");
            }
            catch (Exception e)
            {
                theSession.listingWindow().writeLine("Exception during unbind: "+ e.toString());
                throw e;
            }
            
        }
        catch(Exception e)
        {
            try
            {
               theSession.listingWindow().writeLine("Exception during onUnload: "+ e.toString());
            }
            catch (Exception ex) 
            {
               //Unfortunately, if we get an exception here we cannot report it
            }
        }
    }
       



}
