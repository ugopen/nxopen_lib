#ifndef NXOpen_CAE_POSTANNOTATION_HXX_INCLUDED
#define NXOpen_CAE_POSTANNOTATION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_PostAnnotation.ja
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
#include <NXOpen/TransientObject.hxx>
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
        class PostAnnotation;
    }
    class NXColor;
    namespace CAE
    {
        class PostAnnotationImpl;
        /**  @brief  Controls appearance of a annoation object in a postview. User must call @link CAE::PostAnnotation::Draw CAE::PostAnnotation::Draw@endlink   
                          to make changes visible.
                

          <br> To obtain an instance of this class use CAE::Post  <br> 
         <br>  Created in NX8.5.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  PostAnnotation : public NXOpen::TransientObject
        {
            /** Annotation styles */
            public: enum Style
            {
                StyleBox/** box */ ,
                StyleBoxWithLeader/** box with leader */ ,
                StyleBoxAtModelLocation/** box at model location */ 
            };

            /** Annotation value type */
            public: enum ValueType
            {
                ValueTypeNone/** none */ ,
                ValueTypeResultAndEntity/** result and entity */ ,
                ValueTypeResult/** result */ ,
                ValueTypeEntity/** entity */ 
            };

            /** Annotation text alignment */
            public: enum TextAlignment
            {
                TextAlignmentLeft/** left */ ,
                TextAlignmentRight/** right */ ,
                TextAlignmentCenter/** center */ 
            };

            private: PostAnnotationImpl * m_postannotation_impl;
            /// \cond NX_NO_DOC 
            public: explicit PostAnnotation(void *ptr);
            /// \endcond 
            /** Frees the object from memory.  After this method is called,
                        it is illegal to use the object. In .NET, this method is automatically
                        called when the object is deleted by the garbage collector. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: virtual ~PostAnnotation();
            /** Deletes the annotation. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void Delete
            (
            );
            /** Draw annotation object on graphics screen. If NX is in batch mode, nothing happens.
                        After setting paramters user has to call draw to reflect changes.
                    
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void Draw
            (
            );
            /** Show/Hide annotation object on graphics screen. If NX is in batch mode, nothing happens 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void Show
            (
                bool show /** true will show annotation, false will hide*/
            );
            /**Returns  the annotation name
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXString Name
            (
            );
            /**Sets  the annotation name
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the annotation name
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            void SetName
            (
                const char * name /** name */ 
            );
            /**Returns  the annotation style
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::PostAnnotation::Style DisplayStyle
            (
            );
            /**Sets  the annotation style
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetDisplayStyle
            (
                NXOpen::CAE::PostAnnotation::Style style /** style */ 
            );
            /**Returns  the annotation value type
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::PostAnnotation::ValueType DisplayValueType
            (
            );
            /**Sets  the annotation value type
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetDisplayValueType
            (
                NXOpen::CAE::PostAnnotation::ValueType valueType /** value type */ 
            );
            /** Put the user text in each box
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetUserText
            (
                const std::vector<NXString> & usertext /** usertext */ 
            );
            /** Ask the user text in each box
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void GetUserText
            (
                std::vector<NXString> & usertext /** usertext */ 
            );
            /**Returns  the box drawing
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool DrawBox
            (
            );
            /**Sets  the box drawing
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetDrawBox
            (
                bool drawBox /** draw box */ 
            );
            /**Returns  the box filling
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool BoxFill
            (
            );
            /**Sets  the box filling
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetBoxFill
            (
                bool boxFill /** box fill */ 
            );
            /**Returns  the box tranluceny
             <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::CAE::PostAnnotation::BoxTranslucency NXOpen::CAE::PostAnnotation::BoxTranslucency@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  Use NXOpen::CAE::PostAnnotation::BoxTranslucency instead.") bool BoxTranluceny
            (
            );
            /**Sets  the box tranluceny
             <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::CAE::PostAnnotation::SetBoxTranslucency NXOpen::CAE::PostAnnotation::SetBoxTranslucency@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  Use NXOpen::CAE::PostAnnotation::SetBoxTranslucency instead.") void SetBoxTranluceny
            (
                bool boxTranluceny /** box tranluceny */ 
            );
            /**Returns  the box color
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::NXColor * BoxColor
            (
            );
            /**Sets  the box color
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetBoxColor
            (
                NXOpen::NXColor * boxColor /** box color */ 
            );
            /**Returns  the text color
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::NXColor * TextColor
            (
            );
            /**Sets  the text color
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetTextColor
            (
                NXOpen::NXColor * textColor /** text color */ 
            );
            /**Returns  the text alignment
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: NXOpen::CAE::PostAnnotation::TextAlignment BoxTextAlignment
            (
            );
            /**Sets  the text alignment
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetBoxTextAlignment
            (
                NXOpen::CAE::PostAnnotation::TextAlignment boxTextAlignment /** box text alignment */ 
            );
            /**Returns  the box translucency
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool BoxTranslucency
            (
            );
            /**Sets  the box translucency
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetBoxTranslucency
            (
                bool boxTranslucency /** box translucency */ 
            );
            /**Returns  the display unit option
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: bool DisplayUnit
            (
            );
            /**Sets  the display unit option
             <br>  Created in NX1953.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetDisplayUnit
            (
                bool displayUnit /** displayunit */ 
            );
            /** Updates the annotation created with group reference after the entities in the group are modified.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void UpdateAnnotation
            (
            );
            /** Set annotation refrence group name. Clears all existing entities in the annotation.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            public: void SetReferenceGroup
            (
                const NXString & newRefgroupName /** new refgroup name */ 
            );
            /** Set annotation refrence group name. Clears all existing entities in the annotation.
                    
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") OR sc_results_viewer (" Simcenter Results Viewer") */
            void SetReferenceGroup
            (
                const char * newRefgroupName /** new refgroup name */ 
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
