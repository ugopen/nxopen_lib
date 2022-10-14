#ifndef NXOpen_ANNOTATIONS_PMIFILTER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_PMIFILTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_PmiFilter.ja
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
#include <NXOpen/NXObject.hxx>
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
        class PmiFilter;
    }
    namespace Assemblies
    {
        class Component;
    }
    class NXObject;
    class View;
    namespace Annotations
    {
        class _PmiFilterBuilder;
        class PmiFilterImpl;
        /** Represents a base class for a PMI filter. 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  PmiFilter : public NXOpen::NXObject
        {
            /** Represents a type of PMI filter that can be created using the Part
                        Navigator. */
            public: enum FilterType
            {
                FilterTypeByType/** Specifies a PMI filter defined by a set of PMI types */,
                FilterTypeByView/** Specifies a PMI filter defined by a set of component model views */,
                FilterTypeByComponent/** Specifies a PMI filter defined by a set of components */
            };

            /** Specifies the type of component method used on the associated
                        components for display. */
            public: enum ComponentMethod
            {
                ComponentMethodSelected/** Specifies all components will be used */,
                ComponentMethodSelectedAndChildren/** Specifies all components and their children will be used */,
                ComponentMethodAll/** Specifies all components will be used */
            };

            private: PmiFilterImpl * m_pmifilter_impl;
            private: friend class  _PmiFilterBuilder;
            protected: PmiFilter();
            public: ~PmiFilter();
            /** Gets the type of PMI filter.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiFilter::FilterType GetFilterType
            (
            );
            /** Gets the components associated with the PMI filter.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Assemblies::Component *> GetComponents
            (
            );
            /** Sets the components associated with the PMI filter. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetComponents
            (
                const std::vector<NXOpen::Assemblies::Component *> & components /** components */ 
            );
            /** Gets the component method of the PMI filter.  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::PmiFilter::ComponentMethod GetComponentMethod
            (
            );
            /** Sets the component method of the PMI filter. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void SetComponentMethod
            (
                NXOpen::Annotations::PmiFilter::ComponentMethod componentMethod /** component method */ 
            );
            /** Applies the PMI filter to a view. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void ApplyToView
            (
                NXOpen::View * view /** Specifies the model view in which the filter is to be applied */
            );
            /** Removes a PMI filter from a view. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void RemoveFromView
            (
                NXOpen::View * view /** Specifies the model view in which the filter should be removed */
            );
            /** Gets the views where the PMI filter is applied  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::View *> GetAppliedViews
            (
            );
            /** Enables or disables the PMI filter in a given view 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void EnableInView
            (
                NXOpen::View * view /** Specifies the model view in which the filter should be enabled or disabled */,
                bool enabled /** Specifies the flag indicating that the filter should be enabled*/
            );
            /** Creates a copy of the PMI filter  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: NXOpen::Annotations::PmiFilter * Copy
            (
            );
            /** Determines if the PMI filter is enabled in the view  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool IsEnabled
            (
                NXOpen::View * view /** Specifies the model view to query */
            );
            /** Updates the PMI display in the associated views of the filter
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: void UpdatePmiDisplay
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