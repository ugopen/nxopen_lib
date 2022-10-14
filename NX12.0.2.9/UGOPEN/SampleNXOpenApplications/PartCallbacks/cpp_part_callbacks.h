//----------------------------------------------------------------------------
//                  Copyright (c) 2007 UGS Corp.
//                      All rights reserved
//----------------------------------------------------------------------------
// 
//
// cpp_part_callbacks.h
//
// Description:
//     This simple demo registers part callbacks for every available reason
//     via the C++ language.
//
//     This file must be compiled with cpp_part_callbacks.cpp.
//
//     See cpp_part_callbacks.cpp for more detailed instructions.
//
//---------------------------------------------------------------------------/

#include <iostream>
#include <uf_defs.h>
#include <uf.h>

#include <NXOpen/Session.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>


using namespace std;
using namespace NXOpen;
class CppPartCallbacks;
extern CppPartCallbacks *theCppPartCallbacks;


class CppPartCallbacks
{
    // class members
    public:
        //-----------------------------------------------------
        // Used to tell us if we've already registered our callbacks
        //-----------------------------------------------------
        static int registered;

        //-----------------------------------------------------
        // The ids of the registered callbacks are used if
        // you ever want to unregister a callback.
        // If you plan to register the callback once for
        // the enitre session, and don't intend to remove them,
        // (recommended) tracking the id may not be necessary.
        //-----------------------------------------------------
        static int idPartCreated1;
        static int idPartOpened1;
        static int idPartSaved1;
        static int idPartSavedAs1;
        static int idPartClosed1;
        static int idPartModified1;
        static int idPartRenamed1;
        static int idWorkPartChanged1;

        static Session* theSession;
        static ListingWindow* lw;

        CppPartCallbacks();
        ~CppPartCallbacks();

        //-----------------------------------------------------
        // Callback Prototypes
        //-----------------------------------------------------
        void PartCreated1(BasePart* p);
        void PartOpened1(BasePart* p);
        void PartSaved1(BasePart* p);
        void PartSavedAs1(BasePart* p);
        void PartClosed1(BasePart* p);
        void PartModified1(BasePart* p);
        void PartRenamed1(BasePart* p);
        void WorkPartChanged1(BasePart* p);

    private:
        //-----------------------------------------------------
        // this does the work to register the callbacks
        //-----------------------------------------------------
        void InitializeCallbacks();

};
