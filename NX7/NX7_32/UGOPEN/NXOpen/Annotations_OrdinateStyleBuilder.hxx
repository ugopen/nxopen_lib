#ifndef NXOpen_ANNOTATIONS_ORDINATESTYLEBUILDER_HXX_INCLUDED
#define NXOpen_ANNOTATIONS_ORDINATESTYLEBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Annotations_OrdinateStyleBuilder.ja
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
#include <NXOpen/Annotations_OrdinateStyleBuilder.hxx>
#include <NXOpen/Dimensions.hxx>
#include <NXOpen/GeometricUtilities_IComponentBuilder.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Annotations
    {
        class OrdinateStyleBuilder;
    }
    namespace GeometricUtilities
    {
        class IComponentBuilder;
    }
    namespace Annotations
    {
        class _OrdinateStyleBuilderBuilder;
        /**
            Represents a @link Annotations::OrdinateStyleBuilder Annotations::OrdinateStyleBuilder@endlink .
            This class queries and sets ordinate specific preferences when
            creating or editing an ordinate set or ordinate dimension.
            */
        class NXOPENCPPEXPORT OrdinateStyleBuilder : public TaggedObject, public virtual GeometricUtilities::IComponentBuilder
        {
            private: friend class  _OrdinateStyleBuilderBuilder;
            protected: OrdinateStyleBuilder();
            /**Returns  the positive direction of measurement for an ordinate set  <br> License requirements : None */
            public: NXOpen::Annotations::OrdinatePositiveDirection PositiveDirection
            (
            );
            /**Sets  the positive direction of measurement for an ordinate set  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetPositiveDirection
            (
                NXOpen::Annotations::OrdinatePositiveDirection positiveDirection /** positivedirection */ 
            );
            /**Returns  the name display style for an ordinate set  <br> License requirements : None */
            public: NXOpen::Annotations::OrdinateOriginDisplayOption DisplayNameStyle
            (
            );
            /**Sets  the name display style for an ordinate set  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDisplayNameStyle
            (
                NXOpen::Annotations::OrdinateOriginDisplayOption displayNameStyle /** displaynamestyle */ 
            );
            /**Returns  the display dimension line preference for an ordinate set  <br> License requirements : None */
            public: NXOpen::Annotations::OrdinateLineArrowDisplayOption DisplayDimensionLine
            (
            );
            /**Sets  the display dimension line preference for an ordinate set  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDisplayDimensionLine
            (
                NXOpen::Annotations::OrdinateLineArrowDisplayOption displayDimensionLine /** displaydimensionline */ 
            );
            /**Returns  the ordinate origin user defined text  <br> License requirements : None */
            public: NXString UserDefinedText
            (
            );
            /**Sets  the ordinate origin user defined text  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetUserDefinedText
            (
                const NXString & userDefinedText /** userdefinedtext */ 
            );
            /**Returns  the align symbol with baseline preference  <br> License requirements : None */
            public: bool AlignSymbolWithBaseline
            (
            );
            /**Sets  the align symbol with baseline preference  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetAlignSymbolWithBaseline
            (
                bool alignSymbolWithBaseline /** alignsymbolwithbaseline */ 
            );
            /**Returns  the symbol angle in degress with respect to the baseline.
                    This option only applies if the name display style is User-Defined and the
                    the value of the Align Symbol with Baseline preference is false  <br> License requirements : None */
            public: double SymbolAngle
            (
            );
            /**Sets  the symbol angle in degress with respect to the baseline.
                    This option only applies if the name display style is User-Defined and the
                    the value of the Align Symbol with Baseline preference is false  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSymbolAngle
            (
                double symbolAngle /** symbolangle */ 
            );
            /**Returns  the symbol scale  <br> License requirements : None */
            public: double SymbolScale
            (
            );
            /**Sets  the symbol scale  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSymbolScale
            (
                double symbolScale /** symbolscale */ 
            );
            /**Returns  the symbol aspect ratio  <br> License requirements : None */
            public: double SymbolAspectRatio
            (
            );
            /**Sets  the symbol aspect ratio  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSymbolAspectRatio
            (
                double symbolAspectRatio /** symbolaspectratio */ 
            );
            /**Returns  the symbol length  <br> License requirements : None */
            public: double SymbolLength
            (
            );
            /**Sets  the symbol length  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSymbolLength
            (
                double symbolLength /** symbollength */ 
            );
            /**Returns  the symbol height  <br> License requirements : None */
            public: double SymbolHeight
            (
            );
            /**Sets  the symbol height  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetSymbolHeight
            (
                double symbolHeight /** symbolheight */ 
            );
            /**Returns  the dogleg setting.
                        This specifies which options are used to specify the dogleg  <br> License requirements : None */
            public: NXOpen::Annotations::OrdinateDoglegDefinition DoglegSetting
            (
            );
            /**Sets  the dogleg setting.
                        This specifies which options are used to specify the dogleg  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDoglegSetting
            (
                NXOpen::Annotations::OrdinateDoglegDefinition doglegSetting /** doglegsetting */ 
            );
            /**Returns  the dogleg angle. 
                        The valid range is greater than zero and less than or equal to 90 degrees  <br> License requirements : None */
            public: double DoglegAngle
            (
            );
            /**Sets  the dogleg angle. 
                        The valid range is greater than zero and less than or equal to 90 degrees  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDoglegAngle
            (
                double doglegAngle /** doglegangle */ 
            );
            /**Returns  the dogleg start offset. 
                        This is the offset between the dimension line and the start position of the dogleg.
                        The value must be greater than or equal to zero  <br> License requirements : None */
            public: double DoglegStartOffset
            (
            );
            /**Sets  the dogleg start offset. 
                        This is the offset between the dimension line and the start position of the dogleg.
                        The value must be greater than or equal to zero  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDoglegStartOffset
            (
                double doglegStartOffset /** doglegstartoffset */ 
            );
            /**Returns  the dogleg end offset.
                        This is the offset between the dimension line and the end position of the dogleg.
                        This value must be greater than or equal to zero and less than or equal to the
                        start offset  <br> License requirements : None */
            public: double DoglegEndOffset
            (
            );
            /**Sets  the dogleg end offset.
                        This is the offset between the dimension line and the end position of the dogleg.
                        This value must be greater than or equal to zero and less than or equal to the
                        start offset  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDoglegEndOffset
            (
                double doglegEndOffset /** doglegendoffset */ 
            );
            /**Returns  the dogleg creation option  <br> License requirements : None */
            public: NXOpen::Annotations::OrdinateDoglegCreationOption DoglegCreationOption
            (
            );
            /**Sets  the dogleg creation option  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetDoglegCreationOption
            (
                NXOpen::Annotations::OrdinateDoglegCreationOption doglegCreationOption /** doglegcreationoption */ 
            );
            /**Returns  the distance from the baseline to the first margin.
                        This can be a positive or negative number. 
                        The positive direction is away from the view's center  <br> License requirements : None */
            public: double MarginFirstOffset
            (
            );
            /**Sets  the distance from the baseline to the first margin.
                        This can be a positive or negative number. 
                        The positive direction is away from the view's center  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetMarginFirstOffset
            (
                double marginFirstOffset /** marginfirstoffset */ 
            );
            /**Returns  the interval distance between successive margins  <br> License requirements : None */
            public: double MarginSpacing
            (
            );
            /**Sets  the interval distance between successive margins  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetMarginSpacing
            (
                double marginSpacing /** marginspacing */ 
            );
            /**Returns  the number of margins to create.
                        The maximum is 32  <br> License requirements : None */
            public: int NumberOfMargins
            (
            );
            /**Sets  the number of margins to create.
                        The maximum is 32  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetNumberOfMargins
            (
                int numberOfMargins /** numberofmargins */ 
            );
            /**Returns  the ordinate text orientation  <br> License requirements : None */
            public: NXOpen::Annotations::TextOrientation OrdinateTextOrientation
            (
            );
            /**Sets  the ordinate text orientation  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetOrdinateTextOrientation
            (
                NXOpen::Annotations::TextOrientation ordinateTextOrientation /** ordinatetextorientation */ 
            );
            /**Returns  the ordinate text angle  <br> License requirements : None */
            public: double OrdinateTextAngle
            (
            );
            /**Sets  the ordinate text angle  <br> License requirements : geometric_tol ("GDT") OR drafting ("DRAFTING") */
            public: void SetOrdinateTextAngle
            (
                double ordinateTextAngle /** ordinatetextangle */ 
            );
            /** Returns true if the inputs to the component are sufficient for 
                        commit to be called.  For example, if the component requires
                        you to set some property, this method will return false if
                        you haven't set it.  This method throws a not-yet-implemented
                        NXException for some components.
                     @return  Was self validation successful  <br> License requirements : solid_modeling ("SOLIDS MODELING") */
            public: virtual bool Validate
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif
