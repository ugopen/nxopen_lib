#ifndef NXOpen_VALIDATE_PERSISTENTRESULT_HXX_INCLUDED
#define NXOpen_VALIDATE_PERSISTENTRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Validate_PersistentResult.ja
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
#include <NXOpen/NXObject.hxx>
#include <NXOpen/Validation.hxx>
#include <NXOpen/libnxopencpp_validate_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Validate
    {
        class PersistentResult;
    }
    class NXObject;
    class TaggedObject;
    namespace Validate
    {
        class _PersistentResultBuilder;
        class PersistentResultImpl;
        /**
             Represents a @link NXOpen::Validate::PersistentResult NXOpen::Validate::PersistentResult@endlink  object.
            
         <br>  Created in NX1872.0.0.  <br>  
        */
        class NXOPENCPP_VALIDATEEXPORT  PersistentResult : public NXOpen::NXObject
        {
            private: PersistentResultImpl * m_persistentresult_impl;
            private: friend class  _PersistentResultBuilder;
            protected: PersistentResult();
            public: ~PersistentResult();
            /** Add the @link Validate::PersistentResult Validate::PersistentResult@endlink  tracking objects.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void AddTrackingObjects
            (
                const NXString & key /** key */ ,
                const std::vector<NXOpen::TaggedObject *> & objects /** objects */ 
            );
            /** Add the @link Validate::PersistentResult Validate::PersistentResult@endlink  tracking objects.
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            void AddTrackingObjects
            (
                const char * key /** key */ ,
                const std::vector<NXOpen::TaggedObject *> & objects /** objects */ 
            );
            /** Get the @link Validate::PersistentResult Validate::PersistentResult@endlink  tracking objects which trigger the @link Validate::PersistentResult Validate::PersistentResult@endlink  re-run when modified. For example, if a PersistentResult tracks a Face, it will re-run when the Face is modfied. @return   
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::TaggedObject *> GetTrackingObjects
            (
                const NXString & key /** key */ 
            );
            /** Get the @link Validate::PersistentResult Validate::PersistentResult@endlink  tracking objects which trigger the @link Validate::PersistentResult Validate::PersistentResult@endlink  re-run when modified. For example, if a PersistentResult tracks a Face, it will re-run when the Face is modfied. @return   
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            std::vector<NXOpen::TaggedObject *> GetTrackingObjects
            (
                const char * key /** key */ 
            );
            /**Returns  the checker class id. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXString CheckerClassId
            (
            );
            /**Sets  the checker class id. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetCheckerClassId
            (
                const NXString & classId /** class id */ 
            );
            /**Sets  the checker class id. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            void SetCheckerClassId
            (
                const char * classId /** class id */ 
            );
            /**Returns  the error level. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Validation::Result ErrorLevel
            (
            );
            /**Sets  the error level. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: void SetErrorLevel
            (
                NXOpen::Validation::Result errorLevel /** error level */ 
            );
            /**Returns  the result's uptodate status. 
             <br>  Created in NX1872.0.0.  <br>  
             <br> License requirements : None */
            public: bool UpToDateStatus
            (
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
