#ifndef NXOpen_MECHATRONICS_MECHATRONICSSESSION_HXX_INCLUDED
#define NXOpen_MECHATRONICS_MECHATRONICSSESSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Mechatronics_MechatronicsSession.ja
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
        class MechatronicsSession;
    }
    class Session;
    namespace Mechatronics
    {
        class LogicObject;
    }
    namespace Mechatronics
    {
        class MechatronicsSessionImpl;
        /** Represents Mechatronics session  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
         <br>  Created in NX9.0.0.  <br>  
        */
        class NXOPENCPP_MECHATRONICSEXPORT  MechatronicsSession
        {
            /** Represents the action of simulation. */
            public: enum SimulationAction
            {
                SimulationActionStart/** Start   */,
                SimulationActionRestart/** Restart */,
                SimulationActionPause/** Pause   */,
                SimulationActionResume/** Resume  */,
                SimulationActionStop/** Stop    */
            };

            private: MechatronicsSessionImpl * m_mechatronicssession_impl;
            private: NXOpen::Session* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit MechatronicsSession(NXOpen::Session *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~MechatronicsSession();
            /** Control the Simulation. 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : nx_mcd_core ("MECHATRONICS CONCEPT DESIGNER") */
            public: void PerformSimulation
            (
                NXOpen::Mechatronics::MechatronicsSession::SimulationAction action /** action */ 
            );
            /** Gets defined logical types in configuration file 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void GetLogicalTypes
            (
                std::vector<NXString> & logicalTypeNames /** Array of type names */,
                std::vector<NXString> & logicalTypeBitmaps /** Array of type bitmaps */
            );
            /** Gets defined logical attribute names in configuration file 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: void GetLogicalAttributeNames
            (
                std::vector<NXString> & attributeNames /** Array of defined attribute names */
            );
            /** Gets attribute values of logical object  @return  Array of logical attribute values 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXString> GetLogicalAttributeValues
            (
                NXOpen::Mechatronics::LogicObject * logicalObject /** Logical object */,
                std::vector<NXString> & attributeNames /** Array of logical attribute names */
            );
            /** Gets exportable logical objects  @return  Array of exportable logical objects 
             <br>  Created in NX9.0.0.  <br>  
             <br> License requirements : None */
            public: std::vector<NXOpen::Mechatronics::LogicObject *> GetExportableLogicalObjects
            (
                NXOpen::Mechatronics::LogicObject * logicalObject /** Logical object */
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