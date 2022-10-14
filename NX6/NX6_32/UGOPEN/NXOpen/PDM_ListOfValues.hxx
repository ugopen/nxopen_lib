#ifndef NXOpen_PDM_LISTOFVALUES_HXX_INCLUDED
#define NXOpen_PDM_LISTOFVALUES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_ListOfValues.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace PDM
    {
        class ListOfValues;
    }
    namespace PDM
    {
    }
    namespace PDM
    {
        /** Represents list of values to be used in search query */
        class NXOPENCPPEXPORT ListOfValues : public TransientObject
        {
            public: explicit ListOfValues(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~ListOfValues();
        };
    }
}
#undef EXPORTLIBRARY
#endif