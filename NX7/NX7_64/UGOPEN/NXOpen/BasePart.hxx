#ifndef NXOpen_BASEPART_HXX_INCLUDED
#define NXOpen_BASEPART_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     BasePart.ja
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
#include <NXOpen/Display_DynamicSectionBuilder.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/PartCloseResponses.hxx>
#include <NXOpen/PartLoadStatus.hxx>
#include <NXOpen/PartReopenReport.hxx>
#include <NXOpen/PartSaveStatus.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class BasePart;
    class ArcCollection;
    namespace Assemblies
    {
        class AssemblyManager;
    }
    namespace Assemblies
    {
        class ComponentAssembly;
    }
    namespace Assemblies
    {
        class ProductOutlineManager;
    }
    class AxisCollection;
    namespace CAE
    {
        class FunctionCollection;
    }
    class ColorManager;
    class CoordinateSystemCollection;
    class CurveCollection;
    class DatumCollection;
    class DirectionCollection;
    namespace Display
    {
        class CameraCollection;
    }
    namespace Display
    {
        class CgfxAttrCollection;
    }
    namespace Display
    {
        class CgfxMattexCollection;
    }
    namespace Display
    {
        class DecalCollection;
    }
    namespace Display
    {
        class DynamicSectionBuilder;
    }
    namespace Display
    {
        class DynamicSectionCollection;
    }
    namespace Display
    {
        class GridCollection;
    }
    namespace Display
    {
        class SelPrefCollection;
    }
    namespace Display
    {
        class TrueShadingCollection;
    }
    class EllipseCollection;
    class ExpressionCollection;
    namespace Features
    {
        class BaseFeatureCollection;
    }
    namespace Fields
    {
        class FieldManager;
    }
    class FontCollection;
    namespace GeometricAnalysis
    {
        class AnalysisManager;
    }
    class Group;
    class GroupBuilder;
    class HyperbolaCollection;
    namespace Layer
    {
        class CategoryCollection;
    }
    namespace Layer
    {
        class LayerManager;
    }
    class LayoutCollection;
    class LightCollection;
    class LineCollection;
    class MaterialManager;
    class MeasureManager;
    class ModelingViewCollection;
    class NXMatrixCollection;
    class NXObject;
    class OffsetCollection;
    namespace Optimization
    {
        class DesignStudyCollection;
    }
    namespace Optimization
    {
        class OptimizationCollection;
    }
    namespace PDM
    {
        class PdmPart;
    }
    class ParabolaCollection;
    class PartCloseResponses;
    class PartLoadStatus;
    class PartReopenReport;
    class PartSaveOptions;
    class PartSaveStatus;
    class PlaneCollection;
    class PlotManager;
    class PointCollection;
    namespace Preferences
    {
        class PartPreferences;
    }
    class ReferenceSet;
    class RuleManager;
    class ScCollectorCollection;
    class ScalarCollection;
    class SectionCollection;
    class SplineCollection;
    class UnitCollection;
    namespace UserDefinedObjects
    {
        class UserDefinedObjectManager;
    }
    class ViewCollection;
    class WCS;
    class XformCollection;
    class _BasePartBuilder;
    /** Base class for an NX part.  <br> Use the @link NXOpen::PartCollection NXOpen::PartCollection@endlink  class to load or create a part. Use @link NXOpen::PartCollection::Work NXOpen::PartCollection::Work@endlink  to obtain the current work part. <br> */
    class NXOPENCPPEXPORT BasePart : public NXObject
    {
        /** Controls the information written to a bookmark file. */
        public: enum BookmarkOption
        {
            BookmarkOptionAll/** Write component groups, load options, and structure. */,
            BookmarkOptionComponentGroupsLoadOptions/** Write component groups and load options. */,
            BookmarkOptionComponentGroupsOnly/** Write component groups only. */
        };

        /** The units of the part file. */
        public: enum Units
        {
            UnitsInches/** inches */ ,
            UnitsMillimeters/** millimeters */ 
        };

        /** Used to specify whether a part's components should be saved (if modified)
            when the part is saved. */
        public: enum SaveComponents
        {
            SaveComponentsFalse/** false */ ,
            SaveComponentsTrue/** true */ 
        };

        /** Used to specify whether a part should be closed after it is saved. */
        public: enum CloseAfterSave
        {
            CloseAfterSaveFalse/** false */ ,
            CloseAfterSaveTrue/** true */ 
        };

        /** Used to specify whether or not to close a part's components during a close operation. */
        public: enum CloseWholeTree
        {
            CloseWholeTreeFalse/** false */ ,
            CloseWholeTreeTrue/** true */ 
        };

         /** Contains part history event information */
        public:
        struct HistoryEventInformation
        {
            public: /** program name */NXString Program;
            public: /** user id */NXString User;
            public: /** type of machine. eg.  NT Intel */NXString Machine;
            public: /** time of last change */NXString Time;
            public: /** version number */int Version;
            public: HistoryEventInformation() :
                Program(),
                User(),
                Machine(),
                Time(),
                Version()
            {
            }
            /** Constructor for the HistoryEventInformation struct. */ 
            public: HistoryEventInformation(NXString INIT_program /** program name */, 
                    NXString INIT_user /** user id */, 
                    NXString INIT_machine /** type of machine. eg.  NT Intel */, 
                    NXString INIT_time /** time of last change */, 
                    int INIT_version /** version number */) :
                Program(INIT_program),
                User(INIT_user),
                Machine(INIT_machine),
                Time(INIT_time),
                Version(INIT_version)
            {
            }
        };

        /** Indicates how part close should handle component parts when they are modified */
        public: enum CloseModified
        {
            CloseModifiedUseResponses/** Use the responses in
                        @link PartCloseResponses PartCloseResponses@endlink  to determine whether to close a
                        modified part or not */,
            CloseModifiedCloseModified/** Close all modified parts */,
            CloseModifiedDontCloseModified/** Do not close any modified parts */
        };

        /** Specifies the preview mode of the part file. */
        public: enum PartPreview
        {
            PartPreviewNone/** No preview image is stored for the part. */,
            PartPreviewOnSave/** Create a preview image when the part is saved. */,
            PartPreviewOnDemand/** Create a preview image on demand. */
        };

         /** Transient part return data */
        public:
        struct TransientStatus
        {
            public: /** Part is transient */bool Trans;
            public: /** Did part start out in a transient state */bool InitiallyTransient;
            public: /** Part is locked in a transient state */bool Locked;
            public: /** Part has transient children */bool TransientChildren;
            public: TransientStatus() :
                Trans(),
                InitiallyTransient(),
                Locked(),
                TransientChildren()
            {
            }
            /** Constructor for the TransientStatus struct. */ 
            public: TransientStatus(bool INIT_trans /** Part is transient */, 
                    bool INIT_initially_transient /** Did part start out in a transient state */, 
                    bool INIT_locked /** Part is locked in a transient state */, 
                    bool INIT_transient_children /** Part has transient children */) :
                Trans(INIT_trans),
                InitiallyTransient(INIT_initially_transient),
                Locked(INIT_locked),
                TransientChildren(INIT_transient_children)
            {
            }
        };

         /** Incomplete part return data */
        public:
        struct IncompleteStatus
        {
            public: /** Parts structure is incomplete */bool StructIncomplete;
            public: /** Part has components pending */bool PendIncomplete;
            public: /** Part has incomplete children */bool IncompleteChildren;
            public: IncompleteStatus() :
                StructIncomplete(),
                PendIncomplete(),
                IncompleteChildren()
            {
            }
            /** Constructor for the IncompleteStatus struct. */ 
            public: IncompleteStatus(bool INIT_struct_incomplete /** Parts structure is incomplete */, 
                    bool INIT_pend_incomplete /** Part has components pending */, 
                    bool INIT_incomplete_children /** Part has incomplete children */) :
                StructIncomplete(INIT_struct_incomplete),
                PendIncomplete(INIT_pend_incomplete),
                IncompleteChildren(INIT_incomplete_children)
            {
            }
        };

        private: friend class  _BasePartBuilder;
        protected: BasePart();
        /**Returns  the leaf name of the part  <br> License requirements : None */
        public: NXString Leaf
        (
        );
        /**Returns  the full path of the part  <br> License requirements : None */
        public: NXString FullPath
        (
        );
        /**Returns  the units of the part file.  <br> License requirements : None */
        public: NXOpen::BasePart::Units PartUnits
        (
        );
        /** Saves the part whether it is modified or not.  @return  Parts that could not be saved and their associated errors.  <br> License requirements : None */
        public: NXOpen::PartSaveStatus * Save
        (
            NXOpen::BasePart::SaveComponents saveComponentParts /** The part's
                        components are saved if modified if this parameter is set to
                        @link BasePart::SaveComponentsTrue BasePart::SaveComponentsTrue@endlink . */,
            NXOpen::BasePart::CloseAfterSave close /** The part is closed if
                        this parameter is set to @link BasePart::CloseAfterSaveTrue BasePart::CloseAfterSaveTrue@endlink . */
        );
        /** Creates copy of target part.  @return  Parts that could could not saved and their associated errors.  <br> License requirements : None */
        public: NXOpen::PartSaveStatus * SaveAs
        (
            const NXString & newFileName /** name of new part file to create   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Saves a temporary part with the given name.  <br> License requirements : None */
        public: void AssignPermanentName
        (
            const NXString & newFileName /** name of new part file to create   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
        );
        /** Reopens a loaded part.  @return  The reloaded part  <br> License requirements : None */
        public: NXOpen::BasePart * Reopen
        (
            NXOpen::BasePart::CloseWholeTree wholeTree /** If true, unloads all components of the part.
                        If false, unloads only the top-level part */,
            NXOpen::BasePart::CloseModified closeModified /** Behavior of close if component
                        parts are modified. */,
            NXOpen::PartCloseResponses * responses /** Class representing list of parts to close or leave open if modified. Only
                        used if closed_modified is set to
                        @link BasePart::CloseModifiedUseResponses BasePart::CloseModifiedUseResponses@endlink . If
                        @link BasePart::CloseModifiedUseResponses BasePart::CloseModifiedUseResponses@endlink  is set, then
                        any parts that are candidates for being closed that are not in this list
                        will be closed whether modified or not. See
                        @link PartCloseResponses PartCloseResponses@endlink  for how to add responses to this
                        class. */,
            NXOpen::PartReopenReport ** reopenReport /** Report
                       containing results of reopen command */
        );
        /** Reopens a loaded part.  @return  The reloaded part  <br> License requirements : None */
        public: NXOpen::BasePart * ReopenAs
        (
            const NXString & fileName /** name of part file to open   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            NXOpen::BasePart::CloseModified closeModified /** Behavior of close if component
                        parts are modified. */,
            NXOpen::PartCloseResponses * responses /** Class representing list of parts to close or leave open if modified. Only
                        used if closed_modified is set to
                        @link BasePart::CloseModifiedUseResponses BasePart::CloseModifiedUseResponses@endlink . If
                        @link BasePart::CloseModifiedUseResponses BasePart::CloseModifiedUseResponses@endlink  is set, then
                        any parts that are candidates for being closed that are not in this list
                        will be closed whether modified or not. See
                        @link PartCloseResponses PartCloseResponses@endlink  for how to add responses to this
                        class. */,
            NXOpen::PartReopenReport ** reopenReport /** Report
                       containing results of reopen command */
        );
        /** Closes an open part.  <br> License requirements : None */
        public: void Close
        (
            NXOpen::BasePart::CloseWholeTree wholeTree /** If true, unloads all components of the part.
                        If false, unloads only the top-level part */,
            NXOpen::BasePart::CloseModified closeModified /** Behavior of close if component
                        parts are modified. */,
            NXOpen::PartCloseResponses * responses /** Class representing list of parts to close or leave open if modified. Only
                        used if closed_modified is set to
                        @link BasePart::CloseModifiedUseResponses BasePart::CloseModifiedUseResponses@endlink . If
                        @link BasePart::CloseModifiedUseResponses BasePart::CloseModifiedUseResponses@endlink  is set, then
                        any parts that are candidates for being closed that are not in this list
                        will be closed whether modified or not. See
                        @link PartCloseResponses PartCloseResponses@endlink  for how to add responses to this
                        class. */
        );
        /**Returns  the load status of a part. Set to true if part is fully loaded
                and set to false if the part is partially loaded.  <br> License requirements : None */
        public: bool IsFullyLoaded
        (
        );
        /**Returns  the read-only status of a part. Set to true if part is read-only
                and set to false if the part is modifiable.  <br> License requirements : None */
        public: bool IsReadOnly
        (
        );
        /** Ensures that this part is fully loaded. If the part is already fully loaded
                (@link BasePart::IsFullyLoaded BasePart::IsFullyLoaded@endlink  returns true) then
                this method has no effect.
             @return  If the part could not be loaded, this object contains the error information.  <br> License requirements : None */
        public: NXOpen::PartLoadStatus * LoadFully
        (
        );
        /** Ensures that this part is fully loaded. If the part is already fully loaded
                (@link BasePart::IsFullyLoaded BasePart::IsFullyLoaded@endlink  returns true) then
                this method has no effect.
                Does not load any components regardless of the current load option.
             @return  If the part could not be loaded, this object contains the error information.  <br> License requirements : None */
        public: NXOpen::PartLoadStatus * LoadThisPartFully
        (
        );
        /** Ensure that feature data is loaded for a part.  @return  If the part could not be loaded, this object contains the error information.  <br> License requirements : None */
        public: NXOpen::PartLoadStatus * LoadFeatureDataForSelection
        (
        );
        /** Reverse blank all the objects in the part.  <br> License requirements : None */
        public: void ReverseBlankAll
        (
        );
        /** Get history of part  @return  list of history data for the part. The list is sorted in
                                    descending order on version number.  <br> License requirements : None */
        public: std::vector<NXOpen::BasePart::HistoryEventInformation> GetHistoryInformation
        (
        );
        /**Returns  the preview mode  <br> License requirements : None */
        public: NXOpen::BasePart::PartPreview PartPreviewMode
        (
        );
        /**Sets  the preview mode  <br> License requirements : None */
        public: void SetPartPreviewMode
        (
            NXOpen::BasePart::PartPreview mode /** mode */ 
        );
        /** Get the preview image  <br> License requirements : None */
        public: void GetPreviewImage
        (
            int* width /** image width */,
            int* height /** image height */,
            std::vector<int> & pixels /** Array of pixels  */
        );
        /**Returns  the component assembly.  <br> License requirements : None */
        public: NXOpen::Assemblies::ComponentAssembly * ComponentAssembly
        (
        );
        /** Remove the transient status from the input part  <br> License requirements : None */
        public: void RemoveTransience
        (
        );
        /** Reinstate the transient status to the formerly transient input part  <br> License requirements : None */
        public: void ReinstateTransience
        (
        );
        /** Inquire whether the provided part is flagged as being transient  @return   <br> License requirements : None */
        public: NXOpen::BasePart::TransientStatus GetTransientStatus
        (
        );
        /** Inquire whether the provided part is flagged as being incomplete  @return   <br> License requirements : None */
        public: NXOpen::BasePart::IncompleteStatus GetIncompleteStatus
        (
        );
        /** Make additions necessary to complete the incomplete assembly structure of the input part  <br> License requirements : None */
        public: void CompleteStructure
        (
        );
        /**Returns  the field main.  <br> License requirements : None */
        public: NXOpen::Fields::FieldManager * FieldManager
        (
        );
        /** Saves a bookmark file.  <br> License requirements : None */
        public: void SaveBookmark
        (
            const NXString & fileName /** Name of bookmark file.   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
            NXOpen::BasePart::BookmarkOption option /** option */ 
        );
        /** Creates a @link Display::DynamicSectionBuilder Display::DynamicSectionBuilder@endlink  
                The base part must be a displayable part, otherwise an 
                exception will be thrown.
                 <br> 
                By default, the section builder uses the current work view. 
                The current work view must be a modeling view, otherwise an exception 
                will be thrown.    
                 <br>           
                 <br> This method has been deprecated. Use @link BasePart::DynamicSections BasePart::DynamicSections @endlink and @link BasePart::SetDynamicSections BasePart::SetDynamicSections @endlink  
                to create a section builder.
                 <br> 
              @return  
         @deprecated Deprecated in NX6 <br> 
         <br> License requirements : None */
        public: NXOpen::Display::DynamicSectionBuilder * CreateDynamicSectionBuilder
        (
            bool loadFromView /** If true, reads section information from
                                                     working view. Otherwise, default section
                                                     is created. */
        );
        /** Creates a Groups builder  @return  GroupBuilder object  <br> License requirements : None */
        public: NXOpen::GroupBuilder * CreateGatewayGroupBuilder
        (
            NXOpen::Group * group /** group */ 
        );
        /** Creates a @link ReferenceSet ReferenceSet@endlink  object  @return  New reference set object  <br> License requirements : None */
        public: NXOpen::ReferenceSet * CreateReferenceSet
        (
        );
        /** Deletes a @link ReferenceSet ReferenceSet@endlink  object  <br> License requirements : None */
        public: void DeleteReferenceSet
        (
            NXOpen::ReferenceSet * referenceSetObject /** Reference set object to be deleted*/
        );


        private: NXOpen::WCS *wCS;
        /** Returns the WCS instance belonging to this part */
        public: NXOpen::WCS *WCS()
        {
            return wCS;
        }
        private: NXOpen::ArcCollection *arcs;
        /** Returns the ArcCollection instance belonging to this part */
        public: NXOpen::ArcCollection *Arcs()
        {
            return arcs;
        }
        private: NXOpen::ParabolaCollection *parabolas;
        /** Returns the ParabolaCollection instance belonging to this part */
        public: NXOpen::ParabolaCollection *Parabolas()
        {
            return parabolas;
        }
        private: NXOpen::GeometricAnalysis::AnalysisManager *analysisManager;
        /** Returns the GeometricAnalysisManager for part */
        public: NXOpen::GeometricAnalysis::AnalysisManager *AnalysisManager()
        {
            return analysisManager;
        }
        private: NXOpen::MeasureManager *measureManager;
        /** Returns the measure manager for this part */
        public: NXOpen::MeasureManager *MeasureManager()
        {
            return measureManager;
        }
        private: NXOpen::Layer::LayerManager *layers;
        /** Returns the LayerManager for this part */
        public: NXOpen::Layer::LayerManager *Layers()
        {
            return layers;
        }
        private: NXOpen::XformCollection *xforms;
        /** Returns the XformCollection instance belonging to this part */
        public: NXOpen::XformCollection *Xforms()
        {
            return xforms;
        }
        private: NXOpen::OffsetCollection *offsets;
        /** Returns the OffsetCollection instance belonging to this part */
        public: NXOpen::OffsetCollection *Offsets()
        {
            return offsets;
        }
        private: NXOpen::PlaneCollection *planes;
        /** Return a collection of Planes */
        public: NXOpen::PlaneCollection *Planes()
        {
            return planes;
        }
        private: NXOpen::HyperbolaCollection *hyperbolas;
        /** Returns the HyperbolaCollection instance belonging to this part */
        public: NXOpen::HyperbolaCollection *Hyperbolas()
        {
            return hyperbolas;
        }
        private: NXOpen::CurveCollection *curves;
        /** Returns the CurveCollection instance belonging to this part */
        public: NXOpen::CurveCollection *Curves()
        {
            return curves;
        }
        private: NXOpen::PointCollection *points;
        /** Returns the PointCollection instance belonging to this part */
        public: NXOpen::PointCollection *Points()
        {
            return points;
        }
        private: NXOpen::EllipseCollection *ellipses;
        /** Returns the EllipseCollection instance belonging to this part */
        public: NXOpen::EllipseCollection *Ellipses()
        {
            return ellipses;
        }
        private: NXOpen::LineCollection *lines;
        /** Returns the LineCollection instance belonging to this part */
        public: NXOpen::LineCollection *Lines()
        {
            return lines;
        }
        private: NXOpen::SplineCollection *splines;
        /** Returns the SplineCollection instance belonging to this part */
        public: NXOpen::SplineCollection *Splines()
        {
            return splines;
        }
        private: NXOpen::NXMatrixCollection *nXMatrices;
        /** Returns the NXMatrixCollection instance belonging to this part */
        public: NXOpen::NXMatrixCollection *NXMatrices()
        {
            return nXMatrices;
        }
        private: NXOpen::ScalarCollection *scalars;
        /** Returns the ScalarCollection instance belonging to this part */
        public: NXOpen::ScalarCollection *Scalars()
        {
            return scalars;
        }
        private: NXOpen::FontCollection *fonts;
        /** Returns the FontCollection instance belonging to this part */
        public: NXOpen::FontCollection *Fonts()
        {
            return fonts;
        }
        private: NXOpen::DatumCollection *datums;
        /** Returns the DatumCollection instance belonging to this part */
        public: NXOpen::DatumCollection *Datums()
        {
            return datums;
        }
        private: NXOpen::ViewCollection *views;
        /** Returns the ViewCollection instance belonging to this part */
        public: NXOpen::ViewCollection *Views()
        {
            return views;
        }
        private: NXOpen::ExpressionCollection *expressions;
        /** Returns the ExpressionCollection instance belonging to this part */
        public: NXOpen::ExpressionCollection *Expressions()
        {
            return expressions;
        }
        private: NXOpen::UnitCollection *unitCollection;
        /** Returns a collection of Units */
        public: NXOpen::UnitCollection *UnitCollection()
        {
            return unitCollection;
        }
        private: NXOpen::DirectionCollection *directions;
        /** Returns the DirectionCollection instance belonging to this part */
        public: NXOpen::DirectionCollection *Directions()
        {
            return directions;
        }
        private: NXOpen::ModelingViewCollection *modelingViews;
        /** Returns the ModelingViewCollection instance belonging to this part */
        public: NXOpen::ModelingViewCollection *ModelingViews()
        {
            return modelingViews;
        }
        private: NXOpen::Layer::CategoryCollection *layerCategories;
        /** Returns a collection of layer categories */
        public: NXOpen::Layer::CategoryCollection *LayerCategories()
        {
            return layerCategories;
        }
        private: NXOpen::RuleManager *ruleManager;
        /** Returns the rule manager for this part */
        public: NXOpen::RuleManager *RuleManager()
        {
            return ruleManager;
        }
        private: NXOpen::Preferences::PartPreferences *preferences;
        /** Returns the PartPreferences instance belonging to this part */
        public: NXOpen::Preferences::PartPreferences *Preferences()
        {
            return preferences;
        }
        private: NXOpen::AxisCollection *axes;
        /** Returns the AxisCollection instance belonging to this part */
        public: NXOpen::AxisCollection *Axes()
        {
            return axes;
        }
        private: NXOpen::LightCollection *lights;
        /** Returns the LightCollection instance belonging to this part */
        public: NXOpen::LightCollection *Lights()
        {
            return lights;
        }
        private: NXOpen::SectionCollection *sections;
        /** Returns the SectionCollection instance belonging to this part */
        public: NXOpen::SectionCollection *Sections()
        {
            return sections;
        }
        private: NXOpen::ScCollectorCollection *scCollectors;
        /** Returns the ScCollectorCollection instance belonging to this part */
        public: NXOpen::ScCollectorCollection *ScCollectors()
        {
            return scCollectors;
        }
        private: NXOpen::CoordinateSystemCollection *coordinateSystems;
        /** Returns the CoordinateSystemCollection instance belonging to this part */
        public: NXOpen::CoordinateSystemCollection *CoordinateSystems()
        {
            return coordinateSystems;
        }
        private: NXOpen::LayoutCollection *layouts;
        /** Returns the LayoutCollection instance belonging to this part */
        public: NXOpen::LayoutCollection *Layouts()
        {
            return layouts;
        }
        private: NXOpen::PDM::PdmPart *pDMPart;
        /** Returns the instance of the PDM.PdmPart class */
        public: NXOpen::PDM::PdmPart *PDMPart()
        {
            return pDMPart;
        }
        private: NXOpen::Display::CameraCollection *cameras;
        /** Returns the Display.CameraCollection instance belonging to this part */
        public: NXOpen::Display::CameraCollection *Cameras()
        {
            return cameras;
        }
        private: NXOpen::Display::DynamicSectionCollection *dynamicSections;
        /** Returns the Display.DynamicSectionCollection instance belonging to this part */
        public: NXOpen::Display::DynamicSectionCollection *DynamicSections()
        {
            return dynamicSections;
        }
        private: NXOpen::Display::DecalCollection *decals;
        /** Returns the Display.DecalCollection instance belonging to this part */
        public: NXOpen::Display::DecalCollection *Decals()
        {
            return decals;
        }
        private: NXOpen::UserDefinedObjects::UserDefinedObjectManager *userDefinedObjectManager;
        /** Returns the @link UserDefinedObjects::UserDefinedObjectManager UserDefinedObjects::UserDefinedObjectManager@endlink  belonging to this session */
        public: NXOpen::UserDefinedObjects::UserDefinedObjectManager *UserDefinedObjectManager()
        {
            return userDefinedObjectManager;
        }
        private: NXOpen::CAE::FunctionCollection *functions;
        /** Returns the CAE.FunctionCollection for this part*/
        public: NXOpen::CAE::FunctionCollection *Functions()
        {
            return functions;
        }
        private: NXOpen::Display::SelPrefCollection *selPref;
        /** Returns the Display.SelPrefCollection instance belonging to this part */
        public: NXOpen::Display::SelPrefCollection *SelPref()
        {
            return selPref;
        }
        private: NXOpen::PlotManager *plotManager;
        /** Returns the PlotManager instance belonging to this part */
        public: NXOpen::PlotManager *PlotManager()
        {
            return plotManager;
        }
        private: NXOpen::Features::BaseFeatureCollection *baseFeatures;
        /** Returns the FeatureCollection instance belonging to this part */
        public: NXOpen::Features::BaseFeatureCollection *BaseFeatures()
        {
            return baseFeatures;
        }
        private: NXOpen::ColorManager *colors;
        /** Manages the standard NX colors */
        public: NXOpen::ColorManager *Colors()
        {
            return colors;
        }
        private: NXOpen::Optimization::OptimizationCollection *optimization;
        /** Returns the optimization instance belonging to this part */
        public: NXOpen::Optimization::OptimizationCollection *Optimization()
        {
            return optimization;
        }
        private: NXOpen::MaterialManager *materialManager;
        /** Returns the Material Manager belonging to this Part */
        public: NXOpen::MaterialManager *MaterialManager()
        {
            return materialManager;
        }
        private: NXOpen::Optimization::DesignStudyCollection *designStudy;
        /** Returns the design study instance belonging to this part */
        public: NXOpen::Optimization::DesignStudyCollection *DesignStudy()
        {
            return designStudy;
        }
        private: NXOpen::PartSaveOptions *saveOptions;
        /** Returns the PartSaveOptions instance belonging to this part */
        public: NXOpen::PartSaveOptions *SaveOptions()
        {
            return saveOptions;
        }
        private: NXOpen::Assemblies::ProductOutlineManager *assemblies;
        /** Returns the @link NXOpen::Assemblies::ProductOutlineManager NXOpen::Assemblies::ProductOutlineManager@endlink  belonging to this session */
        public: NXOpen::Assemblies::ProductOutlineManager *Assemblies()
        {
            return assemblies;
        }
        private: NXOpen::Assemblies::AssemblyManager *assemblyManager;
        /** Returns the @link NXOpen::Assemblies::AssemblyManager NXOpen::Assemblies::AssemblyManager@endlink  belonging to this session */
        public: NXOpen::Assemblies::AssemblyManager *AssemblyManager()
        {
            return assemblyManager;
        }
        private: NXOpen::Display::TrueShadingCollection *sHEDObjs;
        /** Returns the Display.TrueShadingCollection instance belonging to this part */
        public: NXOpen::Display::TrueShadingCollection *SHEDObjs()
        {
            return sHEDObjs;
        }
        private: NXOpen::Display::GridCollection *grids;
        /** Returns the Display.GridCollection instance belonging to this part */
        public: NXOpen::Display::GridCollection *Grids()
        {
            return grids;
        }
        public: virtual void initialize();
    };
}
#undef EXPORTLIBRARY
#endif