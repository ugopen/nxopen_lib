#ifndef NXOpen_CAE_MESHPOINT_HXX_INCLUDED
#define NXOpen_CAE_MESHPOINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MeshPoint.ja
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
#include <NXOpen/ILocation.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/IOrientation.hxx>
#include <NXOpen/SmartObject.hxx>
#include <NXOpen/ugmath.hxx>
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
        class MeshPoint;
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class ILocation;
    class INXObject;
    class IOrientation;
    class SmartObject;
    namespace CAE
    {
        class _MeshPointBuilder;
        class MeshPointImpl;
        /**
         Represents a smart @link MeshPoint MeshPoint@endlink . 
         <br> To obtain an instance of this object use on of the creator in @link CAE::MeshPointCollection CAE::MeshPointCollection@endlink .  <br> 
         <br>  Created in NX5.0.2.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  MeshPoint : public SmartObject, public virtual IOrientation, public virtual ILocation
        {
            private: MeshPointImpl * m_meshpoint_impl;
            private: friend class  _MeshPointBuilder;
            protected: MeshPoint();
            public: ~MeshPoint();
            /**Returns  the coordinates of the point 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d Coordinates
            (
            );
            /** Sets the coordinates of the point 
             <br>  Created in NX5.0.2.  <br>  
             <br> License requirements : None */
            public: void SetCoordinates
            (
                const NXOpen::Point3d & coordinates /** coordinates */ 
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