#ifndef NXOpen_CAE_MODELCHECKMANAGER_HXX_INCLUDED
#define NXOpen_CAE_MODELCHECKMANAGER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_ModelCheckManager.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class ModelCheckManager;
    }
    namespace CAE
    {
        class CaePart;
    }
    namespace CAE
    {
        class MechanicalLoadSumBuilder;
    }
    namespace CAE
    {
        class SolidPropertyCheckBuilder;
    }
    namespace CAE
    {
        /**  @brief  Provides method for creating  builder for 
            node element operation commands in a fem part  

           <br> To obtain an instance of this class, refer to @link CAE::CaePart CAE::CaePart@endlink  <br> */
        class NXOPENCPPEXPORT ModelCheckManager
        {
            private: NXOpen::CAE::CaePart* m_owner;
            public: explicit ModelCheckManager(NXOpen::CAE::CaePart *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Creates a builder for mechanical load summary command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::MechanicalLoadSumBuilder * CreateMechanicalLoadSumBuilder
            (
            );
            /** Creates a builder for solid properties check command @return   <br> License requirements : nx_masterfem ("Finite Element Modeling") */
            public: NXOpen::CAE::SolidPropertyCheckBuilder * CreateSolidPropertyCheckBuilder
            (
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif