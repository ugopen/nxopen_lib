/*
 *
 * Copyright (c) 2005 UGS Corp. 
 *     All Rights Reserved.
 *
 * 
 */

package nxopen.examples; 

import java.awt.Dimension;
import java.awt.GridLayout;
import java.rmi.RemoteException;
import java.util.Iterator;

import javax.swing.JEditorPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSplitPane;
import javax.swing.JTree;
import javax.swing.event.TreeSelectionEvent;
import javax.swing.event.TreeSelectionListener;
import javax.swing.tree.DefaultMutableTreeNode;
import javax.swing.tree.TreeSelectionModel;

import nxopen.*;
import nxopen.features.Feature;
import nxopen.features.FeatureCollection;

/**
 * @author pesumner
 *
 */
public class FeaturesBrowser extends JPanel 
                            implements TreeSelectionListener {
    
    private JEditorPane htmlPane;
    private JTree tree; 
    private Part part;
    
    private class FeatureInfo {
        
        public String featureName = "";
        public nxopen.features.Feature feature;
        
        public FeatureInfo(nxopen.features.Feature feature) throws NXException, RemoteException{
            this.feature = feature;
            featureName = feature.journalIdentifier();
        }
        
        public String toString() {
            return featureName;
        }
    }
    
    public FeaturesBrowser(Part part) throws Exception {
        super(new GridLayout(1,0));
        
        this.part = part;
        String name = "";
        name = part.name();

        //Create the nodes.
        DefaultMutableTreeNode top =
            new DefaultMutableTreeNode(name);
        createNodes(top);

        //Create a tree that allows one selection at a time.
        tree = new JTree(top);
        tree.getSelectionModel().setSelectionMode
                (TreeSelectionModel.SINGLE_TREE_SELECTION);

        //Listen for when the selection changes.
        tree.addTreeSelectionListener(this);

        //Create the scroll pane and add the tree to it. 
        JScrollPane treeView = new JScrollPane(tree);

        //Create the HTML viewing pane.
        htmlPane = new JEditorPane();
        htmlPane.setEditable(false);
        //initHelp();
        JScrollPane htmlView = new JScrollPane(htmlPane);

        //Add the scroll panes to a split pane.
        JSplitPane splitPane = new JSplitPane(JSplitPane.VERTICAL_SPLIT);
        splitPane.setTopComponent(treeView);
        splitPane.setBottomComponent(htmlView);

        Dimension minimumSize = new Dimension(100, 50);
        htmlView.setMinimumSize(minimumSize);
        treeView.setMinimumSize(minimumSize);
        splitPane.setDividerLocation(100); //XXX: ignored in some releases
                                           //of Swing. bug 4101306
        //workaround for bug 4101306:
        //treeView.setPreferredSize(new Dimension(100, 100)); 

        splitPane.setPreferredSize(new Dimension(500, 300));

        //Add the split pane to this panel.
        add(splitPane);
    }

    private void createNodes(DefaultMutableTreeNode top) throws Exception {
        DefaultMutableTreeNode category = null;
        DefaultMutableTreeNode featureNode = null;

        category = new DefaultMutableTreeNode("Features");
        top.add(category);
        
        FeatureCollection features = part.features();
        
        for (Iterator i = features.iterator(); i.hasNext();) {

            //Feature on Part
            Feature feature = (Feature)i.next();
            featureNode = new DefaultMutableTreeNode(new FeatureInfo(feature));
            category.add(featureNode);
        }
    }
    
    private void displayDetails(FeatureInfo featureInfo) throws Exception {
         if (featureInfo != null) {
            StringBuffer details = new StringBuffer();
            details.append("Parents:\n");
            Feature [] relatives = featureInfo.feature.getParents();
            for ( int i=0; i < relatives.length; ++i )
                details.append("   " + relatives[i].journalIdentifier() + "\n");
            details.append("Children:\n");
            relatives = featureInfo.feature.getChildren();
            for ( int i=0; i < relatives.length; ++i )
                details.append("   " + relatives[i].journalIdentifier() + "\n");
            Expression [] expressions = featureInfo.feature.getExpressions();
            details.append("Expressions:\n");
            for (int i=0; i < expressions.length; ++i )
                details.append("   " + expressions[i].equation() + "\n");
           
            htmlPane.setText(details.toString());
        } else { //null feature
            htmlPane.setText("Non feature node selected.");
        }
    }


    /** Required by TreeSelectionListener interface. */
    public void valueChanged(TreeSelectionEvent e) {
        DefaultMutableTreeNode node = (DefaultMutableTreeNode)
                           tree.getLastSelectedPathComponent();

        if (node == null) return;

        Object nodeInfo = node.getUserObject();
        try {
            if (node.isLeaf() && nodeInfo.getClass() != String.class ) {
                FeatureInfo feature = (FeatureInfo)nodeInfo;
                displayDetails(feature);
            } else {
                displayDetails(null); 
            }
        }
        catch (Exception ex) {
            FeatureViewer.reportException(ex);
        }
    }


}
