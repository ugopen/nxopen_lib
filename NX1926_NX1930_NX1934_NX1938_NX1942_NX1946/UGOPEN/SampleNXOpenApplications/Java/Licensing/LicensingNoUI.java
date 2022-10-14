/*==================================================================================================

            Copyright 2010 Siemens Product Lifecycle Management Software Inc. All Rights Reserved.
                   Unpublished - All rights reserved

====================================================================================================
File description:
Example of java journal with no UI
 
*/

import nxopen.NXException;
import nxopen.Session;
import nxopen.SessionFactory;


public class LicensingNoUI  {

    public static void main(String args[]) 
    {
    
        Session session = null;
        
        try 
        {
            session = (Session) SessionFactory.get("Session");
            LicensingBase.doWork(session);
        } 
        catch (Exception ex) 
        {
            ex.printStackTrace();
        }

    }


}
