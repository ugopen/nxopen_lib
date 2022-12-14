#ifndef NXOpen_MFGVIEWMAKER_CLONEMODELVIEWSBUILDER_HXX_INCLUDED
#define NXOpen_MFGVIEWMAKER_CLONEMODELVIEWSBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MFGViewMaker_CloneModelViewsBuilder.ja
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
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libmfgviewmakeropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace MFGViewMaker
    {
        class CloneModelViewsBuilder;
    }
    class Builder;
    class ModelingView;
    class ModelingViewList;
    class TaggedObject;
    namespace MFGViewMaker
    {
        class _CloneModelViewsBuilderBuilder;
        class CloneModelViewsBuilderImpl;
        /** Clone Model Views  <br> To create a new instance of this class, use @link NXOpen::MFGViewMaker::MFGViewMakerManager::CreateCloneModelViewsBuilder  NXOpen::MFGViewMaker::MFGViewMakerManager::CreateCloneModelViewsBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        CloneWithTrace </td> <td> 
         
        1 </td> </tr> 

        </table>  

         <br>  Created in NX11.0.1.  <br>  
        */
        class MFGVIEWMAKEROPENCPPEXPORT  CloneModelViewsBuilder : public NXOpen::Builder
        {
            private: CloneModelViewsBuilderImpl * m_clonemodelviewsbuilder_impl;
            private: friend class  _CloneModelViewsBuilderBuilder;
            protected: CloneModelViewsBuilder();
            public: ~CloneModelViewsBuilder();
            /**Returns  a Source Part 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::TaggedObject * SourcePart
            (
            );
            /**Sets  a Source Part 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetSourcePart
            (
                NXOpen::TaggedObject * sourcePart /** sourcepart */ 
            );
            /** Returns the non-predefined model views of the source part  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: std::vector<NXOpen::ModelingView *> GetModelViewsOfSourcePart
            (
                std::vector<NXString> & viewNames /** viewnames */ 
            );
            /**Returns  the selected model views 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::ModelingViewList * SelectedModelViews
            (
            );
            /** Add model view to selected model view list 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void AddModelViewToSelection
            (
                NXOpen::ModelingView * modelView /** modelview */ 
            );
            /** Add model views to selected model view list  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void AddModelViewsToSelection
            (
                const std::vector<NXOpen::ModelingView *> & modelView /** modelview */ 
            );
            /** Clears the seleced model views list  
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void ClearSelectedModelViews
            (
            );
            /**Returns  a Target Part 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::TaggedObject * TargetPart
            (
            );
            /**Sets  a Target Part 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetTargetPart
            (
                NXOpen::TaggedObject * targetPart /** targetpart */ 
            );
            /**Returns  the Keep reference to source 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: bool CloneWithTrace
            (
            );
            /**Sets  the Keep reference to source 
             <br>  Created in NX11.0.1.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetCloneWithTrace
            (
                bool cloneWithTrace /** clonewithtrace */ 
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
