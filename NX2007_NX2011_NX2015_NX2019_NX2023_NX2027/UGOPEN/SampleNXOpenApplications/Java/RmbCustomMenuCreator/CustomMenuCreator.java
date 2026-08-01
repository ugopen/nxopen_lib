//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Menu Creator
//=============================================================================
//



//------------------------------------------------------------------------------
//These imports are needed for the following sample code
//------------------------------------------------------------------------------
import java.rmi.RemoteException;
import java.util.Vector;

import nxopen.BaseSession;
import nxopen.CustomPopupMenu;
import nxopen.CustomPopupMenuHandler;
import nxopen.CustomPopupMenuItem;
import nxopen.NXException;
import nxopen.Session;
import nxopen.SessionFactory;

import nxopen.TreeListNode;
import nxopen.UI;
import nxopen.CustomPopupMenuHandler.AddCustomPopupMenuCallback;
import nxopen.CustomPopupMenuHandler.CustomPopupMenuInvokedCallback;
import nxopen.pdm.PdmNavigatorNode;

import nxopen.SessionFactory;
import nxopen.UFSession;
import nxopen.uf.UFUgmgr;



//------------------------------------------------------------------------------
//Represents CustomMenuCreator class
//------------------------------------------------------------------------------
public class CustomMenuCreator implements AddCustomPopupMenuCallback, CustomPopupMenuInvokedCallback
{
    //class members
    private Session m_Session = null;
    private  UI m_UI = null;
    private UFUgmgr m_ugMgr = null;

    private CustomPopupMenuHandler m_Handler;

    static CustomMenuCreator m_Instance = null;
    
    public static nxopen.UFSession m_ufSession = null;
    

    //------------------------------------------------------------------------------
    //Constructor for MenuCreator class
    //------------------------------------------------------------------------------
    private CustomMenuCreator() throws Exception, RemoteException
    {
        m_ufSession = (UFSession)SessionFactory.get("UFSession");
        m_ugMgr = m_ufSession.ugmgr();
    }
    
    /**
    *   Returns a single instance of the singleton class
    *
    *   @return CustomMenuCreator
    */
    public static CustomMenuCreator getInstance() throws RemoteException, Exception
    {
        if( m_Instance == null )
        {
            m_Instance = new CustomMenuCreator();
        }
        return m_Instance;
        
    }
    
    /**
    *  Removes the instance
    */
    public static void removeInstance() throws RemoteException, NXException
    {
        if( m_Instance != null )
        {
            m_Instance.cleanup();
        }
         m_Instance = null;
    }
    
    /**
    *  Disposes the handler object
    */
    public void cleanup() throws RemoteException, NXException 
    {
        if( m_Handler != null )
        {
            m_Handler.dispose();
            m_Handler = null;
        }
    }
    
    /**
    *   Registers the callback methods with the menu handler
    *
    */
    public void registerCallBack() throws RemoteException, NXException
    {
        m_Session = (Session)SessionFactory.get("Session");
       
        m_UI = (UI)SessionFactory.get("UI");
        if( m_Handler == null )
        {
            m_Handler=m_UI.createCustomPopupMenuHandler();
            m_Handler.registerAddCustomPopupMenuCallback( this );
            m_Handler.registerCustomPopupMenuInvokedCallback( this );
        }
    }
    
    /**
    *  Returns the handler object
    */
    public CustomPopupMenuHandler getHandler()
    {
        return m_Handler;
    }
    
    /**
    *   Returns the UI object
    */
    public UI getUI()
    {
        return m_UI;
    }
    
    /**
    *   Main method
    */
    public static void main(String [] argv) throws Exception
    {
        CustomMenuCreator menuCreator = null;
        try
        {
            menuCreator = CustomMenuCreator.getInstance();
            menuCreator.registerCallBack();

        }
        catch(Exception ex)
        {
            if(  menuCreator != null && menuCreator.getUI() != null   )
            {
                menuCreator.getUI().nxmessageBox().show("CustomMenuCreator", nxopen.NXMessageBox.DialogType.INFORMATION, ex.getMessage());
            }
            else
            {
                ex.printStackTrace();
            }
        }
    }
    

    /** 
    *  GetUnloadOption 
    *  Make sure you specify AtTermination for the unload option. 
    *  If you unload the library before the NX Session Terminates 
    *  bad things could happen when we try to execute a udo 
    *  callback that no longer exists in the session. 
    */
    public static final int getUnloadOption()
    {
        return BaseSession.LibraryUnloadOption.EXPLICITLY;

    }
    
    /**
    *  Following method cleanup any housekeeping chores that may be needed.
    *  This method is automatically called by NX.
    */
    public static void onUnload() throws NXException, RemoteException
    {
        CustomMenuCreator.removeInstance();

    }
    
    /**
    *   Callback method to add custom menus/submenus
    *
    */
    public int addCustomPopupMenuCallback()throws NXException, RemoteException
    {
        try
        {
            StringBuffer message = new StringBuffer();
            TreeListNode[] treeListNode = m_Handler.getSelectedNodes();
            if( treeListNode != null && treeListNode.length > 0)
            {
                message.append( " The Following Objects were selected :");
                message.append( "\n" );
                for( int i=0;i<treeListNode.length; ++i )
                {
                    if(treeListNode[i] instanceof PdmNavigatorNode )
                    {
                    
                        String uid = (( PdmNavigatorNode )treeListNode[i]).getUid();
                        message.append( " UID :");
                        message.append( uid );
                        message.append( "\n" );
                    
                        String type = (( PdmNavigatorNode )treeListNode[i]).getNodeType();
                        message.append( " Type :");
                        message.append( type );
                        message.append( "\n" );
                    }
                }
            }
            
            //
            // Add the Top Level Menus/Separators. Top level menus/menu items/seperators
            // must be added by calling menu handler. Subsequent sublevel menus/menu items/seperators
            // can be added by calling add methods on the corresponding parent menu/submenu.
            //
            m_Handler.addMenuSeparator();
   
            CustomPopupMenuItem itemMM1 = m_Handler.addMenuItem(1,"Main Menu 1");

            CustomPopupMenu menuMM2 = m_Handler.addMenu (2,"Main Menu 2");

            CustomPopupMenuItem itemMM3 = m_Handler.addMenuItem (6,"Revise");
            
            if ((treeListNode.length == 1) && 
                (treeListNode[0] instanceof PdmNavigatorNode ) &&
                (( PdmNavigatorNode )treeListNode[0]).getNodeType().equals("ItemRevision"))
            {
                //
                // Create an new menu only when there is 1 selection and the selection is ItemRevision
                //
                CustomPopupMenuItem itemMM4 = m_Handler.addMenuItem(7,"Main Menu 3");
            }
            else
            {
                // Code below will show the number of selection objects and the object type of the
                // first selection
            
                message.append (treeListNode.length);
                message.append( "\n" );
                if (treeListNode[0] instanceof PdmNavigatorNode)
                {
                    message.append ((( PdmNavigatorNode )treeListNode[0]).getNodeType());
                    message.append( "\n" );
                }
                           
                // Disable the menu when multiple selection and for any selection object which is
                // not item revision
                itemMM3.setDisabled();
            }
                 
            //
            // Add the First Level Menus/Separators to "Main Menu 2"
            //
            CustomPopupMenuItem subMenuSM21 = menuMM2.addMenuItem(3, "Sub Menu 2-1");
       
            menuMM2.addMenuSeparator();
            CustomPopupMenu subMenuSM22 = menuMM2.addMenu (4, "Sub Menu 2-2");

            // 
            // Add Second Level Menu to "Sub Menu 2-2"
            //
            CustomPopupMenuItem subMenuSM221 = subMenuSM22.addMenuItem (5,"Sub Menu 2-2-1");
       
            // m_UI.nxmessageBox().show("MenuCreator", nxopen.NXMessageBox.DialogType.INFORMATION, message.toString());
        }
        catch( Throwable e  )
        {
            e.printStackTrace();
          
        }
        return 0;
    }

    /**
    *   Callback method that gets invoked when a custom menu
    *   is selected.
    */
    public int customPopupMenuInvokedCallback()throws NXException, RemoteException
    {

        CustomPopupMenuItem invokedItem =  m_Handler.getInvokedCommand();
        String commandInvoked = invokedItem.getName();
        
        Vector<String> uids = new Vector<String>();
        Vector<String> nodeTypes = new Vector<String>();
        
        StringBuffer message = new StringBuffer();
        message.append ( "The menu ");
        message.append( commandInvoked );
        message.append ( " was invoked.");
        message.append ("\n");
        
        TreeListNode[] treeListNode = m_Handler.getSelectedNodes();
        if( treeListNode != null && treeListNode.length > 0)
        {
            message.append ("SELECTED NODE UIDS: ");
            message.append( "\n" );
            
            for( int i=0;i<treeListNode.length; ++i )
            {
                if(treeListNode[i] instanceof PdmNavigatorNode )
                {   
                    String uid = (( PdmNavigatorNode )treeListNode[i]).getUid();
                    uids.add(uid);
                    message.append( uid );
                    message.append( "\n" );
                }
            }
            message.append ("SELECTED NODE TYPES: ");
            message.append( "\n" );
            
            for( int i=0;i<treeListNode.length; ++i )
            {
                if(treeListNode[i] instanceof PdmNavigatorNode )
                {
                    String type = (( PdmNavigatorNode )treeListNode[i]).getNodeType();
                    nodeTypes.add(type);
                    message.append( type );
                    message.append( "\n" );
                }
            }
                    
            if (commandInvoked.equals("Revise"))
            {
                message.append ("NEW REVISION ID: ");
                message.append( "\n" );
                message.append ("Implement Teamcenter user exits function to show output");
                message.append( "\n" );
                //
                // Uncomment code below after implementing the user exits method
                //
                // UFUgmgr.InvokePdmServerData outputData = m_ugMgr.invokePdmServer(2, uids.get(0));
                // int outputcode = outputData.outputCode;
                // String name = outputData.outputString;
                // message.append (name);
                // message.append( "\n" );

            }
            else
            {
                message.append ("SELECTED OBJECT NAMES: ");
                message.append( "\n" );
                message.append ("Implement Teamcenter user exits function to show output");
                message.append( "\n" );
                //
                // Uncomment code below after implementing the user exits method
                //

                // for (int i=0; i < uids.size(); i++)
                // {
                //     UFUgmgr.InvokePdmServerData outputData = m_ugMgr.invokePdmServer(1, uids.get(i));
                //     int outputcode = outputData.outputCode;
                //     String name = outputData.outputString;
                //     message.append (name);
                //     message.append( "\n" );
                // }
                
            }  
        }
         
        m_UI.nxmessageBox().show("MenuCreator", nxopen.NXMessageBox.DialogType.INFORMATION, message.toString());
        return 0;
    }
    
}
