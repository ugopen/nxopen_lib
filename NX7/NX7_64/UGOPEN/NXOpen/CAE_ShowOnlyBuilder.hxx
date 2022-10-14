#ifndef NXOpen_CAE_SHOWONLYBUILDER_HXX_INCLUDED
#define NXOpen_CAE_SHOWONLYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ShowOnlyBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_ShowOnlyBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ShowOnlyBuilder;
    }
    class Builder;
    class SelectObjectList;
    namespace CAE
    {
        class _ShowOnlyBuilderBuilder;
        /**
            Represents a @link CAE::ShowOnlyBuilder CAE::ShowOnlyBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::ShowHideManager::CreateShowOnlyBuilder CAE::ShowHideManager::CreateShowOnlyBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ShowOnlyBuilder : public Builder
        {
            private: friend class  _ShowOnlyBuilderBuilder;
            protected: ShowOnlyBuilder();
            /**Returns  the selection  <br> License requirements : None */
            public: NXOpen::SelectObjectList * Selection
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif