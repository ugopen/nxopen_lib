#ifndef NXOpen_JAMTESTNAMESPACE_OMPPSUBOBJECT_HXX_INCLUDED
#define NXOpen_JAMTESTNAMESPACE_OMPPSUBOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     JamTestNamespace_OMPPSubobject.ja
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
#include <NXOpen/JamTestNamespace_OMPPSubobject.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopenjamtestcpp_exports.hxx>
namespace NXOpen
{
    namespace JamTestNamespace
    {
        class OMPPSubobject;
    }
    namespace JamTestNamespace
    {
        class _OMPPSubobjectBuilder;
        /**  <br> Test class <br> */
        class NXOPENJAMTESTCPPEXPORT OMPPSubobject : public TaggedObject
        {
            private: friend class  _OMPPSubobjectBuilder;
            protected: OMPPSubobject();
            /**Returns   <br> License requirements : None */
            public: int Id
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif