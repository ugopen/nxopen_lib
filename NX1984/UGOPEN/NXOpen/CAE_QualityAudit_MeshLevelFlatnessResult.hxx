#ifndef NXOpen_CAE_QUALITYAUDIT_MESHLEVELFLATNESSRESULT_HXX_INCLUDED
#define NXOpen_CAE_QUALITYAUDIT_MESHLEVELFLATNESSRESULT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_QualityAudit_MeshLevelFlatnessResult.ja
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
#include <NXOpen/ugmath.hxx>
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
            class MeshLevelFlatnessResult;
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
    class TaggedObject;
    namespace CAE
    {
        namespace QualityAudit
        {
            class _MeshLevelFlatnessResultBuilder;
            class MeshLevelFlatnessResultImpl;
            /**  @brief  The Quality Audit MeshLevelFlatnessResult is a class containing information about failed flatness check on universal connections at mesh level. 

               <br> To obtain this type of results see @link CAE::QualityAudit::MeshLevelConnectionAngleCheck CAE::QualityAudit::MeshLevelConnectionAngleCheck@endlink .  <br> 
             <br>  Created in NX1847.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  MeshLevelFlatnessResult : public NXOpen::CAE::QualityAudit::Result
            {
                private: MeshLevelFlatnessResultImpl * m_meshlevelflatnessresult_impl;
                private: friend class  _MeshLevelFlatnessResultBuilder;
                protected: MeshLevelFlatnessResult();
                public: ~MeshLevelFlatnessResult();
                /**Returns  the connection. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::IConnection * Connection
                (
                );
                /**Returns  the definition index . See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: int DefinitionIndex
                (
                );
                /**Returns  the location index. See @link NXOpen::CAE::Connections::ILocationsContainer NXOpen::CAE::Connections::ILocationsContainer@endlink  for details  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: int LocationIndex
                (
                );
                /**Returns  the coordinate index. See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: int CoordinateIndex
                (
                );
                /**Returns  the flange index of the first point. See @link NXOpen::CAE::Connections::Location NXOpen::CAE::Connections::Location@endlink  for details  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: int FlangeIndex
                (
                );
                /**Returns  the distance.  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: double Distance
                (
                );
                /**Returns  the result point.  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::Point3d Point
                (
                );
                /**Returns  the result object.  
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::TaggedObject * ResultEntity
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