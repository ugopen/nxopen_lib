#ifndef NXOpen_CAM_GENERALPROPERTIESBUILDER_HXX_INCLUDED
#define NXOpen_CAM_GENERALPROPERTIESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_GeneralPropertiesBuilder.ja
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
    namespace CAM
    {
        class GeneralPropertiesBuilder;
    }
    class Builder;
    class SelectNXObjectList;
    namespace CAM
    {
        class _GeneralPropertiesBuilderBuilder;
        class GeneralPropertiesBuilderImpl;
        /**
            Represents a @link NXOpen::CAM::GeneralPropertiesBuilder NXOpen::CAM::GeneralPropertiesBuilder@endlink  to be used for setting the name
            of a specified CAM object.
             <br> To create a new instance of this class, use @link NXOpen::PropertiesManager::CreateGeneralCAMPropertiesBuilder  NXOpen::PropertiesManager::CreateGeneralCAMPropertiesBuilder @endlink  <br> 
         <br>  Created in NX9.0.1.  <br>  
        */
        class NXOPENCPP_CAMEXPORT  GeneralPropertiesBuilder : public NXOpen::Builder
        {
            private: GeneralPropertiesBuilderImpl * m_generalpropertiesbuilder_impl;
            private: friend class  _GeneralPropertiesBuilderBuilder;
            protected: GeneralPropertiesBuilder();
            public: ~GeneralPropertiesBuilder();
            /**Returns  the selected object(s) list. 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::SelectNXObjectList * SelectedObjects
            (
            );
            /**Returns  the name of the selected CAM object. 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name of the selected CAM object. 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : None */
            public: void SetName
            (
                const NXString & name /** name */ 
            );
            /**Sets  the name of the selected CAM object. 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : None */
            void SetName
            (
                const char * name /** name */ 
            );
            /** Lists the object information to the listing window 
             <br>  Created in NX9.0.1.  <br>  
             <br> License requirements : None */
            public: void Information
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