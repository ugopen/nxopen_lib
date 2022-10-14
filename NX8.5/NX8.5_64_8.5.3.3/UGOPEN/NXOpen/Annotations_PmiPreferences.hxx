#ifndef NXOpen_ANNOTATIONS_PMIPREFERENCES_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiPreferences.ja
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
#include <NXOpen/Annotations.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class PmiPreferences;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        class PmiPreferencesImpl;
        /** Represents line and arrow preferences 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiPreferences : public TransientObject
        {
            private: PmiPreferencesImpl * m_pmipreferences_impl;
            /// \cond NX_NO_DOC 
            public: explicit PmiPreferences(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                    it is illegal to use the object.  In .NET, this method is automatically
                    called when the object is deleted by the garbage collector.  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PmiPreferences();
            /**Returns  the default annotation plane for PMI symbols 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiDefaultPlane DefaultPlane
            (
            );
            /**Sets  the default annotation plane for PMI symbols 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDefaultPlane
            (
                NXOpen::Annotations::PmiDefaultPlane defaultPlane /** default plane */ 
            );
            /**Returns  the toggle for display through shaded models 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool ShadedDisplay
            (
            );
            /** 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetShadedDisplay
            (
                bool shadedDisplay /** shaded display */ 
            );
            /**Returns  the initial letter for datum labels 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DatumLabel
            (
            );
            /**Sets  the initial letter for datum labels 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDatumLabel
            (
                const NXString & datumLabel /** datum label */ 
            );
            /**Sets  the initial letter for datum labels 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            void SetDatumLabel
            (
                const char * datumLabel /** datum label */ 
            );
            /**Returns  the flag indicating whether the PMI would be created view independent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: bool CreateViewIndependent
            (
            );
            /**Sets  the flag indicating whether the PMI would be created view independent 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCreateViewIndependent
            (
                bool createViewIndependent /** create view independent */ 
            );
            /**Returns  the rectangular region width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double PmiRegionWidth
            (
            );
            /**Sets  the rectangular region width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPmiRegionWidth
            (
                double width /** width */ 
            );
            /**Returns  the rectangular region height 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double PmiRegionHeight
            (
            );
            /**Sets  the rectangular region height 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPmiRegionHeight
            (
                double height /** height */ 
            );
            /**Returns  the circular/annular region outer diameter 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double PmiRegionOuterDiameter
            (
            );
            /**Sets  the circular/annular region outer diameter 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPmiRegionOuterDiameter
            (
                double outerDiameter /** outer diameter */ 
            );
            /**Returns  the circular/annular region inner diameter 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double PmiRegionInnerDiameter
            (
            );
            /**Sets  the circular/annular region inner diameter 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPmiRegionInnerDiameter
            (
                double innerDiameter /** inner diameter */ 
            );
            /**Returns  the flag indicating whether to resize on create 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool ResizeOnCreate
            (
            );
            /** 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetResizeOnCreate
            (
                bool resizeOnCreate /** resize on create */ 
            );
            /**Returns  the flag indicating whether to resize on view save 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: bool ResizeOnViewSave
            (
            );
            /** 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetResizeOnViewSave
            (
                bool resizeOnViewSave /** resize on view save */ 
            );
            /**Returns  the resize method 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiResizeMethod ResizeMethod
            (
            );
            /** 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public: void SetResizeMethod
            (
                NXOpen::Annotations::PmiResizeMethod resizeMethod /** resize method */ 
            );
            /**Returns  the flag indicating whether PMI support for geometry  sharing is available
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool PmiSupportForGeometrySharing
            (
            );
            /** 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetPmiSupportForGeometrySharing
            (
                bool pmiSupportForGeomSharing /** pmi support for geom sharing */ 
            );
            /**Returns  the value indicating precise option of PMI Effectivity for prime geometry
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DisplayPmiEffectivityMethod DisplayPmiEffectivityMethod
            (
            );
            /** 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : nx_pmi_effectivity ("NX PMI EFFECTIVITY") */
            public: void SetDisplayPmiEffectivityMethod
            (
                NXOpen::Annotations::DisplayPmiEffectivityMethod displayPmiEffectivityMethod /** display pmi effectivity method */ 
            );
            /**Returns  the value indicating precise option of PMI Effectivity for reference geometry
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::DisplayPmiEffectivityMethod DisplayPmiEffectivityReferenceMethod
            (
            );
            /** 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : nx_pmi_effectivity ("NX PMI EFFECTIVITY") */
            public: void SetDisplayPmiEffectivityReferenceMethod
            (
                NXOpen::Annotations::DisplayPmiEffectivityMethod displayPmiEffectivityReferenceMethod /** display pmi effectivity reference method */ 
            );
            /**Returns  the flag indicating PMI associated objects components loaded for reference
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: bool DisplayPmiAssociatedComponentsLoadedForReference
            (
            );
            /** 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : nx_pmi_effectivity ("NX PMI EFFECTIVITY") */
            public: void SetDisplayPmiAssociatedComponentsLoadedForReference
            (
                bool displayPmiAssociatedComponentsLoadedForReference /** display pmi associated components loaded for reference */ 
            );
            /**Returns  the flag indicating the display of Effectivity Filtered PMI node in Part Navigator
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : None */
            public: bool DisplayEffectivityFilterNodesInPartNavigator
            (
            );
            /** 
             <br>  Created in NX8.5.1.  <br>  
             <br> License requirements : nx_pmi_effectivity ("NX PMI EFFECTIVITY") */
            public: void SetDisplayEffectivityFilterNodesInPartNavigator
            (
                bool displayEffectivityFilterNodesInPartNavigator /** display effectivity filter nodes in part navigator */ 
            );
            /**Returns  the PMI query dialog visibility from mb3 option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: bool DisplayPmiQueryDialogFromMb3
            (
            );
            /**Sets  the PMI query dialog visibility from mb3 option 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetDisplayPmiQueryDialogFromMb3
            (
                bool withDialog /** withdialog */ 
            );
        }; //lint !e1712 default constructor not defined for class  

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