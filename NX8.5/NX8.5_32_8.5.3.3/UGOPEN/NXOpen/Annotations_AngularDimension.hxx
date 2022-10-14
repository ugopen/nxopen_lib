#ifndef NXOpen_ANNOTATIONS_ANGULARDIMENSION_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ANGULARDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_AngularDimension.ja
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
#include <NXOpen/Annotations_Dimension.hxx>
#include <NXOpen/Annotations_IAngularTolerance.hxx>
#include <NXOpen/Annotations_AngularTolerance.hxx>
#include <NXOpen/INXObject.hxx>
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
        class AngularDimension;
    }
    namespace Annotations
    {
        class AngularTolerance;
    }
    namespace Annotations
    {
        class Dimension;
    }
    namespace Annotations
    {
        class IAngularTolerance;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    namespace Annotations
    {
        class _AngularDimensionBuilder;
        class AngularDimensionImpl;
        /** Represents an angular dimension  <br> Abstract class  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  AngularDimension : public Annotations::Dimension, public virtual Annotations::IAngularTolerance
        {
            private: AngularDimensionImpl * m_angulardimension_impl;
            private: friend class  _AngularDimensionBuilder;
            protected: AngularDimension();
            public: ~AngularDimension();
            /** Returns the tolerance  @return  
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::Annotations::AngularTolerance * GetTolerance
            (
            );
            /** Sets the tolerance.
                        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: virtual void SetTolerance
            (
                NXOpen::Annotations::AngularTolerance * tolerances /** tolerances */ 
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