//***********************************************************************************
 //                                                                                 *
 //        Copyright 2011 Siemens Product Lifecycle Management Software Inc.        *
 //                               All Rights Reserved.                              *
 //                                                                                 *
 //**********************************************************************************

//

#using <mscorlib.dll>

using namespace System;

//NXOpen specifics
using namespace NXOpen;
using namespace NXOpen::UF;
using namespace NXOpen::Utilities;

public ref class SampleApplication
{
public:
    SampleApplication(){}

    void Run(String^ ufName)
    {
        Session^ theSession = Session::GetSession();
        UFSession^ theUfSession = UFSession::GetUFSession();

        ListingWindow^ lw = theSession->ListingWindow;
        lw->Open();
        String^ outputLine = "Running Managed C++ Sample Application. Executed through the function: " + ufName;
        lw->WriteLine(outputLine);
    }

    static int GetUnloadOption(String^ dummy) 
    {
        return UFConstants::UF_UNLOAD_IMMEDIATELY;
    }

    static void Main(void)
    {
        SampleApplication^ sampleApplication = gcnew SampleApplication();
        sampleApplication->Run("Main");
    }

    //ufget is a User Exit for File-->Open menu option. To execute this function, the environment variable 
    //USER_RETRIEVE should be defined to the path of the dll built from this automation program.
    
    static int ufget(array<System::String^> ^dummy)
    {
        SampleApplication^ sampleApplication = gcnew SampleApplication();
        sampleApplication->Run("ufget");
        return 0;
    }
};

