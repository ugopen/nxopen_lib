#ifndef NXOpen_CAE_LAMINATEGLOBALLAYUPMGR_HXX_INCLUDED
#define NXOpen_CAE_LAMINATEGLOBALLAYUPMGR_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_LaminateGlobalLayupMgr.ja
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
#include <NXOpen/CAE_LaminateLayupOffsetBuilder.hxx>
#include <NXOpen/CAE_LaminateMatOrientationBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAE
    {
        class LaminateGlobalLayupMgr;
    }
    namespace CAE
    {
        class FEModel;
    }
    namespace CAE
    {
        class FlatPatternsBuilder;
    }
    namespace CAE
    {
        class GlobalLayupImportFromPptBuilder;
    }
    namespace CAE
    {
        class Laminate;
    }
    namespace CAE
    {
        class LaminateDrapingDataBuilder;
    }
    namespace CAE
    {
        class LaminateExtrudeSetup;
    }
    namespace CAE
    {
        class LaminateExtrudeSetupBuilder;
    }
    namespace CAE
    {
        class LaminateExtrudeSetupCollection;
    }
    namespace CAE
    {
        class LaminateFillSetupBuilder;
    }
    namespace CAE
    {
        class LaminateGlobalLayup;
    }
    namespace CAE
    {
        class LaminateGlobalLayupCollection;
    }
    namespace CAE
    {
        class LaminateImportedLayupBuilder;
    }
    namespace CAE
    {
        class LaminateLayupOffset;
    }
    namespace CAE
    {
        class LaminateLayupOffsetBuilder;
    }
    namespace CAE
    {
        class LaminateLayupOffsetCollection;
    }
    namespace CAE
    {
        class LaminateMatOrientation;
    }
    namespace CAE
    {
        class LaminateMatOrientationBuilder;
    }
    namespace CAE
    {
        class LaminateMatOrientationCollection;
    }
    namespace CAE
    {
        class LaminatePly;
    }
    namespace CAE
    {
        class LaminateSelectEntitiesBuilder;
    }
    namespace CAE
    {
        class LaminateViewDrapingResultsBuilder;
    }
    namespace CAE
    {
        class LayupGrowth;
    }
    namespace CAE
    {
        class LayupGrowthBuilder;
    }
    namespace CAE
    {
        class LayupGrowthCollection;
    }
    namespace CAE
    {
        class ViewLaminateBuilder;
    }
    namespace CAE
    {
        class LaminateGlobalLayupMgrImpl;
        /** Represent the laminate global layup manager which manages all the global layups in the laminate ply-based modeling project  <br> To obtain an instance of this class, refer to @link CAE::FEModel CAE::FEModel@endlink  <br> */
        class NXOPENCPPEXPORT  LaminateGlobalLayupMgr
        {
            private: LaminateGlobalLayupMgrImpl * m_laminategloballayupmgr_impl;
            private: NXOpen::CAE::FEModel* m_owner;
            /** Constructor */
            public: explicit LaminateGlobalLayupMgr(NXOpen::CAE::FEModel *owner);
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            public: ~LaminateGlobalLayupMgr();
            /** The newest function can be found in the laminate ply  @return  created builder 
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAE::LaminateDrapingDataBuilder * CreateLaminateDrapingDataBuilder
            (
                NXOpen::CAE::LaminatePly * laminatePly /** ply for which we will edit the draping data */
            );
            /** Creates a @link CAE::GlobalLayupImportFromPptBuilder CAE::GlobalLayupImportFromPptBuilder@endlink   @return   <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::GlobalLayupImportFromPptBuilder * CreateGlobalLayupImportFromPptBuilder
            (
            );
            /** Creates a @link CAE::LayupGrowthBuilder CAE::LayupGrowthBuilder@endlink   @return  
             @deprecated Deprecated in NX7.5.0 <br> 
             <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public:  NX_DEPRECATED("Deprecated in NX7.5.0") NXOpen::CAE::LayupGrowthBuilder * CreateLayupGrowthBuilder
            (
                NXOpen::CAE::LayupGrowth * layupgrowth /** Layup Growth */
            );
            /** Creates a @link CAE::LaminateLayupOffsetBuilder CAE::LaminateLayupOffsetBuilder@endlink   @return   <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateLayupOffsetBuilder * CreateLayupOffsetBuilder
            (
                NXOpen::CAE::LaminateLayupOffset * layupoffset /** Laminate Layup Offset */
            );
            /** Creates a @link CAE::LaminateMatOrientationBuilder CAE::LaminateMatOrientationBuilder@endlink   @return   <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateMatOrientationBuilder * CreateLaminateMatOrientationBuilder
            (
                NXOpen::CAE::LaminateMatOrientation * matOrientation /** Laminate Material Orientation */
            );
            /** Creates a @link CAE::ViewLaminateBuilder CAE::ViewLaminateBuilder@endlink   @return   <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::ViewLaminateBuilder * CreateViewLaminateBuilder
            (
                NXOpen::CAE::Laminate * laminate /** Inherited laminate physical */,
                int zoneIndex /** Zone index */
            );
            /** Creates a @link CAE::FlatPatternsBuilder CAE::FlatPatternsBuilder@endlink   @return   <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::FlatPatternsBuilder * CreateFlatPatternsBuilder
            (
            );
            /** Creates a @link CAE::FlatPatternsBuilder CAE::FlatPatternsBuilder@endlink   @return   <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateViewDrapingResultsBuilder * CreateViewDrapingResultsBuilder
            (
                NXOpen::CAE::LaminateGlobalLayup * globalLayup /** Global Layup */,
                NXOpen::CAE::LaminatePly * ply /** Ply */
            );
            /**Returns  the default layup offset  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateLayupOffset * DefaultLayupOffset
            (
            );
            /**Sets  the default layup offset  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetDefaultLayupOffset
            (
                NXOpen::CAE::LaminateLayupOffset * defaultLayup /** default layup offset */
            );
            /**Returns  the default material orientation  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: int DefaultMaterialOrientation
            (
            );
            /**Sets  the default material orientation  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void SetDefaultMaterialOrientation
            (
                int defaultOrientation /** the default material orientation */
            );
            /** A method to remove a material orientation  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void RemoveMaterialOrientation
            (
                int matOrientation /** the material orientation to remove */
            );
            /** A method to remove a layup offset  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void RemoveLayupOffset
            (
                int layupOffset /** the layup offset to remove */
            );
            /** Creates a @link CAE::LaminateExtrudeSetupBuilder CAE::LaminateExtrudeSetupBuilder@endlink   @return  created builder  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateExtrudeSetupBuilder * CreateLaminateExtrudeSetupBuilder
            (
                NXOpen::CAE::LaminateExtrudeSetup * extrudeSetup /** extrude setup */ 
            );
            /** Creates a @link CAE::LaminateFillSetupBuilder CAE::LaminateFillSetupBuilder@endlink   @return  created builder  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateFillSetupBuilder * CreateLaminateFillSetupBuilder
            (
                NXOpen::CAE::LaminateExtrudeSetup * extrudeSetup /** extrude setup */ 
            );
            /** Creates a @link CAE::LaminateImportedLayupBuilder CAE::LaminateImportedLayupBuilder@endlink   @return  created builder  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateImportedLayupBuilder * CreateLaminateImportedLayupBuilder
            (
                NXOpen::CAE::LaminateGlobalLayup * globalLayup /** global layup */ 
            );
            /** Compute draping for all the plies of all the global layups in the part. 
                        Plies that are already computed wont be recomputed.  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void UpdateDraping
            (
            );
            /** Display global layup manager information  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void Information
            (
            );
            /** Compute zones for all laminate properties in the model.  
                        Reads the global layups, updates the draping and calculates the zones on the laminate.
                        Existing zones will be overriden.  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void ComputeZones
            (
            );
            /** Export zone information to a CSV file.  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void ExportZoneInformation
            (
                const NXString & csvFilename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Creates a @link CAE::LaminateSelectEntitiesBuilder CAE::LaminateSelectEntitiesBuilder@endlink   @return  created builder  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: NXOpen::CAE::LaminateSelectEntitiesBuilder * CreateLaminateSelectEntitiesBuilder
            (
            );
            /** For each zone of each @link CAE::Laminate CAE::Laminate@endlink  in the model, create an element group  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void ExportZonesAsGroups
            (
            );
            /** For each zone of each @link CAE::Laminate CAE::Laminate@endlink  in the model, create an equivalent laminate physical property  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void ExportZonesAsLaminates
            (
            );
            /** For each @link CAE::LaminateGlobalLayup CAE::LaminateGlobalLayup@endlink  in the model, create a group with the draping domain entities  <br> License requirements : nx_lam_comp_adv ("Laminate Composites Advanced") */
            public: void ExportDrapingDomainAsGroups
            (
            );


            /** Collection of managed global layups */
            public: NXOpen::CAE::LaminateGlobalLayupCollection *GlobalLayups();
            /** Collection of managed layup growth rules */
            public: NXOpen::CAE::LayupGrowthCollection *LayupGrowths();
            /** Collection of managed layup offset rules */
            public: NXOpen::CAE::LaminateLayupOffsetCollection *LayupOffsets();
            /** Collection of material orientations */
            public: NXOpen::CAE::LaminateMatOrientationCollection *MatOrientations();
            /** Collection of laminate extrusion setup */
            public: NXOpen::CAE::LaminateExtrudeSetupCollection *ExtrudeSetups();
        }; //lint !e1712 default constructor not defined for class  

    }
}
#undef EXPORTLIBRARY
#endif
