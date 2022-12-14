#ifndef NXOpen_TOOLING_INITPROJECTBUILDER_HXX_INCLUDED
#define NXOpen_TOOLING_INITPROJECTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Tooling_InitProjectBuilder.ja
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
#include <NXOpen/SelectObjectList.hxx>
#include <NXOpen/Tooling_InitProjectBuilder.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Tooling
    {
        class InitProjectBuilder;
    }
    class Builder;
    class SelectBodyList;
    namespace Tooling
    {
        class _InitProjectBuilderBuilder;
        /** Mold Wizard initialize project builder  <br> To create a new instance of this class, use @link Tooling::InitProjectCollection::CreateBuilder Tooling::InitProjectCollection::CreateBuilder@endlink  <br> 
        Default values.
        <table border="1"> 
         
        <tr><th> 
        Property</th>  <th> 
        Value</th> </tr>
        <tr><td> 
         
        Configuration </td> <td> 
         
        Default </td> </tr> 

        <tr><td> 
         
        Material </td> <td> 
         
        None </td> </tr> 

        <tr><td> 
         
        Rename </td> <td> 
         
        0 </td> </tr> 

        <tr><td> 
         
        Unit </td> <td> 
         
        Millimeter </td> </tr> 

        </table>  
        */
        class NXOPENCPPEXPORT InitProjectBuilder : public Builder
        {
            /** the material type includes None and Nylon */
            public: enum MaterialId
            {
                MaterialIdNone/** None material is set */,
                MaterialIdNylon/** Nylon material type */
            };

            /** the configuration type includes default and orig */
            public: enum ConfigurationId
            {
                ConfigurationIdDefault/** Default configuration */,
                ConfigurationIdOrig/** Original configuration */
            };

            /** the unit type includes metric and inch project type */
            public: enum UnitId
            {
                UnitIdMillimeter/** metric project */,
                UnitIdInch/** english project */
            };

            private: friend class  _InitProjectBuilderBuilder;
            protected: InitProjectBuilder();
            /**Returns  the body will be used as product to create Mold Wizard project  <br> License requirements : None */
            public: NXOpen::SelectBodyList * BodySelect
            (
            );
            /**Returns  the project path access functions  <br> License requirements : None */
            public: NXString PathName
            (
            );
            /**Sets  the project path access functions  <br> License requirements : None */
            public: void SetPathName
            (
                const NXString & pathName /** pathname */ 
            );
            /**Returns  the project name access functions  <br> License requirements : None */
            public: NXString ProjectName
            (
            );
            /**Sets  the project name access functions  <br> License requirements : None */
            public: void SetProjectName
            (
                const NXString & projectName /** projectname */ 
            );
            /**Returns  the material access functions  <br> License requirements : None */
            public: NXOpen::Tooling::InitProjectBuilder::MaterialId Material
            (
            );
            /**Sets  the material access functions  <br> License requirements : None */
            public: void SetMaterial
            (
                NXOpen::Tooling::InitProjectBuilder::MaterialId material /** material */ 
            );
            /**Returns  the shrinkage access functions <br> License requirements : None */
            public: NXString Shrinkage
            (
            );
            /**Sets  the shrinkage access functions <br> License requirements : None */
            public: void SetShrinkage
            (
                const NXString & shrinkage /** shrinkage */ 
            );
            /**Returns  the configuration access functions <br> License requirements : None */
            public: NXOpen::Tooling::InitProjectBuilder::ConfigurationId Configuration
            (
            );
            /**Sets  the configuration access functions <br> License requirements : None */
            public: void SetConfiguration
            (
                NXOpen::Tooling::InitProjectBuilder::ConfigurationId configuration /** configuration */ 
            );
            /**Returns  the project unit access functions  <br> License requirements : None */
            public: NXOpen::Tooling::InitProjectBuilder::UnitId Unit
            (
            );
            /**Sets  the project unit access functions  <br> License requirements : None */
            public: void SetUnit
            (
                NXOpen::Tooling::InitProjectBuilder::UnitId unit /** unit */ 
            );
            /**Returns  the rename dialog allows users to define rename rules  <br> License requirements : None */
            public: bool Rename
            (
            );
            /**Sets  the rename dialog allows users to define rename rules  <br> License requirements : None */
            public: void SetRename
            (
                bool rename /** rename */ 
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
