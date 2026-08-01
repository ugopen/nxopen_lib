#============================================================================
#                  Copyright (c) 2023 Siemens
#                      All rights reserved
#============================================================================
# 
#============================================================================

import NXOpen

def ExecuteMe(arg1, arg2, arg3, arg4, arg5):

    try:
        theSession = NXOpen.Session.GetSession()
        theSession.ListingWindow.WriteLine("    From PythonToBeExecuted")
        theSession.ListingWindow.WriteLine("        Integer argument " + str(arg1))
        theSession.ListingWindow.WriteLine("        float argument " + str(arg2))
        theSession.ListingWindow.WriteLine("        bool argument " + str(arg3))
        theSession.ListingWindow.WriteLine("        string argument " + str(arg4))
        theSession.ListingWindow.WriteLine("        TaggedObject argument (returning WorkPart's Name) " + arg5.Name)
    except Exception as ex:
        # ---- Enter your exception handling code here -----
        raise ex


