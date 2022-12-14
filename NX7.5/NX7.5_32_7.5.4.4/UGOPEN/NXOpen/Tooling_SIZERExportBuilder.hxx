#ifndef NXOpen_TOOLING_SIZEREXPORTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_SIZEREXPORTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_SIZERExportBuilder.ja
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
#include <NXOpen/Tooling_SIZERExportBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class SIZERExportBuilder;
    }
    class Builder;
    namespace Motion
    {
        class Graph;
    }
    namespace Motion
    {
        class MotionSolution;
    }
    namespace Tooling
    {
        class _SIZERExportBuilderBuilder;
        class SIZERExportBuilderImpl;
        /** Exports input parameters for motor selection to SIZER drive design to
                support the sizing, configuration, and selection of drive components.  <br> To create a new instance of this class, use @link Tooling::SIZERCollection::CreateExportBuilder Tooling::SIZERCollection::CreateExportBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  SIZERExportBuilder : public Builder
        {
             /** Defines the mechanical data. */
            public:
            struct  MechanicalData
            {
                public: /** Unique ID                */int Id;
                public: /** Mechanical Name          */NXString Name;
                public: /** Motion solution          */NXOpen::Motion::MotionSolution * Solution;
                public: /** Torque graph in solution */NXOpen::Motion::Graph * TorqueGraph;
                public: /** Speed graph in solution  */NXOpen::Motion::Graph * SpeedGraph;
                public: /** Friction Torque value    */double FrictionTorque;
                public: /** System Efficiency value  */double SystemEfficiency;
                public: /** Load Inertia value       */double LoadInertia;
                public: /** Additional Inertia value */double AdditionalInertia;
                public: MechanicalData() :
                    Id(),
                    Name(),
                    Solution(),
                    TorqueGraph(),
                    SpeedGraph(),
                    FrictionTorque(),
                    SystemEfficiency(),
                    LoadInertia(),
                    AdditionalInertia()
                {
                }
                /** Constructor for the MechanicalData struct. */ 
                public: MechanicalData(int idInitial /** Unique ID                */, 
                        const NXString &nameInitial /** Mechanical Name          */, 
                        NXOpen::Motion::MotionSolution * solutionInitial /** Motion solution          */, 
                        NXOpen::Motion::Graph * torqueGraphInitial /** Torque graph in solution */, 
                        NXOpen::Motion::Graph * speedGraphInitial /** Speed graph in solution  */, 
                        double frictionTorqueInitial /** Friction Torque value    */, 
                        double systemEfficiencyInitial /** System Efficiency value  */, 
                        double loadInertiaInitial /** Load Inertia value       */, 
                        double additionalInertiaInitial /** Additional Inertia value */) :
                    Id(idInitial),
                    Name(nameInitial),
                    Solution(solutionInitial),
                    TorqueGraph(torqueGraphInitial),
                    SpeedGraph(speedGraphInitial),
                    FrictionTorque(frictionTorqueInitial),
                    SystemEfficiency(systemEfficiencyInitial),
                    LoadInertia(loadInertiaInitial),
                    AdditionalInertia(additionalInertiaInitial)
                {
                }
            };

            private: SIZERExportBuilderImpl * m_sizerexportbuilder_impl;
            private: friend class  _SIZERExportBuilderBuilder;
            protected: SIZERExportBuilder();
            public: ~SIZERExportBuilder();
            /** Gets all groups of mechanical data.  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void GetMechanicalData
            (
                std::vector<NXOpen::Tooling::SIZERExportBuilder::MechanicalData> & mechanicalData /** Array of mechanical data */
            );
            /** Sets all groups of mechanical data.  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetMechanicalData
            (
                const std::vector<NXOpen::Tooling::SIZERExportBuilder::MechanicalData> & mechanicalData /** Array of mechanical data */
            );
            /**Returns  the output *.mdix file, which is exported to SIZER.  <br> License requirements : None */
            public: NXString OutputFile
            (
            );
            /**Sets  the output *.mdix file, which is exported to SIZER.  <br> License requirements : mechanisms ("MECHANISMS") */
            public: void SetOutputFile
            (
                const NXString & outputFile /** outputfile */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
