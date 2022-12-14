#ifndef NXOpen_SECTION_HXX_INCLUDED
#define NXOpen_SECTION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Section.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/SectionData.hxx>
#include <NXOpen/SelectionIntentRule.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class Section;
    class DisplayableObject;
    class ICurve;
    class NXObject;
    class Point;
    class SectionData;
    class SelectionIntentRule;
    class _SectionBuilder;
    /** Represents a section
     <br> 
    Section consists of "chained_entity", a chain  or a single entity of edge or curve.
    The entire chain(or a single entity) may be used by the section or only a portion of the chain 
    (or single entity) might be used. The portion of the chain (or single entity) that is used is
    defined by the "start_connector" and "end_connector". 
     <br> 
     <br> 
    start_connector: It represents the start of the portion of the chain (or single entity) that is used. 
    If "start_connector" is null (Nothing), then the start point of the chained_entity along its "natural" 
    direction is used.
     <br> 
     <br> 
    start_connector_intersection_point: The point of intersection of the "chained_entity" and the 
    "start_connector". This is used to determine what portion of the chain to use in case the 
    "start_connector" intersects the "chained_entity" in multiple locations.
     <br> 
     <br> 
    end_connector: It represents the end of the portion of the chain (or single entity) that is used.
     <br> 
     <br> 
    end_connector_intersection_point: The point of intersection of the "chained_entity" and the 
    "end_connector". This is used to determine what portion of the chain to use in case the "end_connector" 
    intersects the "chained_entity" in multiple locations.
     <br> 
     <br> To create a new instance of this class, use @link SectionCollection::CreateSection SectionCollection::CreateSection@endlink  <br> */
    class NXOPENCPPEXPORT Section : public DisplayableObject
    {
        /** Defines mode with respect to feature create or edit mode.
             */
        public: enum Mode
        {
            ModeCreate/** Feature is being created */,
            ModeEdit/** Feature is being edited */
        };

        private: friend class  _SectionBuilder;
        protected: Section();
        /**Sets  the chaining tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetChainingTolerance
        (
            double chaining_tolerance /** chaining tolerance*/
        );
        /**Sets  the distance tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetDistanceTolerance
        (
            double distance_tolerance /** distance tolerance*/
        );
        /**Sets  the angle tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetAngleTolerance
        (
            double angle_tolerance /** angle tolerance*/
        );
        /**Returns  the chaining tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: double ChainingTolerance
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link ChainingTolerance() ChainingTolerance@endlink instead.
        @deprecated
        */
        public: double GetChainingTolerance
        (
        ) { return this->ChainingTolerance(); }
        /**Returns  the distance tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: double DistanceTolerance
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link DistanceTolerance() DistanceTolerance@endlink instead.
        @deprecated
        */
        public: double GetDistanceTolerance
        (
        ) { return this->DistanceTolerance(); }
        /**Returns  the angle tolerance  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: double AngleTolerance
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link AngleTolerance() AngleTolerance@endlink instead.
        @deprecated
        */
        public: double GetAngleTolerance
        (
        ) { return this->AngleTolerance(); }
        /** Adds selection intent rules to the section. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void AddToSection
        (
            const std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules. To create selection intent rules see
                                             documentation of @link ScRuleFactory ScRuleFactory@endlink 
                                             for more details. */,
            NXOpen::NXObject * seed /** Seed curve, edge or face*/,
            NXOpen::NXObject * start_connector /** It represents the start of the portion of the chain 
                                                                         (or single entity) that is used. If "start_connector" 
                                                                         is null (Nothing), then the start point of the 
                                                                         chained_entity along its "natural" direction is used. 
                                                                         It can be point, curve or edge */,
            const NXOpen::Point3d & start_connector_intersection_point /** The point of intersection of the "chained_entity"
                                                                            and the "start_connector". This is used to determine
                                                                            what portion of the chain to use in case the 
                                                                            "start_connector" intersects the "chained_entity" 
                                                                            in multiple locations.*/,
            NXOpen::NXObject * end_connector /** It represents the end of the portion of the chain (or single entity) that is used.
                                                                       It can be point, curve or edge */,
            const NXOpen::Point3d & end_connector_intersection_point /** The point of intersection of the "chained_entity" 
                                                                          and the "end_connector". This is used to determine 
                                                                          what portion of the chain to use in case 
                                                                          the "end_connector" intersects the "chained_entity" 
                                                                          in multiple locations.*/,
            const NXOpen::Point3d & help_point /** This is used to determine which portion 
                                                    of the chain to use for creating section.*/,
            NXOpen::Section::Mode feature_mode /** Feature create or edit mode.*/
        );
        /** Adds selection intent rules to the section. <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void AddToSection
        (
            const std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules. To create selection intent rules see
                                             documentation of @link ScRuleFactory ScRuleFactory@endlink 
                                             for more details. */,
            NXOpen::NXObject * seed /** Seed curve, edge or face*/,
            NXOpen::NXObject * start_connector /** It represents the start of the portion of the chain 
                                                                         (or single entity) that is used. If "start_connector" 
                                                                         is null (Nothing), then the start point of the 
                                                                         chained_entity along its "natural" direction is used. 
                                                                         It can be point, curve or edge */,
            NXOpen::NXObject * end_connector /** It represents the end of the portion of the chain (or single entity) that is used.
                                                                       It can be point, curve or edge */,
            const NXOpen::Point3d & help_point /** This is used to determine which portion 
                                                    of the chain to use for creating section.*/,
            NXOpen::Section::Mode feature_mode /** Feature create or edit mode.*/
        );
        /** Removes selection intent rules from the section.
             <br>  
            To get selection intent rules of the section 
            see documentation for @link Section::GetSectionData Section::GetSectionData@endlink  and
            @link SectionData::GetRules  SectionData::GetRules @endlink  for more details. 
             <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void RemoveRules
        (
            const std::vector<NXOpen::SelectionIntentRule *> & rules /** Selection intent rules.*/,
            NXOpen::NXObject * start_connector /** It represents the start of the portion of 
                                                                         the chain (or single entity) that is used. 
                                                                         If "start_connector" is null (Nothing), 
                                                                         then the start point of the chained_entity 
                                                                         along its "natural" direction is used. 
                                                                         It can be be point, curve or edge */,
            NXOpen::NXObject * end_connector /** It represents the end of the portion of 
                                                                       the chain (or single entity) that is used. 
                                                                       It can be be point, curve or edge */,
            NXOpen::Section::Mode feature_mode /** Feature create or edit mode*/
        );
        /** Removes one section element curve.
             <br>  
            To get selection element
            see documentation for @link Section::GetSectionData Section::GetSectionData@endlink  and
            @link SectionData::GetSectionElementsData  SectionData::GetSectionElementsData @endlink  for more details.
             <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void RemoveSingleSectionElement
        (
            NXOpen::ICurve * section_element /** The element that constructs the section */,
            NXOpen::ICurve * start_connector /** The element that is connected to the 
                                       section_element, at the start_point*/,
            const NXOpen::Point3d & start_point /** Start point*/,
            NXOpen::ICurve * end_connector /** The element that is connected to the 
                                       section_element, at the end_point*/,
            const NXOpen::Point3d & end_point /** End Point*/,
            NXOpen::Section::Mode feature_mode /** Feature create or edit mode*/
        );
        /** Removes one section element curve.
             <br>  
            To get selection element
            see documentation for @link Section::GetSectionData Section::GetSectionData@endlink  and
            @link SectionData::GetSectionElementsData  SectionData::GetSectionElementsData @endlink  for more details.
             <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void RemoveSingleSectionElement
        (
            NXOpen::ICurve * section_element /** The element that constructs the section */,
            NXOpen::NXObject * start_connector /** The element that is connected to the 
                                       section_element near it's start_point*/,
            NXOpen::NXObject * end_connector /** The element that is connected to the 
                                       section_element near it's end_point*/,
            NXOpen::Section::Mode feature_mode /** Feature create or edit mode*/
        );
        /** Removes all the selection intent rules related to the section element.
             <br>  
            To get selection elements of the section, see documentation for @link Section::GetSectionData Section::GetSectionData@endlink  and
            @link SectionData::GetSectionElementsData  SectionData::GetSectionElementsData @endlink  for more details.
             <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void RemoveRules
        (
            NXOpen::ICurve * section_element /** The element that constructs the section */,
            NXOpen::ICurve * start_connector /** The element that is connected to the 
                                       section_element, at the start_point*/,
            const NXOpen::Point3d & start_point /** Start point */,
            NXOpen::ICurve * end_connector /** The element that is connected to the 
                                       section_element, at the end_point */,
            const NXOpen::Point3d & end_point /** End point*/,
            NXOpen::Section::Mode feature_mode /** Feature create or edit mode.*/
        );
        /** Removes all the selection intent rules related to the section element.
             <br>  
            To get selection elements of the section, see documentation for @link Section::GetSectionData Section::GetSectionData@endlink  and
            @link SectionData::GetSectionElementsData  SectionData::GetSectionElementsData @endlink  for more details.
             <br> 
             <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void RemoveRules
        (
            NXOpen::ICurve * section_element /** The element that constructs the section */,
            NXOpen::NXObject * start_connector /** The element that is connected to the 
                                       section_element near it's start_point*/,
            NXOpen::NXObject * end_connector /** The element that is connected to the 
                                       section_element near it's end_point */,
            NXOpen::Section::Mode feature_mode /** Feature create or edit mode.*/
        );
        /** Sets the start element and the direction of the section.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void SetStartAndDirection
        (
            NXOpen::ICurve * start_element /** The element, curve or edge, specifying
                                                        the starting of the section.
                                                        If the section is a loop, then the loop is started
                                                        by start_element and the direction is 
                                                        followed the input direction. 
                                                        If the section is not a loop, then the section can be started 
                                                        by other element, but the direction of the section is defined by
                                                        the start_element and 
                                                        direction. */,
            const NXOpen::Point3d & start_point /** The origin of the vector that defines the direction of
                                                         the section. This point has to be on the start_element. */,
            const NXOpen::Vector3d & direction /** The direction of the vector defines the direction of
                                                        the section. */
        );
        /** Gets the start element and the direction of the section.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetStartAndDirection
        (
            NXOpen::ICurve ** start_element /** The element, curve or edge, specifying
                                                        the starting of the section.
                                                        If the section is a loop, then the loop is started
                                                        by start_element and the direction is 
                                                        followed the input direction. 
                                                        If the section is not a loop, then the section can be started 
                                                        by other element, but the direction of the section is defined by
                                                        the  start_element and direction. */,
            NXOpen::Point3d* start_point /** The origin of the vector that defines the direction of
                                                         the section. This point has to be on the start_element. */,
            NXOpen::Vector3d* direction /** The direction of the vector defines the direction of
                                                        the section. */
        );
        /** Gets the section data  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void GetSectionData
        (
            std::vector<NXOpen::SectionData *> & section_data /** Section data consists of selection intent rules,
                                                       section elements, start and end connector. */
        );
        /** Destroy the section object  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void Destroy
        (
        );
        /** Reverse the section direction  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void ReverseDirection
        (
        );
        /** Add smart point into section.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void AddSmartPoint
        (
            NXOpen::Point * smart_pt /** Smart point tobe added into section. */,
            double tol /** Tolerance. */
        );
        /** Allow self intersecting section or not. By default self intersection is allowed.  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
        public: void AllowSelfIntersection
        (
            bool allow_self_intersection /** True if self-intersecting section is allowed else false*/
        );
    };
}
#undef EXPORTLIBRARY
#endif
