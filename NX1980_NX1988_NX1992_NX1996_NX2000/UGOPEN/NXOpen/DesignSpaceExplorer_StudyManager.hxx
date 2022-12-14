#ifndef NXOpen_DESIGNSPACEEXPLORER_STUDYMANAGER_HXX_INCLUDED
#define NXOpen_DESIGNSPACEEXPLORER_STUDYMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     DesignSpaceExplorer_StudyManager.ja
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
#include <NXOpen/libdesignspaceexploreropencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace DesignSpaceExplorer
    {
        class StudyManager;
    }
    class Session;
    class Part;
    namespace DesignSpaceExplorer
    {
        class StudyManagerImpl;

        /// \cond NX_NO_DOC 
        /** Represents the Design Space Explorer Study Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX1980.0.0.  <br>  
        */
        class DESIGNSPACEEXPLOREROPENCPPEXPORT  StudyManager
        {
            private: StudyManagerImpl * m_studymanager_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit StudyManager(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            private: static StudyManager* theStudyManager;
            /** Returns the StudyManager object for the running session which serves as the 'gateway' class for the application API.  
                References to all other objects in this API are obtained either directly or indirectly via methods and properties on this class.  
                Platform Session should be initialized using 'GetSession' method from NXOpen API prior to this call.  
            */
            public: static StudyManager* GetStudyManager(NXOpen::Session *owner);
            public: ~StudyManager();

            /// \cond NX_NO_DOC 
            /** Set the active study in the work part 
             <br>  Created in NX1980.0.0.  <br>  
             <br> License requirements : None */
            public: void UpdateActiveStudy
            (
                NXOpen::Part * part /** part */ 
            );

            /// \endcond 
        }; //lint !e1712 default constructor not defined for class  


        /// \endcond 
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
