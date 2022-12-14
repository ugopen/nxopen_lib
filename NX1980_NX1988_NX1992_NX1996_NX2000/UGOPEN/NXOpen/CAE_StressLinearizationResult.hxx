#ifndef NXOpen_CAE_STRESSLINEARIZATIONRESULT_HXX_INCLUDED
#define NXOpen_CAE_STRESSLINEARIZATIONRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_StressLinearizationResult.ja
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
#include <NXOpen/TransientObject.hxx>
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
        class StressLinearizationResult;
    }
    namespace CAE
    {
        class StressLinearizationResultImpl;
        /** Represent a @link NXOpen::CAE::StressLinearizationResult NXOpen::CAE::StressLinearizationResult@endlink .  <br> An instance of this class is obtained through @link NXOpen::CAE::StressLinearization::ComputeAll NXOpen::CAE::StressLinearization::ComputeAll@endlink   <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  StressLinearizationResult : public NXOpen::TransientObject
        {
             /** Stress Linearization input and output entity*/
            public:
            struct StressState
            {
                public: /** Global Coordinates */NXOpen::Point3d Location;
                public: /** Local X Coordinate along SCL */double XLocal;
                public: /** xx */ double XX;
                public: /** yy */ double YY;
                public: /** zz */ double ZZ;
                public: /** xy */ double XY;
                public: /** yz */ double YZ;
                public: /** zx */ double ZX;
                public: /** sigma 11 */ double Sigma11;
                public: /** sigma 22 */ double Sigma22;
                public: /** sigma 33 */ double Sigma33;
                public: /** maxshear */ double MaxShear;
                public: /** intensity */ double Intensity;
                public: /** vonmises */ double VonMises;
                public: StressState() :
                    Location(),
                    XLocal(),
                    XX(),
                    YY(),
                    ZZ(),
                    XY(),
                    YZ(),
                    ZX(),
                    Sigma11(),
                    Sigma22(),
                    Sigma33(),
                    MaxShear(),
                    Intensity(),
                    VonMises()
                {
                }
                /** Constructor for the StressState struct. */ 
                public: StressState(const NXOpen::Point3d &locationInitial /** Global Coordinates */, 
                        double xLocalInitial /** Local X Coordinate along SCL */, 
                        double xXInitial /** xx */ , 
                        double yYInitial /** yy */ , 
                        double zZInitial /** zz */ , 
                        double xYInitial /** xy */ , 
                        double yZInitial /** yz */ , 
                        double zXInitial /** zx */ , 
                        double sigma11Initial /** sigma 11 */ , 
                        double sigma22Initial /** sigma 22 */ , 
                        double sigma33Initial /** sigma 33 */ , 
                        double maxShearInitial /** maxshear */ , 
                        double intensityInitial /** intensity */ , 
                        double vonMisesInitial /** vonmises */ ) :
                    Location(locationInitial),
                    XLocal(xLocalInitial),
                    XX(xXInitial),
                    YY(yYInitial),
                    ZZ(zZInitial),
                    XY(xYInitial),
                    YZ(yZInitial),
                    ZX(zXInitial),
                    Sigma11(sigma11Initial),
                    Sigma22(sigma22Initial),
                    Sigma33(sigma33Initial),
                    MaxShear(maxShearInitial),
                    Intensity(intensityInitial),
                    VonMises(vonMisesInitial)
                {
                }
            };

            private: StressLinearizationResultImpl * m_stresslinearizationresult_impl;
            /// \cond NX_NO_DOC 
            public: explicit StressLinearizationResult(void *ptr);
            /// \endcond 
            /**Returns  the iteration index 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: int IterationIndex
            (
            );
            /**Returns  the iteration name 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString IterationName
            (
            );
            /** Get the membrane stresses 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXOpen::CAE::StressLinearizationResult::StressState> GetMembrane
            (
            );
            /** Get the bending stresses 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXOpen::CAE::StressLinearizationResult::StressState> GetBending
            (
            );
            /** Get the membrane+bending stresses 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXOpen::CAE::StressLinearizationResult::StressState> GetMembranePlusBending
            (
            );
            /** Get the peak stresses 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXOpen::CAE::StressLinearizationResult::StressState> GetPeak
            (
            );
            /** Get the total stresses 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXOpen::CAE::StressLinearizationResult::StressState> GetTotal
            (
            );
            /** Dispose the StressLinearizationResult object 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~StressLinearizationResult();
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
