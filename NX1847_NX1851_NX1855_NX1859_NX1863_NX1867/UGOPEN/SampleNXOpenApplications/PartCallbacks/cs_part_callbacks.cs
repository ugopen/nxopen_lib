//----------------------------------------------------------------------------
//                  Copyright (c) 2007 UGS Corp.
//                      All rights reserved
//----------------------------------------------------------------------------
//  
//
// cs_part_callbacks.cs
//
// Description:
//     This simple demo registers part callbacks for every available reason
//     via the C Sharp language.
//
//     Note you must add a reference to the following .Net component when
//     compiling in Visual Studio: System.Windows.Forms
//
//     After compiling and linking this demo program, the output library needs
//     to be placed in a folder called startup (for example c:\user_dir\startup).
//     Also the UGII_USER_DIR enviornment variable needs to point to the startup
//     directory's parent folder (for example: UGII_USER_DIR=c:\user_dir).
//     Once you have the startup directory and user dir environment variable
//     set up, start NX.  The part callbacks will be registered at startup.
//     Now anytime you create new, open, save, save as, close, modify, rename,
//     or change the workpart your callbacks will be executed.
//
//     To demo all of the available part callbacks at runtime - compile and link
//     execute_all_part_callbacks.c.
//     Then start NX and go to File->Execute->NX Open and select your compiled
//     execute_all_callbacks program.
//
//---------------------------------------------------------------------------/


using NXOpen;
using NXOpen.Utilities;
using NXOpenUI;
using System.Windows.Forms;

namespace MyProject
{

    // <summary>
    //   MyClass is used to demo registration of part related callbacks
    // </summary>
    //
    public class MyClass
    {

        //-----------------------------------------------------
        // Used to tell us if we've already registered our callbacks
        //-----------------------------------------------------
        static int registered = 0;

        //-----------------------------------------------------
        // The ids of the registered callbacks are used if
        // you ever want to unregister a callback.
        // If you plan to register the callback once for
        // the enitre session, and don't intend to remove them ,
        // (recommended) tracking the id may not be necessary.
        //-----------------------------------------------------
        static int idPartCreated1 = 0;
        static int idPartOpened1 = 0;
        static int idPartSaved1 = 0;
        static int idPartSavedAs1 = 0;
        static int idPartClosed1 = 0;
        static int idPartModified1 = 0;
        static int idPartRenamed1 = 0;
        static int idWorkPartChanged1 = 0;
        static Session theSession = null;
        static ListingWindow lw = null;


        //-----------------------------------------------------
        // Called when a new part is created
        // Prints the name of the created part to the listing window
        //-----------------------------------------------------
        public static void PartCreated1(BasePart p)
        {
            lw.Open();
            lw.WriteLine("    CS created: " + p.FullPath);
        }

        //-----------------------------------------------------
        // Called when a part is opened
        // Prints the name of the opened part to the listing window
        //-----------------------------------------------------
        public static void PartOpened1(BasePart p)
        {
            lw.Open();
            lw.WriteLine("    CS opened: " + p.FullPath);
        }

        //-----------------------------------------------------
        // Called when a part is saved
        // Prints the name of the saved part to the listing window
        //-----------------------------------------------------
        public static void PartSaved1(BasePart p)
        {
            lw.Open();
            lw.WriteLine("    CS saved: " + p.FullPath);
        }

        //-----------------------------------------------------
        // Called when a part is saved as
        // Prints the name of the saved as part to the listing window
        //-----------------------------------------------------
        public static void PartSavedAs1(BasePart p)
        {
            lw.Open();
            lw.WriteLine("    CS saved as: " + p.FullPath);
        }

        //-----------------------------------------------------
        // Called when a part is closed
        // Prints the name of the closed part to the listing window
        //-----------------------------------------------------
        public static void PartClosed1(BasePart p)
        {
            lw.Open();
            lw.WriteLine("    CS closed: " + p.FullPath);
        }

        //-----------------------------------------------------
        // Called when a part is modified for the first time
        // Prints the name of the modified part to the listing window
        //-----------------------------------------------------
        public static void PartModified1(BasePart p)
        {
            lw.Open();
            lw.WriteLine("    CS modified: " + p.FullPath);
        }

        //-----------------------------------------------------
        // Called when a part is renamed
        // Prints the name of the renamed part to the listing window
        //-----------------------------------------------------
        public static void PartRenamed1(BasePart p)
        {
            lw.Open();
            lw.WriteLine("    CS renamed: " + p.FullPath);
        }

        //-----------------------------------------------------
        // Called when the workpart changes
        // Prints the name of old workpart and new workpart to the listing window
        //-----------------------------------------------------
        public static void WorkPartChanged1(BasePart p)
        {
            lw.Open();
            lw.WriteLine("    CS work part changed");
            if (p == null)
            {
                lw.WriteLine("        Old Work Part: NULL");
            }
            else
            {
                lw.WriteLine("        Old Work Part: " + p.FullPath);
            }
            if (theSession.Parts.Work == null)
            {
                lw.WriteLine("        New Work Part: NULL");
            }
            else
            {
                lw.WriteLine("        New Work Part: " + theSession.Parts.Work.FullPath);
            }

        }


        //-----------------------------------------------------
        // Called when NX starts up
        // registers the part callbacks with NX
        //-----------------------------------------------------
        public static int Startup()
        {
            if( theSession == null )
            {
                theSession = Session.GetSession();
            }
            if( lw == null )
            {
                lw = theSession.ListingWindow;
            }
            if (registered == 0)
            {
                idPartCreated1 = theSession.Parts.AddPartCreatedHandler(new NXOpen.PartCollection.PartCreatedHandler(MyClass.PartCreated1));
                idPartOpened1 = theSession.Parts.AddPartOpenedHandler(new NXOpen.PartCollection.PartOpenedHandler(MyClass.PartOpened1));
                idPartSaved1 = theSession.Parts.AddPartSavedHandler(new NXOpen.PartCollection.PartSavedHandler(MyClass.PartSaved1));
                idPartSavedAs1 = theSession.Parts.AddPartSavedAsHandler(new NXOpen.PartCollection.PartSavedAsHandler(MyClass.PartSavedAs1));
                idPartClosed1 = theSession.Parts.AddPartClosedHandler(new NXOpen.PartCollection.PartClosedHandler(MyClass.PartClosed1));
                idPartModified1 = theSession.Parts.AddPartModifiedHandler(new NXOpen.PartCollection.PartModifiedHandler(MyClass.PartModified1));
                idPartRenamed1 = theSession.Parts.AddPartRenamedHandler(new NXOpen.PartCollection.PartRenamedHandler(MyClass.PartRenamed1));
                idWorkPartChanged1 = theSession.Parts.AddWorkPartChangedHandler(new NXOpen.PartCollection.WorkPartChangedHandler(MyClass.WorkPartChanged1));
                registered = 1;
            }
            return 0;
        }

        //-----------------------------------------------------
        //  Main()
        //    Called manually from File->Execute->NX Open
        //-----------------------------------------------------
        public static void Main()
        {
            //
            // TODO: Add application code here
            //
            if( theSession == null )
            {
                theSession = Session.GetSession();
            }
            if( lw == null )
            {
                lw = theSession.ListingWindow;
            }
            if (registered == 0)
            {
                System.Windows.Forms.MessageBox.Show( "Registering CS callbacks" );
                Startup();
                registered = 1;
            }
           

        }

        //-----------------------------------------------------
        //  GetUnloadOption()
        //
        //    Used to tell NX when to unload this library
        //
        //    Available options include: 
        //       Session.LibraryUnloadOption.Immediately
        //       Session.LibraryUnloadOption.Explicitly
        //       Session.LibraryUnloadOption.AtTermination
        //
        //    Any programs that register callbacks must use 
        //    AtTermination as the unload option.
        //-----------------------------------------------------
        public static int GetUnloadOption(string dummy)
        {
            return (int)Session.LibraryUnloadOption.AtTermination;
        }

    }

}
