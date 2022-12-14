#ifndef NXOpen_ANNOTATIONS_IRECTANGULARTARGET_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_IRECTANGULARTARGET_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_IRectangularTarget.ja
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
#include <NXOpen/Annotations.hxx>
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
        class IRectangularTarget;
    }
    class Expression;
    class INXObject;
    namespace Annotations
    {
        /** Represents interface class for a rectangular datum target 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  IRectangularTarget : public virtual NXOpen::INXObject
        {
            public: virtual ~IRectangularTarget() {}
            /** Returns the target length  @return  Length data 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::Annotations::Value GetLength
            (
            ) = 0;
            /** Sets the target length.
                        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetLength
            (
                const NXOpen::Annotations::Value & length /** New length data */
            ) = 0;
            /** Returns the target width  @return  Width data 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: virtual NXOpen::Annotations::Value GetWidth
            (
            ) = 0;
            /** Sets the target width.
                        NOTE: This method should not be used to edit a read-only object such as a Mirrored PMI object.
                              If it is, the changes will be overridden when the part is updated. 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") */
            public: virtual void SetWidth
            (
                const NXOpen::Annotations::Value & width /** New width data */
            ) = 0;
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
