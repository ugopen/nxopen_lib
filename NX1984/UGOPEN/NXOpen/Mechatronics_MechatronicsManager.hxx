#ifndef NXOpen_MECHATRONICS_MECHATRONICSMANAGER_HXX_INCLUDED
#define NXOpen_MECHATRONICS_MECHATRONICSMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_MechatronicsManager.ja
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
#include <NXOpen/Mechatronics_SystemRoot.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_mechatronics_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Mechatronics
    {
        class MechatronicsManager;
    }
    class Part;
    namespace Mechatronics
    {
        class DependencyCreatorBuilder;
    }
    namespace Mechatronics
    {
        class ElectricalPartCollection;
    }
    namespace Mechatronics
    {
        class FunctionObjectCollection;
    }
    namespace Mechatronics
    {
        class LogicObjectCollection;
    }
    namespace Mechatronics
    {
        class RequirementCollection;
    }
    namespace Mechatronics
    {
        class SystemObject;
    }
    namespace Mechatronics
    {
        class SystemRoot;
    }
    class NXObject;
    namespace Mechatronics
    {
        class MechatronicsManagerImpl;
        /** Contains the collection objects for creating and iterating over Mechatronics Designer System Navigator objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
         <br>  Created in NX7.5.1.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  MechatronicsManager
        {
            private: MechatronicsManagerImpl * m_mechatronicsmanager_impl;
            private: NXOpen::Part* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit MechatronicsManager(NXOpen::Part *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~MechatronicsManager();
            /** Log entity to delete. Use this method to log entity to delete if the root part
                        is not work part.
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void LogEntityToDelete
            (
                NXOpen::NXObject * object /** object */ 
            );
            /** Exports function and(or) logical model to XML file. 
             <br>  @deprecated Deprecated in NX9.0.0.  Please use another method with the same name instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Please use another method with the same name instead.") void ExportModel
            (
                const NXString & path /** path */ ,
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Exports function and(or) logical model to XML file. 
             <br>  @deprecated Deprecated in NX9.0.0.  Please use another method with the same name instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void ExportModel
            (
                const char * path /** path */ ,
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Imports function and(or) logical model via XML file. 
             <br>  @deprecated Deprecated in NX9.0.0.  Please use another method with the same name instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Please use another method with the same name instead.") void ImportModel
            (
                const NXString & path /** path */ ,
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Imports function and(or) logical model via XML file. 
             <br>  @deprecated Deprecated in NX9.0.0.  Please use another method with the same name instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void ImportModel
            (
                const char * path /** path */ ,
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Saves the data model to teamcenter. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SaveToTeamcenter
            (
            );
            /** Refreshes function and(or) logical model from teamcenter. 
             <br>  @deprecated Deprecated in NX9.0.0.  Please use another method with the same name instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Please use another method with the same name instead.") void RefreshFromTeamcenter
            (
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Saves the data model to teamcenter. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void SaveToTeamcenter
            (
                bool requirement /** Save the Requirement Model? */,
                bool function /** Save the Function Model? */,
                bool logic /** Save the Logical Model? */
            );
            /** Exports data model to XML file. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void ExportModel
            (
                const NXString & path /** The path of XML file */,
                bool requirement /** Export the Requirement Model? */,
                bool function /** Export the Function Model? */,
                bool logic /** Export the Logical Model? */
            );
            /** Exports data model to XML file. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void ExportModel
            (
                const char * path /** The path of XML file */,
                bool requirement /** Export the Requirement Model? */,
                bool function /** Export the Function Model? */,
                bool logic /** Export the Logical Model? */
            );
            /** Imports data model from XML file. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void ImportModel
            (
                const NXString & path /** The path of XML file */,
                bool overrideModel /** Override the existing model? */,
                bool requirement /** Import the Requirement Model? */,
                bool function /** Import the Function Model? */,
                bool logic /** Import the Logical Model? */
            );
            /** Imports data model from XML file. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void ImportModel
            (
                const char * path /** The path of XML file */,
                bool overrideModel /** Override the existing model? */,
                bool requirement /** Import the Requirement Model? */,
                bool function /** Import the Function Model? */,
                bool logic /** Import the Logical Model? */
            );
            /** Refreshes data model in system navigator from teamcenter. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void RefreshFromTeamcenter
            (
                bool requirement /** Refresh the Requirement Model? */,
                bool function /** Refresh the Function Model? */,
                bool logic /** Refresh the Logical Model? */
            );
            /** Opens the specified function model. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void OpenFunctionModel
            (
                const NXString & itemMFKID /** The Item MFK ID of root function */,
                const NXString & variantRule /** The variant rule of root function */
            );
            /** Opens the specified function model. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void OpenFunctionModel
            (
                const char * itemMFKID /** The Item MFK ID of root function */,
                const char * variantRule /** The variant rule of root function */
            );
            /** Opens the specified logical model. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void OpenLogicalModel
            (
                const NXString & itemMFKID /** The Item MFK ID of root logical */,
                const NXString & variantRule /** The variant rule of root logical */
            );
            /** Opens the specified logical model. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void OpenLogicalModel
            (
                const char * itemMFKID /** The Item MFK ID of root logical */,
                const char * variantRule /** The variant rule of root logical */
            );
            /** Opens the specified requirement model. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void OpenRequirementModel
            (
                const NXString & itemMFKID /** The Item MFK ID of root requirement */,
                const NXString & variantRule /** The variant rule of root requirement */
            );
            /** Opens the specified requirement model. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void OpenRequirementModel
            (
                const char * itemMFKID /** The Item MFK ID of root requirement */,
                const char * variantRule /** The variant rule of root requirement */
            );
            /** Adds existing function as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void AddExistingFunction
            (
                NXOpen::Mechatronics::SystemObject * object /** The parent object */,
                const NXString & itemMFKID /** The Item MFK ID of child function item */,
                const NXString & instanceName /** The instance name of child function item */
            );
            /** Adds existing function as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void AddExistingFunction
            (
                NXOpen::Mechatronics::SystemObject * object /** The parent object */,
                const char * itemMFKID /** The Item MFK ID of child function item */,
                const char * instanceName /** The instance name of child function item */
            );
            /** Adds existing logical as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void AddExistingLogical
            (
                NXOpen::Mechatronics::SystemObject * object /** The parent object */,
                const NXString & itemMFKID /** The Item MFK ID of child logical item */,
                const NXString & instanceName /** The instance name of child logical item */
            );
            /** Adds existing logical as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void AddExistingLogical
            (
                NXOpen::Mechatronics::SystemObject * object /** The parent object */,
                const char * itemMFKID /** The Item MFK ID of child logical item */,
                const char * instanceName /** The instance name of child logical item */
            );
            /** Adds existing requirement as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void AddExistingRequirement
            (
                NXOpen::Mechatronics::SystemObject * object /** The parent object */,
                const NXString & itemMFKID /** The Item MFK ID of child requirement item */,
                const NXString & instanceName /** The instance name of child requirement item */
            );
            /** Adds existing requirement as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            void AddExistingRequirement
            (
                NXOpen::Mechatronics::SystemObject * object /** The parent object */,
                const char * itemMFKID /** The Item MFK ID of child requirement item */,
                const char * instanceName /** The instance name of child requirement item */
            );
            /** Adds existing requirement as tracelink of specified object. 
             <br>  @deprecated Deprecated in NX9.0.0.  Please use @link SystemObject::CreateTraceLink SystemObject::CreateTraceLink@endlink  instead. <br>  

             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NX_DEPRECATED("Deprecated in NX9.0.0.  Please use SystemObject::CreateTraceLink instead.") void PasteTraceLink
            (
                NXOpen::Mechatronics::SystemObject * object /** object */ 
            );
            /** Creates a system root object in specified part.  @return  Return the system root 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::SystemRoot * CreateSystemRoot
            (
                NXOpen::Mechatronics::SystemRoot::Type rootType /** The type of system root */
            );
            /** Creates a @link NXOpen::Mechatronics::DependencyCreatorBuilder NXOpen::Mechatronics::DependencyCreatorBuilder@endlink  object.  @return  DependencyCreator Builder 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::DependencyCreatorBuilder * CreateDependencyCreatorBuilder
            (
            );
            /** Loads the data models as saved in last time.  @return  Return information if some item revisions are deleted 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXString LoadAsSaved
            (
            );
            /**  @brief  Gets the system root object in the specified part.  

               @return  Return the system root 
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: NXOpen::Mechatronics::SystemRoot * GetSystemRoot
            (
                NXOpen::Mechatronics::SystemRoot::Type rootType /** The type of system root */
            );
            /**  @brief  Copies the system engeering objects to the clipboard.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void CopySystemObject
            (
                const std::vector<NXOpen::Mechatronics::SystemObject *> & objects /** The objects to be copied */
            );
            /**  @brief  Cuts the system engeering objects.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void CutSystemObject
            (
                const std::vector<NXOpen::Mechatronics::SystemObject *> & objects /** The objects to be cutted */
            );
            /**  @brief  Pastes the system engeering objects from the clipboard.  

              
             <br>  Created in NX11.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("Mechatronics Concept Designer") */
            public: void PasteSystemObject
            (
                NXOpen::Mechatronics::SystemObject * parent /** parent */ 
            );


            /** Returns the FunctionObjectCollection instance belonging to this part 
             <br>  Created in NX7.5.0.  <br>  
            */
            public: NXOpen::Mechatronics::FunctionObjectCollection *FunctionObjectCollection();
            /** Returns the LogicObjectCollection instance belonging to this part 
             <br>  Created in NX8.5.0.  <br>  
            */
            public: NXOpen::Mechatronics::LogicObjectCollection *LogicObjectCollection();
            /** Returns the RequirementCollection instance belonging to this part 
             <br>  Created in NX8.5.0.  <br>  
            */
            public: NXOpen::Mechatronics::RequirementCollection *RequirementCollection();
            /** Returns the ElectricalPartCollection instance belonging to this part 
             <br>  Created in NX9.0.0.  <br>  
            */
            public: NXOpen::Mechatronics::ElectricalPartCollection *ElectricalPartCollection();
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