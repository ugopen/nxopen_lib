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


    public static void Run()
    {
        DoLog("In NXOpenRemotingService.Main - getting session\n");
        Session theSession = Session.GetSession();
        UFSession theUFSession = UFSession.GetUFSession();
        try
        {
            int port = 4567;
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
        Thread.Sleep(Timeout.Infinite);
        DoLog("\n\nSERVICE ENDED!!!\n\n");
    }
}



