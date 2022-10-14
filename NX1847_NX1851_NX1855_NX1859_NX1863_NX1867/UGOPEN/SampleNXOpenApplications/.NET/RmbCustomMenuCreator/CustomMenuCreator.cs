//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Block Styler
//=============================================================================
//

using System;
using System.Collections.Generic;
using System.Text;
using NXOpen;
using NXOpen.UF;



namespace rmbopen
{
    public class CustomMenuCreator
    {
        //class members
        public static Session m_Session = null;
        public static UI m_UI = null;
        private UFUgmgr m_ugMgr = null;
        static CustomMenuCreator m_Instance = null;
        static CustomPopupMenuHandler m_MenuHandler;
        public static NXOpen.UF.UFSession m_ufSession = null;


        /**
        *  Constructor
        */
        private CustomMenuCreator()
        {
            m_MenuHandler = null;
            m_ufSession = NXOpen.UF.UFSession.GetUFSession();
            m_ugMgr = m_ufSession.Ugmgr;
        }

        /**
        *   Returns a single instance of the singleton class
        *
        *   @return CustomMenuCreator
        */
        static CustomMenuCreator GetInstance()
        {
            if (m_Instance == null)
            {
                m_Instance = new CustomMenuCreator();
            }
            return m_Instance;
        }

        /**
        *   Registers the callback methods with the menu handler
        *
        */
        void RegisterCallbacks()
        {
            if (m_MenuHandler != null)
            {
                //
                // Menu handler has already been created and callbacks registered
                //
                return;
            }
            try
            {
                // Initialize the NX Open C++ API environment
                m_Session = NXOpen.Session.GetSession();

                //
                // Get The NX open UI object
                //
                m_UI = NXOpen.UI.GetUI();

                //
                //Create Popup Menu Handler 
                //
                m_MenuHandler = m_UI.CreateCustomPopupMenuHandler();

                // Registration of callback functions

                // registers the AddPopupMenu Call back
                m_MenuHandler.RegisterAddCustomPopupMenuCallback(this.AddCustomPopupMenuCallback);

                // registers the popupMeny Invoked call back 
                m_MenuHandler.RegisterCustomPopupMenuInvokedCallback(this.CustomPopupMenuInvokedCallback);
            }
            catch (NXException ex)
            {
                m_UI.NXMessageBox.Show("MenuCreator", NXOpen.NXMessageBox.DialogType.Error, ex.Message);
                throw;
             }
         }

        /**
        *   Main method
        */
        public static void Main () 
        {
            try
            {
                CustomMenuCreator menuCreator = GetInstance();
                menuCreator.RegisterCallbacks();
            }
            catch(Exception ex)
            {
                //---- Enter your exception handling code here -----
                m_UI.NXMessageBox.Show("CustomMenuCreator", NXOpen.NXMessageBox.DialogType.Information, ex.Message);
            }
        }

        /**
        *  Startup 
        *  Entrypoint used when program is loaded automatically 
        *  as NX starts up. Note this application must be placed in a 
        *  special folder for NX to find and load it during startup. 
        *  Refer to the NX Open documentation for more details on how 
        *  NX finds and loads applications during startup. 
        */ 
        public static int Startup()
        {
            int retValue = 0;
            try
            {
                CustomMenuCreator menuCreator = GetInstance();
                menuCreator.RegisterCallbacks();
            }
            catch (NXOpen.NXException ex)
            {
                // ---- Enter your exception handling code here ----- 
                UI.GetUI().NXMessageBox.Show("Caught exception",
                NXMessageBox.DialogType.Error, ex.Message);
            }
            return retValue;
        }


        /** 
        *  GetUnloadOption 
        *  Make sure you specify AtTermination for the unload option. 
        *  If you unload the library before the NX Session Terminates 
        *  bad things could happen when we try to execute a udo 
        *  callback that no longer exists in the session. 
        */
        public static int GetUnloadOption()
        {
            //Unloads the image when the NX session terminates 
            return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly); 
        }
       
        /**
        *  Following method cleanup any housekeeping chores that may be needed.
        *  This method is automatically called by NX.
        */
        public static void UnloadLibrary() 
        {
            try
            {
                if( m_MenuHandler != null )
                {
                     m_MenuHandler.Dispose();
                     m_MenuHandler = null;
                }
                if( m_Instance != null )
                {
                    m_Instance = null;
                }
            }
            catch(Exception ex)
            {
                //---- Enter your exception handling code here -----
                m_UI.NXMessageBox.Show("Menu creator", NXOpen.NXMessageBox.DialogType.Information, ex.Message);
            }
        }
        
       
        
        /**
        *   Callback method to add custom menus/submenus
        *
        */
        public int AddCustomPopupMenuCallback()
        {   
            StringBuilder message = new StringBuilder();

            try
            {
                //
                // The List of object selected in the Tree  can be queried.
                //
                TreeListNode[] treeListNode;
                m_MenuHandler.GetSelectedNodes(out treeListNode);

                //
                // The selected object(s) can be queried. Following is an example of using 
                // querying selected objects.
                //                
                if( treeListNode != null && treeListNode.Length > 0)
                {
                    message.Append( " The Following Objects were selected :");
                    message.Append( "\n" );
                    for( int i=0;i<treeListNode.Length; ++i )
                    {
                        if (treeListNode[i] is NXOpen.PDM.PdmNavigatorNode)
                        {
                            String uid = ((NXOpen.PDM.PdmNavigatorNode)treeListNode[i]).GetUid();
                            message.Append( " UID :");
                            message.Append( uid );
                            message.Append( "\n" );

                            String type = ((NXOpen.PDM.PdmNavigatorNode)treeListNode[i]).GetNodeType();
                            message.Append( " Type :");
                            message.Append( type );
                            message.Append( "\n" );
                        }
                    }
                }

                //
                // Add the Top Level Menus/Separators. Top level menus/menu items/seperators
                // must be added by calling menu handler. Subsequent sublevel menus/menu items/seperators
                // can be added by calling add methods on the corresponding parent menu/submenu.
                //
                m_MenuHandler.AddMenuSeparator();     
                CustomPopupMenuItem itemMM1 = m_MenuHandler.AddMenuItem(1,"Main Menu 1");
                CustomPopupMenu menuMM2 = m_MenuHandler.AddMenu (2,"Main Menu 2");

                CustomPopupMenuItem itemMM3 = m_MenuHandler.AddMenuItem(6, "Revise");
            
                if ((treeListNode.Length == 1) && 
                (treeListNode[0] is NXOpen.PDM.PdmNavigatorNode ) &&
                ((NXOpen.PDM.PdmNavigatorNode)treeListNode[0]).GetNodeType().Equals("ItemRevision"))
                {
                    //
                    // Create an new menu only when there is 1 selection and the selection is ItemRevision
                    //
                    CustomPopupMenuItem itemMM4 = m_MenuHandler.AddMenuItem(7, "Main Menu 3");
                }
                else
                {
                    // Code below will show the number of selection objects and the object type of the
                    // first selection
            
                    message.Append (treeListNode.Length);
                    message.Append( "\n" );
                    if (treeListNode[0] is NXOpen.PDM.PdmNavigatorNode)
                    {
                        message.Append(((NXOpen.PDM.PdmNavigatorNode)treeListNode[0]).GetNodeType());
                        message.Append( "\n" );
                    }
                           
                    // Disable the menu when multiple selection and for any selection object which is
                    // not item revision
                    itemMM3.SetDisabled();
                }

                //
                // Add the First Level Menus/Separators to "Main Menu 2"
                //
                CustomPopupMenuItem subMenuSM21 = menuMM2.AddMenuItem(3, "Sub Menu 2-1");
                menuMM2.AddMenuSeparator();
                CustomPopupMenu subMenuSM22 = menuMM2.AddMenu (4, "Sub Menu 2-2");

                // 
                // Add Second Level Menu to "Sub Menu 2-2"
                //
                CustomPopupMenuItem subMenuSM221 = subMenuSM22.AddMenuItem (5,"Sub Menu 2-2-1");
                // Any menu/submenu/menuItem can be disabled by calling SetDisabled method
                subMenuSM221.SetDisabled();  
           
                // m_UI.NXMessageBox.Show("MenuCreator", NXOpen.NXMessageBox.DialogType.Information, message.ToString());
            }
            catch (NXException ex)
            {

                m_UI.NXMessageBox.Show("MenuCreator", NXOpen.NXMessageBox.DialogType.Error, ex.Message);
            }
            return 0;
        }

        /**
        *   Callback method that gets invoked when a custom menu
        *   is selected.
        */
        public int CustomPopupMenuInvokedCallback()
        {
            // m_UI.NXMessageBox.Show("MenuCreator", NXOpen.NXMessageBox.DialogType.Information, "CAME HERE");
            //
            // The invoked menu item can be queried. Menu Item can be again queried for
            // ID and name.
            //
            CustomPopupMenuItem menuItem = m_MenuHandler.GetInvokedCommand();

            //
            // The List of object selected in the Tree  can be queried.
            //
            TreeListNode[] treeListNode;
            m_MenuHandler.GetSelectedNodes(out treeListNode);

            if (treeListNode == null || treeListNode.Length == 0)
            {
                // No selected nodes
                return 0;
            }

            string[] uids = new string[treeListNode.Length];
            string[] nodeTypes = new string[treeListNode.Length];
            for (int i = 0; i < treeListNode.Length; i++)
            {
                //
                // For each Object returned in the List the UID and Object Type can be queried. Need
                // to cast the object to NXOpen::TcModelObjectItem before quering the UID and Type.
                //
                String uid = ((NXOpen.PDM.PdmNavigatorNode)treeListNode[i]).GetUid();
                String type = ((NXOpen.PDM.PdmNavigatorNode)treeListNode[i]).GetNodeType();
                uids[i] = uid;
                nodeTypes[i] = type;
            }
            ListingWindow lw = m_Session.ListingWindow;

            lw.Open();
            lw.WriteLine(" ");
            lw.WriteLine("Inside popupMenuInvokedCallBack Callback ");
            lw.WriteLine("COMMAND NAME: ");
            lw.WriteLine(menuItem.GetName());
            lw.WriteLine("SELECTED NODE UIDS: ");
            for (int i = 0; i < uids.Length; i++)
            {
                lw.WriteLine(uids[i]);
            }

            lw.WriteLine("SELECTED NODE TYPES: ");
            for (int i = 0; i < nodeTypes.Length; i++)
            {
                lw.WriteLine(nodeTypes[i]);
            }


            if (menuItem.GetName().Equals("Revise"))
            {
                lw.WriteLine("NEW REVISION ID: ");
                lw.WriteLine("Implement Teamcenter user exits function to show output");
                //
                // Uncomment code below after implementing the user exits method
                //
                // int errorCode = 0;
                // string name = null;
                // m_ugMgr.InvokePdmServer(2, uids[0], out errorCode, out name);
                // lw.WriteLine(name);
            }
            else
            {
                lw.WriteLine("SELECTED NODE NAMES: ");
                lw.WriteLine("Implement Teamcenter user exits function to show output");
                //
                // Uncomment code below after implementing the user exits method
                //

                // for (int i = 0; i < uids.Length; i++)
                // {
                //     int errorCode = 0;
                //     string name = null;
                //     m_ugMgr.InvokePdmServer(1, uids[i], out errorCode, out name);
                //     lw.WriteLine(name);
                // }
            }  

            return 0;
        }
    }
}
