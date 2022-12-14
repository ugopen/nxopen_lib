#ifndef NXOpen_DRAWINGS_FLATPATTERNOBJECT_HXX_INCLUDED
#define NXOpen_DRAWINGS_FLATPATTERNOBJECT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Drawings_FlatPatternObject.ja
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
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_drawings_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Drawings
    {
        class FlatPatternObject;
    }
    class CartesianCoordinateSystem;
    namespace Drawings
    {
        class FlatPatternObjectImpl;
        /** Provides an interface to the data available for flat pattern objects on drawing
                views. 
         <br>  Created in NX6.0.3.  <br>  
        */
        class NXOPENCPP_DRAWINGSEXPORT  FlatPatternObject : public NXOpen::TransientObject
        {
            private: FlatPatternObjectImpl * m_flatpatternobject_impl;
            /// \cond NX_NO_DOC 
            public: explicit FlatPatternObject(void *ptr);
            /// \endcond 
            /** Returns the point object containing the attributes the user put on the
                        original datum CSYS feature. This is the prototype object. The 
                        recommended procedure is to use the point to obtain attribute values 
                        and to use GetOrigin and GetDirections to obtain the geometrical data 
                        because of mappings to occurrences and to the drawing sheet.  @return  
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::CartesianCoordinateSystem * GetFlatSolidObject
            (
            );
            /** Returns the origin of the marker object (the point on the drawing). 
                        The point has been transformed to drawing sheet coordinates.  @return  
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: NXOpen::Point3d GetOrigin
            (
            );
            /** Returns the X and Y direction vectors that correspond to the flattened
                        datum csys feature object. The vectors have been transformed to
                        drawing sheet coordinates. 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: void GetDirections
            (
                NXOpen::Vector3d* xDirection /** X direction of simulated CSYS */,
                NXOpen::Vector3d* yDirection /** Y direction of simulated CSYS */
            );
            /** Frees the memory of the underlying class 
             <br>  Created in NX6.0.3.  <br>  
             <br> License requirements : None */
            public: virtual ~FlatPatternObject();
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
