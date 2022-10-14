#ifndef NXOpen_CAE_GROUPMETHOD_HXX_INCLUDED
#define NXOpen_CAE_GROUPMETHOD_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_GroupMethod.ja
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
#include <NXOpen/SelectionMethod.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class GroupMethod;
    }
    class SelectionMethod;
    class TaggedObject;
    namespace CAE
    {
    }
    namespace CAE
    {
        /** Represents the output from the Group smart selector method
             <br> To obtain an instance of this class use CAE::SmartSelectionManager <br> */
        class NXOPENCPPEXPORT GroupMethod : public SelectionMethod
        {
            public: explicit GroupMethod(void *ptr);
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.   <br> License requirements : None */
            public: virtual ~GroupMethod();
            /** Returns the resultant entities  @return  Resultant entities  <br> License requirements : None */
            public: std::vector<NXOpen::TaggedObject *> GetEntities
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif