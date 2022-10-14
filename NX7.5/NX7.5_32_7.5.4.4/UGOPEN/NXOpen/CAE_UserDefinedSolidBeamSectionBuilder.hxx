#ifndef NXOpen_CAE_USERDEFINEDSOLIDBEAMSECTIONBUILDER_HXX_INCLUDED
#define NXOpen_CAE_USERDEFINEDSOLIDBEAMSECTIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_UserDefinedSolidBeamSectionBuilder.ja
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
#include <NXOpen/CAE_BeamSection.hxx>
#include <NXOpen/CAE_UserDefinedSolidBeamSectionBuilder.hxx>
#include <NXOpen/CAE_IBeamSectionBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class UserDefinedSolidBeamSectionBuilder;
    }
    namespace CAE
    {
        class IBeamSectionBuilder;
    }
    namespace CAE
    {
        class SelectCAEFace;
    }
    class Direction;
    namespace CAE
    {
        class _UserDefinedSolidBeamSectionBuilderBuilder;
        class UserDefinedSolidBeamSectionBuilderImpl;
        /**
            Represents a @link CAE::UserDefinedSolidBeamSectionBuilder CAE::UserDefinedSolidBeamSectionBuilder@endlink 
             <br> To create a new instance of this class, use @link CAE::BeamSectionCollection::CreateUserDefinedSolidBeamSectionBuilder CAE::BeamSectionCollection::CreateUserDefinedSolidBeamSectionBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  UserDefinedSolidBeamSectionBuilder : public CAE::IBeamSectionBuilder
        {
            private: UserDefinedSolidBeamSectionBuilderImpl * m_userdefinedsolidbeamsectionbuilder_impl;
            private: friend class  _UserDefinedSolidBeamSectionBuilderBuilder;
            protected: UserDefinedSolidBeamSectionBuilder();
            public: ~UserDefinedSolidBeamSectionBuilder();
            /**Returns  the section descriptor name  <br> License requirements : None */
            public: NXString DescriptorName
            (
            );
            /**Sets  the section descriptor name  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetDescriptorName
            (
                const NXString & descriptorName /** descriptorname */ 
            );
            /**Returns  the solid face  <br> License requirements : None */
            public: NXOpen::CAE::SelectCAEFace * SolidFace
            (
            );
            /**Returns  the option to define reference vector  <br> License requirements : None */
            public: NXOpen::CAE::BeamSection::DirectionOption DirectionType
            (
            );
            /**Sets  the option to define reference vector  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetDirectionType
            (
                NXOpen::CAE::BeamSection::DirectionOption directionType /** directiontype */ 
            );
            /**Returns  the reference vector  <br> License requirements : None */
            public: NXOpen::Direction * ReferenceVector
            (
            );
            /**Sets  the reference vector  <br> License requirements : nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation") */
            public: void SetReferenceVector
            (
                NXOpen::Direction * referenceVector /** referencevector */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif