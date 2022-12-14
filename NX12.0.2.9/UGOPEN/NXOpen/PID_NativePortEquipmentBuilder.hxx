#ifndef NXOpen_PID_NATIVEPORTEQUIPMENTBUILDER_HXX_INCLUDED
#define NXOpen_PID_NATIVEPORTEQUIPMENTBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PID_NativePortEquipmentBuilder.ja
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
#include <NXOpen/PID_NativeEquipment.hxx>
#include <NXOpen/PID_NativeSheet.hxx>
#include <NXOpen/PID_PortEquipmentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libpidopencpp_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace PID
    {
        class NativePortEquipmentBuilder;
    }
    namespace PID
    {
        class NativeManager;
    }
    namespace PID
    {
        class NativeEquipment;
    }
    namespace PID
    {
        class NativeSheet;
    }
    namespace PID
    {
        class PortEquipmentBuilder;
    }
    namespace PID
    {
        class NativePortEquipmentBuilderImpl;

        /// \cond NX_NO_DOC 
        /**  @brief 
            Builder used to model a piece of PortEquipment.  

         
             <br> To obtain an instance of this class, refer to @link NXOpen::PID::NativeManager  NXOpen::PID::NativeManager @endlink  <br> 
         <br>  Created in NX12.0.1.  <br>  
        */
        class PIDOPENCPPEXPORT  NativePortEquipmentBuilder
        {
            private: NativePortEquipmentBuilderImpl * m_nativeportequipmentbuilder_impl;
            private: NXOpen::PID::NativeManager* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit NativePortEquipmentBuilder(NXOpen::PID::NativeManager *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~NativePortEquipmentBuilder();
            /** Gets the owning sheet of this sheet element. Its setting method works only in creation mode.  @return  
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::PID::NativeSheet * GetOwningSheet
            (
                NXOpen::PID::PortEquipmentBuilder * builder /** builder */ 
            );
            /** Sets the owning sheet of this sheet element. Its setting method works only in creation mode. 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetOwningSheet
            (
                NXOpen::PID::PortEquipmentBuilder * builder /** builder */ ,
                NXOpen::PID::NativeSheet * owningSheet /** owningsheet */ 
            );
            /** Get the native node.  @return  
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: NXOpen::PID::NativeEquipment * GetNode
            (
                NXOpen::PID::PortEquipmentBuilder * builder /** builder */ 
            );
            /** Set the native node. 
             <br>  Created in NX12.0.1.  <br>  
             <br> License requirements : nx_pid_design_author ("NX P and ID Design Author") */
            public: void SetNode
            (
                NXOpen::PID::PortEquipmentBuilder * builder /** builder */ ,
                NXOpen::PID::NativeEquipment * equipment /** equipment */ 
            );
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
