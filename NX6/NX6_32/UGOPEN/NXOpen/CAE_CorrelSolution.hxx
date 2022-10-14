#ifndef NXOpen_CAE_CORRELSOLUTION_HXX_INCLUDED
#define NXOpen_CAE_CORRELSOLUTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_CorrelSolution.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class CorrelSolution;
    }
    class NXObject;
    namespace CAE
    {
        class _CorrelSolutionBuilder;
        /** Represents a @link CAE::CorrelSolution CAE::CorrelSolution@endlink  */
        class NXOPENCPPEXPORT CorrelSolution : public NXObject
        {
            private: friend class  _CorrelSolutionBuilder;
            protected: CorrelSolution();
            /** Returns the correlation solution name  @return  the @link CAE::CorrelSolution CAE::CorrelSolution@endlink   name  <br> License requirements : None */
            public: NXString GetSolutionName
            (
            );
            /** Sets the correlation solution name  <br> License requirements : None */
            public: void SetSolutionName
            (
                const NXString & solutionName /** solutionname */ ,
                bool renameResultFile /** if there are result files associated with the solution, rename the files or not*/
            );
            /** Deletes a correlation solution, including all events and excitations
                        under it  <br> License requirements : None */
            public: void Destroy
            (
                bool deleteResultFile /** delete the result files associated with the solution or not */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif