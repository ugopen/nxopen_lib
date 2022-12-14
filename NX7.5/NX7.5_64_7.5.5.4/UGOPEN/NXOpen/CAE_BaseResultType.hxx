#ifndef NXOpen_CAE_BASERESULTTYPE_HXX_INCLUDED
#define NXOpen_CAE_BASERESULTTYPE_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_BaseResultType.ja
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
#include <NXOpen/CAE_BaseResultType.hxx>
#include <NXOpen/CAE_Result.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class BaseResultType;
    }
    namespace CAE
    {
        class _BaseResultTypeBuilder;
        class BaseResultTypeImpl;
        /** This class provides interfaces to query result type attributes  <br> An instance of this class can not be obtained <br> */
        class NXOPENCPPEXPORT  BaseResultType : public TaggedObject
        {
            private: BaseResultTypeImpl * m_baseresulttype_impl;
            private: friend class  _BaseResultTypeBuilder;
            protected: BaseResultType();
            public: ~BaseResultType();
            /**Returns  the @link CAE::Result::Quantity CAE::Result::Quantity@endlink  for this result type  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::Quantity Quantity
            (
            );
            /**Returns  the @link CAE::Result::Location CAE::Result::Location@endlink  where this result type is defined <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::Location Location
            (
            );
            /**Returns  the @link CAE::Result::DataType CAE::Result::DataType@endlink  for this result type  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXOpen::CAE::Result::DataType Datatype
            (
            );
            /**Returns  the name for this result type  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString Name
            (
            );
            /**Returns  the user defined name of this result type  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: NXString UserName
            (
            );
            /**Sets  the user defined name of this result type  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetUserName
            (
                const NXString & name /** name */ 
            );
            /**Returns a value indicating whether the result type is a complex value  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: bool Complex
            (
            );
            /**Returns the sections where this result is defined. 
                       This method should be used to find out what are those sections.
                       If a result contain both shell and beam elements and this result is defined
                       in different sections of respective elements, say TOP, BOTTOM, StressRecoveryPointC etc.,
                       then all of them will be returned in this array.
                     @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXOpen::CAE::Result::Section> GetSectionDefined
            (
            );
            /** Return all results components available for this result type     @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: std::vector<NXString> AskComponents
            (
                std::vector<NXOpen::CAE::Result::Component> & components /** components */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
