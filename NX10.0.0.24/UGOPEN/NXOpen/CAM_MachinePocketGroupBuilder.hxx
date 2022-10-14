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
#include <NXOpen/libnxopencpp_cam_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

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
        class InheritableTextBuilder;
    }
    namespace CAM
    {
        class NCGroupBuilder;
    }
    namespace CAM
    {
        class _MachinePocketGroupBuilderBuilder;
        class MachinePocketGroupBuilderImpl;
        /** Represents a MachinePocketGroup Builder  <br> To create a new instance of this class, use @link NXOpen::CAM::NCGroupCollection::CreateMachinePocketGroupBuilder  NXOpen::CAM::NCGroupCollection::CreateMachinePocketGroupBuilder @endlink  <br> 
         <br>  Created in NX5.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  MachinePocketGroupBuilder : public NXOpen::CAM::NCGroupBuilder
        {
            /** the register type 
             <br>  @deprecated Deprecated in NX8.5.0.  This @link NXOpen::CAM::MachinePocketGroupBuilder::RegisterType NXOpen::CAM::MachinePocketGroupBuilder::RegisterType@endlink  is no longer supported. <br>  
            */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  This NXOpen::CAM::MachinePocketGroupBuilder::RegisterType is no longer supported.") enum RegisterType
            {
                RegisterTypeSameAsPocketId/** use same as pocket id*/,
                RegisterTypeSpecify/** use specify*/
            };

            private: MachinePocketGroupBuilderImpl * m_machinepocketgroupbuilder_impl;
            private: friend class  _MachinePocketGroupBuilderBuilder;
            protected: MachinePocketGroupBuilder();
            public: ~MachinePocketGroupBuilder();
            /**Returns  the pocket id 
             <br>  Created in NX5.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * PocketIdBuilder
            (
            );
            /**Returns  the pocket id in string
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableTextBuilder * PocketIdStringBuilder
            (
            );
            /**Returns  the adjust register type 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link CAM::MachinePocketGroupBuilder::AdjustIdBuilder CAM::MachinePocketGroupBuilder::AdjustIdBuilder @endlink and @link CAM::MachinePocketGroupBuilder::SetAdjustIdBuilder CAM::MachinePocketGroupBuilder::SetAdjustIdBuilder @endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use CAM::MachinePocketGroupBuilder::AdjustIdBuilder CAM::MachinePocketGroupBuilder::AdjustIdBuilder @endlink and @link CAM::MachinePocketGroupBuilder::SetAdjustIdBuilder CAM::MachinePocketGroupBuilder::SetAdjustIdBuilder @endlink  instead.") NXOpen::CAM::MachinePocketGroupBuilder::RegisterType AdjustRegisterType
            (
            );
            /**Sets  the adjust register type 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link CAM::MachinePocketGroupBuilder::AdjustIdBuilder CAM::MachinePocketGroupBuilder::AdjustIdBuilder @endlink and @link CAM::MachinePocketGroupBuilder::SetAdjustIdBuilder CAM::MachinePocketGroupBuilder::SetAdjustIdBuilder @endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use CAM::MachinePocketGroupBuilder::AdjustIdBuilder CAM::MachinePocketGroupBuilder::AdjustIdBuilder @endlink and @link CAM::MachinePocketGroupBuilder::SetAdjustIdBuilder CAM::MachinePocketGroupBuilder::SetAdjustIdBuilder @endlink  instead.") void SetAdjustRegisterType
            (
                NXOpen::CAM::MachinePocketGroupBuilder::RegisterType type /** type */ 
            );
            /**Returns  the adjust id 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * AdjustIdBuilder
            (
            );
            /**Returns  the cutcom register type 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link CAM::MachinePocketGroupBuilder::CutcomIdBuilder CAM::MachinePocketGroupBuilder::CutcomIdBuilder @endlink and @link CAM::MachinePocketGroupBuilder::SetCutcomIdBuilder CAM::MachinePocketGroupBuilder::SetCutcomIdBuilder @endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use CAM::MachinePocketGroupBuilder::CutcomIdBuilder CAM::MachinePocketGroupBuilder::CutcomIdBuilder @endlink and @link CAM::MachinePocketGroupBuilder::SetCutcomIdBuilder CAM::MachinePocketGroupBuilder::SetCutcomIdBuilder @endlink  instead.") NXOpen::CAM::MachinePocketGroupBuilder::RegisterType CutcomRegisterType
            (
            );
            /**Sets  the cutcom register type 
             <br>  @deprecated Deprecated in NX8.5.0.  Use @link CAM::MachinePocketGroupBuilder::CutcomIdBuilder CAM::MachinePocketGroupBuilder::CutcomIdBuilder @endlink and @link CAM::MachinePocketGroupBuilder::SetCutcomIdBuilder CAM::MachinePocketGroupBuilder::SetCutcomIdBuilder @endlink  instead. <br>  

             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public:  NX_DEPRECATED("Deprecated in NX8.5.0.  Use CAM::MachinePocketGroupBuilder::CutcomIdBuilder CAM::MachinePocketGroupBuilder::CutcomIdBuilder @endlink and @link CAM::MachinePocketGroupBuilder::SetCutcomIdBuilder CAM::MachinePocketGroupBuilder::SetCutcomIdBuilder @endlink  instead.") void SetCutcomRegisterType
            (
                NXOpen::CAM::MachinePocketGroupBuilder::RegisterType type /** type */ 
            );
            /**Returns  the cutcom id 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::InheritableIntBuilder * CutcomIdBuilder
            (
            );
            /** Creates a new holding system builder  @return  holding system builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::HoldingSystemBuilder * CreateHoldingSystemBuilder
            (
                int position /** position */,
                const NXString & name /** Holding system name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a new holding system builder  @return  holding system builder
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            NXOpen::CAM::HoldingSystemBuilder * CreateHoldingSystemBuilder
            (
                int position /** position */,
                const char * name /** Holding system name   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /**Returns  the holding systems list 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAM::HoldingSystemBuilderList * HoldingSystemsList
            (
            );
            /**Returns  the channel's name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXString ChannelName
            (
            );
            /**Sets  the channel's name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetChannelName
            (
                const NXString & name /** the channel's name */
            );
            /**Sets  the channel's name 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            void SetChannelName
            (
                const char * name /** the channel's name */
            );
            /**Returns  the number of tools 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: int NumberOfTools
            (
            );
            /**Sets  the number of tools 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : cam_base ("CAM BASE") */
            public: void SetNumberOfTools
            (
                int numTools /** the number of tools */
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