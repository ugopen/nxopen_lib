#ifndef NXOpen_FEATURES_AECDESIGN_PROJECTSETUPBUILDER_HXX_INCLUDED
#define NXOpen_FEATURES_AECDESIGN_PROJECTSETUPBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Features_AECDesign_ProjectSetupBuilder.ja
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
#include <NXOpen/Features_Industry_ProjectStructureNode.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_features_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Features
    {
        namespace AECDesign
        {
            class ProjectSetupBuilder;
        }
    }
    class Builder;
    namespace Features
    {
        namespace Industry
        {
            class ProjectStructureNode;
        }
    }
    class Part;
    namespace Features
    {
        namespace AECDesign
        {
            class _ProjectSetupBuilderBuilder;
            class ProjectSetupBuilderImpl;
            /**  @brief 
                    Represents a project setup builder for AEC.
                     

             
                    
                    This builder is used to setup project in AEC. 
                    
                     <br> To create a new instance of this class, use @link NXOpen::Features::AECDesignCollection::CreateAecProjectSetupBuilder  NXOpen::Features::AECDesignCollection::CreateAecProjectSetupBuilder @endlink  <br> 
             <br>  Created in NX2007.0.0.  <br>  
            */
            class NXOPENCPP_FEATURESEXPORT  ProjectSetupBuilder : public NXOpen::Builder
            {
                private: ProjectSetupBuilderImpl * m_projectsetupbuilder_impl;
                private: friend class  _ProjectSetupBuilderBuilder;
                protected: ProjectSetupBuilder();
                public: ~ProjectSetupBuilder();
                /**Returns  the project name 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : None */
                public: NXString ProjectName
                (
                );
                /**Sets  the project name 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_bim ("AEC Design") */
                public: void SetProjectName
                (
                    const NXString & projectName /** projectname */ 
                );
                /**Sets  the project name 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_bim ("AEC Design") */
                void SetProjectName
                (
                    const char * projectName /** projectname */ 
                );
                /** Add shared parts 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_bim ("AEC Design") */
                public: void AddSharedParts
                (
                    const std::vector<NXOpen::Part *> & parts /** the parts used to add to shared node. */
                );
                /** Gets the structure root node.  @return  the root structure node. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Features::Industry::ProjectStructureNode * GetRootNode
                (
                );
                /**Returns  the flag to indicate whether it is new structure or not. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsNewStructure
                (
                );
                /**Sets  the flag to indicate whether it is new structure or not. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_bim ("AEC Design") */
                public: void SetNewStructure
                (
                    bool isNewStructure /** isnewstructure */ 
                );
                /**Returns  the flag to indicate whether it is to save as the shared part. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : None */
                public: bool IsSaveAsSharePart
                (
                );
                /**Sets  the flag to indicate whether it is to save as the shared part. 
                 <br>  Created in NX2007.0.0.  <br>  
                 <br> License requirements : nx_bim ("AEC Design") */
                public: void SetSaveAsSharePart
                (
                    bool isSaveAsSharePart /** issaveassharepart */ 
                );
            };
        }
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
