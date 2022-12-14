#ifndef NXOpen_SKETCHHELPEDGEOMETRICCONSTRAINT_HXX_INCLUDED
#define NXOpen_SKETCHHELPEDGEOMETRICCONSTRAINT_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     SketchHelpedGeometricConstraint.ja
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
#include <NXOpen/INXObject.hxx>
#include <NXOpen/ISketchHelpedConstraint.hxx>
#include <NXOpen/SketchGeometricConstraint.hxx>
#include <NXOpen/ugmath.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    class SketchHelpedGeometricConstraint;
    namespace Assemblies
    {
        class Component;
    }
    class BasePart;
    class INXObject;
    class ISketchHelpedConstraint;
    class SketchGeometricConstraint;
    class _SketchHelpedGeometricConstraintBuilder;
    /** Represents a geometric sketch constraint that has a help point or help parameter */
    class NXOPENCPPEXPORT SketchHelpedGeometricConstraint : public SketchGeometricConstraint, public virtual ISketchHelpedConstraint
    {
        private: friend class  _SketchHelpedGeometricConstraintBuilder;
        protected: SketchHelpedGeometricConstraint();
        /** Gets the help data for the constraint  <br> License requirements : None */
        public: virtual void GetHelpData
        (
            bool* has_help_point1 /** Whether the constraint's first associated geometric item has an associated help point */,
            bool* has_help_point2 /** Whether the constraint's second associated geometric item has an associated help point */,
            bool* has_help_parameter1 /** Whether the constraint's first associated geometric item has an associated help parameter */,
            bool* has_help_parameter2 /** Whether the constraint's second associated geometric item has an associated help parameter */,
            NXOpen::Point3d* help_point1 /** The first help point.  Not used unless has_help_point1 is true. */,
            NXOpen::Point3d* help_point2 /** The second help point.  Not used unless has_help_point2 is true. */,
            double* help_parameter1 /** The first help parameter.  Not used unless has_help_parameter1 is true. */,
            double* help_parameter2 /** The second help parameter.  Not used unless has_help_parameter2 is true. */
        );
        /** Sets the help points for the constraint  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: virtual void SetHelpPoints
        (
            bool has_help1 /** Whether the constraint's first associated geometric item has an associated help point */,
            bool has_help2 /** Whether the constraint's second associated geometric item has an associated help point */,
            const NXOpen::Point3d & help_point1 /** The first help point.  Not used unless has_help1 is true. */,
            const NXOpen::Point3d & help_point2 /** The second help point.  Not used unless has_help2 is true. */
        );
        /** Sets the help parameters for the constraint  <br> License requirements : solid_modeling ("SOLIDS MODELING") OR drafting ("DRAFTING") */
        public: virtual void SetHelpParameters
        (
            bool has_help1 /** Whether the constraint's first associated geometric item has an associated help parameter */,
            bool has_help2 /** Whether the constraint's second associated geometric item has an associated help parameter */,
            double help_parameter1 /** The first help parameter.  Not used unless has_help1 is true. */,
            double help_parameter2 /** The second help parameter.  Not used unless has_help2 is true. */
        );
    };
}
#undef EXPORTLIBRARY
#endif
