#ifndef NXOpen_FEATURES_SHIPDESIGN_HULLBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_HULLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_HullBuilder.ja
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
#include <NXOpen/Features_ShipDesign_PlateSystemBuilder.hxx>
#include <NXOpen/Features_ShipDesign_HullBuilder.hxx>
#include <NXOpen/ScCollector.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace ShipDesign
        {
            class HullBuilder;
        }
    }
    namespace Features
    {
        namespace ShipDesign
        {
            class PlateSystemBuilder;
        }
    }
    class ScCollector;
    class SelectBody;
    namespace Features
    {
        namespace ShipDesign
        {
            class _HullBuilderBuilder;
            class HullBuilderImpl;
            /**
                This class is used to create or edit a @link Features::ShipDesign::Hull Features::ShipDesign::Hull@endlink  feature.
                 <br> To create a new instance of this class, use @link Features::ShipCollection::CreateHullBuilder  Features::ShipCollection::CreateHullBuilder @endlink  <br> 
            Default values.
            <table border="1"> 
             
            <tr><th> 
            Property</th>  <th> 
            Value</th> </tr>
            <tr><td> 
             
            Offset.Value </td> <td> 
             
            0 (millimeters part), 0 (inches part) </td> </tr> 

            <tr><td> 
             
            Primary </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            PrimaryOnReference </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            Secondary1 </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            Secondary1OnReference </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            Secondary2 </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            <tr><td> 
             
            Secondary2OnReference </td> <td> 
             
            FwdPortToInUp </td> </tr> 

            </table>  

             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  HullBuilder : public Features::ShipDesign::PlateSystemBuilder
            {
                /** 
                        Indicates the method that is being used to define the mold face of the hull. 
                        */
                public: enum Types
                {
                    TypesSheetBody/** Mold face is being defined by a selected sheet body. */,
                    TypesFaces/** Mold face is being defined by selected faces. */
                };

                private: HullBuilderImpl * m_hullbuilder_impl;
                private: friend class  _HullBuilderBuilder;
                protected: HullBuilder();
                public: ~HullBuilder();
                /**Returns  the sheet body selected that defines the overall shape of the hull. This is only used if the 
                        @link Features::ShipDesign::HullBuilder::TypesSheetBody Features::ShipDesign::HullBuilder::TypesSheetBody@endlink  is set. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::SelectBody * MoldFaceSheet
                (
                );
                /**Returns  the faces selected that defines the overall shape of the hull. This is only used if the 
                        @link Features::ShipDesign::HullBuilder::TypesFaces Features::ShipDesign::HullBuilder::TypesFaces@endlink  is set. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::ScCollector * MoldFaces
                (
                );
                /**Returns  the method used to define the mold face of the hull. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::ShipDesign::HullBuilder::Types Type
                (
                );
                /**Sets  the method used to define the mold face of the hull. 
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") */
                public: void SetType
                (
                    NXOpen::Features::ShipDesign::HullBuilder::Types type /** type */ 
                );
            };
        }
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
