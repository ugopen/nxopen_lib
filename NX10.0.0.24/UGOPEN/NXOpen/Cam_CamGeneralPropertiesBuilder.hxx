#ifndef NXOpen_CAM_CAMGENERALPROPERTIESBUILDER_HXX_INCLUDED
#define NXOpen_CAM_CAMGENERALPROPERTIESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Cam_CamGeneralPropertiesBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
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
    namespace Cam
    {
        class CamGeneralPropertiesBuilder;
    }
    class Builder;
    class SelectNXObjectList;
    namespace Cam
    {
        class _CamGeneralPropertiesBuilderBuilder;
        class CamGeneralPropertiesBuilderImpl;
        /**
            Represents a @link NXOpen::Cam::CamGeneralPropertiesBuilder NXOpen::Cam::CamGeneralPropertiesBuilder@endlink  to be used for setting the name
            of a specified CAM object.
             <br> To create a new instance of this class, use @link NXOpen::PropertiesManager::CreateCamGeneralPropertiesBuilder  NXOpen::PropertiesManager::CreateCamGeneralPropertiesBuilder @endlink  <br> 
         <br>  @deprecated Deprecated in NX9.0.1.  Use @link NXOpen::CAM::GeneralPropertiesBuilder NXOpen::CAM::GeneralPropertiesBuilder@endlink  instead. <br>  

         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  NX_DEPRECATED("Deprecated in NX9.0.1.  Use NXOpen::CAM::GeneralPropertiesBuilder instead.")  CamGeneralPropertiesBuilder : public NXOpen::Builder
        {
            private: CamGeneralPropertiesBuilderImpl * m_camgeneralpropertiesbuilder_impl;
            private: friend class  _CamGeneralPropertiesBuilderBuilder;
            protected: CamGeneralPropertiesBuilder();
            public: ~CamGeneralPropertiesBuilder();
            /**Returns  the selected object(s) list. 
             <br>  @deprecated Deprecated in NX9.0.1.  Use @link NXOpen::CAM::GeneralPropertiesBuilder NXOpen::CAM::GeneralPropertiesBuilder@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.1.  Use NXOpen::CAM::GeneralPropertiesBuilder instead.") NXOpen::SelectNXObjectList * SelectedObjects
            (
            );
            /**Returns  the name of the selected CAM object. 
             <br>  @deprecated Deprecated in NX9.0.1.  Use @link NXOpen::CAM::GeneralPropertiesBuilder NXOpen::CAM::GeneralPropertiesBuilder@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.1.  Use NXOpen::CAM::GeneralPropertiesBuilder instead.") NXString Name
            (
            );
            /**Sets  the name of the selected CAM object. 
             <br>  @deprecated Deprecated in NX9.0.1.  Use @link NXOpen::CAM::GeneralPropertiesBuilder NXOpen::CAM::GeneralPropertiesBuilder@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.1.  Use NXOpen::CAM::GeneralPropertiesBuilder instead.") void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name of the selected CAM object. 
             <br>  @deprecated Deprecated in NX9.0.1.  Use @link NXOpen::CAM::GeneralPropertiesBuilder NXOpen::CAM::GeneralPropertiesBuilder@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Lists the object information to the listing window 
             <br>  @deprecated Deprecated in NX9.0.1.  Use @link NXOpen::CAM::GeneralPropertiesBuilder NXOpen::CAM::GeneralPropertiesBuilder@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : None */
            public:  NX_DEPRECATED("Deprecated in NX9.0.1.  Use NXOpen::CAM::GeneralPropertiesBuilder instead.") void Information
            (
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
