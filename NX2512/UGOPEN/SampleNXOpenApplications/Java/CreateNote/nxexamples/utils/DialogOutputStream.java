package nxexamples.utils;

import java.awt.BorderLayout;
import javax.swing.*;

/*
 * This class is an OutputStream that writes the output to a scrollable text area
 * of a new dialog. 
 */
// TODO This class was created for debugging purposes to redirect System.err
// to this output stream.  If this class is used for non-debugging purposes, 
// some work should be done on this class to optimize its performance.
public class DialogOutputStream extends java.io.OutputStream
{
    private JTextArea textArea;
    
    public void write(int c)
    {
        if ( textArea == null )
            buildDialog();
        textArea.append("" + (char)c);
    }
    private void buildDialog()
    {
        JFrame frame = new JFrame("err");
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        textArea = new JTextArea(20, 80);
        JScrollPane pane = new JScrollPane(textArea);
        frame.getContentPane().add(pane, BorderLayout.CENTER);
        frame.pack();
        frame.setVisible(true);           
    }
}
