#ifndef NXOpen_CAE_CONNECTIONS_UTILS_HXX_INCLUDED
#define NXOpen_CAE_CONNECTIONS_UTILS_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_Connections_Utils.ja
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
#include <NXOpen/CAE_Connections_CommonTypes.hxx>
#include <NXOpen/CAE_Connections_LMIEConnection.hxx>
#include <NXOpen/TaggedObject.hxx>
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
        namespace Connections
        {
            class Utils;
        }
    }
    namespace CAE
    {
        class CaeSession;
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
        namespace Connections
        {
            class LMIEConnection;
        }
    }
    namespace CAE
    {
        namespace Connections
        {
            class LumpedMass;
        }
    }
    namespace CAE
    {
        class FemPart;
    }
    class INXObject;
    class TaggedObject;
    class Unit;
    namespace CAE
    {
        namespace Connections
        {
            class UtilsImpl;
            /** Contains universal connections utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaeSession  NXOpen::CAE::CaeSession @endlink  <br> 
             <br>  Created in NX12.0.0.  <br>  
            */
            class NXOPENCPP_CAEEXPORT  Utils
            {
                private: UtilsImpl * m_utils_impl;
                private: NXOpen::CAE::CaeSession* m_owner;
                /// \cond NX_NO_DOC 
                public: explicit Utils(NXOpen::CAE::CaeSession *owner);


                /// \endcond 
                public: 
                /**Returns the tag of this object.  */
                tag_t Tag() const; 
                public: ~Utils();
                /** Filters a list of connections by type  @return  all connections matching the specified connection type 
                 <br>  Created in NX12.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::Connections::IConnection *> FilterConnectionsByType
                (
                    const std::vector<NXOpen::CAE::Connections::IConnection *> & iConnections /** The array of input connections */,
                    NXOpen::CAE::Connections::ConnectionType type /** The connection type to filter by */
                );
                /** Returns the intermediate connection representations of lumped mass connections  @return  The intermediate connection representations 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::Connections::LMIEConnection *> GetInterchangeDataFromLumpedMass
                (
                    NXOpen::Unit * conversionLengthUnit /** The length unit */,
                    NXOpen::Unit * conversionMassUnit /** The mass unit */,
                    const std::vector<NXOpen::CAE::Connections::LumpedMass *> & iConnections /** The array of input lumped mass connections */,
                    const NXString & iAbsoluteExportPath /** The absolute path where the connections are to be exported */
                );
                /** Returns the intermediate connection representations of lumped mass connections  @return  The intermediate connection representations 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                std::vector<NXOpen::CAE::Connections::LMIEConnection *> GetInterchangeDataFromLumpedMass
                (
                    NXOpen::Unit * conversionLengthUnit /** The length unit */,
                    NXOpen::Unit * conversionMassUnit /** The mass unit */,
                    const std::vector<NXOpen::CAE::Connections::LumpedMass *> & iConnections /** The array of input lumped mass connections */,
                    const char * iAbsoluteExportPath /** The absolute path where the connections are to be exported */
                );
                /** Exports the intermediate connection representations of lumped mass connections to external file. File type is determined by the extension. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void ExportLumpedMassInterchangeData
                (
                    const std::vector<NXOpen::CAE::Connections::LMIEConnection *> & iConnections /** The array of input lumped mass intermediate representations */,
                    const NXString & iAbsoluteExportPath /** The absolute path where the connections are to be exported */,
                    bool iConvertConnectionDataFromPartUnits /** If the interchange data unit system is different from the part unit system, we want to convert the data before exporting */
                );
                /** Exports the intermediate connection representations of lumped mass connections to external file. File type is determined by the extension. 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                void ExportLumpedMassInterchangeData
                (
                    const std::vector<NXOpen::CAE::Connections::LMIEConnection *> & iConnections /** The array of input lumped mass intermediate representations */,
                    const char * iAbsoluteExportPath /** The absolute path where the connections are to be exported */,
                    bool iConvertConnectionDataFromPartUnits /** If the interchange data unit system is different from the part unit system, we want to convert the data before exporting */
                );
                /** Returns the projection points of the connections per geometry flanges
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: void GetProjectionPoints
                (
                    const std::vector<NXOpen::CAE::Connections::IConnection *> & iConnections /** The array of input connections */,
                    std::vector<NXOpen::INXObject *> & oFlanges /** The array of the geometry flange objects */,
                    std::vector<NXOpen::Point3d> & oProjectionPoints /** The array of the projection points */,
                    std::vector<int> & oFlangeObjectIndexList /** The array of projection point index ranges per flanges. The size of the array is number of flanges + 1. For the flange i the index range is [oFlangeObjectIndexList[i], ..., oFlangeObjectIndexList[i + 1] - 1]. */
                );
                /** Imports the intermediate connection representations of lumped mass connections from external file. File type is determined by the extension.  @return  The intermediate connection representations 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: std::vector<NXOpen::CAE::Connections::LMIEConnection *> ImportLumpedMassInterchangeData
                (
                    NXOpen::INXObject * contextPart /** contextpart */ ,
                    const NXString & iAbsoluteImportPath /** The absolute path where the connections are to be imported from */
                );
                /** Imports the intermediate connection representations of lumped mass connections from external file. File type is determined by the extension.  @return  The intermediate connection representations 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                std::vector<NXOpen::CAE::Connections::LMIEConnection *> ImportLumpedMassInterchangeData
                (
                    NXOpen::INXObject * contextPart /** contextpart */ ,
                    const char * iAbsoluteImportPath /** The absolute path where the connections are to be imported from */
                );
                /** Create standalone LMIEConnection  @return  The created standalone LMIEConnection 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : None */
                public: NXOpen::CAE::Connections::LMIEConnection * CreateLmieconnection
                (
                    NXOpen::INXObject * contextPart /** contextpart */ 
                );
                /** Map CAD Prt geometry in FemPart  @return  Mapped cad feature in FemPart 
                 <br>  Created in NX1847.0.0.  <br>  
                 <br> License requirements : nx_masterfem ("Finite Element Modeling") */
                public: NXOpen::TaggedObject * MapObject
                (
                    NXOpen::CAE::FemPart * femPart /** The context fem part*/,
                    NXOpen::TaggedObject * cadFeature /** The cad entity */,
                    bool syncGeomData /** Synchronize CAD Geometry option if new entitiy is created */
                );
                /** Reimport mesh created by external mesher. The work part should be a FEM meshed with an external mesher. 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment") */
                public: void ReimportMesh
                (
                );
                /** Splits the warped quads by invoking an external mesher. The work part should be a FEM meshed with an external mesher. 
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : sc_gso_abmesh (" Simcenter GSO Ansa Batch Mesh environment") */
                public: void SplitWarpedQuads
                (
                );
                /** Redo labeling of current work AFEM. The work part should be a AFEM.  
                 <br>  Created in NX1872.0.0.  <br>  
                 <br> License requirements : sc_gso_creation (" Simcenter GSO BIW Creation environment") */
                public: void RelabelAfem
                (
                );
            }; //lint !e1712 default constructor not defined for class  

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
