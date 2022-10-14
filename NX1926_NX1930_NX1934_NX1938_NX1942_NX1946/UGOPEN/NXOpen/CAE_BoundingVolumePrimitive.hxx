#ifndef NXOpen_CAE_BOUNDINGVOLUMEPRIMITIVE_HXX_INCLUDED
#define NXOpen_CAE_BOUNDINGVOLUMEPRIMITIVE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_BoundingVolumePrimitive.ja
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
        class BoundingVolumePrimitive;
    }
    namespace CAE
    {
        /** Used to specify the containment for the Bounding Volume Primitive.*/
        enum CaeBoundingVolumePrimitiveContainment
        {
            CaeBoundingVolumePrimitiveContainmentInside/** completely inside the primitive */,
            CaeBoundingVolumePrimitiveContainmentInsideCrossing/** completely inside or partially inside the primitive */,
            CaeBoundingVolumePrimitiveContainmentOutside/** completely outside the primitive */,
            CaeBoundingVolumePrimitiveContainmentOutsideCrossing/** completely outside or partially outside the primitive */
        };

        /** the bounding volume creation method */
        enum CaeBoundingVolumePrimitiveType
        {
            CaeBoundingVolumePrimitiveTypeBoxCsysAndEdgeLengths/** box csys and edge lengths */ ,
            CaeBoundingVolumePrimitiveTypeBoxTwoDiagonalPoints/** box two diagonal points */ ,
            CaeBoundingVolumePrimitiveTypeCylinderCsysDiameterAndHeight/** cylinder csys diameter and height */ ,
            CaeBoundingVolumePrimitiveTypeCylinderTwoPointsAndDiameter/** cylinder two points and diameter */ ,
            CaeBoundingVolumePrimitiveTypeSphereOriginAndDiameter/** sphere origin and diameter */ ,
            CaeBoundingVolumePrimitiveTypeArbitraryVolume/** arbitrary volume */ 
        };

    }
    namespace CAE
    {
        class _BoundingVolumePrimitiveBuilder;
        class BoundingVolumePrimitiveImpl;
        /**
             Represents a Bounding Volume Primitive class @link NXOpen::CAE::BoundingVolumePrimitive NXOpen::CAE::BoundingVolumePrimitive@endlink . 
             <br> This is a sub object  <br> 
         <br>  Created in NX12.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  BoundingVolumePrimitive : public NXOpen::TaggedObject
        {
            private: BoundingVolumePrimitiveImpl * m_boundingvolumeprimitive_impl;
            private: friend class  _BoundingVolumePrimitiveBuilder;
            protected: BoundingVolumePrimitive();
            public: ~BoundingVolumePrimitive();
            /**Returns the contaiment for the Bounding Volume Primitive.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CaeBoundingVolumePrimitiveContainment Containment
            (
            );
            /**Sets the contaiment for the Bounding Volume Primitive.
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetContainment
            (
                NXOpen::CAE::CaeBoundingVolumePrimitiveContainment containment /** containment */ 
            );
            /**Gets the type for the Bounding Volume Primitive. @return  
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::CaeBoundingVolumePrimitiveType GetCreationMethod
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