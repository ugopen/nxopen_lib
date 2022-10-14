/*=============================================================================

                    Copyright (c) 2008 Siemens PLM Solutions
                    Unpublished - All rights reserved

===============================================================================
File description: Sample NX/Open Application
===============================================================================

=============================================================================
*/
using System;
using System.IO;
using System.Threading;
using System.Runtime.Remoting;
using System.Runtime.Remoting.Channels;
using System.Runtime.Remoting.Channels.Http;
using System.Runtime.Remoting.Lifetime;
using System.Runtime.Remoting.Messaging;
using System.Runtime.Serialization.Formatters;
using System.Diagnostics;

using System.Collections;

using NXOpen;
using NXOpen.Utilities;
using NXOpen.UF;

public class NXOpenRemotingService
{

    public static int port = 4567;
    public static Session theSession;
    public static UFSession theUFSession;
    
    //The first flag indicates that we are unloading the dll.  The second flag indicates that the service has completed.  This is needed as the
    //Run and the unload will be run in in two different threads.  We indicate that we are unloading so that we can end the while loop
    //and then output a message to the syslog that the service has ended.  However, since we have two threads, we do not want the unload method to 
    //proceed until the service loop is done processing.
    public static bool isUnloaded = false;
    public static bool serviceEnded = false; 


    public static void DoLog(String s)
    {
        Session.GetSession().LogFile.WriteLine(s);
    }

    public static void Main(String[] args)
    {
        Start();
    }

    public static void Start()
    {
        Thread serverThread = new Thread(new ThreadStart(Run));
        serverThread.Start();
    }

    // This method should only peform the following operations:
    // - Setting up Remoting 
    // - Obtaining the session
    // - Exporting the session
    // 
    // If you make other calls especially NXOpen calls that may involve the UI
    // (such as ListingWindow).  This may put NX in state of an infinite loop.
    // Calls to the LogFile API are acceptable though.
    public static void Run()
    {
        DoLog("In NXOpenRemotingService.Main - getting session\n");
        theSession = Session.GetSession();
        theUFSession = UFSession.GetUFSession();
        try
        {
            DoLog("Starting NX Service\n");

            LifetimeServices.LeaseTime = System.TimeSpan.FromDays(10000);

            SoapServerFormatterSinkProvider provider = new SoapServerFormatterSinkProvider();
            provider.TypeFilterLevel = System.Runtime.Serialization.Formatters.TypeFilterLevel.Full;

            // Create the IDictionary to set the port on the channel instance.

            IDictionary props = new Hashtable();
            props["port"] = port;

            // Create a new http channel with the given provider and properties
            ChannelServices.RegisterChannel(new HttpChannel(props, null, provider), false);

            DoLog("\n\n");
            DoLog("Exporting Session object");
            RemotingServices.Marshal(theSession, "NXOpenSession");

            DoLog("Exporting UFSession Object");
            RemotingServices.Marshal(theUFSession, "UFSession");


            DoLog("NX Service started on port " + port + "\n");

        }
        catch (Exception e)
        {
            DoLog(e.ToString());
        }
        while (!isUnloaded)
        {
            Thread.Sleep(1000);
        }
        
        DoLog("\n\nSERVICE ENDED!!!\n\n");
        serviceEnded = true;
    }


    public static int GetUnloadOption(string dummy) 
    { 
        return (int)Session.LibraryUnloadOption.Explicitly; 
    }


    public static void UnloadLibrary(string arg)
    {
        isUnloaded = true;
        while (!serviceEnded)
        {

        }

        DoLog("Disconnecting Session object");
        RemotingServices.Disconnect(theSession);

        DoLog("Disconnecting UFSession Object");
        RemotingServices.Disconnect(theUFSession);
    }

}



