#ifndef NXOpen_CAE_RESPONSESIMULATION_SOLUTIONATTRIBUTES_HXX_INCLUDED
#define NXOpen_CAE_RESPONSESIMULATION_SOLUTIONATTRIBUTES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ResponseSimulation_SolutionAttributes.ja
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
#include <NXOpen/Expression.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class SolutionAttributes;
        }
    }
    class Expression;
    namespace CAE
    {
        namespace ResponseSimulation
        {
            class _SolutionAttributesBuilder;
            class SolutionAttributesImpl;
            /** Represents attributes setting of response analysis meta solution */
            class NXOPENCPPEXPORT  SolutionAttributes : public TaggedObject
            {
                private: SolutionAttributesImpl * m_solutionattributes_impl;
                private: friend class  _SolutionAttributesBuilder;
                protected: SolutionAttributes();
                public: ~SolutionAttributes();
                /**Returns  the rigid body tolerance. The mode whose stiffness is smaller than this tolerance
                        will be considered as a rigid body.
                        
                 @deprecated Deprecated in NX6.0.0 <br> 
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public:  NX_DEPRECATED("Deprecated in NX6.0.0") double RigidBodyTolerance
                (
                );
                /**Sets  the rigid body tolerance. The mode whose stiffness is smaller than this tolerance
                        will be considered as a rigid body.
                        
                 @deprecated Deprecated in NX6.0.0 <br> 
                 <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public:  NX_DEPRECATED("Deprecated in NX6.0.0") void SetRigidBodyTolerance
                (
                    double tolerance /** tolerance */ 
                );
                /**Returns  the tolerance expression  <br> License requirements : nx_response_anlys ("NX Response Analysis") */
                public: NXOpen::Expression * RigidBodyToleranceExp
                (
                );
            };
        }
    }
}
#undef EXPORTLIBRARY
#endif
