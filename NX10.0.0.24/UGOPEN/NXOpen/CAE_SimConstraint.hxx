#ifndef NXOpen_CAE_SIMCONSTRAINT_HXX_INCLUDED
#define NXOpen_CAE_SIMCONSTRAINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_SimConstraint.ja
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
#include <NXOpen/CAE_SimBC.hxx>
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
        class SimConstraint;
    }
    namespace CAE
    {
        class SimBC;
    }
    namespace CAE
    {
        class _SimConstraintBuilder;
        class SimConstraintImpl;
        /**  @brief  Represents a constraint  

           <br> To create a new instance of this class, use @link NXOpen::CAE::SimConstraintCollection::CreateConstraint  NXOpen::CAE::SimConstraintCollection::CreateConstraint @endlink  <br> 
         <br>  Created in NX4.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  SimConstraint : public NXOpen::CAE::SimBC
        {
            private: SimConstraintImpl * m_simconstraint_impl;
            private: friend class  _SimConstraintBuilder;
            protected: SimConstraint();
            public: ~SimConstraint();
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
