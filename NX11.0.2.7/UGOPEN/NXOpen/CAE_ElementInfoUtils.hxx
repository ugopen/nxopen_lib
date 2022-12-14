#ifndef NXOpen_CAE_ELEMENTINFOUTILS_HXX_INCLUDED
#define NXOpen_CAE_ELEMENTINFOUTILS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ElementInfoUtils.ja
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
#include <NXOpen/CAE_BeamElementInfoHandler.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class ElementInfoUtils;
    }
    namespace CAE
    {
        class NodeElementManager;
    }
    namespace CAE
    {
        class BeamElementInfoHandler;
    }
    namespace CAE
    {
        class FEElement;
    }
    class CoordinateSystem;
    namespace CAE
    {
        class ElementInfoUtilsImpl;
        /**
            Represents a system to query information about FE-based elements
             <br> To obtain an instance of this class, refer to @link NXOpen::CAE::NodeElementManager  NXOpen::CAE::NodeElementManager @endlink  <br> 
         <br>  Created in NX11.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ElementInfoUtils
        {
            private: ElementInfoUtilsImpl * m_elementinfoutils_impl;
            private: NXOpen::CAE::NodeElementManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit ElementInfoUtils(NXOpen::CAE::NodeElementManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~ElementInfoUtils();
            /** Returns the centroids of 2D and 3d finite elements in absolute or reference coordinate system.
                    Use a tag of NULL for coordinateSystem to indicate the absolute coordinate system.
                    It will fail if given wrong type of elements  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::Point3d> Ask2d3dElementCentroids
            (
                const std::vector<NXOpen::CAE::FEElement *> & elements /** elements */ ,
                NXOpen::CoordinateSystem * coordinateSystem /** coordinatesystem */ 
            );
            /** Returns the areas of the 2D finite elements.
                    It will fail if given wrong type of elements  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<double> Ask2dElementAreas
            (
                const std::vector<NXOpen::CAE::FEElement *> & elements /** elements */ 
            );
            /** Returns the normals of the 2D finite elements.
                    It will fail if given wrong type of elements  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<NXOpen::Vector3d> Ask2dElementNormals
            (
                const std::vector<NXOpen::CAE::FEElement *> & elements /** elements */ 
            );
            /** Returns the volumes of the 3D finite elements.
                    It will fail if given wrong type of elements  @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: std::vector<double> Ask3dElementVolumes
            (
                const std::vector<NXOpen::CAE::FEElement *> & elements /** elements */ 
            );
            /** Returns a @link  NXOpen::CAE::BeamElementInfoHandler   NXOpen::CAE::BeamElementInfoHandler @endlink   @return  
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::BeamElementInfoHandler * CreateBeamElementInfoHandler
            (
            );
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
