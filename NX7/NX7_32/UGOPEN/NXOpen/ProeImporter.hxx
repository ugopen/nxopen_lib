#ifndef NXOpen_PROEIMPORTER_HXX_INCLUDED
#define NXOpen_PROEIMPORTER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     ProeImporter.ja
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
#include <NXOpen/ProeImporter.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class ProeImporter;
    class Builder;
    class _ProeImporterBuilder;
    /**
        Represents a @link ProeImporter ProeImporter@endlink  to be used when importing the ProE Data
        This class is created using @link DexManager DexManager@endlink .  <br> To create a new instance of this class, use @link DexManager::CreateIgesImporter DexManager::CreateIgesImporter@endlink  <br> 
    Default values.
    <table border="1"> 
     
    <tr><th> 
    Property</th>  <th> 
    Value</th> </tr>
    <tr><td> 
     
    HealBodies </td> <td> 
     
    0 </td> </tr> 

    <tr><td> 
     
    IncludeNonManifoldObj </td> <td> 
     
    0 </td> </tr> 

    </table>  
    */
    class NXOPENCPPEXPORT ProeImporter : public Builder
    {
        private: friend class  _ProeImporterBuilder;
        protected: ProeImporter();
        /** Save the settings - this will save the settings to a file specified  <br> License requirements : None */
        public: void SaveSettings
        (
            const NXString & filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /**Returns  the input file -  name of a file which is being imported  <br> License requirements : None */
        public: NXString InputFile
        (
        );
        /**Sets  the input file -  name of a file which is being imported  <br> License requirements : None */
        public: void SetInputFile
        (
            const NXString & filename /** filename */ 
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
        /**Returns  the heal bodies - if set to true then imported data will be healed  <br> License requirements : None */
        public: bool HealBodies
        (
        );
        /**Sets  the heal bodies - if set to true then imported data will be healed  <br> License requirements : None */
        public: void SetHealBodies
        (
            bool healBodies /** healbodies */ 
        );
        /**Returns  the include non manifold obj - if set to true then non-manifold objects from proe will also 
                    be imported  <br> License requirements : None */
        public: bool IncludeNonManifoldObj
        (
        );
        /**Sets  the include non manifold obj - if set to true then non-manifold objects from proe will also 
                    be imported  <br> License requirements : None */
        public: void SetIncludeNonManifoldObj
        (
            bool includeNonManifoldObj /** includenonmanifoldobj */ 
        );
    };
}
#undef EXPORTLIBRARY
#endif
