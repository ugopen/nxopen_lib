#ifndef NXOpen_PREFERENCES_ROUTINGPATH_HXX_INCLUDED
#define NXOpen_PREFERENCES_ROUTINGPATH_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_RoutingPath.ja
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
    namespace Preferences
    {
        class RoutingPath;
    }
    namespace Preferences
    {
        class RoutingApplicationView;
    }
    namespace Preferences
    {
        /** The RoutingPath object stores a set of path preferences.  <br> To obtain an instance of this class, refer to @link Preferences::RoutingApplicationView Preferences::RoutingApplicationView@endlink  <br> */
        class NXOPENCPPEXPORT RoutingPath
        {
            /** Describes the types of curves allowed in a routing application.  */
            public: enum CurveType
            {
                CurveTypeLine/** UF_ROUTE_AV_CURVES_LINES */,
                CurveTypeArc/** UF_ROUTE_AV_CURVES_ARCS */,
                CurveTypeSpline/** UF_ROUTE_AV_CURVES_SPLINES */
            };

            /** Describes the types of corners allowed in a routing application.  */
            public: enum AllowedCornerType
            {
                AllowedCornerTypeNone/** UF_ROUTE_AV_CORNERS_NONE */,
                AllowedCornerTypeBend/** UF_ROUTE_AV_CORNERS_BEND */,
                AllowedCornerTypeCope/** UF_ROUTE_AV_CORNERS_COPE */,
                AllowedCornerTypeMiter/** UF_ROUTE_AV_CORNERS_MITER */,
                AllowedCornerTypeSbend/** UF_ROUTE_AV_CORNERS_SBEND */
            };

            /** Describes the types of corners allowed in a routing application.  */
            public: enum DefaultCornerType
            {
                DefaultCornerTypeNone = -1/** No Corner*/,
                DefaultCornerTypeBend/** Bend Corner*/,
                DefaultCornerTypeMiter/** Miter Corner */,
                DefaultCornerTypeBendTable/** Not really a corner type.
                                                                                  Used to indicate use of bend table in
                                                                                  conjunction with a Bend corner */
            };

            /** Describes method used to determine bend radius on a bend or sbend corner */
            public: enum RadiusMethod
            {
                RadiusMethodRadius/** Use specified radius */,
                RadiusMethodRatio/** Use ratio to stock diameter to determine radius */,
                RadiusMethodTable/** Use radius obtained from a bend table lookup */
            };

            /** Describes units of specified radius value [JA_ROUTE_PATH_PREFS_radius_method_radius only]. */
            public: enum RadiusUnits
            {
                RadiusUnitsNone/** Unspecified. Use units of part file. */,
                RadiusUnitsInches/** Use inch units */,
                RadiusUnitsMillimeters/** Use metric (mm) units */
            };

            /** Should Smart RCPs be created during path creation in Create Path? */
            public: enum CreateSmartRcps
            {
                CreateSmartRcpsFalse/** Do not create smart RCPs. */,
                CreateSmartRcpsTrue/** Create smart RCPs. */
            };

            /** Should duplicate RCPs be merged after a Transform [Move or Copy] operation? */
            public: enum MergeDupRcps
            {
                MergeDupRcpsFalse/** Do not merge duplicate RCPs. */,
                MergeDupRcpsTrue/** Merge duplicate RCPs. */
            };

            /** Should a branch selection confirmation dialog be show during Path selection? */
            public: enum ConfirmBranchSel
            {
                ConfirmBranchSelFalse/** Do not confirm branch selection. */,
                ConfirmBranchSelTrue/** Confirm branch selection. */
            };

            /** Should fixed length splines ignore length constraint violations and update? */
            public: enum ContinueUpdOnError
            {
                ContinueUpdOnErrorFalse/** false */ ,
                ContinueUpdOnErrorTrue/** true */ 
            };

            /** Path curve chaining methods */
            public: enum ChainMethod
            {
                ChainMethodNoBranch/** Curves must be mono-connected */,
                ChainMethodContinuous/** Tangents must match at each connection */,
                ChainMethodTangent/** Use curve with closest tangent when searching */,
                ChainMethodCycle/** Return all chains */,
                ChainMethodMinDist/** Chain with minimum path length */,
                ChainMethodMaxDist/** Chain with maximum path length */
            };

            /** Chain occurrences of curves ? [i.e. curves not in the work part] */
            public: enum OccChainable
            {
                OccChainableFalse/** false */ ,
                OccChainableTrue/** true */ 
            };

            /** Display a certain routing object? */
            public: enum DisplayObject
            {
                DisplayObjectFalse/** false */ ,
                DisplayObjectTrue/** true */ 
            };

            /** Create slope associativity constraints during line path creation [from ports only] */
            public: enum CreateSlopeConstraints
            {
                CreateSlopeConstraintsFalse/** false */ ,
                CreateSlopeConstraintsTrue/** true */ 
            };

            private: NXOpen::Preferences::RoutingApplicationView* m_owner;
            public: explicit RoutingPath(NXOpen::Preferences::RoutingApplicationView *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** Query the types of curves allowed in an application view  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Preferences::RoutingPath::CurveType> GetAllowedCurves
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetAllowedCurves
            (
                const std::vector<NXOpen::Preferences::RoutingPath::CurveType> & allowed_curves /** allowed curves */ 
            );
            /** Query the types of corners allowed in an application view  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Preferences::RoutingPath::AllowedCornerType> GetAllowedCorners
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetAllowedCorners
            (
                const std::vector<NXOpen::Preferences::RoutingPath::AllowedCornerType> & allowed_corners /** allowed corners */ 
            );
            /** Query the default corner type in an application view  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::DefaultCornerType GetDefaultCorner
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetDefaultCorner
            (
                NXOpen::Preferences::RoutingPath::DefaultCornerType default_corner /** default corner */ 
            );
            /** Query wether the default corner should use bend ratio.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::RadiusMethod GetBendRadiusMethod
            (
            );
            /** Set whether the default corner should use bend ratio.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetBendRadiusMethod
            (
                NXOpen::Preferences::RoutingPath::RadiusMethod radius_method /** radius method */ 
            );
            /** Needs a work part and a loaded applicaiton view.
                        Radius units are converted to work part units automatically.
                        Returns -1 and quits if input requirements are not met.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetBendRadius
            (
            );
            /** Needs a work part and a loaded applicaiton view.
                        Radius units are assumed to be work part units and are set automatically.
                        Returns -1 and quits if input requirements are not met.  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetBendRadius
            (
                double bend_radius /** bend radius */ 
            );
            /** Query bend radius units stored in path preferences  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::RadiusUnits GetBendRadiusUnits
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetBendRadiusUnits
            (
                NXOpen::Preferences::RoutingPath::RadiusUnits radius_units /** radius units */ 
            );
            /** Query default bend ratio. Used when default corner uses bend ratio method  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetBendRatio
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetBendRatio
            (
                double bend_ratio /** bend ratio */ 
            );
            /** Query default bend table. Used when default corner uses bend table method  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetBendTable
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetBendTable
            (
                const NXString & bend_table_name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Query loaded bend table names. A bend table maps a stock outer diameter to a
                        radius appropriate for a certain bending machine  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXString> GetBendTables
            (
            );
            /** Query loaded bend table filenames. A bend table file can contain one or more named
                        bend tables. Loading a bend table file loads all its constituent tables into memory.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXString> GetBendTableFilenames
            (
            );
            /** Load a specified bend table file.  @return  Descriptive error text, when appropriate  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString LoadBendTableFile
            (
                const NXString & bend_table_filename /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Query bend radius from a loaded bend table. Returns a radius of -1 if input table is not
                        loaded  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetBendTableRadius
            (
                const NXString & bend_table_name /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */,
                double diameter /** diameter */ 
            );
            /** Create smart RCPs during path creation?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::CreateSmartRcps GetCreateSmartRcps
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetCreateSmartRcps
            (
                NXOpen::Preferences::RoutingPath::CreateSmartRcps create_smart /** create smart */ 
            );
            /** Merge duplicate RCPs after a Transform [Move or Copy] operation?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::MergeDupRcps GetMergeDuplicateRcps
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetMergeDuplicateRcps
            (
                NXOpen::Preferences::RoutingPath::MergeDupRcps merge_duplicates /** merge duplicates */ 
            );
            /** Confirm branch selection during Path selection?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::ConfirmBranchSel GetConfirmBranchSelection
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetConfirmBranchSelection
            (
                NXOpen::Preferences::RoutingPath::ConfirmBranchSel confirm_branch_sel /** confirm branch sel */ 
            );
            /** Query default stock offset expression used by Create Path and Create Stock Offset Port [via Qualify Part]  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXString GetStockOffsetExpression
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetStockOffsetExpression
            (
                const NXString & stock_offset_exp /**   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** Query default down direction for fixed length splines  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::ContinueUpdOnError GetContinueUpdateOnError
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetContinueUpdateOnError
            (
                NXOpen::Preferences::RoutingPath::ContinueUpdOnError update /** update */ 
            );
            /** Create slope constraints during line path creation to and from fitting ports?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::CreateSlopeConstraints GetCreateSlopeConstraints
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetCreateSlopeConstraints
            (
                NXOpen::Preferences::RoutingPath::CreateSlopeConstraints create_slope_constraints /** create slope constraints */ 
            );
            /** Query path curve chaining method  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::ChainMethod GetCurveChainingMethod
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetCurveChainingMethod
            (
                NXOpen::Preferences::RoutingPath::ChainMethod chain_method /** chain method */ 
            );
            /** Query all the types of chainable curve types  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: std::vector<NXOpen::Preferences::RoutingPath::CurveType> GetChainableCurveTypes
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetChainableCurveTypes
            (
                const std::vector<NXOpen::Preferences::RoutingPath::CurveType> & chainable_curve_types /** chainable curve types */ 
            );
            /** Query if curve occurrences [curves not in the work part] are chainable  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::OccChainable GetOccurrenceChainable
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetOccurrenceChainable
            (
                NXOpen::Preferences::RoutingPath::OccChainable occ_chainable /** occ chainable */ 
            );
            /** Display RCPs?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::DisplayObject GetDisplayRcps
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetDisplayRcps
            (
                NXOpen::Preferences::RoutingPath::DisplayObject display_rcps /** display rcps */ 
            );
            /** Display ports?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::DisplayObject GetDisplayPorts
            (
            );
            /** Display ports in the model?  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetDisplayPorts
            (
                NXOpen::Preferences::RoutingPath::DisplayObject display_ports /** display ports */ 
            );
            /** Display segment constraints?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::DisplayObject GetDisplaySegmentConstraints
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetDisplaySegmentConstraints
            (
                NXOpen::Preferences::RoutingPath::DisplayObject display_constraints /** display constraints */ 
            );
            /** Display anchors?  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::DisplayObject GetDisplayAnchors
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetDisplayAnchors
            (
                NXOpen::Preferences::RoutingPath::DisplayObject display_anchors /** display anchors */ 
            );
            /** Displayed port length  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: double GetDisplayPortLength
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetDisplayPortLength
            (
                double display_port_length /** display port length */ 
            );
            /** Heal Path curve type.  @return   <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: NXOpen::Preferences::RoutingPath::CurveType GetHealPathCurveType
            (
            );
            /**  <br> License requirements : routing_combined ("Routing Combined") OR routing_electrical ("Routing Electrical") OR routing_mechanical ("Routing Mechanical") */
            public: void SetHealPathCurveType
            (
                NXOpen::Preferences::RoutingPath::CurveType heal_path_curve_type /** heal path curve type */ 
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
