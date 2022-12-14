#ifndef NXOpen_TOOLING_PROFILESPLITBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_PROFILESPLITBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_ProfileSplitBuilder.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/Section.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_ProfileSplitBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class ProfileSplitBuilder;
    }
    class Builder;
    class Direction;
    class Expression;
    class Section;
    class SelectBodyList;
    namespace Tooling
    {
        class _ProfileSplitBuilderBuilder;
        /** The ProfileSplit builder  <br> To create a new instance of this class, use @link Tooling::ProfileSplitCollection::CreateProfileSplitBuilder Tooling::ProfileSplitCollection::CreateProfileSplitBuilder@endlink  <br> */
        class NXOPENCPPEXPORT ProfileSplitBuilder : public Builder
        {
            private: friend class  _ProfileSplitBuilderBuilder;
            protected: ProfileSplitBuilder();
            /**Returns  the selected body to be splitted  <br> License requirements : None */
            public: NXOpen::SelectBodyList * SelectBody
            (
            );
            /**Returns  the selected profile  <br> License requirements : None */
            public: NXOpen::Section * SelectProfile
            (
            );
            /** Start traverse function to get edge loop  <br> License requirements : None */
            public: void StTraverse
            (
            );
            /**Returns  the extruded vector to return  <br> License requirements : None */
            public: NXOpen::Direction * DefVector
            (
            );
            /**Sets  the extruded vector to return  <br> License requirements : None */
            public: void SetDefVector
            (
                NXOpen::Direction * defVector /** defvector */ 
            );
            /**Returns  the extruded start distance  <br> License requirements : None */
            public: NXOpen::Expression * ExtDist1
            (
            );
            /**Returns  the extruded end distance  <br> License requirements : None */
            public: NXOpen::Expression * ExtDist2
            (
            );
            /**Returns  the associative flag  <br> License requirements : None */
            public: bool DefAssociative
            (
            );
            /**Sets  the associative flag  <br> License requirements : None */
            public: void SetDefAssociative
            (
                bool defassociative /** defassociative */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
