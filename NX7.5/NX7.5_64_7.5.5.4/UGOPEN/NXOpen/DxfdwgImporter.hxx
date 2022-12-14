#ifndef NXOpen_DXFDWGIMPORTER_HXX_INCLUDED
#define NXOpen_DXFDWGIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DxfdwgImporter.ja
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
#include <NXOpen/DxfdwgImporter.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class DxfdwgImporter;
    class Builder;
    class _DxfdwgImporterBuilder;
    class DxfdwgImporterImpl;
    /**
        Represents a @link DxfdwgImporter DxfdwgImporter@endlink  to be used when importing the IGES Data
        This class is created using @link DexManager DexManager@endlink .  <br> To create a new instance of this class, use @link DexManager::CreateDxfdwgImporter DexManager::CreateDxfdwgImporter@endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    ImportCurvesAsSketch </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    ImportPolylineTo </td> <td> 
     
    Splines </td> </tr> 

    <tr><td> 
     
    ImportTo </td> <td> 
     
    NewMetric </td> </tr> 

    <tr><td> 
     
    ImportTo2D (deprecated) </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    ImportToTeamcenter </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    IncludeModelSpace (deprecated) </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    SendLayoutsTo </td> <td> 
     
    ImportedView </td> </tr> 

    <tr><td> 
     
    SendModelDataTo </td> <td> 
     
    Modeling </td> </tr> 

    </table>  
    */
    class NXOPENCPPEXPORT  DxfdwgImporter : public Builder
    {
        /** Import To option */
        public: enum ImportToEnum
        {
            ImportToEnumNewMetric/** import dxf/dwg file to new part with metric units */,
            ImportToEnumNewEnglish/** import dxf/dwg file to new part with english units */,
            ImportToEnumWork/** import dxf/dwg file to work part */
        };

        /** Import Polylines as option */
        public: enum ImportPolylinesAs
        {
            ImportPolylinesAsSplines/** import polylines as splines */,
            ImportPolylinesAsArcLines/** import polylines as arc/lines */
        };

        /** Send Model data to option */
        public: enum SendModelDataAs
        {
            SendModelDataAsModeling/** send model data to modeling */,
            SendModelDataAsDrawingView/** send model data to drawing view */,
            SendModelDataAsDrawingSheet/** send model data to drawing sheet */
        };

        /** Send Layouts data to option */
        public: enum SendLayoutsAs
        {
            SendLayoutsAsImportedView/** send model data to modeling */,
            SendLayoutsAsDrawingView/** send model data to drawing view */,
            SendLayoutsAsDrawingSheet/** send model data to drawing sheet */
        };

        private: DxfdwgImporterImpl * m_dxfdwgimporter_impl;
        private: friend class  _DxfdwgImporterBuilder;
        protected: DxfdwgImporter();
        public: ~DxfdwgImporter();
        /** The set user credentials - this will set user name, password and group in NX Manager mode <br> License requirements : None */
        public: void SetUserCredential
        (
            const NXString & user /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & passwd /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & group /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Saves the save settings - this will save the settings to a file specified  <br> License requirements : None */
        public: void SaveSettings
        (
            const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**Returns  the input file - name of a file which is being imported <br> License requirements : None */
        public: NXString InputFile
        (
        );
        /**Sets  the input file - name of a file which is being imported <br> License requirements : None */
        public: void SetInputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the import to - this option will determine the destination for imported autocad file. it can
                    either be new (englies/metric) or work part.  <br> License requirements : None */
        public: NXOpen::DxfdwgImporter::ImportToEnum ImportTo
        (
        );
        /**Sets  the import to - this option will determine the destination for imported autocad file. it can
                    either be new (englies/metric) or work part.  <br> License requirements : None */
        public: void SetImportTo
        (
            NXOpen::DxfdwgImporter::ImportToEnum importTo /** importto */ 
        );
        /**Returns  Import to 2D - this options decides if autocad data should be converted to 2d
                 drawing views or not 
         @deprecated Deprecated in NX7.5.2 <br> 
         <br> License requirements : None */
        public:  NX_DEPRECATED("Deprecated in NX7.5.2") bool ImportTo2D
        (
        );
        /**Sets  Import to 2D - this options decides if autocad data should be converted to 2d
                 drawing views or not 
         @deprecated Deprecated in NX7.5.2 <br> 
         <br> License requirements : None */
        public:  NX_DEPRECATED("Deprecated in NX7.5.2") void SetImportTo2D
        (
            bool importTo2d /** importto2d */ 
        );
        /**Returns  Include mode space - this option will determine if the model space data in autocad
                should be converted to drawing views or not.  
         @deprecated Deprecated in NX7.5.2 <br> 
         <br> License requirements : None */
        public:  NX_DEPRECATED("Deprecated in NX7.5.2") bool IncludeModelSpace
        (
        );
        /**Sets  Include mode space - this option will determine if the model space data in autocad
                should be converted to drawing views or not.  
         @deprecated Deprecated in NX7.5.2 <br> 
         <br> License requirements : None */
        public:  NX_DEPRECATED("Deprecated in NX7.5.2") void SetIncludeModelSpace
        (
            bool includeModelSpace /** includemodelspace */ 
        );
        /**Returns  the output file - if autocad file is imported to new part then this name will be used to
                    write the output.  <br> License requirements : None */
        public: NXString OutputFile
        (
        );
        /**Sets  the output file - if autocad file is imported to new part then this name will be used to
                    write the output.  <br> License requirements : None */
        public: void SetOutputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  ImportToTeamcenter- if set to true then assembly will be imported into Teamcenter  <br> License requirements : None */
        public: bool ImportToTeamcenter
        (
        );
        /**Sets  ImportToTeamcenter- if set to true then assembly will be imported into Teamcenter  <br> License requirements : None */
        public: void SetImportToTeamcenter
        (
            bool importToTeamcenter /** importtoteamcenter */ 
        );
        /**Returns  the import polyline to group - this will determine if polylines will be imported as splines or 
                    lines/arcs.  <br> License requirements : None */
        public: NXOpen::DxfdwgImporter::ImportPolylinesAs ImportPolylineTo
        (
        );
        /**Sets  the import polyline to group - this will determine if polylines will be imported as splines or 
                    lines/arcs.  <br> License requirements : None */
        public: void SetImportPolylineTo
        (
            NXOpen::DxfdwgImporter::ImportPolylinesAs importPolylineTo /** importpolylineto */ 
        );
        /**Returns  the send model data to - this will determine the destination for model data 
                     <br> License requirements : None */
        public: NXOpen::DxfdwgImporter::SendModelDataAs SendModelDataTo
        (
        );
        /**Sets  the send model data to - this will determine the destination for model data 
                     <br> License requirements : None */
        public: void SetSendModelDataTo
        (
            NXOpen::DxfdwgImporter::SendModelDataAs sendModelDataTo /** sendmodeldatato */ 
        );
        /**Returns  the send layouts  to - this will determine the destination for layout data 
                     <br> License requirements : None */
        public: NXOpen::DxfdwgImporter::SendLayoutsAs SendLayoutsTo
        (
        );
        /**Sets  the send layouts  to - this will determine the destination for layout data 
                     <br> License requirements : None */
        public: void SetSendLayoutsTo
        (
            NXOpen::DxfdwgImporter::SendLayoutsAs sendLayoutsTo /** sendlayoutsto */ 
        );
        /**Returns  ImportCurvesAsSketch - When model data is imported on drawing sheet then this can be turned on
                 to create sketch curves  <br> License requirements : None */
        public: bool ImportCurvesAsSketch
        (
        );
        /**Sets  ImportCurvesAsSketch - When model data is imported on drawing sheet then this can be turned on
                 to create sketch curves  <br> License requirements : None */
        public: void SetImportCurvesAsSketch
        (
            bool importCurvesAsSketch /** importcurvesassketch */ 
        );
        /**Returns  the settings file - definition file for default options <br> License requirements : None */
        public: NXString SettingsFile
        (
        );
        /**Sets  the settings file - definition file for default options <br> License requirements : None */
        public: void SetSettingsFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the file open flag - should be set to false if doing file import <br> License requirements : None */
        public: bool FileOpenFlag
        (
        );
        /**Sets  the file open flag - should be set to false if doing file import <br> License requirements : None */
        public: void SetFileOpenFlag
        (
            bool doingFileOpen /** doingfileopen */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif
