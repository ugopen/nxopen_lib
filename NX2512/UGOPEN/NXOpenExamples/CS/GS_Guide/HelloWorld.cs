/*==================================================================================================
  
                      Copyright (c) 2022 Siemens PLM 
                   Unpublished - All rights reserved

==================================================================================================*/

using System;
using NXOpen;

public class NXJournal
{
    public static void Main()
    {
        Session theSession = Session.GetSession();

        Guide.InfoWriteLine("Hello, World!");

    }
}
