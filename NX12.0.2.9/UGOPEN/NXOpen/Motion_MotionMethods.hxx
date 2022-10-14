#ifndef NXOpen_MOTION_MOTIONMETHODS_HXX_INCLUDED
#define NXOpen_MOTION_MOTIONMETHODS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Motion_MotionMethods.ja
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
#include <NXOpen/libnxopencpp_motion_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Motion
    {
        class MotionMethods;
    }
    namespace Motion
    {
        class MotionSession;
    }
    class NXObject;
    namespace Motion
    {
        class MotionMethodsImpl;
        /**Represents a @link NXOpen::Motion::MotionMethods NXOpen::Motion::MotionMethods@endlink  class <br> To obtain an instance of this class, refer to @link NXOpen::Motion::MotionSession  NXOpen::Motion::MotionSession @endlink  <br> 
         <br>  Created in NX8.0.0.  <br>  
        */
        class NXOPENCPP_MOTIONEXPORT  MotionMethods
        {
            private: MotionMethodsImpl * m_motionmethods_impl;
            private: NXOpen::Motion::MotionSession* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit MotionMethods(NXOpen::Motion::MotionSession *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~MotionMethods();
            /** Copies the connector parameters 
             <br>  @deprecated Deprecated in NX12.0.0.  Use @link MotionMethods::CopyParameters MotionMethods::CopyParameters@endlink  instead. <br>  

             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: NX_DEPRECATED("Deprecated in NX12.0.0.  Use MotionMethods::CopyParameters instead.") void CopyConnectorParameters
            (
                NXOpen::NXObject * sourceConnector /** Source connector from which parameters are copied */,
                NXOpen::NXObject * destinationConnector /** Destination connector to which the parameters are copied */
            );
            /** Check all motion objects 
             <br>  Created in NX8.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void ModelCheck
            (
                bool listWarning /** whether to display the checking result if only warnings found without error */
            );
            /** Copy parameters from source to destination. Source and Destination must be of the same type.
                         Only objects that support this command in Motion Navigator are supported. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void CopyParameters
            (
                NXOpen::NXObject * source /** Source object from which parameters are copied */,
                NXOpen::NXObject * destination /** Destination object to which the parameters are copied */
            );
            /** Export parameters of an entity into a txt file.
                        Only objects that support this command in Motion Navigator are supported. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void ExportParameters
            (
                NXOpen::NXObject * entity /** entity to export */,
                const NXString & fileName /** file to export to */
            );
            /** Export parameters of an entity into a txt file.
                        Only objects that support this command in Motion Navigator are supported. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void ExportParameters
            (
                NXOpen::NXObject * entity /** entity to export */,
                const char * fileName /** file to export to */
            );
            /** Import parameters of an object into a txt file.
                        Only objects that support this command in Motion Navigator are supported. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            public: void ImportParameters
            (
                NXOpen::NXObject * entity /** entity to import */,
                const NXString & fileName /** file to import from */
            );
            /** Import parameters of an object into a txt file.
                        Only objects that support this command in Motion Navigator are supported. 
             <br>  Created in NX12.0.0.  <br>  
             <br> License requirements : mechanisms ("MECHANISMS") */
            void ImportParameters
            (
                NXOpen::NXObject * entity /** entity to import */,
                const char * fileName /** file to import from */
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