#ifndef NXOpen_TOOLING_FAMILYMOLDBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_FAMILYMOLDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_FamilyMoldBuilder.ja
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
#include <NXOpen/Tooling_FamilyMoldBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class FamilyMoldBuilder;
    }
    class Builder;
    namespace Tooling
    {
        class _FamilyMoldBuilderBuilder;
        /** Creates a Mold Wizard Family Mold builder  <br> To create a new instance of this class, use @link Tooling::FamilyMoldCollection::CreateFamilyMoldBuilder Tooling::FamilyMoldCollection::CreateFamilyMoldBuilder@endlink  <br> */
        class NXOPENCPPEXPORT FamilyMoldBuilder : public Builder
        {
            private: friend class  _FamilyMoldBuilderBuilder;
            protected: FamilyMoldBuilder();
            /**Returns  the method to get the selected item name from family mold builder  <br> License requirements : None */
            public: NXString ListItem
            (
            );
            /**Sets  the method to get the selected item name from family mold builder  <br> License requirements : None */
            public: void SetListItem
            (
                const NXString & strListItem /** strlistitem */ 
            );
            /**Returns  the method to get the selected item index from family mold builder  <br> License requirements : None */
            public: int ItemIndex
            (
            );
            /**Sets  the method to get the selected item index from family mold builder  <br> License requirements : None */
            public: void SetItemIndex
            (
                int intItemIndex /** intitemindex */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
