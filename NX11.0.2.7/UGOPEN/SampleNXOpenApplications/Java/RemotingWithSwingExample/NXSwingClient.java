/*=============================================================================

                    Copyright (c) 2014 Siemens PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: Remoting Example with Java Swing
===============================================================================

=============================================================================
*/

import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.ConnectException;

import nxopen.*;
import nxopen.uf.*;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.*;
import javax.swing.JTextArea;
import javax.swing.JButton;
import javax.swing.JOptionPane;

import java.awt.*;
import java.awt.event.*;

public class NXSwingClient extends JFrame implements ActionListener {
    
    public static NXRemoteServer server;
    public static Session theSession;
    public static UFSession theUFSession;
    public static boolean isExecutionCompleted = false;
    private JPanel contentPane;
    private JTextArea textAreaExample;
    private JButton executeButton;
    
    /**
     * Launch the application.
     */
    public static void main(String[] args) {
        EventQueue.invokeLater(new Runnable() {
            public void run() {
                try {
                    NXSwingClient frame = new NXSwingClient();
                    frame.setVisible(true);
                    frame.reportServer();
                }
                catch (Exception e) {
                    JOptionPane.showMessageDialog(null, "Exception occured!", "RemotingWithSwingExample",JOptionPane.ERROR_MESSAGE);
                }
            }
        });
    }

    /**
     * Create the frame.
    */
    public NXSwingClient() {
        /**
         * Create the Window and setup dimensions, border, and layout styling
         */
        setDefaultCloseOperation(exitWindow());
        setBounds(100, 100, 450, 300);
        contentPane = new JPanel();
        contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
        contentPane.setLayout(new BorderLayout(0, 0));
        setContentPane(contentPane);
        
        /**
         * Create TextArea and align it to center
         */
        textAreaExample = new JTextArea();
        textAreaExample.setText("Swing Example");
        contentPane.add(textAreaExample, BorderLayout.CENTER);
        
        /**
         * Create Button and align to bottom of frame
         */
        executeButton = new JButton("Execute");
        contentPane.add(executeButton, BorderLayout.SOUTH);
        /**
         * Creates a listener for the button, will execute actionPerformed when pressed
         */
        executeButton.addActionListener(this);
    }
    
    /**
     * actionPerformed listens for the executeButton to be clicked and will then 
     * perform the work within the function
     */
    public void actionPerformed(ActionEvent arg0) 
    {
        try
        {
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
            textAreaExample.append("Line1 startPt = " + startPt.x + " " + startPt.y + " " + startPt.z);
            textAreaExample.append("Line1 endPt = " + endPt.x + " " + endPt.y + " " + endPt.z);
            Point3d pt1 = new Point3d(1, 0, 0);
            Point3d pt2 = new Point3d (.7, .7, 0);
            Point3d pt3 = new Point3d(0, 1, 0);
            Arc arc1 = part1.curves().createArc( pt3, pt2, pt1, false);
            textAreaExample.append("Created arc with radius " + arc1.radius()+"\n");
                
            int nErrs1;
            nErrs1 = theSession.updateManager().doUpdate(markId1);

            PartSaveStatus partSaveStatus1;
            partSaveStatus1 = part1.save(nxopen.BasePart.SaveComponents.TRUE, nxopen.BasePart.CloseAfterSave.FALSE);
            
            partSaveStatus1.dispose();
            partSaveStatus1 = null;

            /**
             * Demonstrate Java UF calls
            */

            UFCurve ufCurve = theUFSession.curve();
            UFCurve.Arc ufArc = new UFCurve.Arc();
            UFPart ufPart = theUFSession.part();
            UFCsys ufCsys = theUFSession.csys();
            part1 = theSession.parts().newDisplay("CreateArcUsingRemoting", Part.Units.INCHES);

            /** 
             * Fill out the data structure 
            */
            ufArc.startAngle = 0.0;
            ufArc.endAngle = 3.0;
            ufArc.arcCenter = new double[] {0.0, 0.0, 1.0};
            ufArc.radius = 2.0;

            /**
             * Get the WCS and fill in data structure
            */
            Tag wcs = ufCsys.askWcs();
            ufArc.matrixTag =  ufCsys.askMatrixOfObject(wcs);

            Tag arcTag = ufCurve.createArc(ufArc);
            UFCurve.Arc arcData =  ufCurve.askArcData(arcTag);
            textAreaExample.append("Created arc using UF"+"\n");
            textAreaExample.append("X Coordinate: " + arcData.arcCenter[0]+"\n");
            textAreaExample.append("Y Coordinate: " + arcData.arcCenter[1]+"\n");
            textAreaExample.append("Z Coordinate: " + arcData.arcCenter[2]+"\n");
            textAreaExample.append("Start Angle: " + arcData.startAngle+"\n");
            textAreaExample.append("End Angle: " + arcData.endAngle+"\n");
            textAreaExample.append("Radius: " + arcData.radius+"\n");

            theUFSession.modeling().update();
        }
        catch(Exception e)
        {
            JOptionPane.showMessageDialog(null, "Exception occured!", "RemotingWithSwingExample",JOptionPane.ERROR_MESSAGE);
        }
        isExecutionCompleted = true;
    }
    
    /**
     * Close connection to server if connection is open and close window
     */
    public int exitWindow() 
    {

        try
        {
            if( server.isShutdownAllowed() )
            {
                textAreaExample.append("Disconnecting from server\n");
                server.shutdown();
            }
        }
        catch (Exception e)
        {
            JOptionPane.showMessageDialog(null, "Exception occured!", "RemotingWithSwingExample",JOptionPane.ERROR_MESSAGE);
        }
        return JFrame.EXIT_ON_CLOSE;
    }
    

        /** Looks up the server in the RMI registry */
    private NXRemoteServer lookupServer() throws Exception
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
        textAreaExample.append("Looking up name of server\n");
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
        textAreaExample.append("Name of server found\n");
        return server;        
    }


    /** 
    * Looks up the server in the RMI registry 
    **/
    public void reportServer() throws Exception
    {
        server = lookupServer();
        textAreaExample.append("Connecting to server\n");
        theSession = server.session();        
        theUFSession = server.ufSession();
        textAreaExample.append("Obtained servers\n");
    }
}
