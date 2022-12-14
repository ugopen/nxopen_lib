#ifndef NXOpen_PDM_PARTOPERATIONCOPYBUILDER_HXX_INCLUDED
#define NXOpen_PDM_PARTOPERATIONCOPYBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PDM_PartOperationCopyBuilder.ja
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
#include <NXOpen/BasePart.hxx>
#include <NXOpen/PDM_PartOperationBuilder.hxx>
#include <NXOpen/PDM_PartOperationBuilder.hxx>
#include <NXOpen/libnxopencpp_pdm_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PDM
    {
        class PartOperationCopyBuilder;
    }
    class BasePart;
    namespace PDM
    {
        class LogicalObject;
    }
    namespace PDM
    {
        class PartOperationBuilder;
    }
    class Part;
    namespace PDM
    {
        class _PartOperationCopyBuilderBuilder;
        class PartOperationCopyBuilderImpl;
        /** Represents a builder class that performs various Save As operations.  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateCopyOperationBuilder  NXOpen::PDM::PdmSession::CreateCopyOperationBuilder @endlink  <br> 
         <br>  Created in NX10.0.0.  <br>  
        */
        class NXOPENCPP_PDMEXPORT  PartOperationCopyBuilder : public NXOpen::PDM::PartOperationBuilder
        {
            /** This enum is used to specify which non-master parts 
                    should be copied to new part during the save as operation. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::CopyNonMasterPartsOption NXOpen::PDM::NonMasterData::CopyNonMasterPartsOption@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
            */
            public: enum NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::PDM::NonMasterData::CopyNonMasterPartsOption instead") CopyNonMasterParts
            {
                CopyNonMasterPartsAll/** save all during save as */,
                CopyNonMasterPartsNone/** save none during save as */
            };

            /** This enum is used to specify which dependent files
                    should be copied to new part during the save as operation. 
             <br>  Created in NX10.0.0.  <br>  
            */
            public: enum CopyDependentFiles
            {
                CopyDependentFilesAll/** save all during save as */,
                CopyDependentFilesNone/** save none during save as */
            };

            /** Represents an operation sub type for copying a part */
            public: enum OperationSubType
            {
                OperationSubTypeDefault/** Save As dialog */,
                OperationSubTypeMakeUnique/** MakeUnique flavour of Save As dialog */
            };

            private: PartOperationCopyBuilderImpl * m_partoperationcopybuilder_impl;
            private: friend class  _PartOperationCopyBuilderBuilder;
            protected: PartOperationCopyBuilder();
            public: ~PartOperationCopyBuilder();
            /** Sets the selected parts. Applicable only for operation types
                        @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                        @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
                        Also returns an array of parts failed to added, these are not removed from the input array though.
                        @link NXOpen::PDM::PartOperationBuilder::GetOperationFailures NXOpen::PDM::PartOperationBuilder::GetOperationFailures@endlink  can be called to get the errors occurred
                        during this operation.
                        
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSelectedPartsToCopy
            (
                const std::vector<NXOpen::BasePart *> & selectedParts /** selectedparts */ ,
                std::vector<NXOpen::BasePart *> & failedParts /** failedparts */ 
            );
            /**Returns  the replace all components. This option specifies whether part will be replaced or copied.             
                        Applicable only for operation types 
                        @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                        @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool ReplaceAllComponentsInSession
            (
            );
            /**Sets  the replace all components. This option specifies whether part will be replaced or copied.             
                        Applicable only for operation types 
                        @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                        @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReplaceAllComponentsInSession
            (
                bool replaceAllComponents /** replaceallcomponents */ 
            );
            /** Add related part to the part undergoing an operation. Example: if user selects a part
                        for Save As which has Linked Part Modules that should also undergo Save As, they should
                        be added as related parts.
                        Applicable only for operation types 
                        @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                        @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void AddRelatedPartsToCopy
            (
                NXOpen::BasePart * basePart /** basepart */ ,
                const std::vector<NXOpen::BasePart *> & relatedParts /** relatedparts */ ,
                std::vector<NXString> & relatedPartsReasons /** relatedpartsreasons */ ,
                NXOpen::PDM::PartOperationBuilder::OperationType operation /** operation */ 
            );
            /** Create NonMaster list for the selected logical Object 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::CreateNonMasterListForLogicalObject NXOpen::PDM::NonMasterData::CreateNonMasterListForLogicalObject@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::PDM::NonMasterData::CreateNonMasterListForLogicalObject instead") void CreateNonMasterListForCopyLogicalObject
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ 
            );
            /** Gets NonMaster list for the given logical Object  @return  Non-master part file names 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::GetNonMasterListForCopyLogicalObject NXOpen::PDM::NonMasterData::GetNonMasterListForCopyLogicalObject@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::PDM::NonMasterData::GetNonMasterListForCopyLogicalObject instead") std::vector<NXString> GetNonMasterListForCopyLogicalObject
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ 
            );
            /** Returns whether or not the non-master part specified for the given @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink will actually
                    get saved during the save as operation.  @return  True means that this non-master will be saved.
                            False means that this non-master will not be saved. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::IsNonMasterForLogicalObjectBeingCopied NXOpen::PDM::NonMasterData::IsNonMasterForLogicalObjectBeingCopied@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::PDM::NonMasterData::IsNonMasterForLogicalObjectBeingCopied instead") bool IsNonMasterForLogicalObjectBeingCopied
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ ,
                const NXString & partName /** the non-master part that the caller wants to save or not save */
            );
            /** Returns whether or not the non-master part specified for the given @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink will actually
                    get saved during the save as operation.  @return  True means that this non-master will be saved.
                            False means that this non-master will not be saved. 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::IsNonMasterForLogicalObjectBeingCopied NXOpen::PDM::NonMasterData::IsNonMasterForLogicalObjectBeingCopied@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            bool IsNonMasterForLogicalObjectBeingCopied
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ ,
                const char * partName /** the non-master part that the caller wants to save or not save */
            );
            /**Get the nonmasters saveAs option for given logical object. Save As option can be one of these
                    @link PartOperationCopyBuilder::CopyNonMasterPartsAll PartOperationCopyBuilder::CopyNonMasterPartsAll@endlink  and 
                    @link PartOperationCopyBuilder::CopyNonMasterPartsNone PartOperationCopyBuilder::CopyNonMasterPartsNone@endlink  @return  
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::GetCopyNonMasterPartsOption NXOpen::PDM::NonMasterData::GetCopyNonMasterPartsOption@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::PDM::NonMasterData::GetCopyNonMasterPartsOption instead") NXOpen::PDM::PartOperationCopyBuilder::CopyNonMasterParts GetCopyNonMasterPartsOption
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ 
            );
            /**Set the nonmasters saveAs option for given logical object. Save As option can be one of these
                    @link PartOperationCopyBuilder::CopyNonMasterPartsAll PartOperationCopyBuilder::CopyNonMasterPartsAll@endlink  and 
                    @link PartOperationCopyBuilder::CopyNonMasterPartsNone PartOperationCopyBuilder::CopyNonMasterPartsNone@endlink 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::SetNonMasterSaveAsOption NXOpen::PDM::NonMasterData::SetNonMasterSaveAsOption@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::PDM::NonMasterData::SetNonMasterSaveAsOption instead") void SetCopyNonMasterPartsOption
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ ,
                NXOpen::PDM::PartOperationCopyBuilder::CopyNonMasterParts saveOption /** saveoption */ 
            );
            /** Sets whether or not the non-master part specified will actually
                    get saved during the save as operation. True means that it will be
                    saved. False means that it will not be saved.  
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::SetSelectedNonMasterToCopy NXOpen::PDM::NonMasterData::SetSelectedNonMasterToCopy@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::PDM::NonMasterData::SetSelectedNonMasterToCopy instead") void SetSelectedNonMasterToCopy
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ ,
                const NXString & partName /** the non-master part whose save option is being set here */
            );
            /** Sets whether or not the non-master part specified will actually
                    get saved during the save as operation. True means that it will be
                    saved. False means that it will not be saved.  
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::SetSelectedNonMasterToCopy NXOpen::PDM::NonMasterData::SetSelectedNonMasterToCopy@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            void SetSelectedNonMasterToCopy
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ ,
                const char * partName /** the non-master part whose save option is being set here */
            );
            /** Sets the name the non-master part will get saved as. It will get saved as the
                    original non-master name if this method is not called.  @return  flag to indicate whether the newName is valid 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::EditNonMasterToCopyName NXOpen::PDM::NonMasterData::EditNonMasterToCopyName@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NX_DEPRECATED("Deprecated in NX11.0.0.  Use NXOpen::PDM::NonMasterData::EditNonMasterToCopyName instead") bool EditNonMasterToCopyName
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ ,
                const NXString & oldName /** the non-master part whose save as name is being set here */,
                const NXString & newName /** the new name */
            );
            /** Sets the name the non-master part will get saved as. It will get saved as the
                    original non-master name if this method is not called.  @return  flag to indicate whether the newName is valid 
             <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::EditNonMasterToCopyName NXOpen::PDM::NonMasterData::EditNonMasterToCopyName@endlink  instead <br>  

             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            bool EditNonMasterToCopyName
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ ,
                const char * oldName /** the non-master part whose save as name is being set here */,
                const char * newName /** the new name */
            );
            /**Returns  the Dependent files Save As option. Save As option can be one of these
                    @link PartOperationCopyBuilder::CopyDependentFilesAll PartOperationCopyBuilder::CopyDependentFilesAll@endlink  and 
                    @link PartOperationCopyBuilder::CopyDependentFilesNone PartOperationCopyBuilder::CopyDependentFilesNone@endlink 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::PartOperationCopyBuilder::CopyDependentFiles DependentFilesToCopyOption
            (
            );
            /**Sets  the Dependent files Save As option. Save As option can be one of these
                    @link PartOperationCopyBuilder::CopyDependentFilesAll PartOperationCopyBuilder::CopyDependentFilesAll@endlink  and 
                    @link PartOperationCopyBuilder::CopyDependentFilesNone PartOperationCopyBuilder::CopyDependentFilesNone@endlink 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetDependentFilesToCopyOption
            (
                NXOpen::PDM::PartOperationCopyBuilder::CopyDependentFiles saveOption /** saveoption */ 
            );
            /** Returns the @link NXOpen::PDM::PartOperationCopyBuilder::OperationSubType NXOpen::PDM::PartOperationCopyBuilder::OperationSubType@endlink  for Create.  @return  
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PDM::PartOperationCopyBuilder::OperationSubType GetOperationSubType
            (
            );
            /** Sets the @link NXOpen::PDM::PartOperationCopyBuilder::OperationSubType NXOpen::PDM::PartOperationCopyBuilder::OperationSubType@endlink  for Create. 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOperationSubType
            (
                NXOpen::PDM::PartOperationCopyBuilder::OperationSubType operationSubType /** operationsubtype */ 
            );
            /** Returns the source part of this logical object.  @return  
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : None */
            public: NXOpen::Part * GetSourcePartFromLogicalObject
            (
                NXOpen::PDM::LogicalObject * logicalObject /** logicalobject */ 
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
