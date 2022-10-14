#ifndef NXOpen_ANNOTATIONS_PMISECTIONVIEWVIEWBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMISECTIONVIEWVIEWBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiSectionViewViewBuilder.ja
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
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class PmiSectionViewViewBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Annotations
    {
        class _PmiSectionViewViewBuilderBuilder;
        class PmiSectionViewViewBuilderImpl;
        /**
                Represents a NXOpen.Annotations.PmiSectionViewViewBuilder
            
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiSectionViewViewBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            private: PmiSectionViewViewBuilderImpl * m_pmisectionviewviewbuilder_impl;
            private: friend class  _PmiSectionViewViewBuilderBuilder;
            protected: PmiSectionViewViewBuilder();
            public: ~PmiSectionViewViewBuilder();
            /**Returns  the section name prefix label 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString SectionNamePrefix
            (
            );
            /**Sets  the section name prefix label 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSectionNamePrefix
            (
                const NXString & sectionNamePrefixLabel /** sectionnameprefixlabel */ 
            );
            /**Sets  the section name prefix label 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            void SetSectionNamePrefix
            (
                const char * sectionNamePrefixLabel /** sectionnameprefixlabel */ 
            );
            /**Returns  the associative plane 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool AssociativePlane
            (
            );
            /**Sets  the associative plane 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetAssociativePlane
            (
                bool associativePlane /** associativeplane */ 
            );
            /**Returns  the clip coplanar objects 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ClipCoplanarObjects
            (
            );
            /**Sets  the clip coplanar objects 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetClipCoplanarObjects
            (
                bool clipCoplanarObjects /** clipcoplanarobjects */ 
            );
            /**Returns  the clip wireframe objects 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool ClipWireframeObjects
            (
            );
            /**Sets  the clip wireframe objects 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetClipWireframeObjects
            (
                bool clipWireframeObjects /** clipwireframeobjects */ 
            );
            /**Returns  the assembly crosshatching 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool AssemblyCrosshatching
            (
            );
            /**Sets  the assembly crosshatching 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetAssemblyCrosshatching
            (
                bool assemblyCrosshatching /** assemblycrosshatching */ 
            );
            /**Returns  the restrict crosshatch angle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: bool RestrictCrosshatchAngle
            (
            );
            /**Sets  the restrict crosshatch angle 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetRestrictCrosshatchAngle
            (
                bool restrictCrosshatchAngle /** restrictcrosshatchangle */ 
            );
            /**Returns  the crosshatch adjacency tolerance 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: double CrosshatchAdjacencyTolerance
            (
            );
            /**Sets  the crosshatch adjacency tolerance 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetCrosshatchAdjacencyTolerance
            (
                double crosshatchAdjacencyTolerance /** crosshatchadjacencytolerance */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not yet implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
            (
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