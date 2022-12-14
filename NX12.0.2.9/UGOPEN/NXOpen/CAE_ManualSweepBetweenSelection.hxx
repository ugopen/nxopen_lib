#ifndef NXOpen_CAE_MANUALSWEEPBETWEENSELECTION_HXX_INCLUDED
#define NXOpen_CAE_MANUALSWEEPBETWEENSELECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ManualSweepBetweenSelection.ja
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
#include <NXOpen/CAE_ManualSweepBetweenListItemSelection.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class ManualSweepBetweenSelection;
    }
    class Builder;
    namespace CAE
    {
        class CAEEdge;
    }
    namespace CAE
    {
        class ManualSweepBetweenListItemSelection;
    }
    namespace CAE
    {
        class ManualSweepBetweenListItemSelectionList;
    }
    namespace CAE
    {
        class SelectCAEFace;
    }
    namespace CAE
    {
        class SelectCAEFaceList;
    }
    namespace CAE
    {
        class _ManualSweepBetweenSelectionBuilder;
        class ManualSweepBetweenSelectionImpl;
        /**
            Builder for creating Manual Hex Mesh - Face Dependency type.
             <br> To create a new instance of this class, use @link NXOpen::CAE::SweepBetweenMeshBuilder::ManualSweepBetween  NXOpen::CAE::SweepBetweenMeshBuilder::ManualSweepBetween @endlink  <br> 
         <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Mesh3dHexBuilder CAE::Mesh3dHexBuilder@endlink . <br>  

         <br>  Created in NX7.5.2.  <br>  
        */
        class NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Mesh3dHexBuilder.") NXOPENCPP_CAEEXPORT  ManualSweepBetweenSelection : public NXOpen::Builder
        {
            private: ManualSweepBetweenSelectionImpl * m_manualsweepbetweenselection_impl;
            private: friend class  _ManualSweepBetweenSelectionBuilder;
            protected: ManualSweepBetweenSelection();
            public: ~ManualSweepBetweenSelection();
            /**Returns  the master face 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Mesh3dHexBuilder CAE::Mesh3dHexBuilder@endlink . <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Mesh3dHexBuilder.") NXOpen::CAE::SelectCAEFace * MasterFace
            (
            );
            /**Returns  the target face 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Mesh3dHexBuilder CAE::Mesh3dHexBuilder@endlink . <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Mesh3dHexBuilder.") NXOpen::CAE::SelectCAEFace * TargetFace
            (
            );
            /**Returns  the Wall face selection 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Mesh3dHexBuilder CAE::Mesh3dHexBuilder@endlink . <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Mesh3dHexBuilder.") NXOpen::CAE::SelectCAEFaceList * WallFaceSelection
            (
            );
            /**Returns  the loop list 
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Mesh3dHexBuilder CAE::Mesh3dHexBuilder@endlink . <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Mesh3dHexBuilder.") NXOpen::CAE::ManualSweepBetweenListItemSelectionList * LoopList
            (
            );
            /** The list item  @return  
             <br>  @deprecated Deprecated in NX10.0.0.  Use @link CAE::Mesh3dHexBuilder CAE::Mesh3dHexBuilder@endlink . <br>  

             <br>  Created in NX7.5.2.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NX_DEPRECATED("Deprecated in NX10.0.0.  Use CAE::Mesh3dHexBuilder.") NXOpen::CAE::ManualSweepBetweenListItemSelection * CreateNewListItem
            (
                NXOpen::CAE::CAEEdge * tMasterEdge /** The master edge */,
                NXOpen::CAE::CAEEdge * tTargetEdge /** The target edge */,
                bool fFlipDirection /** flip direction */
            );
        };
    }
}

#ifdef _MSC_VER
#pragma warning(pop)
#endif
#ifdef __GNUC__
#ifndef NX_NO_GCC_DEPRECATION_WARNINGS
#pragma GCC diagnostic warning "-Wdeprecated-declarations"
#endif
#endif

#undef EXPORTLIBRARY
#endif
