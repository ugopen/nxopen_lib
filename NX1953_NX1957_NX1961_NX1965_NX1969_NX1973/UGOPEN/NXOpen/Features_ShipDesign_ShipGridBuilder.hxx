#ifndef NXOpen_FEATURES_SHIPDESIGN_SHIPGRIDBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_SHIPGRIDBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_ShipGridBuilder.ja
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
#include <NXOpen/Builder.hxx>
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
            class ShipGridBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace ShipDesign
        {
            class _ShipGridBuilderBuilder;
            class ShipGridBuilderImpl;
            /**
                    This class is used to specify the Grid part for the Ship Structures application when there are multiple
                    Grid Part.
                 <br> To create a new instance of this class, use @link NXOpen::Features::ShipCollection::CreateShipGridBuilder  NXOpen::Features::ShipCollection::CreateShipGridBuilder @endlink  <br> 
             <br>  Created in NX1953.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ShipGridBuilder : public NXOpen::Builder
            {
                private: ShipGridBuilderImpl * m_shipgridbuilder_impl;
                private: friend class  _ShipGridBuilderBuilder;
                protected: ShipGridBuilder();
                public: ~ShipGridBuilder();
                /**Returns 
                            the part to which are added newly created Ship objects
                        
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString GridPart
                (
                );
                /**Sets 
                            the part to which are added newly created Ship objects
                        
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                public: void SetGridPart
                (
                    const NXString & gridPart /** gridpart */ 
                );
                /**Sets 
                            the part to which are added newly created Ship objects
                        
                 <br>  Created in NX1953.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") */
                void SetGridPart
                (
                    const char * gridPart /** gridpart */ 
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
