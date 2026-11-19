#include "stdafx.h"

#using <mscorlib.dll>

using namespace System;

// NXOpen specifics
using namespace NXOpen;
using namespace NXOpen::UF;
using namespace NXOpen::Utilities;

public __gc class SampleApplication
{
      public:
            static void Main(void)
            {
                  Session* theSession     = Session::GetSession();
                  UFSession* theUfSession = UFSession::GetUFSession();

                  ListingWindow* lw = theSession->ListingWindow;
                  lw->Open();
                  lw->WriteLine(S"Running C++ the Sample Application");
            }
            static int GetUnloadOption(String* dummy) 
            {
                  return UFConstants::UF_UNLOAD_IMMEDIATELY;
            }
};

