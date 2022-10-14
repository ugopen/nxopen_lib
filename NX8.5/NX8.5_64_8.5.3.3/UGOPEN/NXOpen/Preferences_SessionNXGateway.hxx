#ifndef NXOpen_PREFERENCES_SESSIONNXGATEWAY_HXX_INCLUDED
#define NXOpen_PREFERENCES_SESSIONNXGATEWAY_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_SessionNXGateway.ja
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
#include <NXOpen/libnxopencpp_preferences_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Preferences
    {
        class SessionNXGateway;
    }
    namespace Preferences
    {
        class SessionPreferences;
    }
    namespace Preferences
    {
        class SessionNXGatewayImpl;
        /** Represents the set of NXGateway Preferences applicable to entire session  <br> To obtain an instance of this class, refer to @link Preferences::SessionPreferences  Preferences::SessionPreferences @endlink  <br> 
         <br>  Created in NX3.0.0.  <br>  
        */
        class NXOPENCPP_PREFERENCESEXPORT  SessionNXGateway
        {
            private: SessionNXGatewayImpl * m_sessionnxgateway_impl;
            private: NXOpen::Preferences::SessionPreferences* m_owner;
            /// \cond NX_NO_DOC 
            public: explicit SessionNXGateway(NXOpen::Preferences::SessionPreferences *owner);


            /// \endcond 
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~SessionNXGateway();
            /**Returns  the reference geometry import layer for I-DEAS  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: int ReferenceGeometryImportLayer
            (
            );
            /**Sets  the reference geometry import layer for I-DEAS  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReferenceGeometryImportLayer
            (
                int referenceGeometryImportLayer /** reference geometry import layer */ 
            );
            /**Returns  the reference geometry import color for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: int ReferenceGeometryImportColor
            (
            );
            /**Sets  the reference geometry import color for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetReferenceGeometryImportColor
            (
                int referenceGeometryImportColor /** reference geometry import color */ 
            );
            /**Returns  the wireframe geometry import layer for I-DEAS  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: int WireframeGeometryImportLayer
            (
            );
            /**Sets  the wireframe geometry import layer for I-DEAS  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetWireframeGeometryImportLayer
            (
                int wireframeGeometryImportLayer /** wireframe geometry import layer */ 
            );
            /**Returns  the wireframe geometry import color for I-DEAS  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: int WireframeGeometryImportColor
            (
            );
            /**Sets  the wireframe geometry import color for I-DEAS  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetWireframeGeometryImportColor
            (
                int wireframeGeometryImportColor /** wireframe geometry import color */ 
            );
            /**Returns  the perform fidelity check on import flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool PerformFidelityCheckOnImport
            (
            );
            /**Sets  the perform fidelity check on import flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPerformFidelityCheckOnImport
            (
                bool performFidelityCheckOnImport /** perform fidelity check on import */ 
            );
            /**Returns  the retain fidelity checking information flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool RetainFidelityCheckingInformation
            (
            );
            /**Sets  the retain fidelity checking information flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRetainFidelityCheckingInformation
            (
                bool retainFidelityCheckingInformation /** retain fidelity checking information */ 
            );
            /**Returns  the load product manufacturing information flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool LoadProductManufacturingInformation
            (
            );
            /**Sets  the load product manufacturing information flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLoadProductManufacturingInformation
            (
                bool loadProductManufacturingInformation /** load product manufacturing information */ 
            );
            /**Returns  the load product manufacturing information flag for Solid Edge 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool LoadSolidEdgeProductManufacturingInformation
            (
            );
            /**Sets  the load product manufacturing information flag for Solid Edge 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLoadSolidEdgeProductManufacturingInformation
            (
                bool loadProductManufacturingInformation /** load product manufacturing information */ 
            );
            /**Returns  the load construction geometry flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool LoadConstructionGeometry
            (
            );
            /**Sets  the load construction geometry flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLoadConstructionGeometry
            (
                bool loadConstructionGeometry /** load construction geometry */ 
            );
            /**Returns  the ignore update of identical versions flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool IgnoreUpdateOfIdenticalVersions
            (
            );
            /**Sets  the ignore update of identical versions flag for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetIgnoreUpdateOfIdenticalVersions
            (
                bool ignoreUpdateOfIdenticalVersions /** ignore update of identical versions */ 
            );
            /**Returns  the automatically checking of items revision flag for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool AutomaticallyCheckItemRevisions
            (
            );
            /**Sets  the automatically checking of items revision flag for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAutomaticallyCheckItemRevisions
            (
                bool automaticallyCheckItemRevisions /** automatically check item revisions */ 
            );
            /**Returns  the remove small edges flag. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveSmallEdges
            (
            );
            /**Sets  the remove small edges flag. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRemoveSmallEdges
            (
                bool removeSmallEdges /** remove small edges */ 
            );
            /**Returns  the use repair tolerance flag. One of the heal geometry option for I-DEAS import  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool UseRepairTolerance
            (
            );
            /**Sets  the use repair tolerance flag. One of the heal geometry option for I-DEAS import  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetUseRepairTolerance
            (
                bool useRepairTolerance /** use repair tolerance */ 
            );
            /**Returns  the remove self intersection flag. One of the heal geometry option for I-DEAS import  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveSelfIntersections
            (
            );
            /**Sets  the remove self intersection flag. One of the heal geometry option for I-DEAS import  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRemoveSelfIntersections
            (
                bool removeSelfIntersections /** remove self intersections */ 
            );
            /**Returns  the remove discontinuity flag. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool RemoveDiscontinuity
            (
            );
            /**Sets  the remove discontinuity flag. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRemoveDiscontinuity
            (
                bool removeDiscontinuity /** remove discontinuity */ 
            );
            /**Returns  the suppress surface modification flag. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool SuppressSurfaceModification
            (
            );
            /**Sets  the suppress surface modification flag. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSuppressSurfaceModification
            (
                bool suppressSurfaceModification /** suppress surface modification */ 
            );
            /**Returns  the preserve nominal geometry flag. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool PreserveNominalGeometry
            (
            );
            /**Sets  the preserve nominal geometry flag. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetPreserveNominalGeometry
            (
                bool preserveNominalGeometry /** preserve nominal geometry */ 
            );
            /**Returns  the attach FC data flag for I-DEAS gateway 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool AttachFidelityCheckData
            (
            );
            /**Sets  the attach FC data flag for I-DEAS gateway 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAttachFidelityCheckData
            (
                bool attachFidelityCheckData /** attach fidelity check data */ 
            );
            /**Returns  the heal geometry on import flag for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool HealGeometryOnImport
            (
            );
            /**Sets  the heal geometry on import flag for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetHealGeometryOnImport
            (
                bool healGeometryOnImport /** heal geometry on import */ 
            );
            /**Returns  the tolerance. One of the heal geometry option for I-DEAS import  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: double Tolerance
            (
            );
            /**Sets  the tolerance. One of the heal geometry option for I-DEAS import  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetTolerance
            (
                double tolerance /** tolerance */ 
            );
            /**Returns  the repair tolerance. One of the heal geometry option for I-DEAS import  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: double RepairTolerance
            (
            );
            /**Sets  the repair tolerance. One of the heal geometry option for I-DEAS import  
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetRepairTolerance
            (
                double repairTolerance /** repair tolerance */ 
            );
            /**Returns  the minimum small edge length. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: double MinimumSmallEdgeLength
            (
            );
            /**Sets  the minimum small edge length. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetMinimumSmallEdgeLength
            (
                double minimumSmallEdgeLength /** minimum small edge length */ 
            );
            /**Returns  the angular tolerance. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: double AngularTolerance
            (
            );
            /**Sets  the angular tolerance. One of the heal geometry option for I-DEAS import 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAngularTolerance
            (
                double angularTolerance /** angular tolerance */ 
            );
            /**Returns  the only import design parts flag for Solid Edge. It is under Solid Edge Gateway preferences 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool OnlyImportDesignParts
            (
            );
            /**Sets  the only import design parts flag for Solid Edge. It is under Solid Edge Gateway preferences 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetOnlyImportDesignParts
            (
                bool onlyImportDesignParts /** only import design parts */ 
            );
            /**Returns  the save component part files flag during load for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: bool SaveComponentPartFilesDuringLoad
            (
            );
            /**Sets  the save component part files flag during load for I-DEAS 
             <br>  Created in NX3.0.0.  <br>  
             <br> License requirements : None */
            public: void SetSaveComponentPartFilesDuringLoad
            (
                bool saveComponentPartFilesDuringLoad /** save component part files during load */ 
            );
            /**Returns  the load construction geometry flag for Solid Edge 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: bool LoadSolidEdgeConstructionGeometry
            (
            );
            /**Sets  the load construction geometry flag for Solid Edge 
             <br>  Created in NX4.0.0.  <br>  
             <br> License requirements : None */
            public: void SetLoadSolidEdgeConstructionGeometry
            (
                bool loadConstructionGeometry /** load construction geometry */ 
            );
            /**Returns  the Assembly-level features flag for Solid Edge 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: bool LoadSolidEdgeAssemblyFeatures
            (
            );
            /**Sets  the Assembly-level features flag for Solid Edge 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: void SetLoadSolidEdgeAssemblyFeatures
            (
                bool loadAssemblyFeatures /** load assembly features */ 
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