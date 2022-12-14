#ifndef NXOpen_STEP203CREATOR_HXX_INCLUDED
#define NXOpen_STEP203CREATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Step203Creator.ja
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
#include <NXOpen/DexBuilder.hxx>
#include <NXOpen/ObjectSelector.hxx>
#include <NXOpen/ObjectTypeSelector.hxx>
#include <NXOpen/Step203Creator.hxx>
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
    class Step203Creator;
    class DexBuilder;
    class ObjectSelector;
    class ObjectTypeSelector;
    class _Step203CreatorBuilder;
    class Step203CreatorImpl;
    /**
        Represents a @link Step203Creator Step203Creator@endlink  to be used when exporting the STEP203 Data
        This class is created using @link DexManager DexManager@endlink .
        NULL object will be returned from Commit().
    	The workpart should be present in the session before calling commit().  <br> To create a new instance of this class, use @link DexManager::CreateStep203Creator  DexManager::CreateStep203Creator @endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    BsplineTol </td> <td> 
     
    0.0254 </td> </tr> 

    <tr><td> 
     
    ColorAndLayers </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    EntityNames </td> <td> 
     
    LongName </td> </tr> 

    <tr><td> 
     
    ExportExtRef </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    ExportExtRefAs </td> <td> 
     
    Step </td> </tr> 

    <tr><td> 
     
    ExportFrom </td> <td> 
     
    DisplayPart </td> </tr> 

    <tr><td> 
     
    ProcessHoldFlag </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    ValidationProperties </td> <td> 
     
    0 </td> </tr> 

    </table>  

     <br>  Created in NX6.0.0.  <br>  
    */
    class NXOPENCPPEXPORT  Step203Creator : public DexBuilder
    {
        /** Create the builder */
        public: enum ExportFromOption
        {
            ExportFromOptionDisplayPart/**  export data from displayed part */,
            ExportFromOptionExistingPart/**  export data from existing part which is on disk */
        };

        /** Entity Name Option */
        public: enum EntityNameOption
        {
            EntityNameOptionLongName/** create long names */,
            EntityNameOptionShortName/** create short names */
        };

        /** External Reference Option */
        public: enum ExternalReferenceOption
        {
            ExternalReferenceOptionStep/** output external reference as STEP file */,
            ExternalReferenceOptionNx/** output external reference as NX file */
        };

        private: Step203CreatorImpl * m_step203creator_impl;
        private: friend class  _Step203CreatorBuilder;
        protected: Step203Creator();
        public: ~Step203Creator();
        /** The save settings - this will save the settings to a file sepcified 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SaveSettings
        (
            const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** The save settings - this will save the settings to a file sepcified 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SaveSettings
        (
            const char * filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**Returns  the export from - this option will determine if data from display part or existing part is exported 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Step203Creator::ExportFromOption ExportFrom
        (
        );
        /**Sets  the export from - this option will determine if data from display part or existing part is exported 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetExportFrom
        (
            NXOpen::Step203Creator::ExportFromOption exportFrom /** exportfrom */ 
        );
        /**Returns  the input file  - name of file which is being exported.
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString InputFile
        (
        );
        /**Sets  the input file  - name of file which is being exported.
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetInputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  the input file  - name of file which is being exported.
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetInputFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the output file - the name of step file where output is being written 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString OutputFile
        (
        );
        /**Sets  the output file - the name of step file where output is being written 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetOutputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  the output file - the name of step file where output is being written 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetOutputFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the Settings File to read the default settings  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString SettingsFile
        (
        );
        /**Sets  the Settings File to read the default settings  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetSettingsFile
        (
            const NXString & filename /** filename */ 
        );
        /**Sets  the Settings File to read the default settings  
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetSettingsFile
        (
            const char * filename /** filename */ 
        );
        /**Returns  the export selection block - the object selection will be done by this block. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ObjectSelector * ExportSelectionBlock
        (
        );
        /**Returns  the objectTypes - this is subcomponent being used to set object types filters. This
                    will be used to filter objects based on the types 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::ObjectTypeSelector * ObjectTypes
        (
        );
        /**Returns  the layerMask - You can limit the data you export by only specifying the layers that 
                  contain the appropriate information. You can enter layer numbers or layers ranges 
                  separated by commas. For example, 1, 5, 88-109,190-199, 201, 206-210 is a legal specification.
                  The default setting for Layers to Export is 1-256. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString LayerMask
        (
        );
        /**Sets  the layerMask - You can limit the data you export by only specifying the layers that 
                  contain the appropriate information. You can enter layer numbers or layers ranges 
                  separated by commas. For example, 1, 5, 88-109,190-199, 201, 206-210 is a legal specification.
                  The default setting for Layers to Export is 1-256. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetLayerMask
        (
            const NXString & layerMask /** layermask */ 
        );
        /**Sets  the layerMask - You can limit the data you export by only specifying the layers that 
                  contain the appropriate information. You can enter layer numbers or layers ranges 
                  separated by commas. For example, 1, 5, 88-109,190-199, 201, 206-210 is a legal specification.
                  The default setting for Layers to Export is 1-256. 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetLayerMask
        (
            const char * layerMask /** layermask */ 
        );
        /**Returns  the entity names types long or short
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Step203Creator::EntityNameOption EntityNames
        (
        );
        /**Sets  the entity names types long or short
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetEntityNames
        (
            NXOpen::Step203Creator::EntityNameOption entityNames /** entitynames */ 
        );
        /**Returns  the color and layers - if set to true then NX color and layers will be preserverd
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool ColorAndLayers
        (
        );
        /**Sets  the color and layers - if set to true then NX color and layers will be preserverd
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetColorAndLayers
        (
            bool colorAndLayers /** colorandlayers */ 
        );
        /**Returns  the validation properties - if set to true validation properties will be created
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool ValidationProperties
        (
        );
        /**Sets  the validation properties - if set to true validation properties will be created
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetValidationProperties
        (
            bool validationProperties /** validationproperties */ 
        );
        /**Returns  the export ext ref - if set to true NX data can be output as external reference 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool ExportExtRef
        (
        );
        /**Sets  the export ext ref - if set to true NX data can be output as external reference 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetExportExtRef
        (
            bool exportExtRef /** exportextref */ 
        );
        /**Returns  the export ext ref as - specifiy the external reference type 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXOpen::Step203Creator::ExternalReferenceOption ExportExtRefAs
        (
        );
        /**Sets  the export ext ref as - specifiy the external reference type 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetExportExtRefAs
        (
            NXOpen::Step203Creator::ExternalReferenceOption exportExtRefAs /** exportextrefas */ 
        );
        /**Returns  the bspline tolerance 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: double BsplineTol
        (
        );
        /**Sets  the bspline tolerance 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetBsplineTol
        (
            double bsplineTol /** bsplinetol */ 
        );
        /**Returns  the author 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Author
        (
        );
        /**Sets  the author 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAuthor
        (
            const NXString & author /** author */ 
        );
        /**Sets  the author 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetAuthor
        (
            const char * author /** author */ 
        );
        /**Returns  the company 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Company
        (
        );
        /**Sets  the company 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetCompany
        (
            const NXString & company /** company */ 
        );
        /**Sets  the company 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetCompany
        (
            const char * company /** company */ 
        );
        /**Returns  the authorization 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Authorization
        (
        );
        /**Sets  the authorization 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetAuthorization
        (
            const NXString & authorization /** authorization */ 
        );
        /**Sets  the authorization 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetAuthorization
        (
            const char * authorization /** authorization */ 
        );
        /**Returns  the description 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: NXString Description
        (
        );
        /**Sets  the description 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetDescription
        (
            const NXString & description /** description */ 
        );
        /**Sets  the description 
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        void SetDescription
        (
            const char * description /** description */ 
        );
        /**Returns  the file save flag - set to false if doing file export
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: bool FileSaveFlag
        (
        );
        /**Sets  the file save flag - set to false if doing file export
         <br>  Created in NX6.0.0.  <br>  
         <br> License requirements : None */
        public: void SetFileSaveFlag
        (
            bool doingFileSave /** doingfilesave */ 
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
