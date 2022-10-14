#ifndef NXOpen_POSITIONINGDIMENSION_HXX_INCLUDED
#define NXOpen_POSITIONINGDIMENSION_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     PositioningDimension.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/NXObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class PositioningDimension;
    class Expression;
    class NXObject;
    class _PositioningDimensionBuilder;
    /** Represents a dimension object attached to the feature */
    class NXOPENCPPEXPORT PositioningDimension : public NXObject
    {
        /** Represents the subtype of the positioning dimension */
        public: enum Subtype
        {
            SubtypeHorizontal/** Horizontal dimension */,
            SubtypeVertical/** Vertical dimension */,
            SubtypeParallel/** Parallel dimension */,
            SubtypePerpendicular/** Perpendicular dimension */,
            SubtypeParallelDistance/** Parallel at a distance dimension */,
            SubtypeAngular/** Angular dimension */,
            SubtypePointOntoPoint/** Point onto point dimension */,
            SubtypePointOntoLine/** Point onto line dimension */,
            SubtypeLineOntoLine/** Line onto line dimension */
        };

        private: friend class  _PositioningDimensionBuilder;
        protected: PositioningDimension();
        /**
            Returns the subtype of the dimension.
             @return  Subtype of the dimension  <br> License requirements : solid_modeling ("SOLIDS MODELING"), features_modeling ("FEATURES MODELING") */
        public: NXOpen::PositioningDimension::Subtype GetSubtype
        (
        );
        /**Returns  
            the expression for the dimension.
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), features_modeling ("FEATURES MODELING") */
        public: NXOpen::Expression * Expression
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Expression() Expression@endlink instead.
        @deprecated
        */
        public: NXOpen::Expression * GetExpression
        (
        ) { return this->Expression(); }
        /**Returns  
            the target entity.
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), features_modeling ("FEATURES MODELING") */
        public: NXOpen::NXObject * Target
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Target() Target@endlink instead.
        @deprecated
        */
        public: NXOpen::NXObject * GetTarget
        (
        ) { return this->Target(); }
        /**Returns  
            the tool entity.
             <br> License requirements : solid_modeling ("SOLIDS MODELING"), features_modeling ("FEATURES MODELING") */
        public: NXOpen::NXObject * Tool
        (
        );
        /** <b>Deprecated</b>:<br>
        &nbsp;&nbsp;&nbsp;Use @link Tool() Tool@endlink instead.
        @deprecated
        */
        public: NXOpen::NXObject * GetTool
        (
        ) { return this->Tool(); }
    };
}
#undef EXPORTLIBRARY
#endif