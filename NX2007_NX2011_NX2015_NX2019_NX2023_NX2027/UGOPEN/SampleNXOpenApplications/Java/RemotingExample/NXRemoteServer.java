//
//      Copyright (c) 2005 UGS Corp.
//         All rights reserved
//          Written by V.A.L.

import java.rmi.Remote;
import java.rmi.RemoteException;
import nxopen.*;

/** Remote interface to a server object.  The server object has
 * methods for obtaining an NX session and for shutting down the server */
public interface NXRemoteServer extends Remote
{
    /** Returns a NX Session object */
    Session session() throws RemoteException, NXException;
    
    /** Returns a UF Session object */
    UFSession ufSession() throws RemoteException, NXException;

    /** Returns true if remote clients have permission to shut down
     * the server */
    boolean isShutdownAllowed() throws RemoteException;
    
    /** Shuts down the server.  Warning: this method does not
     * save the server's state before shutting down.  Any unsaved changes
     * to any parts cannot be restored.
     * @throws A RemoteException if remote clients do not have permission
     * to shut down the server.  Use isShutdownAllowed to test for permission
     */
    void shutdown() throws RemoteException;
    
}
