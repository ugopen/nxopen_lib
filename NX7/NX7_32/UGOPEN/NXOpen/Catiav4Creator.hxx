#ifndef NXOpen_CATIAV4CREATOR_HXX_INCLUDED
#define NXOpen_CATIAV4CREATOR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Catiav4Creator.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/Catiav4Creator.hxx>
#include <NXOpen/ObjectSelector.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Catiav4Creator;
    class Builder;
    class ObjectSelector;
    class _Catiav4CreatorBuilder;
    /**
        Represents a @link Catiav4Creator Catiav4Creator@endlink  to be used when exporting the IGES Data
        This class is created using @link DexManager DexManager@endlink .  <br> To create a new instance of this class, use @link DexManager::CreateCatiav4Creator DexManager::CreateCatiav4Creator@endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    WriteSolidAs </td> <td> 
     
    VOLUMEs </td> </tr> 

    </table>  
    */
    class NXOPENCPPEXPORT Catiav4Creator : public Builder
    {
        /** Options for outputing solid bodies to CATIA V4 */
        public: enum SolidBodyOutputOption
        {
            SolidBodyOutputOptionVOLUMEs/** output NX solid bodies as Volumes in CATIA */,
            SolidBodyOutputOptionSolide/** output NX solid bodies as SOLIDE in CATIA */
        };

        private: friend class  _Catiav4CreatorBuilder;
        protected: Catiav4Creator();
        /** The save settings - this will save the settings to a file sepcified  <br> License requirements : None */
        public: void SaveSettings
        (
            const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**Returns  the export selection block - the object selection will be done by this block.  <br> License requirements : None */
        public: NXOpen::ObjectSelector * ExportSelectionBlock
        (
        );
        /**Returns  the output file - the exported data will be written to file specified  <br> License requirements : None */
        public: NXString OutputFile
        (
        );
        /**Sets  the output file - the exported data will be written to file specified  <br> License requirements : None */
        public: void SetOutputFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the settings file - The definition file to read default options  <br> License requirements : None */
        public: NXString SettingsFile
        (
        );
        /**Sets  the settings file - The definition file to read default options  <br> License requirements : None */
        public: void SetSettingsFile
        (
            const NXString & filename /** filename */ 
        );
        /**Returns  the write solid as - this will decide if solids should be written as SOLIDE or Volumes  <br> License requirements : None */
        public: NXOpen::Catiav4Creator::SolidBodyOutputOption WriteSolidAs
        (
        );
        /**Sets  the write solid as - this will decide if solids should be written as SOLIDE or Volumes  <br> License requirements : None */
        public: void SetWriteSolidAs
        (
            NXOpen::Catiav4Creator::SolidBodyOutputOption writeSolidAs /** writesolidas */ 
        );
        /**Returns  the file save flag - this should be set to false if doing File Export  <br> License requirements : None */
        public: bool FileSaveFlag
        (
        );
        /**Sets  the file save flag - this should be set to false if doing File Export  <br> License requirements : None */
        public: void SetFileSaveFlag
        (
            bool doingFileSave /** doingfilesave */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif
