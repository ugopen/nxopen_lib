#ifndef NXOpen_CAM_MACHINEPOCKETGROUPBUILDER_HXX_INCLUDED
#define NXOpen_CAM_MACHINEPOCKETGROUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_MachinePocketGroupBuilder.ja
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
#include <NXOpen/CAM_NCGroupBuilder.hxx>
#include <NXOpen/ObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class MachinePocketGroupBuilder;
    }
    namespace CAM
    {
        class HoldingSystemBuilder;
    }
    namespace CAM
    {
        class HoldingSystemBuilderList;
    }
    namespace CAM
    {
        class InheritableIntBuilder;
    }
    namespace CAM
    {
        class NCGroupBuilder;
    }
    namespace CAM
    {
        class _MachinePocketGroupBuilderBuilder;
        class MachinePocketGroupBuilderImpl;
        /** Represents a MachinePocketGroup Builder  <br> To create a new instance of this class, use @link CAM::NCGroupCollection::CreateMachinePocketGroupBuilder CAM::NCGroupCollection::CreateMachinePocketGroupBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  MachinePocketGroupBuilder : public CAM::NCGroupBuilder
        {
            /** the register type */
            public: enum RegisterType
            {
                RegisterTypeSameAsPocketId/** use same as pocket id*/,
                RegisterTypeSpecify/** use specify*/
            };

            private: MachinePocketGroupBuilderImpl * m_machinepocketgroupbuilder_impl;
            private: friend class  _MachinePocketGroupBuilderBuilder;
            protected: MachinePocketGroupBuilder();
            public: ~MachinePocketGroupBuilder();
            /**Returns  the pocket id  <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * PocketIdBuilder
            (
            );
            /**Returns  the adjust register type  <br> License requirements : None */
            public: NXOpen::CAM::MachinePocketGroupBuilder::RegisterType AdjustRegisterType
            (
            );
            /**Sets  the adjust register type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetAdjustRegisterType
            (
                NXOpen::CAM::MachinePocketGroupBuilder::RegisterType type /** type */ 
            );
            /**Returns  the adjust id  <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * AdjustIdBuilder
            (
            );
            /**Returns  the cutcom register type  <br> License requirements : None */
            public: NXOpen::CAM::MachinePocketGroupBuilder::RegisterType CutcomRegisterType
            (
            );
            /**Sets  the cutcom register type  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetCutcomRegisterType
            (
                NXOpen::CAM::MachinePocketGroupBuilder::RegisterType type /** type */ 
            );
            /**Returns  the cutcom id  <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * CutcomIdBuilder
            (
            );
            /** Creates a new holding system builder  @return  holding system builder <br> License requirements : None */
            public: NXOpen::CAM::HoldingSystemBuilder * CreateHoldingSystemBuilder
            (
                int position /** position */,
                const NXString & name /** Holding system name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the holding systems list  <br> License requirements : None */
            public: NXOpen::CAM::HoldingSystemBuilderList * HoldingSystemsList
            (
            );
            /**Returns  the channel's name  <br> License requirements : None */
            public: NXString ChannelName
            (
            );
            /**Sets  the channel's name  <br> License requirements : cam_base ("CAM BASE") */
            public: void SetChannelName
            (
                const NXString & name /** the channel's name */
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif