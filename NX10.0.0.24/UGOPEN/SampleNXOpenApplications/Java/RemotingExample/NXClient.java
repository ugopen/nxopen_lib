//
//      Copyright (c) 2005 UGS Corp.
//         All rights reserved
//          Written by V.A.L.

import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.ConnectException;

import nxopen.*;
import nxopen.uf.*;

/** Sample NX client program.  It binds to a remote server,
 * create some geometry, queries the geometry, saves the part, and
 * shuts down the server. */
class NXClient
{
    /** Looks up the server in the RMI registry */
    private static NXRemoteServer lookupServer() throws Exception
    {
        NXRemoteServer server = null;
        String host = System.getProperty("nxexamples.remoting.host");
        if ( host == null || host.equals(""))
            host = "localhost";
        String serverName = System.getProperty("nxexamples.remoting.servername");        
        if ( serverName == null )
            serverName = "NXServer";
        int bindTimeout = 0;
        if ( System.getProperty("nxexamples.remoting.rmilookuptimeout") != null)
            bindTimeout = Integer.parseInt(System.getProperty("nxexamples.remoting.rmilookuptimeout"));

        String name = "//" + host + "/" + serverName;
        System.out.println("Looking up name of server");
        int time = 0;
        // Look up the server.  Keep trying until it is found or
        // the amount of time we have tried exceeds the amount specified
        // in the property nxexamples.remoting.rmilookuptimeout
        do
        {   
            try
            {
                server = (NXRemoteServer)Naming.lookup(name);
            }
            catch ( NotBoundException e )
            {
                time += 1000;
                if ( time > bindTimeout )
                    throw e;
                Thread.sleep(1000);
            }
            catch ( ConnectException e )
            {
                time += 1000;
                if ( time > bindTimeout )
                    throw e;
                Thread.sleep(1000);
            }

        }
        while(server == null);
        System.out.println("Name of server found");
        return server;        
    }
    
    public static void main(String [] args) throws Exception
    {
        NXRemoteServer server = lookupServer();
        try
        {
            Session theSession = server.session();        
            
            int markId1;
            markId1 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Create Part");
            Part part1 = theSession.parts().newDisplay("wwwz", Part.Units.INCHES);
            Line line1;
            Line line2;
            line1 = part1.curves().createLine(
                new Point3d(-4.0, 2.0, 0.0), 
                new Point3d(4.5, 2.0, 0.0));
            line2 = part1.curves().createLine(
                new Point3d(4.5, 2.0, 0.0),
                new Point3d(4.5, -1.0, 0.0) );
            Point3d startPt = line1.startPoint();
            Point3d endPt = line1.endPoint();
            System.out.println("Line1 startPt = " + startPt.x + " " + startPt.y + " " + startPt.z);
            System.out.println("Line1 endPt = " + endPt.x + " " + endPt.y + " " + endPt.z);
            Point3d pt1 = new Point3d(1, 0, 0);
            Point3d pt2 = new Point3d (.7, .7, 0);
            Point3d pt3 = new Point3d(0, 1, 0);
            Arc arc1 = part1.curves().createArc( pt3, pt2, pt1, false);
            System.out.println("Created arc with radius " + arc1.radius());
                
            int nErrs1;
            nErrs1 = theSession.updateManager().doUpdate(markId1);

            PartSaveStatus partSaveStatus1;
            partSaveStatus1 = part1.save(nxopen.BasePart.SaveComponents.TRUE, nxopen.BasePart.CloseAfterSave.FALSE);
            
            partSaveStatus1.dispose();
            partSaveStatus1 = null;


 
            // Demonstrate Java UF calls

            UFSession theUFSession = server.ufSession();
            UFCurve ufCurve = theUFSession.curve();
            UFCurve.Arc ufArc = new UFCurve.Arc();
            UFPart ufPart = theUFSession.part();
            UFCsys ufCsys = theUFSession.csys();
            part1 = theSession.parts().newDisplay("CreateArcUsingRemoting", Part.Units.INCHES);

            /* Fill out the data structure */
            ufArc.startAngle = 0.0;
            ufArc.endAngle = 3.0;
            ufArc.arcCenter = new double[] {0.0, 0.0, 1.0};
            ufArc.radius = 2.0;

            // Get the WCS and fill in data structure
            Tag wcs = ufCsys.askWcs();
            ufArc.matrixTag =  ufCsys.askMatrixOfObject(wcs);

            Tag arcTag = ufCurve.createArc(ufArc);
            UFCurve.Arc arcData =  ufCurve.askArcData(arcTag);
            System.out.println("Created arc using UF");
            System.out.println("X Coordinate: " + arcData.arcCenter[0]);
            System.out.println("Y Coordinate: " + arcData.arcCenter[1]);
            System.out.println("Z Coordinate: " + arcData.arcCenter[2]);
            System.out.println("Start Angle: " + arcData.startAngle);
            System.out.println("End Angle: " + arcData.endAngle);
            System.out.println("Radius: " + arcData.radius);
    
            theUFSession.modeling().update();
    
            ufPart.save();
        }
        finally
        {
            if ( server.isShutdownAllowed() )
                server.shutdown();
        }
    }
}
