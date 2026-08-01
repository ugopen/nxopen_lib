/*
 *
 * Copyright (c) 2005 UGS Corp. 
 *     All Rights Reserved.
 *
 * 
 */
package nxexamples.createnote;

import nxexamples.utils.*;

import java.io.PrintStream;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;

import nxopen.*;

/*
 * The main class for this example
 */
public class CreateNoteExample implements Runnable
{
    public static int getUnloadOption() { return BaseSession.LibraryUnloadOption.EXPLICITLY; }
    
    public static void main(String[] args) throws Exception 
    {
        // On Windows, redirect stderr to somewhere that it can be seen.
        if ( System.getProperty("os.name").toLowerCase().startsWith("windows"))
        {
            PrintStream newerr = new PrintStream(new DialogOutputStream());
            System.setErr(newerr);
        }
        SwingUtilities.invokeLater( new CreateNoteExample() );
    }
    
    
    public void run() 
    {
        UserSymbolDialog d = null;
        try 
        {
            Session theSession =(Session)SessionFactory.get("Session");
            UI theUI = (UI)SessionFactory.get("UI");
            

            
            theSession.setUndoMark(Session.MarkVisibility.VISIBLE, "Create notes");
            d = new UserSymbolDialog(theSession, theUI);
            for(;;)
            {
                if ( d.showDialog() != JOptionPane.OK_OPTION )
                    break;
         
                // Get the note creation data that the user entered on the form
                UserSymbolDialog.NoteCreationData data = d.getNoteCreationData();
                if ( data == null )
                    continue;
                Part workPart = theSession.parts().work();
                Selection.DialogResponse response;
                // Create notes at the position specified by the user, until the user cancels
                for(;;)
                {
                    Selection.SelectScreenPositionData selectedPosition = 
                        theUI.selectionManager().selectScreenPosition("Select location for new note");
                    response = selectedPosition.response;
                    if ( response != Selection.DialogResponse.PICK )
                        break;
                    workPart.annotations().createNote(data.noteText, selectedPosition.screenPosition,
                            AxisOrientation.HORIZONTAL, data.letteringPrefs, data.userSymPrefs );
                }
                if ( response != Selection.DialogResponse.BACK )
                    break;
            }
        }
        catch (Exception e)
        {
            e.printStackTrace(System.err);
        }
        finally
        {
            d.doDispose();
        }
    }
    
}
