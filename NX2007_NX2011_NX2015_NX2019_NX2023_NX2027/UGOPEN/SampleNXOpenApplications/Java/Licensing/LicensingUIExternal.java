/*==================================================================================================

            Copyright 2010 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example of java journal with UI to be called outside of NX
 
*/
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;
import nxopen.NXException;
import nxopen.Session;
import nxopen.SessionFactory;
import java.awt.*;
import java.awt.event.*;
import java.awt.font.*;

import javax.swing.*;




public class LicensingUIExternal extends javax.swing.JDialog {


    public LicensingUIExternal(java.awt.Frame parent, boolean modal, Session session) 
    {
        super(parent, modal);
        theSession = session;        
        initComponents();
    }


    private void initComponents() {

        jButton1 = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.DISPOSE_ON_CLOSE);
        
        setTitle("License Example");
        setAlwaysOnTop(true);

        jButton1.setText("Create Part");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jButton1, javax.swing.GroupLayout.DEFAULT_SIZE, 376, Short.MAX_VALUE)
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 124, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        java.awt.Dimension screenSize = java.awt.Toolkit.getDefaultToolkit().getScreenSize();
        setBounds((screenSize.width-408)/2, (screenSize.height-178)/2, 408, 178);
    }

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) 
    {
        try
        {
            LicensingBase.doWork(theSession);
        }
        catch(Exception e)
        {
            JOptionPane.showMessageDialog(this, "Exception on creating Part",
                    "Status", JOptionPane.INFORMATION_MESSAGE);
                    
            return;
        }
        
        JOptionPane.showMessageDialog(this, "Part Created",
                    "Status", JOptionPane.INFORMATION_MESSAGE);
    }

    public static void main(String args[]) 
    {
    
        Session session = null;
        
        try 
        {
            session = (Session) SessionFactory.get("Session");
        } 
        catch (NXException ex) 
        {
            ex.printStackTrace();
        }
        

        LicensingUIExternal dialog = new LicensingUIExternal(new javax.swing.JFrame(), true, session);
        dialog.addWindowListener(new java.awt.event.WindowAdapter() 
        {

            public void windowClosing(java.awt.event.WindowEvent e) {
                System.exit(0);
            }
        });


        dialog.setVisible(true);
    }

    private javax.swing.JButton jButton1;
    private Session theSession;

}
