#ifndef NXOpen_PREFERENCES_ANNOTATIONPREFERENCES_HXX_INCLUDED
#define NXOpen_PREFERENCES_ANNOTATIONPREFERENCES_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_AnnotationPreferences.ja
//
//  Generated by:
//     apiwrap
//
//  WARNING:
//    This file is automatically generated - do not edit by hand
//
#include <vector>
#include <NXOpen/NXString.hxx>
#include <NXOpen/Annotations_AngularTolerance.hxx>
#include <NXOpen/Annotations_DimensionPreferences.hxx>
#include <NXOpen/Annotations_LetteringPreferences.hxx>
#include <NXOpen/Annotations_LineAndArrowPreferences.hxx>
#include <NXOpen/Annotations_LinearTolerance.hxx>
#include <NXOpen/Annotations_PmiPreferences.hxx>
#include <NXOpen/Annotations_SymbolPreferences.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class AnnotationPreferences;
    }
    namespace Annotations
    {
        class AnnotationManager;
    }
    namespace Annotations
    {
        class AngularTolerance;
    }
    namespace Annotations
    {
        class DimensionPreferences;
    }
    namespace Annotations
    {
        class LetteringPreferences;
    }
    namespace Annotations
    {
        class LineAndArrowPreferences;
    }
    namespace Annotations
    {
        class LinearTolerance;
    }
    namespace Annotations
    {
        class PmiPreferences;
    }
    namespace Annotations
    {
        class SymbolPreferences;
    }
    namespace Preferences
    {
        /** Represents the global preferences for annotations  <br> To obtain an instance of this class, refer to @link AnnotationManager AnnotationManager@endlink  <br> */
        class NXOPENCPPEXPORT AnnotationPreferences
        {
            private: NXOpen::Annotations::AnnotationManager* m_owner;
            public: explicit AnnotationPreferences(NXOpen::Annotations::AnnotationManager *owner): m_owner(owner)
            {
            }
            public: tag_t Tag() const;
            /** Returns the global lettering preferences for the part  @return   <br> License requirements : None */
            public: NXOpen::Annotations::LetteringPreferences * GetLetteringPreferences
            (
            );
            /** Returns the global line and arrow preferences for the part  @return   <br> License requirements : None */
            public: NXOpen::Annotations::LineAndArrowPreferences * GetLineAndArrowPreferences
            (
            );
            /** Returns the global symbol preferences for the part  @return   <br> License requirements : None */
            public: NXOpen::Annotations::SymbolPreferences * GetSymbolPreferences
            (
            );
            /** Returns the global dimension preferences for the part  @return   <br> License requirements : None */
            public: NXOpen::Annotations::DimensionPreferences * GetDimensionPreferences
            (
            );
            /** Returns the global angular tolerances for the part  @return   <br> License requirements : None */
            public: NXOpen::Annotations::AngularTolerance * GetAngularTolerances
            (
            );
            /** Returns the global linear tolerances for the part  @return   <br> License requirements : None */
            public: NXOpen::Annotations::LinearTolerance * GetLinearTolerances
            (
            );
            /** Returns the global PMI preferences for the part  @return   <br> License requirements : None */
            public: NXOpen::Annotations::PmiPreferences * GetPmiPreferences
            (
            );
            /** Sets the global lettering preferences for the part  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLetteringPreferences
            (
                NXOpen::Annotations::LetteringPreferences * lettering_prefs /** */
            );
            /** Sets the global line and arrow preferences for the part  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLineAndArrowPreferences
            (
                NXOpen::Annotations::LineAndArrowPreferences * prefs /** */
            );
            /** Sets the global symbol preferences for the part  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSymbolPreferences
            (
                NXOpen::Annotations::SymbolPreferences * prefs /** */
            );
            /** Sets the global dimension preferences for the part  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDimensionPreferences
            (
                NXOpen::Annotations::DimensionPreferences * prefs /** */
            );
            /** Sets the global angular tolerances for the part  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetAngularTolerances
            (
                NXOpen::Annotations::AngularTolerance * prefs /** */
            );
            /** Sets the global linear tolerances for the part  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetLinearTolerances
            (
                NXOpen::Annotations::LinearTolerance * prefs /** */
            );
            /** Sets the global PMI preferences for the part  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetPmiPreferences
            (
                NXOpen::Annotations::PmiPreferences * pmi_prefs /** */
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
