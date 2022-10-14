#ifndef NXOpen_MOTION_BODYCONTACTBUILDER_HXX_INCLUDED
#define NXOpen_MOTION_BODYCONTACTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_BodyContactBuilder.ja
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
#include <NXOpen/Builder.hxx>
#include <NXOpen/Motion_BodyContactBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Motion
    {
        class BodyContactBuilder;
    }
    class Builder;
    namespace Motion
    {
        class BodyContactAdams;
    }
    namespace Motion
    {
        class BodyContactRecurdyn;
    }
    class SelectNXObjectList;
    namespace Motion
    {
        class _BodyContactBuilderBuilder;
        /** Represents a @link Motion::BodyContactBuilder Motion::BodyContactBuilder@endlink 
              <br> To create a new instance of this class, use @link Motion::BodyContactCollection::CreateBodyContactBuilder Motion::BodyContactCollection::CreateBodyContactBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        AdamsParameters.CoulombFrictionOption </td> <td> 
         
        Off </td> </tr> 

        <tr><td> 
         
        AdamsParameters.DynamicCoefficient </td> <td> 
         
        0.2 </td> </tr> 

        <tr><td> 
         
        AdamsParameters.ForceExponent </td> <td> 
         
        2.0 </td> </tr> 

        <tr><td> 
         
        AdamsParameters.ForceModelType </td> <td> 
         
        Impact </td> </tr> 

        <tr><td> 
         
        AdamsParameters.FrictionVelocity </td> <td> 
         
        0.1 (millimeters part), 0.003937 (inches part) </td> </tr> 

        <tr><td> 
         
        AdamsParameters.MaterialDamping </td> <td> 
         
        10.0 (millimeters part), 57.0993 (inches part) </td> </tr> 

        <tr><td> 
         
        AdamsParameters.PenetrationDepth </td> <td> 
         
        0.01 (millimeters part), 0.0003937 (inches part) </td> </tr> 

        <tr><td> 
         
        AdamsParameters.RestitutionCoefficent </td> <td> 
         
        0.85 </td> </tr> 

        <tr><td> 
         
        AdamsParameters.StaticCoefficient </td> <td> 
         
        0.3 </td> </tr> 

        <tr><td> 
         
        AdamsParameters.StictionVelocity </td> <td> 
         
        0.01 (millimeters part), 0.0003937 (inches part) </td> </tr> 

        <tr><td> 
         
        AdamsParameters.Stiffness </td> <td> 
         
        100000.0 (millimeters part), 570993.142 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.BufferRadiusFactor </td> <td> 
         
        1.2 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.ContactTypeOption </td> <td> 
         
        Solid </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.CoulombFrictionOption </td> <td> 
         
        Off </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.DynamicCoefficient </td> <td> 
         
        0.2 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.FirstGeometryBoundingBufferLength </td> <td> 
         
        20 (millimeters part),  0.7874 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.FirstGeometryMaxFacetSizeFactor </td> <td> 
         
        2.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.FirstGeometryMaxFacetSizeFactorFlag </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.FirstGeometryMaximumPenetration </td> <td> 
         
        1.0 (millimeters part), 0.03937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.FirstGeometryPlaneToleranceFactor </td> <td> 
         
        5.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.FirstGeometryPlaneToleranceFactorSolidContact </td> <td> 
         
        3.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.ForceExponent </td> <td> 
         
        2.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.ForceModelType </td> <td> 
         
        Impact </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.FrictionVelocity </td> <td> 
         
        0.1 (millimeters part), 0.003937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.GlobalMaxPenetration </td> <td> 
         
        10.0 (millimeters part),  0.3937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.LocalMaxPenetration </td> <td> 
         
        0.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.MaterialDamping </td> <td> 
         
        10.0 (millimeters part),  57.0993 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.MaximumStepSizeFactor </td> <td> 
         
        2.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.PenetrationDepth </td> <td> 
         
        0.01 (millimeters part), 0.0003937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.ReboundDampingFactor </td> <td> 
         
        0.25 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.ReboundDampingFactorFlag </td> <td> 
         
        True </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.SecondGeometryBoundingBufferLength </td> <td> 
         
        20 (millimeters part),  0.7874 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.SecondGeometryMaxFacetSizeFactor </td> <td> 
         
        2.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.SecondGeometryMaxFacetSizeFactorFlag </td> <td> 
         
        False </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.SecondGeometryMaximumPenetration </td> <td> 
         
        1.0 (millimeters part), 0.03937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.SecondGeometryPlaneToleranceFactor </td> <td> 
         
        5.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.SecondGeometryPlaneToleranceFactorSolidContact </td> <td> 
         
        3.0 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.StaticCoefficient </td> <td> 
         
        0.3 </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.StictionVelocity </td> <td> 
         
        0.01 (millimeters part), 0.0003937 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.Stiffness </td> <td> 
         
        100000.0 (millimeters part), 570993.142 (inches part) </td> </tr> 

        <tr><td> 
         
        RecurdynParameters.SurfaceTypeOption </td> <td> 
         
        Faceted </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT BodyContactBuilder : public Builder
        {
            private: friend class  _BodyContactBuilderBuilder;
            protected: BodyContactBuilder();
            /**Returns  the selection of the first contact geometry  <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * FirstContactGeometry
            (
            );
            /**Returns  the selection of the second contact geometry  <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SecondContactGeometry
            (
            );
            /**Returns  the name  <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Returns the 3D BodyContact's subobject (the adams parameters)   <br> License requirements : None */
            public: NXOpen::Motion::BodyContactAdams * AdamsParameters
            (
            );
            /**Returns  the 3D BodyContact's subobject (the recurdyn parameters)  <br> License requirements : None */
            public: NXOpen::Motion::BodyContactRecurdyn * RecurdynParameters
            (
            );
            /**Returns  the contact's name. Deprecated, please use name attribute instead 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : None */
            public: NXString ContactName
            (
            );
            /**Sets  the contact's name. Deprecated, please use name attribute instead 
             @deprecated Deprecated in NX6 <br> 
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetContactName
            (
                const NXString & name /** name */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif