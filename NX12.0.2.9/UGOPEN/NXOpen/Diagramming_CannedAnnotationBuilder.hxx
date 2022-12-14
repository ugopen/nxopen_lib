#ifndef NXOpen_DIAGRAMMING_CANNEDANNOTATIONBUILDER_HXX_INCLUDED
#define NXOpen_DIAGRAMMING_CANNEDANNOTATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Diagramming_CannedAnnotationBuilder.ja
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
#include <NXOpen/Diagramming_Annotation.hxx>
#include <NXOpen/Diagramming_AnnotationBuilder.hxx>
#include <NXOpen/Diagramming_LeaderLineBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_diagramming_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Diagramming
    {
        class CannedAnnotationBuilder;
    }
    class Builder;
    namespace Diagramming
    {
        class Annotation;
    }
    namespace Diagramming
    {
        class AnnotationBuilder;
    }
    namespace Diagramming
    {
        class LeaderLineBuilder;
    }
    namespace Diagramming
    {
        class LeaderLineBuilderList;
    }
    namespace Diagramming
    {
        class _CannedAnnotationBuilderBuilder;
        class CannedAnnotationBuilderImpl;
        /**
            Represents a CannedAnnotationBuilder.
             <br> To create a new instance of this class, use @link NXOpen::Diagramming::DiagrammingManager::CreateCannedAnnotationBuilder  NXOpen::Diagramming::DiagrammingManager::CreateCannedAnnotationBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_DIAGRAMMINGEXPORT  CannedAnnotationBuilder : public NXOpen::Builder
        {
            /** Represents the inherit option.
                    
             <br>  Created in NX11.0.0.  <br>  
            */
            public: enum InheritOption
            {
                InheritOptionPreferences/** Setting the inherit from preferences option*/,
                InheritOptionCustomerDefaults/** Setting the inherit from customer defaults option*/,
                InheritOptionSelection/** Setting the inherit from selection option*/
            };

            private: CannedAnnotationBuilderImpl * m_cannedannotationbuilder_impl;
            private: friend class  _CannedAnnotationBuilderBuilder;
            protected: CannedAnnotationBuilder();
            public: ~CannedAnnotationBuilder();
            /**Returns  the annotation of this canned annotation. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::AnnotationBuilder * AnnotationBuilder
            (
            );
            /**Returns  the list of the leader lines. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::LeaderLineBuilderList * LeaderLines
            (
            );
            /** Create a new @link NXOpen::Diagramming::LeaderLineBuilder NXOpen::Diagramming::LeaderLineBuilder@endlink  builder.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Diagramming::LeaderLineBuilder * CreateLeaderLine
            (
            );
            /**Returns  the flag that indicates if the text box in the canned annotation is modifiable. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool TextBoxModifiable
            (
            );
            /**Sets  the flag that indicates if the text box in the canned annotation is modifiable. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTextBoxModifiable
            (
                bool isModifiable /** ismodifiable */ 
            );
            /**Returns  the indent value of the text box in the canned annotation. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: int TextBoxIndent
            (
            );
            /**Sets  the indent value of the text box in the canned annotation. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTextBoxIndent
            (
                int indent /** indent */ 
            );
            /**Returns  the flag that indicates if the text box in the canned annotation has shadow box. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool TextBoxShadowBox
            (
            );
            /**Sets  the flag that indicates if the text box in the canned annotation has shadow box. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTextBoxShadowBox
            (
                bool isShadowBox /** isshadowbox */ 
            );
            /** Inherit. 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : None */
            public: void Inherit
            (
                NXOpen::Diagramming::CannedAnnotationBuilder::InheritOption inheritOption /** inheritoption */ ,
                NXOpen::Diagramming::Annotation * annotation /** annotation */ 
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
