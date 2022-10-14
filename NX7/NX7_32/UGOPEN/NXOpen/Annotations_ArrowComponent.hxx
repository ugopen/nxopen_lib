#ifndef NXOpen_ANNOTATIONS_ARROWCOMPONENT_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ARROWCOMPONENT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_ArrowComponent.ja
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
#include <NXOpen/Annotations.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class ArrowComponent;
    }
    namespace Annotations
    {
    }
    namespace Annotations
    {
        /** Represents a single arrow in an annotation and can be 
                queried for information about that arrow.  This information 
                includes  the type of arrow, the origin in absolute coordinates, 
                and the arrow angle*/
        class NXOPENCPPEXPORT ArrowComponent : public TransientObject
        {
            public: explicit ArrowComponent(void *ptr);
            /** Free resources associated with the arrow component. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector.   <br> License requirements : None */
            public: virtual ~ArrowComponent();
            /**Returns  the arrow type. <br> License requirements : None */
            public: NXOpen::Annotations::ArrowheadType Type
            (
            );
            /**Returns  the arrow origin in absolute coordinates.
                    If the annotation is on a drawing, origin is returned 
                    in drawing space. If the annotation is on the model,
                    origin is returned in model space.  <br> License requirements : None */
            public: NXOpen::Point3d Origin
            (
            );
            /**Returns  the arrow angle. <br> License requirements : None */
            public: double ArrowAngle
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif