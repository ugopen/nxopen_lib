#ifndef NXOpen_WELD_WELDMANAGER_HXX_INCLUDED
#define NXOpen_WELD_WELDMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_WeldManager.ja
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
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/Weld_UserDefinedWeldBuilder.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class WeldManager;
    }
    namespace Features
    {
        class FeatureCollection;
    }
    namespace Annotations
    {
        class Annotation;
    }
    class Curve;
    namespace Features
    {
        class Feature;
    }
    class NXObject;
    namespace Weld
    {
        class AutoPointBuilder;
    }
    namespace Weld
    {
        class AutoWeldSymbolsBuilder;
    }
    namespace Weld
    {
        class CharacteristicsBuilder;
    }
    namespace Weld
    {
        class DatumPin;
    }
    namespace Weld
    {
        class DatumPinBuilder;
    }
    namespace Weld
    {
        class DatumSurface;
    }
    namespace Weld
    {
        class DatumSurfaceBuilder;
    }
    namespace Weld
    {
        class EasyPatternBuilder;
    }
    namespace Weld
    {
        class EdgePrep;
    }
    namespace Weld
    {
        class EdgePrepBuilder;
    }
    namespace Weld
    {
        class EdgePrepValuesBuilder;
    }
    namespace Weld
    {
        class ExportWeldBuilder;
    }
    namespace Weld
    {
        class ExportWeldJointBuilder;
    }
    namespace Weld
    {
        class Fill;
    }
    namespace Weld
    {
        class FilletBuilder;
    }
    namespace Weld
    {
        class GrooveBuilder;
    }
    namespace Weld
    {
        class JointExitBuilder;
    }
    namespace Weld
    {
        class PlugSlotBuilder;
    }
    namespace Weld
    {
        class UserDefinedWeldBuilder;
    }
    namespace Weld
    {
        class WeldAdvisorBuilder;
    }
    namespace Weld
    {
        class WeldBeadBuilder;
    }
    namespace Weld
    {
        class WeldFillBuilder;
    }
    namespace Weld
    {
        class WeldImportBuilder;
    }
    namespace Weld
    {
        class WeldJoint;
    }
    namespace Weld
    {
        class WeldJointBuilder;
    }
    namespace Weld
    {
        class WeldLabelBuilder;
    }
    namespace Weld
    {
        class WeldObjectBuilder;
    }
    namespace Weld
    {
        class WeldPointBuilder;
    }
    namespace Weld
    {
        class WeldPointExitBuilder;
    }
    namespace Weld
    {
        class WeldPreferenceBuilder;
    }
    namespace Weld
    {
        class WeldManagerImpl;
        /** Manages weld features and assistant tools.  <br> To obtain an instance of this class, refer to @link Features::FeatureCollection  Features::FeatureCollection @endlink  <br> 
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  WeldManager
        {
            private: WeldManagerImpl * m_weldmanager_impl;
            private: NXOpen::Features::FeatureCollection* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit WeldManager(NXOpen::Features::FeatureCollection *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~WeldManager();
            /** Creates a @link Weld::GrooveBuilder Weld::GrooveBuilder@endlink  object.  @return  WeldGroove feature builder
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::GrooveBuilder * CreateWeldGrooveBuilder
            (
                NXOpen::Features::Feature * weldGroove /** Groove Weld to be edited, if NULL then create a new one */
            );
            /** Creates a @link Weld::WeldPointBuilder Weld::WeldPointBuilder@endlink  object.  @return  WeldPoint feature builder
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldPointBuilder * CreateWeldPointBuilder
            (
                NXOpen::Features::Feature * weldPoint /** @link WeldPointBuilder WeldPointBuilder@endlink 
                                                                          to be edited, if NULL then create a new one */
            );
            /** Creates a @link Weld::WeldImportBuilder Weld::WeldImportBuilder@endlink  object.  @return  Import weld builder 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::WeldImportBuilder * CreateImportBuilder
            (
            );
            /** Creates a @link Weld::WeldJointBuilder Weld::WeldJointBuilder@endlink   @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: NXOpen::Weld::WeldJointBuilder * CreateJointBuilder
            (
                NXOpen::Weld::WeldJoint * weldJoint /** @link Weld::WeldJoint Weld::WeldJoint@endlink  to be edited */
            );
            /** Creates a @link Weld::JointExitBuilder Weld::JointExitBuilder@endlink   @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: NXOpen::Weld::JointExitBuilder * CreateJointExitBuilder
            (
                NXOpen::Weld::WeldJoint * weldJoint /** @link Weld::WeldJoint Weld::WeldJoint@endlink  to be edited */
            );
            /** Creates a @link Weld::JointExitBuilder Weld::JointExitBuilder@endlink  using the curve of a @link Weld::WeldJoint Weld::WeldJoint@endlink   @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: NXOpen::Weld::JointExitBuilder * CreateJointExitBuilderCurve
            (
                NXOpen::Curve * curve /** curve */ 
            );
            /** Creates a @link Weld::ExportWeldBuilder Weld::ExportWeldBuilder@endlink  object.  @return  ExportWeld assistant builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::ExportWeldBuilder * CreateExportWeldBuilder
            (
            );
            /** Creates a @link Weld::EdgePrepValuesBuilder Weld::EdgePrepValuesBuilder@endlink  object.  @return  Edge Prep Values builder
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::EdgePrepValuesBuilder * CreateEdgePrepValuesBuilder
            (
            );
            /** Creates a @link Weld::AutoPointBuilder Weld::AutoPointBuilder@endlink  object.  @return  AutoPoint assistant builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::AutoPointBuilder * CreateAutoPointBuilder
            (
                NXOpen::Features::Feature * unused /** Builder only creates */
            );
            /** Creates a @link Weld::WeldPreferenceBuilder Weld::WeldPreferenceBuilder@endlink  object.  @return  WeldPref assistant builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldPreferenceBuilder * CreatePreferenceBuilder
            (
            );
            /** Creates a @link Weld::UserDefinedWeldBuilder Weld::UserDefinedWeldBuilder@endlink   @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::UserDefinedWeldBuilder * CreateUserDefinedWeldBuilder
            (
                NXOpen::Features::Feature * featureSet /** Builder only creates */
            );
            /** Creates a @link Weld::CharacteristicsBuilder Weld::CharacteristicsBuilder@endlink , used to specify
                   welding characteristics for any welding feature.  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD") */
            public: NXOpen::Weld::CharacteristicsBuilder * CreateCharacteristicsBuilder
            (
                NXOpen::NXObject * object /** object having attributes to be edited. */,
                int weldType /** type of weld feature being created/edited, see uf_weld_types.h. */
            );
            /** Creates a @link Weld::WeldAdvisorBuilder Weld::WeldAdvisorBuilder@endlink  object.  @return  Weld Advisor builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldAdvisorBuilder * CreateWeldAdvisorBuilder
            (
            );
            /** Creates a @link Weld::WeldFillBuilder Weld::WeldFillBuilder@endlink , used to create or edit
                a @link Weld::Fill Weld::Fill@endlink  feature.  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldFillBuilder * CreateFillBuilder
            (
                NXOpen::Weld::Fill * fillFeature /** @link Weld::Fill Weld::Fill@endlink  to be edited */
            );
            /** Creates a @link Weld::WeldBeadBuilder Weld::WeldBeadBuilder@endlink  object.  @return  
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldBeadBuilder * CreateWeldBeadBuilder
            (
                NXOpen::Features::Feature * beadFeature /** Weld Bead to be edited */
            );
            /** Creates a @link Weld::EasyPatternBuilder Weld::EasyPatternBuilder@endlink  object.  @return  EasyPattern assistant builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::EasyPatternBuilder * CreateEasyPatternBuilder
            (
                NXOpen::Features::Feature * patternFeatureSet /** Pattern feature set.  */
            );
            /** Creates a @link Weld::PlugSlotBuilder Weld::PlugSlotBuilder@endlink  object.  @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::PlugSlotBuilder * CreatePlugSlotBuilder
            (
                NXOpen::Features::Feature * feature /** Weld PlugSlott to be edited */
            );
            /** Creates a @link Weld::FilletBuilder Weld::FilletBuilder@endlink  object.  @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::FilletBuilder * CreateFilletBuilder
            (
                NXOpen::Features::Feature * feature /** Weld Fillet to be edited */
            );
            /** Creates a @link Weld::EdgePrepBuilder Weld::EdgePrepBuilder@endlink  object.  @return  
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: NXOpen::Weld::EdgePrepBuilder * CreateEdgePrepBuilder
            (
                NXOpen::Weld::EdgePrep * edgePrepFeature /** Weld Edge Prep Feature to be edited */
            );
            /** Creates a @link Weld::AutoWeldSymbolsBuilder Weld::AutoWeldSymbolsBuilder@endlink  object.  @return  Auto Weld Symbol assistant builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD") */
            public: NXOpen::Weld::AutoWeldSymbolsBuilder * CreateAutoWeldSymbolsBuilder
            (
            );
            /** Creates a @link Weld::WeldObjectBuilder Weld::WeldObjectBuilder@endlink  object.  @return  
             <br>  Created in NX8.0.1.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldObjectBuilder * CreateWeldObjectBuilder
            (
            );
            /** Creates a @link Weld::ExportWeldJointBuilder Weld::ExportWeldJointBuilder@endlink  object.  @return  Export Weld Joint builder
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : structure_weld ("STRUCTURE WELD") */
            public: NXOpen::Weld::ExportWeldJointBuilder * CreateExportWeldJointBuilder
            (
            );
            /** Creates a @link Weld::DatumSurfaceBuilder Weld::DatumSurfaceBuilder@endlink  object.  @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::DatumSurfaceBuilder * CreateDatumSurfaceBuilder
            (
                NXOpen::Weld::DatumSurface * feature /** @link Weld::DatumSurface Weld::DatumSurface@endlink  to be edited */
            );
            /** Creates a @link Weld::DatumPinBuilder Weld::DatumPinBuilder@endlink  object.  @return  
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::DatumPinBuilder * CreateDatumPinBuilder
            (
                NXOpen::Weld::DatumPin * feature /** @link Weld::DatumPin Weld::DatumPin@endlink  to be edited */
            );
            /** The welding annotation to edit, otherwise if NULL, then create a new one  @return  weld label builder
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD") */
            public: NXOpen::Weld::WeldLabelBuilder * CreateWeldLabelBuilder
            (
                NXOpen::Annotations::Annotation * annotation /** The Welding annotation. */
            );
            /** Creates a @link Weld::WeldPointExitBuilder Weld::WeldPointExitBuilder@endlink  object.  @return  
             <br>  Created in NX8.0.2.  <br>  
             <br> License requirements : ugweld ("UG WELD") */
            public: NXOpen::Weld::WeldPointExitBuilder * CreateWeldPointExitBuilder
            (
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
