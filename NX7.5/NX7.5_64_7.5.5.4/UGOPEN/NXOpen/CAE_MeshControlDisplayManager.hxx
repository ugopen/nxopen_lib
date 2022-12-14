#ifndef NXOpen_CAE_MESHCONTROLDISPLAYMANAGER_HXX_INCLUDED
#define NXOpen_CAE_MESHCONTROLDISPLAYMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_MeshControlDisplayManager.ja
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
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class MeshControlDisplayManager;
    }
    namespace CAE
    {
        class CaePart;
    }
    namespace CAE
    {
        class MeshControlDisplayOptionsBuilder;
    }
    namespace CAE
    {
        class MeshControlDisplayManagerImpl;
        /**  @brief  Provides method for creating  builder for 
            mesh control display operation commands in both sim and fem part  

           <br> To obtain an instance of this class, refer to @link CAE::CaePart CAE::CaePart@endlink  <br> */
        class NXOPENCPPEXPORT  MeshControlDisplayManager
        {
            private: MeshControlDisplayManagerImpl * m_meshcontroldisplaymanager_impl;
            private: NXOpen::CAE::CaePart* m_owner;
            /** Constructor */
            public: explicit MeshControlDisplayManager(NXOpen::CAE::CaePart *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~MeshControlDisplayManager();
            /** Creates a builder for node element info command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::MeshControlDisplayOptionsBuilder * CreateBuilder
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
