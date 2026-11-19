//----------------------------------------------------------------------------
//                  Copyright (c) 2023 Siemens
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//----------------------------------------------------------------------------


//CPPToBeExecuted
//
// Mandatory UF Includes
#include <uf.h>
#include <uf_object_types.h>

// Internal Includes
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/UI.hxx>

// Internal+External Includes
#include <NXOpen/Annotations.hxx>
#include <NXOpen/Assemblies_Component.hxx>
#include <NXOpen/Assemblies_ComponentAssembly.hxx>
#include <NXOpen/Body.hxx>
#include <NXOpen/BodyCollection.hxx>
#include <NXOpen/Face.hxx>
#include <NXOpen/Line.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Session.hxx>
#include <NXOpen/NXVariant.hxx>

// Std C++ Includes
#include <iostream>
#include <sstream>
#include <variant>

using namespace NXOpen;
using std::string;
using std::exception;
using std::stringstream;
using std::endl;
using std::cout;
using std::cerr;


extern "C" DllExport void ExecuteMe(std::vector<NXOpen::NXVariant> variants, NXOpen::NXVariant & retVal)
{

    NXOpen::Session* theSession = NXOpen::Session::GetSession();

    try
    {
        // Need to extract the Variant entries from the input
        // This step is needed as each entry can be a singlur object (as this example uses)
        // or it could be a vector<NXOpen::NXVariantEntry>
        // for example if we pass in an int and an array NXString
        // the first argument would be a NXOpen::NXVariantEntry (an int)
        // while the second argument would be std::vector<NXOpen::NXVariantEntry> (a vector of NXOpen::NXString)
        NXOpen::NXVariantEntry entry0 = std::get< NXOpen::NXVariantEntry>(variants[0]);
        NXOpen::NXVariantEntry entry1 = std::get< NXOpen::NXVariantEntry>(variants[1]);
        NXOpen::NXVariantEntry entry2 = std::get< NXOpen::NXVariantEntry>(variants[2]);
        NXOpen::NXVariantEntry entry3 = std::get< NXOpen::NXVariantEntry>(variants[3]);
        NXOpen::NXVariantEntry entry4 = std::get< NXOpen::NXVariantEntry>(variants[4]);

        // Now we extract the arguments.  
        // Please note to reduced code this code assumes the arguments are
        // as expected, and skips testing with std::holds_alternative
        //
        // Also note is possible that null value was sent in, in which case the value will be std::monostate

        int arg0 = std::get<int>(entry0);
        std::string arg0String = std::to_string(arg0);

        double arg1 = std::get<double>(entry1);
        std::string arg1String = std::to_string(arg1);

        bool arg2 = std::get<bool>(entry2);
        std::string arg2String;
        if (arg2)
            arg2String = "true";
        else
            arg2String = "false";

        NXOpen::NXString arg3 = std::get<NXOpen::NXString>(entry3);

        NXOpen::TaggedObject* arg4 = std::get<NXOpen::TaggedObject*>(entry4);

        theSession->ListingWindow()->WriteLine("    From CPPToBeExecuted");
        theSession->ListingWindow()->WriteLine("        Integer argument " + arg0String);
        theSession->ListingWindow()->WriteLine("        float argument " + arg1String);
        theSession->ListingWindow()->WriteLine("        bool argument " + arg2String);
        theSession->ListingWindow()->WriteLine("        string argument " + arg3);
        NXOpen::Part * part = dynamic_cast<NXOpen::Part*>(arg4);
        theSession->ListingWindow()->WriteLine("        TaggedObject argument (returning WorkPart's Name) " + part->Name());

    }
    catch (const NXException& e1)
    {
        // ---- Enter your exception handling code here -----
        throw e1;
    }
}

//------------------------------------------------------------------------------
// Unload Handler
//------------------------------------------------------------------------------
extern "C" DllExport int ufusr_ask_unload()
{
    // Unloads the image when NX session terminates
    return (int)Session::LibraryUnloadOptionImmediately;

}
