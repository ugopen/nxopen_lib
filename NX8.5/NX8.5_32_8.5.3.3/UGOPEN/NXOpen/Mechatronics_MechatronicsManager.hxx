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
    class NXObject;
    namespace Mechatronics
    {
        class MechatronicsManagerImpl;
        /** Contains the collection objects for creating and iterating over Mechatronics Designer System Navigator objects.  <br> To obtain an instance of this class, refer to @link Part  Part @endlink  <br> 
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
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void LogEntityToDelete
            (
                NXOpen::NXObject * object /** object */ 
            );
            /** Exports function and(or) logical model to XML file. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void ExportModel
            (
                const NXString & path /** path */ ,
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Exports function and(or) logical model to XML file. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void ExportModel
            (
                const char * path /** path */ ,
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Imports function and(or) logical model via XML file. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void ImportModel
            (
                const NXString & path /** path */ ,
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Imports function and(or) logical model via XML file. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void ImportModel
            (
                const char * path /** path */ ,
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Saves the function and logical model to teamcenter. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void SaveToTeamcenter
            (
            );
            /** Refreshes function and(or) logical model from teamcenter. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void RefreshFromTeamcenter
            (
                bool bFunction /** bfunction */ ,
                bool bLogical /** blogical */ 
            );
            /** Opens the specified function model. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void OpenFunctionModel
            (
                const NXString & itemID /** itemid */ ,
                const NXString & revisionID /** revisionid */ 
            );
            /** Opens the specified function model. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void OpenFunctionModel
            (
                const char * itemID /** itemid */ ,
                const char * revisionID /** revisionid */ 
            );
            /** Opens the specified logical model. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void OpenLogicalModel
            (
                const NXString & itemID /** itemid */ ,
                const NXString & revisionID /** revisionid */ 
            );
            /** Opens the specified logical model. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void OpenLogicalModel
            (
                const char * itemID /** itemid */ ,
                const char * revisionID /** revisionid */ 
            );
            /** Adds existing function as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void AddExistingFunction
            (
                NXOpen::Mechatronics::SystemObject * object /** object */ ,
                const NXString & itemID /** itemid */ ,
                const NXString & revisionID /** revisionid */ 
            );
            /** Adds existing function as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void AddExistingFunction
            (
                NXOpen::Mechatronics::SystemObject * object /** object */ ,
                const char * itemID /** itemid */ ,
                const char * revisionID /** revisionid */ 
            );
            /** Adds existing logical as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void AddExistingLogical
            (
                NXOpen::Mechatronics::SystemObject * object /** object */ ,
                const NXString & itemID /** itemid */ ,
                const NXString & revisionID /** revisionid */ 
            );
            /** Adds existing logical as children of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void AddExistingLogical
            (
                NXOpen::Mechatronics::SystemObject * object /** object */ ,
                const char * itemID /** itemid */ ,
                const char * revisionID /** revisionid */ 
            );
            /** Adds existing requirement as tracelink of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void AddExistingRequirement
            (
                NXOpen::Mechatronics::SystemObject * object /** object */ ,
                const NXString & itemID /** itemid */ ,
                const NXString & revisionID /** revisionid */ 
            );
            /** Adds existing requirement as tracelink of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            void AddExistingRequirement
            (
                NXOpen::Mechatronics::SystemObject * object /** object */ ,
                const char * itemID /** itemid */ ,
                const char * revisionID /** revisionid */ 
            );
            /** Adds existing requirement as tracelink of specified object. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void PasteTraceLink
            (
                NXOpen::Mechatronics::SystemObject * object /** object */ 
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
