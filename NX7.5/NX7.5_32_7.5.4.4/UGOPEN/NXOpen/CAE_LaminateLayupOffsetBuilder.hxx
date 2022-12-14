#ifndef NXOpen_CAE_LAMINATELAYUPOFFSETBUILDER_HXX_INCLUDED
#define NXOpen_CAE_LAMINATELAYUPOFFSETBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateLayupOffsetBuilder.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#ifdef _MSC_VER
#pragma once
#endif

#include <NXOpen/NXDeprecation.hxx>
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/CAE_LaminateLayupOffsetBuilder.hxx>
#include <NXOpen/CAE_LaminateSelectEntitiesBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class LaminateLayupOffsetBuilder;
    }
    class Builder;
    namespace CAE
    {
        class LaminateSelectEntitiesBuilder;
    }
    namespace CAE
    {
        class SelectCAEFaceList;
    }
    class SelectTaggedObjectList;
    namespace CAE
    {
        class _LaminateLayupOffsetBuilderBuilder;
        class LaminateLayupOffsetBuilderImpl;
        /** Represents a @link CAE::LaminateLayupOffset CAE::LaminateLayupOffset@endlink  builder  <br> To create a new instance of this class, use @link CAE::LaminateGlobalLayupMgr::CreateLayupOffsetBuilder CAE::LaminateGlobalLayupMgr::CreateLayupOffsetBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  LaminateLayupOffsetBuilder : public Builder
        {
            private: LaminateLayupOffsetBuilderImpl * m_laminatelayupoffsetbuilder_impl;
            private: friend class  _LaminateLayupOffsetBuilderBuilder;
            protected: LaminateLayupOffsetBuilder();
            public: ~LaminateLayupOffsetBuilder();
            /** Find or remove a surface if it is duplicated  @return  reference plane position  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXString FindOrRemoveDuplicateSurfaces
            (
                bool remove /** if remove is false, just find the surface otherwise remove it */
            );
            /**Returns  the faces (deprecated) 
             @deprecated Deprecated in NX7.5.1 <br> 
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.1") NXOpen::CAE::SelectCAEFaceList * Faces
            (
            );
            /**Returns  a method to get the selected faces or elements 
             @deprecated Deprecated in NX7.5.2 <br> 
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.2") NXOpen::SelectTaggedObjectList * Objfaces
            (
            );
            /**Returns  the geometric face(s) and element faces on which to assign the layup offset rule  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateSelectEntitiesBuilder * Selection
            (
            );
            /**Sets  the fiber distance  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetFiberDistance
            (
                double fiberDistance /** fiber distance */
            );
            /**Returns  the fiber distance  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: double FiberDistance
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
