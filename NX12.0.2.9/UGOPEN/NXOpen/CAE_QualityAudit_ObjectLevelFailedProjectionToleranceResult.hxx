#ifndef NXOpen_CAE_QUALITYAUDIT_OBJECTLEVELFAILEDPROJECTIONTOLERANCERESULT_HXX_INCLUDED
#define NXOpen_CAE_QUALITYAUDIT_OBJECTLEVELFAILEDPROJECTIONTOLERANCERESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QualityAudit_ObjectLevelFailedProjectionToleranceResult.ja
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
#include <NXOpen/CAE_Connections_IConnection.hxx>
#include <NXOpen/CAE_QualityAudit_Result.hxx>
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
            class ObjectLevelFailedProjectionToleranceResult;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class IConnection;
        }
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class Result;
        }
    }
    namespace CAE
    {
        namespace QualityAudit
        {
            class _ObjectLevelFailedProjectionToleranceResultBuilder;
            class ObjectLevelFailedProjectionToleranceResultImpl;
            /**  @brief The Quality Audit ObjectLevelFailedProjectionToleranceResult is a class containing information about projections 
                    that failed the tolerance criteria although the projection itself was successful. 

               <br> To obtain this type of results see @link CAE::QualityAudit::ObjectLevelProjectionCheck CAE::QualityAudit::ObjectLevelProjectionCheck@endlink .  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  ObjectLevelFailedProjectionToleranceResult : public NXOpen::CAE::QualityAudit::Result
            {
                private: ObjectLevelFailedProjectionToleranceResultImpl * m_objectlevelfailedprojectiontoleranceresult_impl;
                private: friend class  _ObjectLevelFailedProjectionToleranceResultBuilder;
                protected: ObjectLevelFailedProjectionToleranceResult();
                public: ~ObjectLevelFailedProjectionToleranceResult();
                /**Returns  the connection with the failed tolerance projection 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::IConnection * Connection
                (
                );
                /**Returns  the definition index of the tolerance failing projection. See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int DefinitionIndex
                (
                );
                /**Returns  the location index of the tolerance failing projection. See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int LocationIndex
                (
                );
                /**Returns  the coordinate index of the tolerance failing projection in the location. See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int CoordinateIndex
                (
                );
                /**Returns  the flange index of the tolerance failing projection. See @link NXOpen::CAE::Connections::IFlangesContainer NXOpen::CAE::Connections::IFlangesContainer@endlink  for details  
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: int FlangeIndex
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
