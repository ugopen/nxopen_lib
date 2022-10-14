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
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Drawings
    {
        class FlatPatternObject;
    }
    class CartesianCoordinateSystem;
    namespace Drawings
    {
        /** Provides an interface to the data available for flat pattern objects on drawing
                views. */
        class NXOPENCPPEXPORT FlatPatternObject : public TransientObject
        {
            public: explicit FlatPatternObject(void *ptr);
            /** Returns the point object containing the attributes the user put on the
                        original datum CSYS feature. This is the prototype object. The 
                        recommended procedure is to use the point to obtain attribute values 
                        and to use GetOrigin and GetDirections to obtain the geometrical data 
                        because of mappings to occurrences and to the drawing sheet.  @return   <br> License requirements : None */
            public: NXOpen::CartesianCoordinateSystem * GetFlatSolidObject
            (
            );
            /** Returns the origin of the marker object (the point on the drawing). 
                        The point has been transformed to drawing sheet coordinates.  @return   <br> License requirements : None */
            public: NXOpen::Point3d GetOrigin
            (
            );
            /** Returns the X and Y direction vectors that correspond to the flattened
                        datum csys feature object. The vectors have been transformed to
                        drawing sheet coordinates.  <br> License requirements : None */
            public: void GetDirections
            (
                NXOpen::Vector3d* xDirection /** X direction of simulated CSYS */,
                NXOpen::Vector3d* yDirection /** Y direction of simulated CSYS */
            );
            /** Frees the memory of the underlying class  <br> License requirements : None */
            public: virtual ~FlatPatternObject();
        };
    }
}
#undef EXPORTLIBRARY
#endif