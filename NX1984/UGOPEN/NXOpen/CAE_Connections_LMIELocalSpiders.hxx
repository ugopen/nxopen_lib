#ifndef NXOpen_CAE_CONNECTIONS_LMIELOCALSPIDERS_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_LMIELOCALSPIDERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_LMIELocalSpiders.ja
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
#include <NXOpen/CAE_Connections_LMIEPanelOptions.hxx>
#include <NXOpen/CAE_Connections_LMIERegionSelection.hxx>
#include <NXOpen/CAE_Connections_LMIERingOptions.hxx>
#include <NXOpen/CAE_Connections_LMIEError.hxx>
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
        namespace Connections
        {
            class LMIELocalSpiders;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LMIEError;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LMIEPanelOptions;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LMIERegionSelection;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LMIERingOptions;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class _LMIELocalSpidersBuilder;
            class LMIELocalSpidersImpl;
            /**  Mass definition.   <br> No creator  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  LMIELocalSpiders : public NXOpen::CAE::Connections::LMIEError
            {
                private: LMIELocalSpidersImpl * m_lmielocalspiders_impl;
                private: friend class  _LMIELocalSpidersBuilder;
                protected: LMIELocalSpiders();
                public: ~LMIELocalSpiders();
                /**Returns  the mass distribution type 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: double MaxSearchDistance
                (
                );
                /**Sets  the mass distribution type 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: void SetMaxSearchDistance
                (
                    double val /** Max search distance */
                );
                /**Returns  the region selection 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIERegionSelection * RegionSelection
                (
                );
                /**Sets  the region selection 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetRegionSelection
                (
                    NXOpen::CAE::Connections::LMIERegionSelection * opt /** Region selection */
                );
                /** Create a standalone region selection  @return  Region selection 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIERegionSelection * CreateRegionSelection
                (
                );
                /**Returns  the ring options 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIERingOptions * RingOptions
                (
                );
                /**Sets  the ring options 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetRingOptions
                (
                    NXOpen::CAE::Connections::LMIERingOptions * opt /** Ring options */
                );
                /** Create a standalone ring options  @return  Ring options 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIERingOptions * CreateRingOptions
                (
                );
                /**Returns  the panel options 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIEPanelOptions * PanelOptions
                (
                );
                /**Sets  the panel options 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void SetPanelOptions
                (
                    NXOpen::CAE::Connections::LMIEPanelOptions * opt /** Panel options */
                );
                /** Create a standalone panel options  @return  Panel options 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIEPanelOptions * CreatePanelOptions
                (
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