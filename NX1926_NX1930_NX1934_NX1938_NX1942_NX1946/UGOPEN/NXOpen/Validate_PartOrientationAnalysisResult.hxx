#ifndef NXOpen_VALIDATE_PARTORIENTATIONANALYSISRESULT_HXX_INCLUDED
#define NXOpen_VALIDATE_PARTORIENTATIONANALYSISRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_PartOrientationAnalysisResult.ja
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
#include <NXOpen/Validate_AnalysisResult.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_validate_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Validate
    {
        class PartOrientationAnalysisResult;
    }
    namespace Validate
    {
        class AnalysisResult;
    }
    namespace Validate
    {
        class _PartOrientationAnalysisResultBuilder;
        class PartOrientationAnalysisResultImpl;
        /**
             This can be created using a @link NXOpen::Validate::CheckPartOrientationBuilder NXOpen::Validate::CheckPartOrientationBuilder@endlink  object.
            
         <br>  Created in NX1899.0.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  PartOrientationAnalysisResult : public NXOpen::Validate::AnalysisResult
        {
            /** Represents the index of checker used for part orientation optimization */
            public: enum CheckerIndex
            {
                CheckerIndexMinimum/** minimum */ ,
                CheckerIndexSurfaceArea/** Projected Surface Area Checker */ = 0,
                CheckerIndexSupportVolume/** Support Volume Checker */,
                CheckerIndexPrintTime/** Print Time Checker */,
                CheckerIndexOverheat/** Index for Overheat Checker */,
                CheckerIndexMaximum/** Maximum Index of Checkers */
            };

             /** Represents the checker value and range for specific checker 
             <br>  Created in NX1899.0.0.  <br>  
            */
            public:
            struct CheckerValues
            {
                public: /** Index of the checker */NXOpen::Validate::PartOrientationAnalysisResult::CheckerIndex MCheckerIndex;
                public: /** Minimum value of checker */double MCheckerMinValue;
                public: /** Current value of checker */double MCheckerValue;
                public: /** Maximum value of checker */double MCheckerMaxValue;
                public: CheckerValues() :
                    MCheckerIndex((NXOpen::Validate::PartOrientationAnalysisResult::CheckerIndex)0),
                    MCheckerMinValue(),
                    MCheckerValue(),
                    MCheckerMaxValue()
                {
                }
                /** Constructor for the CheckerValues struct. */ 
                public: CheckerValues(NXOpen::Validate::PartOrientationAnalysisResult::CheckerIndex mCheckerIndexInitial /** Index of the checker */, 
                        double mCheckerMinValueInitial /** Minimum value of checker */, 
                        double mCheckerValueInitial /** Current value of checker */, 
                        double mCheckerMaxValueInitial /** Maximum value of checker */) :
                    MCheckerIndex(mCheckerIndexInitial),
                    MCheckerMinValue(mCheckerMinValueInitial),
                    MCheckerValue(mCheckerValueInitial),
                    MCheckerMaxValue(mCheckerMaxValueInitial)
                {
                }
            };

            private: PartOrientationAnalysisResultImpl * m_partorientationanalysisresult_impl;
            private: friend class  _PartOrientationAnalysisResultBuilder;
            protected: PartOrientationAnalysisResult();
            public: ~PartOrientationAnalysisResult();
            /** Get the number of optimal solutions @return  Num of optimum orientation available 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: int GetNumOfOptimumOrientations
            (
            );
            /** Get the optimum orientation at given index
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void GetOptimumOrientation
            (
                int optimumOrientationIndex /** Index of optimum solution, should be within [0, num_of_optimum_orientations) */,
                NXOpen::Point3d* origin /** Origin for the optimum orientation */,
                NXOpen::Vector3d* orientation /** Z direction of the optimum orientation */,
                std::vector<NXOpen::Validate::PartOrientationAnalysisResult::CheckerValues> & checkerValues /** The values of checker and its range. */
            );
            /** Get minimum orientation for specific checker 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: void GetMinimumOrientation
            (
                NXOpen::Validate::PartOrientationAnalysisResult::CheckerIndex checkerIndex /** checker index */ ,
                NXOpen::Point3d* origin /** Origin for the optimum orientation */,
                NXOpen::Vector3d* orientation /** Z direction of the optimum orientation */,
                std::vector<NXOpen::Validate::PartOrientationAnalysisResult::CheckerValues> & checkerValues /** The values of checker and its range */
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
