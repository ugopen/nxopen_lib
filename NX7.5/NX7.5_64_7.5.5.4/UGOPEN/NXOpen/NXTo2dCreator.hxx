#ifndef NXOpen_NXTO2DCREATOR_HXX_INCLUDED
#define NXOpen_NXTO2DCREATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     NXTo2dCreator.ja
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
#include <NXOpen/NXTo2dCreator.hxx>
#include <NXOpen/ObjectSelector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class NXTo2dCreator;
    class Builder;
    class ObjectSelector;
    class TaggedObject;
    class _NXTo2dCreatorBuilder;
    class NXTo2dCreatorImpl;
    /**
        Represents a @link NXTo2dCreator NXTo2dCreator@endlink  to be used when exporting the IGES Data
        This class is created using @link DexManager DexManager@endlink .  <br> To create a new instance of this class, use @link DexManager::CreateNxto2dCreator DexManager::CreateNxto2dCreator@endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    AutoCADRevision </td> <td> 
     
    R2007 </td> </tr> 

    <tr><td> 
     
    BcurveDensity </td> <td> 
     
    2 </td> </tr> 

    <tr><td> 
     
    ConvertGDT </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    ExportData </td> <td> 
     
    ModelData </td> </tr> 

    <tr><td> 
     
    ExportFrom </td> <td> 
     
    DisplayPart </td> </tr> 

    <tr><td> 
     
    FacetBodies </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    Jama </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    MaxLineThickness </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    MaxSystem3DModelSpace </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    MaxSystemPointRes </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    MaxUser3DModelSpace </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    MaxUserPointRes </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    OutputFileType </td> <td> 
     
    NXPartFile </td> </tr> 

    <tr><td> 
     
    OutputTo </td> <td> 
     
    Modeling </td> </tr> 

    <tr><td> 
     
    OverlappingEntities </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    SpCurveTolerance </td> <td> 
     
    0.058 </td> </tr> 

    </table>  
    */
    class NXOPENCPPEXPORT  NXTo2dCreator : public Builder
    {
        /** Export From Option */
        public: enum ExportFromOption
        {
            ExportFromOptionDisplayPart/**  export data from displayed part */,
            ExportFromOptionExistingPart/**  export data from existing part which is on disk */
        };

        /** Output To Option */
        public: enum OutputToOption
        {
            OutputToOptionModeling/** output to modeling */,
            OutputToOptionDrafting/** output to drafting */
        };

        /** Output As Option */
        public: enum OutputAsOption
        {
            OutputAsOptionNXPartFile/** final output as nx part */,
            OutputAsOptionIGESFile/** final output as iges file */,
            OutputAsOptionDXFFile/** final output as dxf file */,
            OutputAsOptionDWGFile/** final output as dwg file */
        };

        /** Export Data Option */
        public: enum ExportDataOption
        {
            ExportDataOptionModelData/** export model data only */,
            ExportDataOptionDrawing/** export drawings only */
        };

        /** AutoCad Revision Option */
        public: enum AutoCADRevisionOption
        {
            AutoCADRevisionOptionR2005/** output autocad version 2005 */,
            AutoCADRevisionOptionR2004/** output autocad version 2004 */,
            AutoCADRevisionOptionR2000/** output autocad version 2000 */,
            AutoCADRevisionOptionR14/** output autocad version R14 */,
            AutoCADRevisionOptionR2007/** output autocad version 2007 */
        };

        private: NXTo2dCreatorImpl * m_nxto2dcreator_impl;
        private: friend class  _NXTo2dCreatorBuilder;
        protected: NXTo2dCreator();
        public: ~NXTo2dCreator();
        /** The set user credentials - this will set user name, password and group in NX Manager mode <br> License requirements : None */
        public: void SetUserCredential
        (
            const NXString & user /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & passwd /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            const NXString & group /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Returns the save settings - this will save nxto2d the settings to a file sepcified  <br> License requirements : None */
        public: void SaveNxto2dSettings
        (
            const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Saves the save settings - this will save dxfdwg the settings to a file sepcified  <br> License requirements : None */
        public: void SaveDxfdwgSettings
        (
            const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Saves the save settings - this will save iges the settings to a file sepcified  <br> License requirements : None */
        public: void SaveIgesSettings
        (
            const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**Returns  the export from - this option will determine if data from display part or existing part is exported  <br> License requirements : None */
        public: NXOpen::NXTo2dCreator::ExportFromOption ExportFrom
        (
        );
        /**Sets  the export from - this option will determine if data from display part or existing part is exported  <br> License requirements : None */
        public: void SetExportFrom
        (
            NXOpen::NXTo2dCreator::ExportFromOption exportFrom /** exportfrom */ 
        );
        /**Returns  the input file - name of file which is being exported  <br> License requirements : None */
        public: NXString InputFile
        (
        );
        /**Sets  the input file - name of file which is being exported  <br> License requirements : None */
        public: void SetInputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the output file - the name of nx/iges/dxf/dwg file where output is being written <br> License requirements : None */
        public: NXString OutputFile
        (
        );
        /**Sets  the output file - the name of nx/iges/dxf/dwg file where output is being written <br> License requirements : None */
        public: void SetOutputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the output to - where to put data in model world or drawing <br> License requirements : None */
        public: NXOpen::NXTo2dCreator::OutputToOption OutputTo
        (
        );
        /**Sets  the output to - where to put data in model world or drawing <br> License requirements : None */
        public: void SetOutputTo
        (
            NXOpen::NXTo2dCreator::OutputToOption outputTo /** outputto */ 
        );
        /**Returns  the output file type - output file format  <br> License requirements : None */
        public: NXOpen::NXTo2dCreator::OutputAsOption OutputFileType
        (
        );
        /**Sets  the output file type - output file format  <br> License requirements : None */
        public: void SetOutputFileType
        (
            NXOpen::NXTo2dCreator::OutputAsOption outputFileType /** outputfiletype */ 
        );
        /**Returns  the nxto2d settings file - settings file to read default otions for nxto2d <br> License requirements : None */
        public: NXString Nxto2dSettingsFile
        (
        );
        /**Sets  the nxto2d settings file - settings file to read default otions for nxto2d <br> License requirements : None */
        public: void SetNxto2dSettingsFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the nxto2d settings file - settings file to read default otions for dxfdwg <br> License requirements : None */
        public: NXString DxfSettingsFile
        (
        );
        /**Sets  the nxto2d settings file - settings file to read default otions for dxfdwg <br> License requirements : None */
        public: void SetDxfSettingsFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the nxto2d settings file - settings file to read default otions for iges <br> License requirements : None */
        public: NXString IgesSettingsFile
        (
        );
        /**Sets  the nxto2d settings file - settings file to read default otions for iges <br> License requirements : None */
        public: void SetIgesSettingsFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the export data - export model data or drawings <br> License requirements : None */
        public: NXOpen::NXTo2dCreator::ExportDataOption ExportData
        (
        );
        /**Sets  the export data - export model data or drawings <br> License requirements : None */
        public: void SetExportData
        (
            NXOpen::NXTo2dCreator::ExportDataOption exportData /** exportdata */ 
        );
        /**Returns  the drawing Name - name of drawing to export <br> License requirements : None */
        public: NXString DrawingName
        (
        );
        /**Sets  the drawing Name - name of drawing to export <br> License requirements : None */
        public: void SetDrawingName
        (
            const NXString & drawingName /** drawingname */ 
        );
        /**Returns  the View Name - name of view to export  <br> License requirements : None */
        public: NXString ViewName
        (
        );
        /**Sets  the View Name - name of view to export  <br> License requirements : None */
        public: void SetViewName
        (
            const NXString & viewName /** viewname */ 
        );
        /**Returns  the export selection block - the object selection will be done by this block.  <br> License requirements : None */
        public: NXOpen::ObjectSelector * ExportSelectionBlock
        (
        );
        /**Returns  the facet bodies - if set to true facet bodies will be exported to 2d part <br> License requirements : None */
        public: bool FacetBodies
        (
        );
        /**Sets  the facet bodies - if set to true facet bodies will be exported to 2d part <br> License requirements : None */
        public: void SetFacetBodies
        (
            bool facetBodies /** facetbodies */ 
        );
        /**Returns  the convert gdt - if set to true then GDT will convertd as group <br> License requirements : None */
        public: bool ConvertGDT
        (
        );
        /**Sets  the convert gdt - if set to true then GDT will convertd as group <br> License requirements : None */
        public: void SetConvertGDT
        (
            bool convertGDT /** convertgdt */ 
        );
        /**Returns  the overlapping entities - if set to true, the overlpping entities will be removed  <br> License requirements : None */
        public: bool OverlappingEntities
        (
        );
        /**Sets  the overlapping entities - if set to true, the overlpping entities will be removed  <br> License requirements : None */
        public: void SetOverlappingEntities
        (
            bool overlappingEntities /** overlappingentities */ 
        );
        /**Returns  the auto cadrevision - this will decide the revision of resultant autocad file.  <br> License requirements : None */
        public: NXOpen::NXTo2dCreator::AutoCADRevisionOption AutoCADRevision
        (
        );
        /**Sets  the auto cadrevision - this will decide the revision of resultant autocad file.  <br> License requirements : None */
        public: void SetAutoCADRevision
        (
            NXOpen::NXTo2dCreator::AutoCADRevisionOption autoCADRevision /** autocadrevision */ 
        );
        /**Returns  the bcurve density -  segment density for b-spline curve  <br> License requirements : None */
        public: int BcurveDensity
        (
        );
        /**Sets  the bcurve density -  segment density for b-spline curve  <br> License requirements : None */
        public: void SetBcurveDensity
        (
            int bcurveDensity /** bcurvedensity */ 
        );
        /**Returns  the jama - if set to true the exported data will be Japanese Automotive compliant  <br> License requirements : None */
        public: bool Jama
        (
        );
        /**Sets  the jama - if set to true the exported data will be Japanese Automotive compliant  <br> License requirements : None */
        public: void SetJama
        (
            bool jama /** jama */ 
        );
        /**Returns  the sp curve tolerance  <br> License requirements : None */
        public: double SpCurveTolerance
        (
        );
        /**Sets  the sp curve tolerance  <br> License requirements : None */
        public: void SetSpCurveTolerance
        (
            double spCurveTolerance /** spcurvetolerance */ 
        );
        /**Returns  the max line thickness - maximum line thickness in resulting iges file  <br> License requirements : None */
        public: double MaxLineThickness
        (
        );
        /**Sets  the max line thickness - maximum line thickness in resulting iges file  <br> License requirements : None */
        public: void SetMaxLineThickness
        (
            double maxLineThickness /** maxlinethickness */ 
        );
        /**Returns  the sys defmaxThreeDmdl space - if set to true then system defined maximum 3D model 
                    space will be used <br> License requirements : None */
        public: bool MaxSystem3DModelSpace
        (
        );
        /**Sets  the sys defmaxThreeDmdl space - if set to true then system defined maximum 3D model 
                    space will be used <br> License requirements : None */
        public: void SetMaxSystem3DModelSpace
        (
            bool maxSystem3DModelSpace /** maxsystem3dmodelspace */ 
        );
        /**Returns  the maxThree dmdl space - if not using system defined maximum 3D model space then specifiy
                    the new value <br> License requirements : None */
        public: double MaxUser3DModelSpace
        (
        );
        /**Sets  the maxThree dmdl space - if not using system defined maximum 3D model space then specifiy
                    the new value <br> License requirements : None */
        public: void SetMaxUser3DModelSpace
        (
            double maxUser3DModelSpace /** maxuser3dmodelspace */ 
        );
        /**Returns  the sys defidentical point resolution - if set to true then system defined tolerance will be
                    used to find identical points  <br> License requirements : None */
        public: bool MaxSystemPointRes
        (
        );
        /**Sets  the sys defidentical point resolution - if set to true then system defined tolerance will be
                    used to find identical points  <br> License requirements : None */
        public: void SetMaxSystemPointRes
        (
            bool maxSystemPointRes /** maxsystempointres */ 
        );
        /**Returns  the identical point resolution - if not using system defined tolerance for identical points then
                    specify new value  <br> License requirements : None */
        public: double MaxUserPointRes
        (
        );
        /**Sets  the identical point resolution - if not using system defined tolerance for identical points then
                    specify new value  <br> License requirements : None */
        public: void SetMaxUserPointRes
        (
            double maxUserPointRes /** maxuserpointres */ 
        );
        /** Sets the drawing  - sets the list of drawings  to translate <br> License requirements : None */
        public: void SetDrawingArray
        (
            const std::vector<NXOpen::TaggedObject *> & objects /** items in list */
        );
    };
}
#undef EXPORTLIBRARY
#endif