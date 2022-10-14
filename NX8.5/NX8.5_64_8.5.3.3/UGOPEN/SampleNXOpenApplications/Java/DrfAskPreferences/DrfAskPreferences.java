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

            theUFSession.ui().openListingWindow();

            UFPart  ufPart = theUFSession.part();
            Tag the_NewPartData= ufPart.newPart(part_name, units);
            String the_AskPartNameData =ufPart.askPartName(the_NewPartData);
            theUFSession.ui().writeListingWindow("Part file specification :    "+ the_AskPartNameData);

            Tag ufPart_Display = ufPart.askDisplayPart(); 
            theUFSession.ui().writeListingWindow("\nDimension Creation method: 1 - Automatic Text;\n");
            theUFSession.ui().writeListingWindow("                           2 - Automatic Text, Appended Text;\n" );
            theUFSession.ui().writeListingWindow("                           3 - Manual Text;\n" );
            theUFSession.ui().writeListingWindow("                           4 - Manual Text, Appended Text.\n" );
            theUFSession.ui().writeListingWindow("Dimension Tag    Creation symbol\n\n" );
            
            UFObj  ufObj = theUFSession.obj();
            nxopen.Tag dimension_tag = Tag.NULL;
            Tag the_CycleObjsInPart = ufObj.cycleObjsInPart(ufPart_Display,UFConstants.UF_dimension_type,dimension_tag);
            
            UFDrf  ufDrf = theUFSession.drf();
            UFDrf.AskPreferencesData the_AskPreferences = ufDrf.askPreferences();

            for(int i=0;i <=99;i++)
            {
                theUFSession.ui().writeListingWindow("Mpi at Index "+i+":  " + the_AskPreferences.mpi[i] + "\n");
                if( i % 3 == 0)
                {
                    theUFSession.ui().writeListingWindow("\n");
                }
            }
            for(int i=0;i <=51;i++)
            {
                theUFSession.ui().writeListingWindow("Mpr at Index "+i+":  "+ the_AskPreferences.mpr[i] + "\n");
                if( i % 3 == 0)
                {
                    theUFSession.ui().writeListingWindow("\n");
                }
            }
            theUFSession.ui().writeListingWindow("DiameterSymbol:  " + the_AskPreferences.diameterValue + "\n");
            theUFSession.ui().writeListingWindow("RadiusSymbol :  " + the_AskPreferences.radiusValue);
            theUFSession.ui().writeListingWindow("\n");

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
				theUFSession.ui().writeListingWindow("\nFailed");
				//theUFSession.ui().writeListingWindow("\n"+ex.getMessage());
				theUFSession.ui().writeListingWindow("\n"+s.getBuffer().toString());
			}
        }
    }

     public static int getUnloadOption() { 
        return BaseSession.LibraryUnloadOption.IMMEDIATELY; 
    }
}
