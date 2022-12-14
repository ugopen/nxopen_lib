#ifndef NXOpen_CAE_CLIPPINGPARAMETERS_HXX_INCLUDED
#define NXOpen_CAE_CLIPPINGPARAMETERS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ClippingParameters.ja
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
#include <NXOpen/CAE_ClippingParameters.hxx>
#include <NXOpen/CAE_Post.hxx>
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        class ClippingParameters;
    }
    namespace CAE
    {
        class _ClippingParametersBuilder;
        class ClippingParametersImpl;
        /** This class is worked as a packet of information that can be used to set the clipping parameters of a @link NXOpen::CAE::Post NXOpen::CAE::Post@endlink  object.
                <br/>Use @link NXOpen::CAE::ResultManager NXOpen::CAE::ResultManager@endlink  to create an @link NXOpen::CAE::ResultParameters NXOpen::CAE::ResultParameters@endlink 
                
                <br/>You can modifiy these values but validation of correctness will only be perfomed 
                when this object is set to a @link NXOpen::CAE::Post NXOpen::CAE::Post@endlink  object
             <br> To obtain an instance of this class use @link NXOpen::Session::ResultManager NXOpen::Session::ResultManager@endlink .  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  ClippingParameters : public NXOpen::TaggedObject
        {
            private: ClippingParametersImpl * m_clippingparameters_impl;
            private: friend class  _ClippingParametersBuilder;
            protected: ClippingParameters();
            public: ~ClippingParameters();
            /** Ask show outline  @return  
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool GetShowOutline
            (
            );
            /** Set show outline 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetShowOutline
            (
                bool showOutline /** showoutline */ 
            );
            /** Ask show clipped ghost  @return  
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool GetShowClippedGhost
            (
            );
            /** Set show clipped ghost 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetShowClippedGhost
            (
                bool showClippedGhost /** showclippedghost */ 
            );
            /** Ask clip value  @return  
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: double GetClipValue
            (
            );
            /** Set clip value 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetClipValue
            (
                double clipValue /** clipvalue */ 
            );
            /** Ask side  @return  
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Post::ClipSide GetSide
            (
            );
            /** Set side 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSide
            (
                NXOpen::CAE::Post::ClipSide side /** side */ 
            );
            /** Ask plane  @return  
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Post::ClipPlane GetPlane
            (
            );
            /** Set plane 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetPlane
            (
                NXOpen::CAE::Post::ClipPlane plane /** plane */ 
            );
            /** Ask coordinate system  @return  
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::CoordinateSystem GetCoordinateSystem
            (
            );
            /** Set coordinate system 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetCoordinateSystem
            (
                NXOpen::CAE::Result::CoordinateSystem coordinateSystem /** coordinatesystem */ 
            );
            /** Ask selected coordinate system 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void GetSelectedCoordinateSystem
            (
                NXOpen::CAE::Result::CoordinateSystemSource* source /** source */ ,
                int* id /** id */ 
            );
            /** Set selected coordinate system 
             <br>  Created in NX7.5.1.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetSelectedCoordinateSystem
            (
                NXOpen::CAE::Result::CoordinateSystemSource source /** source */ ,
                int id /** id */ 
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
