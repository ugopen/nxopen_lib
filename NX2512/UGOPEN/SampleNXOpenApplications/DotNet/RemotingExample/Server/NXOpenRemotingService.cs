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



public class SimpleNXOpenServerLogger
{
    private static string filePath;

    private static object syncLock = new object();

    public SimpleNXOpenServerLogger()
    {
        string logFileDirectory = Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location);
        filePath = logFileDirectory + Path.DirectorySeparatorChar + "NXOpenDotNetServerLog.txt";
    }

    public static void Log(string message)
    {
        lock (syncLock)
        {
            //Append to the log file 
            using (StreamWriter streamWriter = new StreamWriter(filePath, true))
            {
                streamWriter.WriteLine(message);
                streamWriter.Close();
            }
        }
    }
}

public class NXOpenRemotingService
{

    public static int port = 4567;
    public static Session theSession = null;
    public static UFSession theUFSession = null;
    public static UI theUI = null;

    //The first flag indicates that we are unloading the dll.  The second flag indicates that the service has completed.  This is needed as the
    //Run and the unload will be run in in two different threads.  We indicate that we are unloading so that we can end the while loop
    //and then output a message to the syslog that the service has ended.  However, since we have two threads, we do not want the unload method to 
    //proceed until the service loop is done processing.
    public static bool isUnloaded = false;
    public static bool serviceEnded = false;

    public static SimpleNXOpenServerLogger NXOpenServerLog = new SimpleNXOpenServerLogger();

    // While it would be nice to log all server information to NX Syslog while running,
    // so we are going to log to file that is located where the dll is located at
    // And this file will be overriten each time this Server dll is run.
    //
    // This example is meant to show how to do remoting, so it will be left to the customer
    // to determine the best solution for logging of errors.  As this example will not work 
    // well if two different NX sessions both run the same dll located in the same location.
    //

    public static void DoLog(String s)
    {
        SimpleNXOpenServerLogger.Log(s);
    }

    public static void Main(String[] args)
    {
        Start();
    }

    public static void Start()
    {
        //Setup Log file to be beside dll
        // All "session" objects need to be called on main thread, not the created background thread in Start()
        DoLog("In NXOpenRemotingService.Main - getting session\n");
        NXOpenRemotingService.theSession = Session.GetSession();
        NXOpenRemotingService.theUFSession = UFSession.GetUFSession();
        NXOpenRemotingService.theUI = UI.GetUI();
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

            DoLog("Exporting UI Object");
            RemotingServices.Marshal(theUI, "UI");


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

        DoLog("Disconnecting UI Object");
        RemotingServices.Disconnect(theUI);

    }

}



