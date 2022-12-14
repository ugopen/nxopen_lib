#ifndef NXOpen_WELD_WELDPMIBUILDER_HXX_INCLUDED
#define NXOpen_WELD_WELDPMIBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Weld_WeldPmiBuilder.ja
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
#include <NXOpen/Annotations_StyleBuilder.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_weld_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Weld
    {
        class WeldPmiBuilder;
    }
    namespace Annotations
    {
        class StyleBuilder;
    }
    class Builder;
    class CoordinateSystem;
    class SelectNXObjectList;
    namespace Weld
    {
        class _WeldPmiBuilderBuilder;
        class WeldPmiBuilderImpl;
        /** Create PMI symbols for multiple structure welds, this builder's Commit can produce more than one object, 
                the GetCommittedObjects can be used to get the objects and the order of GetCommittedObject's output array is stable.  <br> To create a new instance of this class, use @link NXOpen::Weld::WeldManager::CreateWeldPmiBuilder  NXOpen::Weld::WeldManager::CreateWeldPmiBuilder @endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        PlaneType </td> <td> 
         
        ModelView </td> </tr> 

        <tr><td> 
         
        SpaceFactor </td> <td> 
         
        1.0 </td> </tr> 

        </table>  

         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_WELDEXPORT  WeldPmiBuilder : public NXOpen::Builder
        {
            /** This represents the Orientation Plane Type. */
            public: enum OrientationPlaneType
            {
                OrientationPlaneTypeXYPlane/** xyplane */ ,
                OrientationPlaneTypeXZPlane/** xzplane */ ,
                OrientationPlaneTypeYZPlane/** yzplane */ ,
                OrientationPlaneTypeModelView/** model view */ ,
                OrientationPlaneTypeLastUserDefined/** last user defined */ ,
                OrientationPlaneTypeUserDefined/** user defined */ 
            };

            private: WeldPmiBuilderImpl * m_weldpmibuilder_impl;
            private: friend class  _WeldPmiBuilderBuilder;
            protected: WeldPmiBuilder();
            public: ~WeldPmiBuilder();
            /**Returns  the objects (either features or curves) that are used to create PMI symbols. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * Objects
            (
            );
            /**Returns  the plane type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Weld::WeldPmiBuilder::OrientationPlaneType PlaneType
            (
            );
            /**Sets  the plane type. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD") */
            public: void SetPlaneType
            (
                NXOpen::Weld::WeldPmiBuilder::OrientationPlaneType planeType /** planetype */ 
            );
            /**Returns  the user specified coordinate system. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CoordinateSystem * UserCoordinateSystem
            (
            );
            /**Sets  the user specified coordinate system. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD") */
            public: void SetUserCoordinateSystem
            (
                NXOpen::CoordinateSystem * userCsys /** usercsys */ 
            );
            /**Returns  the @link Annotations::StyleBuilder Annotations::StyleBuilder@endlink  for the annotation. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::StyleBuilder * Style
            (
            );
            /**Returns  the space factor. The value is greater than zero. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: double SpaceFactor
            (
            );
            /**Sets  the space factor. The value is greater than zero. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : ugweld ("UG WELD") OR structure_weld ("STRUCTURE WELD") */
            public: void SetSpaceFactor
            (
                double spaceFactor /** spacefactor */ 
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
