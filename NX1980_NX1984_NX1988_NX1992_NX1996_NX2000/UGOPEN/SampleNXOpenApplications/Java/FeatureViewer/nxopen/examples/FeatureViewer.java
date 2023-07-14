/*
 *
 * Copyright (c) 2005 UGS Corp. 
 *     All Rights Reserved.
 *
 * 
 */
package nxopen.examples;

import java.io.File;
import java.io.PrintWriter;
import java.io.StringWriter;
import java.net.URL;
import java.net.URLClassLoader;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;

import nxopen.*;

/**
 * @author pesumner
 * Creates a browser for viewing the features in the work part
 */
public class FeatureViewer {
    
    private static boolean useSystemLookAndFeel = true;
    
    private static Session theSession;
    
    private static Part getWorkPart() throws NXException, RemoteException {
        return theSession.parts().work();
    }
    
    /**
     * Create the GUI and show it.  For thread safety,
     * this method should be invoked from the
     * event-dispatching thread.
     */
    private static void createAndShowGUI() {
        
        try {
            if ( System.getProperty("remoteserver") == null ) {
                theSession = (Session)SessionFactory.get("Session");
            }
            else {
                theSession = (Session)Naming.lookup(System.getProperty("remoteserver"));
            }
            
            if (useSystemLookAndFeel) {
                try {
                    UIManager.setLookAndFeel(
                        UIManager.getSystemLookAndFeelClassName());
                } catch (Exception e) {
                    System.err.println("Couldn't use system look and feel.");
                }
            }
    
            //Make sure we have nice window decorations.
            JFrame.setDefaultLookAndFeelDecorated(true);
    
            //Create and set up the window.
            JFrame frame = new JFrame("Features Browser");
            frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
    
            //Create and set up the content pane.
            Part workPart = getWorkPart();
            if (workPart == null) {
                throw new Exception("No work part");
            }
            FeaturesBrowser contentPane = new FeaturesBrowser(getWorkPart());
            contentPane.setOpaque(true); //content panes must be opaque
            frame.setContentPane(contentPane);
            
            //Display the window.
            frame.pack();
            frame.setVisible(true);
        }
        catch (Exception e) {
            reportException(e);
        }
    }
    
    public static void reportException(Exception e) {
        StringWriter s = new StringWriter();
        PrintWriter p = new PrintWriter(s);
        p.println("Caught exception " + e );
        e.printStackTrace(p);
        JOptionPane.showMessageDialog(null, s.getBuffer().toString(), "Exception", JOptionPane.ERROR_MESSAGE);
    }   
    
    public static void main(String[] args) throws Exception{
        
        //Schedule a job for the event-dispatching thread:
        //creating and showing this application's GUI.
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                    createAndShowGUI();
                }
        });
    }
    
    public static int getUnloadOption() { 
        return BaseSession.LibraryUnloadOption.EXPLICITLY; 
    }

}
