#ifndef NXOpen_MASSPROPERTIESBUILDER_HXX_INCLUDED
#define NXOpen_MASSPROPERTIESBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     MassPropertiesBuilder.ja
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
#include <NXOpen/MassPropertiesBuilder.hxx>
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    class MassPropertiesBuilder;
    class Builder;
    class SelectNXObjectList;
    class _MassPropertiesBuilderBuilder;
    class MassPropertiesBuilderImpl;
    /** Represents a @link MassPropertiesBuilder MassPropertiesBuilder@endlink  for calculating the weight of
            selected objects as well as informing the part that the assemblies weight property
            data needs to be updated on save.
         <br> To create a new instance of this class, use @link PropertiesManager::CreateMassPropertiesBuilder  PropertiesManager::CreateMassPropertiesBuilder @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    UpdateOnSave </td> <td> 
     
    No </td> </tr> 

    </table>  

     <br>  Created in NX8.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  MassPropertiesBuilder : public Builder
    {
        /** Specifies the Update on Save option that will be applied to all selected objects. */
        public: enum UpdateOptions
        {
            UpdateOptionsNo/** The Update on Save property will be turned off for all selected objects. */,
            UpdateOptionsYes/** The Update on Save property will be turned on for all selected objects. */,
            UpdateOptionsMixed/** The Update on Save property will not change for the selected objects. */
        };

        private: MassPropertiesBuilderImpl * m_masspropertiesbuilder_impl;
        private: friend class  _MassPropertiesBuilderBuilder;
        protected: MassPropertiesBuilder();
        public: ~MassPropertiesBuilder();
        /**Returns  the selected objects list.  
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::SelectNXObjectList * SelectedObjects
        (
        );
        /**Returns  the update on save option.  This option informs the part if it should update the
                    assemblies weight property on save and will be applied to all fully loaded parts
                    contained in the parts list.  The option will be applied to all partially loaded
                    parts as well if the Load Partial Components option is set to true. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::MassPropertiesBuilder::UpdateOptions UpdateOnSave
        (
        );
        /**Sets  the update on save option.  This option informs the part if it should update the
                    assemblies weight property on save and will be applied to all fully loaded parts
                    contained in the parts list.  The option will be applied to all partially loaded
                    parts as well if the Load Partial Components option is set to true. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetUpdateOnSave
        (
            NXOpen::MassPropertiesBuilder::UpdateOptions updateOption /** updateoption */ 
        );
        /**Returns  the load partial components flag.  This flag specifies whether partially loaded
                    components will be fully loaded so the Update on Save setting can be applied
                    to all parts.  The commit may take longer if this flag is turned on. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: bool LoadPartialComponents
        (
        );
        /**Sets  the load partial components flag.  This flag specifies whether partially loaded
                    components will be fully loaded so the Update on Save setting can be applied
                    to all parts.  The commit may take longer if this flag is turned on. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetLoadPartialComponents
        (
            bool loadPartialComponents /** loadpartialcomponents */ 
        );
        /** This will update the weight property of the selected objects immediately. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void UpdateNow
        (
        );
        /**Returns  the accuracy used for weight calculation during Update Now. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: double Accuracy
        (
        );
        /**Sets  the accuracy used for weight calculation during Update Now. 
         <br>  Created in NX8.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAccuracy
        (
            double accuracy /** accuracy */ 
        );
    };
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
