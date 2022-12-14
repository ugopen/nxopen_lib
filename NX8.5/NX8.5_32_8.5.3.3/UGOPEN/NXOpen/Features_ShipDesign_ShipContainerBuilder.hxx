#ifndef NXOpen_FEATURES_SHIPDESIGN_SHIPCONTAINERBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_SHIPDESIGN_SHIPCONTAINERBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_ShipDesign_ShipContainerBuilder.ja
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
#include <NXOpen/Features_ShipDesign_ShipContainerBuilder.hxx>
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
            class ShipContainerBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace ShipDesign
        {
            class _ShipContainerBuilderBuilder;
            class ShipContainerBuilderImpl;
            /**
                    This class is used to specify the "container" part for the Ship Structures application, i.e., that
                    part that should have newly created Ship Stiffeners, Plates, Standard Parts added to it as assembly
                    components. It also holds the "container" name which is used in the generation of Teamcenter Item IDs
                    for newly created components.
                 <br> To create a new instance of this class, use @link Features::ShipCollection::CreateShipContainerBuilder  Features::ShipCollection::CreateShipContainerBuilder @endlink  <br> 
             <br>  Created in NX8.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ShipContainerBuilder : public Builder
            {
                private: ShipContainerBuilderImpl * m_shipcontainerbuilder_impl;
                private: friend class  _ShipContainerBuilderBuilder;
                protected: ShipContainerBuilder();
                public: ~ShipContainerBuilder();
                /**Returns 
                            the part to which are added newly created Ship objects
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString ContainerPart
                (
                );
                /**Sets 
                            the part to which are added newly created Ship objects
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetContainerPart
                (
                    const NXString & containerPart /** containerpart */ 
                );
                /**Sets 
                            the part to which are added newly created Ship objects
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                void SetContainerPart
                (
                    const char * containerPart /** containerpart */ 
                );
                /**Returns 
                            the name used in generating Item IDs for newly created Ship objects
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString ContainerName
                (
                );
                /**Sets 
                            the name used in generating Item IDs for newly created Ship objects
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                public: void SetContainerName
                (
                    const NXString & containerName /** containername */ 
                );
                /**Sets 
                            the name used in generating Item IDs for newly created Ship objects
                        
                 <br>  Created in NX8.0.0.  <br>  
                 <br> License requirements : nx_ship_basic ("Ship Basic Design") OR nx_ship_detail ("Ship Detail Design") OR nx_ship_mfg_prep ("Ship Manufacturing") */
                void SetContainerName
                (
                    const char * containerName /** containername */ 
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
