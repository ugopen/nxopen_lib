#ifndef NXOpen_CAE_ACOUSTICSANDVIBRATIONMANAGER_HXX_INCLUDED
#define NXOpen_CAE_ACOUSTICSANDVIBRATIONMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AcousticsAndVibrationManager.ja
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
        class AcousticsAndVibrationManager;
    }
    namespace CAE
    {
        class SimSimulation;
    }
    namespace CAE
    {
        class AcousticsAndVibrationLoadIdentificationSolutionCollection;
    }
    namespace CAE
    {
        class AcousticsAndVibrationPcaSolutionCollection;
    }
    namespace CAE
    {
        class AcousticsAndVibrationPotentialFlowSolutionCollection;
    }
    namespace CAE
    {
        class AcousticsAndVibrationRandomVatvResponseSolutionCollection;
    }
    namespace CAE
    {
        class AcousticsAndVibrationManagerImpl;
        /** Contains collections of different types of Acoustics And Vibration solutions  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::SimSimulation  NXOpen::CAE::SimSimulation @endlink  <br> 
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  AcousticsAndVibrationManager
        {
            private: AcousticsAndVibrationManagerImpl * m_acousticsandvibrationmanager_impl;
            private: NXOpen::CAE::SimSimulation* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit AcousticsAndVibrationManager(NXOpen::CAE::SimSimulation *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~AcousticsAndVibrationManager();


            /** Returns the Random VATV Response solution collection belonging to this sim part. 
             <br>  Created in NX1872.0.0.  <br>  
            */
            public: NXOpen::CAE::AcousticsAndVibrationRandomVatvResponseSolutionCollection *RandomVatvResponseSolutions();
            /** Returns Load Identification solution collection belonging to this sim part. 
             <br>  Created in NX1872.0.0.  <br>  
            */
            public: NXOpen::CAE::AcousticsAndVibrationLoadIdentificationSolutionCollection *LoadIdentificationSolutions();
            /** Returns Potential Flow solution collection belonging to this sim part. 
             <br>  Created in NX1926.0.0.  <br>  
            */
            public: NXOpen::CAE::AcousticsAndVibrationPotentialFlowSolutionCollection *PotentialFlowSolutions();
            /** Returns Principal Component Analysis solution collection belonging to this sim part. 
             <br>  Created in NX1953.0.0.  <br>  
            */
            public: NXOpen::CAE::AcousticsAndVibrationPcaSolutionCollection *PcaSolutions();
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