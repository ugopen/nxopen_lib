/*==================================================================================================

            Copyright (c) 2004 UGS PLM Solutions.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example to show how to create Arc thru 3 points.
 
*/

import nxopen.*;
import nxopen.uf.*;
import java.io.*;

public class DrfAskPreferences
{
    public static void main(String[] args) throws Exception 
    {
        Session theSession = null;
        UFSession theUFSession = null;
        try
        {
            String part_name = new String("DirPath");
            int units =2; 
            theSession = (Session)SessionFactory.get("Session");
            theUFSession = (UFSession)SessionFactory.get("UFSession");

            theSession.listingWindow().open();

            UFPart  ufPart = theUFSession.part();
            nxopen.Tag the_NewPartData= ufPart.newPart(part_name, units);
            String the_AskPartNameData =ufPart.askPartName(the_NewPartData);
            theSession.listingWindow().writeLine("Part file specification :    "+ the_AskPartNameData);

            nxopen.Tag ufPart_Display = ufPart.askDisplayPart(); 
            theSession.listingWindow().writeLine("\nDimension Creation method: 1 - Automatic Text;\n");
            theSession.listingWindow().writeLine("                           2 - Automatic Text, Appended Text;\n" );
            theSession.listingWindow().writeLine("                           3 - Manual Text;\n" );
            theSession.listingWindow().writeLine("                           4 - Manual Text, Appended Text.\n" );
            theSession.listingWindow().writeLine("Dimension Tag    Creation symbol\n\n" );
            
            UFObj  ufObj = theUFSession.obj();
            nxopen.Tag dimension_tag = nxopen.Tag.NULL;
            nxopen.Tag the_CycleObjsInPart = ufObj.cycleObjsInPart(ufPart_Display,UFConstants.UF_dimension_type,dimension_tag);
            
            UFDrf  ufDrf = theUFSession.drf();
            UFDrf.AskPreferencesData the_AskPreferences = ufDrf.askPreferences();

            for(int i=0;i <=99;i++)
            {
                theSession.listingWindow().writeLine("Mpi at Index "+i+":  " + the_AskPreferences.mpi[i] + "\n");
                if( i % 3 == 0)
                {
                    theSession.listingWindow().writeLine("\n");
                }
            }
            for(int i=0;i <=51;i++)
            {
                theSession.listingWindow().writeLine("Mpr at Index "+i+":  "+ the_AskPreferences.mpr[i] + "\n");
                if( i % 3 == 0)
                {
                    theSession.listingWindow().writeLine("\n");
                }
            }
            theSession.listingWindow().writeLine("DiameterSymbol:  " + the_AskPreferences.diameterValue + "\n");
            theSession.listingWindow().writeLine("RadiusSymbol :  " + the_AskPreferences.radiusValue);
            theSession.listingWindow().writeLine("\n");

            ufPart.save();
        }
        catch (Exception ex)
        {
            if(theUFSession!=null)
            {
                StringWriter s = new StringWriter();
                PrintWriter p = new PrintWriter(s);
                p.println("Caught exception " + ex );
                ex.printStackTrace(p);
                theSession.listingWindow().writeLine("\nFailed");
                theSession.listingWindow().writeLine("\n"+s.getBuffer().toString());
            }
        }
    }

     public static int getUnloadOption() { 
        return BaseSession.LibraryUnloadOption.IMMEDIATELY; 
    }
}
