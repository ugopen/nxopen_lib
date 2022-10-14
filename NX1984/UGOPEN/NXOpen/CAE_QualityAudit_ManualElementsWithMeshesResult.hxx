#ifndef NXOpen_CAE_QUALITYAUDIT_MANUALELEMENTSWITHMESHESRESULT_HXX_INCLUDED
#define NXOpen_CAE_QUALITYAUDIT_MANUALELEMENTSWITHMESHESRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QualityAudit_ManualElementsWithMeshesResult.ja
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
#include <NXOpen/CAE_QualityAudit_IConnectedMeshes.hxx>
#include <NXOpen/CAE_QualityAudit_ManualElementsResult.hxx>
#include <NXOpen/INXObject.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        namespace QualityAudit
        {
            class ManualElementsWithMeshesResult;
        }
    }
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    namespace CAE
    {
        class Mesh;
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class IConnectedMeshes;
        }
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class ManualElementsResult;
        }
    }
    class INXObject;
    namespace CAE
    {
        namespace QualityAudit
        {
            class _ManualElementsWithMeshesResultBuilder;
            class ManualElementsWithMeshesResultImpl;
            /**  @brief  This class contains information about elements connecting meshes and the connected meshes. It is obtained from the @link NXOpen::CAE::QualityAudit::MeshConnectivity NXOpen::CAE::QualityAudit::MeshConnectivity@endlink  action. 

               <br> To obtain this type of results see @link CAE::QualityAudit::MeshConnectivity CAE::QualityAudit::MeshConnectivity@endlink .  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ManualElementsWithMeshesResult : public NXOpen::CAE::QualityAudit::ManualElementsResult, public virtual NXOpen::CAE::QualityAudit::IConnectedMeshes
            {
                private: ManualElementsWithMeshesResultImpl * m_manualelementswithmeshesresult_impl;
                private: friend class  _ManualElementsWithMeshesResultBuilder;
                protected: ManualElementsWithMeshesResult();
                public: ~ManualElementsWithMeshesResult();
                /** Gets the connected meshes from a result 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: virtual std::vector<NXOpen::CAE::Mesh *> GetMeshes
                (
                );
            };
        }
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