#ifndef NXOpen_PARTFAMILY_TEMPLATEMANAGER_HXX_INCLUDED
#define NXOpen_PARTFAMILY_TEMPLATEMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PartFamily_TemplateManager.ja
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
#include <NXOpen/PartFamily_FamilyAttribute.hxx>
#include <NXOpen/PartFamily_InstanceDefinition.hxx>
#include <NXOpen/PartFamily_Template.hxx>
#include <NXOpen/TransientObject.hxx>
#include <NXOpen/libnxopencpp_partfamily_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PartFamily
    {
        class TemplateManager;
    }
    namespace PartFamily
    {
        class FamilyAttribute;
    }
    namespace PartFamily
    {
        class InstanceDefinition;
    }
    namespace PartFamily
    {
        class Template;
    }
    namespace PartFamily
    {
        class TemplateManagerImpl;
        /** This class serves as the manager for all the part family related operations. 
                All operations that create, edit or delete part family objects are done through this class. 
                Use the method @link Part::NewPartFamilyTemplateManager Part::NewPartFamilyTemplateManager@endlink 
                to create new instance of this class.
             
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_PARTFAMILYEXPORT  TemplateManager : public TransientObject
        {
            private: TemplateManagerImpl * m_templatemanager_impl;
            /// \cond NX_NO_DOC 
            public: explicit TemplateManager(void *ptr);
            /// \endcond 
            /** Free resources associated with the instance. After this method
                        is called, it is illegal to use the object.  In .NET, this method
                        is automatically called when the object is deleted by the garbage collector
                     
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: virtual ~TemplateManager();
            /** The list of attribute names of a given type in the owning part
                        These can be used to create part family attributes
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXString> GetSelectableAttributes
            (
                NXOpen::PartFamily::FamilyAttribute::AttrType attrType /** attrtype */ 
            );
            /** Deletes a given part family attribute 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void DeletePartFamilyAttribute
            (
                NXOpen::PartFamily::FamilyAttribute * partFamilyAttribute /** partfamilyattribute */ 
            );
            /** Returns the attributes on the template manager
                        These might include the attributes which have not yet been committed onto the core object and have only been created by this instance of the manager.
                        "Use @link Template::GetAttributes Template::GetAttributes@endlink  to get the committed attributes"   
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<NXOpen::PartFamily::FamilyAttribute *> GetChosenAttributes
            (
            );
            /** Adds new attributes to chosen attributes list of a part family 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void AddToChosenAttributes
            (
                std::vector<NXString> & attrsToAdd /** attrstoadd */ ,
                const std::vector<NXOpen::PartFamily::FamilyAttribute::AttrType> & attrsTypes /** attrstypes */ ,
                int indexAddAt /** indexaddat */ 
            );
            /** Adds new attribute of type asserted mass to chosen attributes list of a part family 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES"), solid_modeling ("SOLIDS MODELING") */
            public: void AddAssertedMassToChosenAttributes
            (
                const NXString & attrToAdd /** attrtoadd */ ,
                int indexAddAt /** indexaddat */ 
            );
            /** Adds new attribute of type asserted mass to chosen attributes list of a part family 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : adv_assemblies ("ADVANCED ASSEMBLIES"), solid_modeling ("SOLIDS MODELING") */
            void AddAssertedMassToChosenAttributes
            (
                const char * attrToAdd /** attrtoadd */ ,
                int indexAddAt /** indexaddat */ 
            );
            /** Move down the specified attributes of a part family by the moveDownCount. 
                        If the attributes cannot be moved down by the specified count, this method will execute the 
                        partial move and return the count that the attributes are actually moved down by.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: int MoveDownAttributes
            (
                const std::vector<NXOpen::PartFamily::FamilyAttribute *> & moveDownAttrs /** movedownattrs */ ,
                int moveDownCount /** movedowncount */ 
            );
            /** Move up the specified attributes of a part family by the moveUpCount. 
                        If the attributes cannot be moved up by the specified count, this method will execute the 
                        partial move and return the count that the attributes are actually moved up by.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: int MoveUpAttributes
            (
                const std::vector<NXOpen::PartFamily::FamilyAttribute *> & moveUpAttrs /** moveupattrs */ ,
                int moveUpCount /** moveupcount */ 
            );
            /** Cut selected attributes of a part family. These will be pasted during paste operation.
                        If previously cut attributes are present then they will be lost because the new ones
                        will overwrite them.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void CutAttributes
            (
                const std::vector<NXOpen::PartFamily::FamilyAttribute *> & cutAttrs /** cutattrs */ 
            );
            /** Paste the cut attributes of a part family. The pasteAfter attribute must be present in
                        chosen attributes list for this operation to succeed.
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void PasteAttributes
            (
                NXOpen::PartFamily::FamilyAttribute * pasteAfter /** pasteafter */ 
            );
            /**Sets  the importable flag value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetImportable
            (
                bool isImportable /** isimportable */ 
            );
            /**Returns  the importable flag value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: bool Importable
            (
            );
            /**Sets  the save directory path value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SetSaveDirectory
            (
                const NXString & saveDirectory /** savedirectory */ 
            );
            /**Sets  the save directory path value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            void SetSaveDirectory
            (
                const char * saveDirectory /** savedirectory */ 
            );
            /**Returns  the save directory path value 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXString SaveDirectory
            (
            );
            /** Creates a part family associated with the owning part  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::PartFamily::Template * CreatePartFamily
            (
            );
            /** Edits a part family associated with the manager/owning part 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void EditPartFamily
            (
            );
            /** Deletes a part family associated with the manager/owning part 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void DeletePartFamily
            (
            );
            /** Creates a part family member if it doesn't exist on disk. @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXString EstablishFamilyInstance
            (
                const NXString & memberName /** membername */ 
            );
            /** Creates a part family member if it doesn't exist on disk. @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            NXString EstablishFamilyInstance
            (
                const char * memberName /** membername */ 
            );
            /** Get the family member definition already present in family @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::PartFamily::InstanceDefinition * GetInstanceDefinition
            (
                const NXString & familyMemberDefnName /** familymemberdefnname */ 
            );
            /** Get the family member definition already present in family @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            NXOpen::PartFamily::InstanceDefinition * GetInstanceDefinition
            (
                const char * familyMemberDefnName /** familymemberdefnname */ 
            );
            /** Creates a new family member definition with the supplied name and places it just under previous family member definition.
                        If the part family is importable, then the otherNameEntry is a mandatory input.
                        Depending on whether we are in managed mode or native, familyMemberDefn name may be os_part_name or 
                        db_part_name, and otherNameEntry may be db_part_name or os_part_name.
                        In case of non-importable part family otherName Entry may be empty.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::PartFamily::InstanceDefinition * AddInstanceDefinition
            (
                const NXString & familyMemberDefnName /** familymemberdefnname */ ,
                NXOpen::PartFamily::InstanceDefinition * previousFamilyMemberDefn /** previousfamilymemberdefn */ ,
                const NXString & otherNameEntry /** othernameentry */ 
            );
            /** Creates a new family member definition with the supplied name and places it just under previous family member definition.
                        If the part family is importable, then the otherNameEntry is a mandatory input.
                        Depending on whether we are in managed mode or native, familyMemberDefn name may be os_part_name or 
                        db_part_name, and otherNameEntry may be db_part_name or os_part_name.
                        In case of non-importable part family otherName Entry may be empty.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            NXOpen::PartFamily::InstanceDefinition * AddInstanceDefinition
            (
                const char * familyMemberDefnName /** familymemberdefnname */ ,
                NXOpen::PartFamily::InstanceDefinition * previousFamilyMemberDefn /** previousfamilymemberdefn */ ,
                const char * otherNameEntry /** othernameentry */ 
            );
            /** Delete the family member defintion from template manager
                    
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void DeleteInstanceDefinition
            (
                NXOpen::PartFamily::InstanceDefinition * familyMemberDefinition /** familymemberdefinition */ 
            );
            /** Reorder (relocate) familyMemberDefinition just after the previousFamilyMemberDefn
                     
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void ReorderInstanceDefinition
            (
                NXOpen::PartFamily::InstanceDefinition * familyMemberDefinition /** familymemberdefinition */ ,
                NXOpen::PartFamily::InstanceDefinition * previousFamilyMemberDefn /** previousfamilymemberdefn */ 
            );
            /** Save the changes in template manager to core part family
                     
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: void SavePartFamily
            (
            );
            /** Get the part family attribute from part family template  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::PartFamily::FamilyAttribute * GetPartFamilyAttribute
            (
                NXOpen::PartFamily::FamilyAttribute::AttrType attrType /** attrtype */ ,
                const NXString & attrName /** attrname */ 
            );
            /** Get the part family attribute from part family template  @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            NXOpen::PartFamily::FamilyAttribute * GetPartFamilyAttribute
            (
                NXOpen::PartFamily::FamilyAttribute::AttrType attrType /** attrtype */ ,
                const char * attrName /** attrname */ 
            );
            /** Save part family and create the family members supplied through input array. It returns success
                        and failure codes via errorCodes array.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<int> SaveFamilyAndCreateMembers
            (
                const std::vector<NXOpen::PartFamily::InstanceDefinition *> & instDefsToCreate /** instdefstocreate */ 
            );
            /** Save part family and update the family members supplied through input array. It returns success
                        and failure codes via errorCodes array.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: std::vector<int> SaveFamilyAndUpdateMembers
            (
                bool forceUpdate /** forceupdate */ ,
                const std::vector<NXOpen::PartFamily::InstanceDefinition *> & instDefsToUpdate /** instdefstoupdate */ 
            );
            /** Save part family and apply the values of chosen family member definition to the template part,
                        It returns failure codes through errorCode.
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: int SaveFamilyAndApplyValues
            (
                NXOpen::PartFamily::InstanceDefinition * familyMemberDefinition /** familymemberdefinition */ 
            );
            /** Get the part family template 
                        This method may return NULL if there is no template associated with the templatemanager
                     @return  
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: NXOpen::PartFamily::Template * GetPartFamilyTemplate
            (
            );
        }; //lint !e1712 default constructor not defined for class  

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