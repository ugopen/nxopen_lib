#ifndef NXOpen_ANNOTATIONS_SYMBOLSTYLEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_SYMBOLSTYLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_SymbolStyleBuilder.ja
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
#include <NXOpen/Annotations.hxx>
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/LineWelds.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_annotations_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace Annotations
    {
        class SymbolStyleBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    class NXColor;
    namespace Annotations
    {
        class _SymbolStyleBuilderBuilder;
        class SymbolStyleBuilderImpl;
        /**
            Represents a @link NXOpen::Annotations::SymbolStyleBuilder NXOpen::Annotations::SymbolStyleBuilder@endlink .
            This class queries and sets preferences for various symbol type annotations when creating or editing.
            
         <br>  Created in NX6.0.0.  <br>  
        */
        class NXOPENCPP_ANNOTATIONSEXPORT  SymbolStyleBuilder : public NXOpen::TaggedObject, public virtual NXOpen::GeometricUtilities::IComponentBuilder
        {
            /** Represents the option to underline the additional FCF text */
            public: enum FcfTextUnderlineOption
            {
                FcfTextUnderlineOptionNone/** none */ ,
                FcfTextUnderlineOptionTop/** top */ ,
                FcfTextUnderlineOptionAll/** all */ 
            };

            private: SymbolStyleBuilderImpl * m_symbolstylebuilder_impl;
            private: friend class  _SymbolStyleBuilderBuilder;
            protected: SymbolStyleBuilder();
            public: ~SymbolStyleBuilder();
            /**Returns  the balloon type 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::BalloonTypes BalloonType
            (
            );
            /**Sets  the balloon type 
             <br>  Created in NX12.0.2.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetBalloonType
            (
                NXOpen::Annotations::BalloonTypes type /** type */ 
            );
            /**Returns  the ID symbol size 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double IdSymbolSize
            (
            );
            /**Sets  the ID symbol size 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetIdSymbolSize
            (
                double idSymbolSize /** idsymbolsize */ 
            );
            /**Returns  the ID symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * IdSymbolColor
            (
            );
            /**Sets  the ID symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetIdSymbolColor
            (
                NXOpen::NXColor * idSymbolColor /** idsymbolcolor */ 
            );
            /**Returns  the ID symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectFont IdSymbolFont
            (
            );
            /**Sets  the ID symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetIdSymbolFont
            (
                NXOpen::DisplayableObject::ObjectFont idSymbolFont /** idsymbolfont */ 
            );
            /**Returns  the ID symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth IdSymbolWidth
            (
            );
            /**Sets  the ID symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetIdSymbolWidth
            (
                NXOpen::Annotations::LineWidth idSymbolWidth /** idsymbolwidth */ 
            );
            /**Returns  the user defined symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * UserDefinedSymbolColor
            (
            );
            /**Sets  the user defined symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetUserDefinedSymbolColor
            (
                NXOpen::NXColor * userDefinedSymbolColor /** userdefinedsymbolcolor */ 
            );
            /**Returns  the user defined symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectFont UserDefinedSymbolFont
            (
            );
            /**Sets  the user defined symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetUserDefinedSymbolFont
            (
                NXOpen::DisplayableObject::ObjectFont userDefinedSymbolFont /** userdefinedsymbolfont */ 
            );
            /**Returns  the user defined symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth UserDefinedSymbolWidth
            (
            );
            /**Sets  the user defined symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetUserDefinedSymbolWidth
            (
                NXOpen::Annotations::LineWidth userDefinedSymbolWidth /** userdefinedsymbolwidth */ 
            );
            /**Returns  the centerline symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * CenterlineSymbolColor
            (
            );
            /**Sets  the centerline symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetCenterlineSymbolColor
            (
                NXOpen::NXColor * centerlineSymbolColor /** centerlinesymbolcolor */ 
            );
            /**Returns  the centerline symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth CenterlineSymbolWidth
            (
            );
            /**Sets  the centerline symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetCenterlineSymbolWidth
            (
                NXOpen::Annotations::LineWidth centerlineSymbolWidth /** centerlinesymbolwidth */ 
            );
            /**Returns  the intersection symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * IntersectionSymbolColor
            (
            );
            /**Sets  the intersection symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetIntersectionSymbolColor
            (
                NXOpen::NXColor * intersectionSymbolColor /** intersectionsymbolcolor */ 
            );
            /**Returns  the intersection symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectFont IntersectionSymbolFont
            (
            );
            /**Sets  the intersection symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetIntersectionSymbolFont
            (
                NXOpen::DisplayableObject::ObjectFont intersectionSymbolFont /** intersectionsymbolfont */ 
            );
            /**Returns  the intersection symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth IntersectionSymbolWidth
            (
            );
            /**Sets  the intersection symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetIntersectionSymbolWidth
            (
                NXOpen::Annotations::LineWidth intersectionSymbolWidth /** intersectionsymbolwidth */ 
            );
            /**Returns  the target symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * TargetSymbolColor
            (
            );
            /**Sets  the target symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetTargetSymbolColor
            (
                NXOpen::NXColor * targetSymbolColor /** targetsymbolcolor */ 
            );
            /**Returns  the target symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectFont TargetSymbolFont
            (
            );
            /**Sets  the target symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetTargetSymbolFont
            (
                NXOpen::DisplayableObject::ObjectFont targetSymbolFont /** targetsymbolfont */ 
            );
            /**Returns  the target symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth TargetSymbolWidth
            (
            );
            /**Sets  the target symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetTargetSymbolWidth
            (
                NXOpen::Annotations::LineWidth targetSymbolWidth /** targetsymbolwidth */ 
            );
            /**Returns  the GD and T symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * GdtSymbolColor
            (
            );
            /**Sets  the GD and T symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetGdtSymbolColor
            (
                NXOpen::NXColor * gdtSymbolColor /** gdtsymbolcolor */ 
            );
            /**Returns  the GD and T symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectFont GdtSymbolFont
            (
            );
            /**Sets  the GD and T symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetGdtSymbolFont
            (
                NXOpen::DisplayableObject::ObjectFont gdtSymbolFont /** gdtsymbolfont */ 
            );
            /**Returns  the GD and T symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth GdtSymbolWidth
            (
            );
            /**Sets  the GD and T symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetGdtSymbolWidth
            (
                NXOpen::Annotations::LineWidth gdtSymbolWidth /** gdtsymbolwidth */ 
            );
            /**Returns  the Weld symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * WeldSymbolColor
            (
            );
            /**Sets  the Weld symbol color 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetWeldSymbolColor
            (
                NXOpen::NXColor * weldSymbolColor /** weldsymbolcolor */ 
            );
            /**Returns  the Weld symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectFont WeldSymbolFont
            (
            );
            /**Sets  the Weld symbol font 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetWeldSymbolFont
            (
                NXOpen::DisplayableObject::ObjectFont weldSymbolFont /** weldsymbolfont */ 
            );
            /**Returns  the Weld symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth WeldSymbolWidth
            (
            );
            /**Sets  the Weld symbol width 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetWeldSymbolWidth
            (
                NXOpen::Annotations::LineWidth weldSymbolWidth /** weldsymbolwidth */ 
            );
            /**Returns  the gap between the weld line and weld type symbol 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : None */
            public: double WeldLineGap
            (
            );
            /**Sets  the gap between the weld line and weld type symbol 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetWeldLineGap
            (
                double gap /** gap */ 
            );
            /**Returns  the surface finish symbol color 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::NXColor * SurfaceFinishColor
            (
            );
            /**Sets  the surface finish symbol color 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSurfaceFinishColor
            (
                NXOpen::NXColor * surfaceFinishColor /** surfacefinishcolor */ 
            );
            /**Returns  the surface finish symbol font 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::DisplayableObject::ObjectFont SurfaceFinishFont
            (
            );
            /**Sets  the surface finish symbol font 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSurfaceFinishFont
            (
                NXOpen::DisplayableObject::ObjectFont surfaceFinishFont /** surfacefinishfont */ 
            );
            /**Returns  the surface finish symbol width 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::LineWidth SurfaceFinishWidth
            (
            );
            /**Sets  the surface finish symbol width 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSurfaceFinishWidth
            (
                NXOpen::Annotations::LineWidth surfaceFinishWidth /** surfacefinishwidth */ 
            );
            /**Returns  the standard 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SurfaceFinishStandard DraftingSurfaceFinishStandard
            (
            );
            /**Sets  the standard 
             <br>  Created in NX7.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDraftingSurfaceFinishStandard
            (
                NXOpen::Annotations::SurfaceFinishStandard standard /** standard */ 
            );
            /**Returns  the weld space factor 
             <br>  Created in NX7.0.0.  <br>  
             <br> License requirements : None */
            public: double WeldSpaceFactor
            (
            );
            /**Sets  the weld space factor 
             <br>  Created in NX6.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetWeldSpaceFactor
            (
                double factor /** factor */ 
            );
            /**Returns  the character size factor that controls the weld symbol size. The value is greater than zero. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: double WeldSymbolSizeFactor
            (
            );
            /**Sets  the character size factor that controls the weld symbol size. The value is greater than zero. 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetWeldSymbolSizeFactor
            (
                double factor /** factor */ 
            );
            /**Returns  the weld symbol standard 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::WeldStandard WeldSymbolStandard
            (
            );
            /**Sets  the weld symbol standard 
             <br>  Created in NX8.5.0.  <br>  
             <br> License requirements : None */
            public: void SetWeldSymbolStandard
            (
                NXOpen::Annotations::WeldStandard standard /** standard */ 
            );
            /**Returns  the option to underline the additional FCF text 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Annotations::SymbolStyleBuilder::FcfTextUnderlineOption FcfAdditionalTextUnderline
            (
            );
            /**Sets  the option to underline the additional FCF text 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetFcfAdditionalTextUnderline
            (
                NXOpen::Annotations::SymbolStyleBuilder::FcfTextUnderlineOption underlineTextOption /** underlinetextoption */ 
            );
            /**Returns  the id symbol attachment method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: bool AttachToIdSymbolVertex
            (
            );
            /**Sets  the id symbol attachment method 
             <br>  Created in NX10.0.0.  <br>  
             <br> License requirements : None */
            public: void SetAttachToIdSymbolVertex
            (
                bool attachToIdSymbolVertex /** attachtoidsymbolvertex */ 
            );
            /**Returns  the string value which specifies the initial letter or letter sequence to
                        use for a datum label Staring Letter. Up to five letters may be specified. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXString DatumLabelStartingLetter
            (
            );
            /**Sets  the string value which specifies the initial letter or letter sequence to
                        use for a datum label Staring Letter. Up to five letters may be specified. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDatumLabelStartingLetter
            (
                const NXString & startingLetter /** startingletter */ 
            );
            /**Sets  the string value which specifies the initial letter or letter sequence to
                        use for a datum label Staring Letter. Up to five letters may be specified. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            void SetDatumLabelStartingLetter
            (
                const char * startingLetter /** startingletter */ 
            );
            /** Validate whether the inputs to the component are sufficient for 
                        commit to be called.  If the component is not in a state to commit
                        then an exception is thrown.  For example, if the component requires
                        you to set some property, this method will throw an exception if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful 
             <br>  Created in NX3.0.1.  <br>  
             <br> License requirements : None */
            public: virtual bool Validate
            (
            );
        };
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