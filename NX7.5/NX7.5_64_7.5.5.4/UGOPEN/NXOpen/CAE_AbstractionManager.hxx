#ifndef NXOpen_CAE_ABSTRACTIONMANAGER_HXX_INCLUDED
#define NXOpen_CAE_ABSTRACTIONMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_AbstractionManager.ja
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
        class AbstractionManager;
    }
    namespace CAE
    {
        class BaseFEModel;
    }
    namespace CAE
    {
        class CircularImprintBuilder;
    }
    namespace CAE
    {
        class PolygonFaceOnMeshBuilder;
    }
    namespace CAE
    {
        class AbstractionManagerImpl;
        /**  @brief  Provides method for creating  builder for
            abstraction commands in a fem part  

           <br> To obtain an instance of this class, refer to @link CAE::BaseFEModel CAE::BaseFEModel@endlink  <br> */
        class NXOPENCPPEXPORT  AbstractionManager
        {
            private: AbstractionManagerImpl * m_abstractionmanager_impl;
            private: NXOpen::CAE::BaseFEModel* m_owner;
            /** Constructor */
            public: explicit AbstractionManager(NXOpen::CAE::BaseFEModel *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~AbstractionManager();
            /** Creates a builder for abstraction Command  @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::CircularImprintBuilder * CreateCircularImprintBuilder
            (
            );
            /** Creates a builder for Polygon Face On Mesh Command  @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::PolygonFaceOnMeshBuilder * CreatePolygonFaceOnMeshBuilder
            (
            );
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
