#ifndef NXOpen_PREFERENCES_PARTFLEXIBLEPRINTEDCIRCUITDESIGN_HXX_INCLUDED
#define NXOpen_PREFERENCES_PARTFLEXIBLEPRINTEDCIRCUITDESIGN_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     Preferences_PartFlexiblePrintedCircuitDesign.ja
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
#include <NXOpen/DisplayableObject.hxx>
#include <NXOpen/NXColor.hxx>
#include <NXOpen/SheetmetalFeatureProperty.hxx>
#include <NXOpen/TaggedObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace Preferences
    {
        class PartFlexiblePrintedCircuitDesign;
    }
    namespace Preferences
    {
        class PartPreferences;
    }
    class Expression;
    class NXColor;
    namespace Preferences
    {
        /** Represents the Flexible Printed Circuit Design preferences applicable to part  <br> Preferences are in control of the part. They can not be created but can only be changed. <br> */
        class NXOPENCPPEXPORT PartFlexiblePrintedCircuitDesign
        {
            /** The members of the following enumerated type are used to identify
                        object types to the FlatPattern API. These are not the usual
                        NX object types; they are ordinary NX objects that are known to
                        the flat pattern feature for the type of outline they provide to
                        a bend region, joggle region, or lightening hole. */
            public: enum FlatPatternObjectType
            {
                FlatPatternObjectTypeBendCenterLine/** Deprecated */,
                FlatPatternObjectTypeBendUpCenterLine/** bend up center line */ ,
                FlatPatternObjectTypeBendDownCenterLine/** bend down center line */ ,
                FlatPatternObjectTypeBendTangentLine/** bend tangent line */ ,
                FlatPatternObjectTypeOuterMoldLine/** outer mold line */ ,
                FlatPatternObjectTypeInnerMoldLine/** inner mold line */ ,
                FlatPatternObjectTypeExteriorCurves/** exterior curves */ ,
                FlatPatternObjectTypeInteriorCurves/** Deprecated */,
                FlatPatternObjectTypeInteriorCutoutCurves/** interior cutout curves */ ,
                FlatPatternObjectTypeInteriorFeatureCurves/** interior feature curves */ ,
                FlatPatternObjectTypeLighteningHoleCenter/** lightening hole center */ ,
                FlatPatternObjectTypeJoggleLine/** joggle line */ ,
                FlatPatternObjectTypeAddedTopGeometry/** added top geometry */ ,
                FlatPatternObjectTypeAddedBottomGeometry/** added bottom geometry */ 
            };

             /** The members of the following structure are the display data for an
                        object in a flat pattern drawing member view. */
            public:
            struct FlatPatternObjectTypeDisplay
            {
                public: /** Object type */NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternObjectType Type;
                public: /** Enabled status for the object type */int IsEnabled;
                public: /** Object color */NXColor* Color;
                public: /** Object Layer */int Layer;
                public: /** Object font */NXOpen::DisplayableObject::ObjectFont Font;
                public: /** Object width */NXOpen::DisplayableObject::ObjectWidth Width;
                public: FlatPatternObjectTypeDisplay() :
                    Type((NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternObjectType)0),
                    IsEnabled(),
                    Color(),
                    Layer(),
                    Font((NXOpen::DisplayableObject::ObjectFont)0),
                    Width((NXOpen::DisplayableObject::ObjectWidth)0)
                {
                }
                /** Constructor for the FlatPatternObjectTypeDisplay struct. */ 
                public: FlatPatternObjectTypeDisplay(NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternObjectType INIT_type /** Object type */, 
                        int INIT_is_enabled /** Enabled status for the object type */, 
                        NXColor* INIT_color /** Object color */, 
                        int INIT_layer /** Object Layer */, 
                        NXOpen::DisplayableObject::ObjectFont INIT_font /** Object font */, 
                        NXOpen::DisplayableObject::ObjectWidth INIT_width /** Object width */) :
                    Type(INIT_type),
                    IsEnabled(INIT_is_enabled),
                    Color(INIT_color),
                    Layer(INIT_layer),
                    Font(INIT_font),
                    Width(INIT_width)
                {
                }
            };

             /** The members of the following structure are the display data for a
                        callout in a flat pattern drawing member view. */
            public:
            struct FlatPatternCalloutTypeDisplay
            {
                public: /** The name of the callout type.
                                    The string is one returned by the 
                                    get_callout_data method, or can
                                    be hand-coded as the application name 'dot' the callout
                                    name, like this:
                                    "FlatPatternView.BendRadius". Neither name is
                                    case sensitive and blanks are not significant. This type
                                    of hand-coded callout type is usable as long as the
                                    callout type name is unique within the application name. 
                                    Beware of changing the defaults and loading old parts. */NXString Type;
                public: /** Enabled status for the callout type. */int IsEnabled;
                public: /** dialog name for the callout type. */NXString Name;
                public: FlatPatternCalloutTypeDisplay() :
                    Type(),
                    IsEnabled(),
                    Name()
                {
                }
                /** Constructor for the FlatPatternCalloutTypeDisplay struct. */ 
                public: FlatPatternCalloutTypeDisplay(NXString INIT_type /** The name of the callout type.
                                            The string is one returned by the 
                                            get_callout_data method, or can
                                            be hand-coded as the application name 'dot' the callout
                                            name, like this:
                                            "FlatPatternView.BendRadius". Neither name is
                                            case sensitive and blanks are not significant. This type
                                            of hand-coded callout type is usable as long as the
                                            callout type name is unique within the application name. 
                                            Beware of changing the defaults and loading old parts. */, 
                        int INIT_is_enabled /** Enabled status for the callout type. */, 
                        NXString INIT_name /** dialog name for the callout type. */) :
                    Type(INIT_type),
                    IsEnabled(INIT_is_enabled),
                    Name(INIT_name)
                {
                }
            };

            private: NXOpen::Preferences::PartPreferences* m_owner;
            public: explicit PartFlexiblePrintedCircuitDesign(NXOpen::Preferences::PartPreferences *owner): m_owner(owner)
            {
            }
            public: 
            /**Returns the tag of this object.  */
            tag_t Tag() const; 
            /** RETURNS the thickness expression  @return  expression object for sheet thickness  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Expression * GetThickness
            (
            );
            /** THE thickness value string  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetThickness
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                const NXString & thickness /** default thickness value for NX Sheetmetal solids   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** RETURNS the bend radius expression  @return  expression object for radius of bend faces <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Expression * GetBendRadius
            (
            );
            /** The bend radius value  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetBendRadius
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                const NXString & bendRadius /** default bend radius value for bend faces   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** RETURNS the bend relief depth  @return  expression object for depth of bend relief  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Expression * GetBendReliefDepth
            (
            );
            /** THE bend relief depth value  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetBendReliefDepth
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                const NXString & bendReliefDepth /** default depth value for bend relief   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** RETURNS the bend relief width  @return  expression object for width of bend relief  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Expression * GetBendReliefWidth
            (
            );
            /** THE bend relief depth value  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetBendReliefWidth
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                const NXString & bendReliefWidth /** default width value for bend relief   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** RETURNS the neutral factor  @return  expression object for neutral factor of bend areas  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Expression * GetNeutralFactor
            (
            );
            /** THE bend relief depth value  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetNeutralFactor
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                const NXString & neutralFactor /** default neutral factor value for bend relief   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** RETURNS the out corner treatment value for Flat as Solid operations  @return  expression object for out corner treatment value  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Expression * GetOuterCornerTreatmentValue
            (
            );
            /** THE outer corner treatment value for Flat as Solid operations  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetOuterCornerTreatmentValue
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                const NXString & outerCornerTreatment /** default value for out corner treatment   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** RETURNS the outer corner treatment type in Flat as Solid operation  @return  outer corner treatment type  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Features::SheetMetal::FeatureProperty GetOuterCornerTreatmentType
            (
            );
            /** SETS the outer corner treatment type in Flat as Solid operation  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetOuterCornerTreatmentType
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                NXOpen::Features::SheetMetal::FeatureProperty outerCornerTreatmentType /** outer corner treatment type */
            );
            /** RETURNS the inner corner treatment value for Flat as Solid operations  @return  expression object for inner corner treatment value  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Expression * GetInnerCornerTreatmentValue
            (
            );
            /** SETS the inner corner treatment value for Flat as Solid operations  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetInnerCornerTreatmentValue
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                const NXString & innerCornerTreatment /** default value for inner corner treatment   <br>  NOTE: The full Unicode character set is not supported for this parameter.  <br> */
            );
            /** RETURNS the inner corner treatment type in Flat as Solid operation  @return  outer corner treatment type  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Features::SheetMetal::FeatureProperty GetInnerCornerTreatmentType
            (
            );
            /** SETS the inner corner treatment type in Flat as Solid operation  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetInnerCornerTreatmentType
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                NXOpen::Features::SheetMetal::FeatureProperty innerCornerTreatmentType /** outer corner treatment type */
            );
            /** RETURNS the flag indicating whether B-Splines are simplified as part of the Flat Solid creation @return  flag   <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: bool GetIsBsplineSimplifiedInFlatSolid
            (
            );
            /** SETS the flag indicating whether or not B-Splines are simplified as part of the Flat Solid creation <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetIsBsplineSimplifiedInFlatSolid
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                bool isBsplineSimplifiedInFlatSolid /** flag  */
            );
            /** RETURNS the flag indicating whether or not system generated bend releifs are removed as part of the Flat Solid creation @return  flag   <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: bool GetIsSystemGeneratedBendReliefRemovedInFlatSolid
            (
            );
            /** SETS the flag indicating whether or not system generated bend releifs are removed as part of the Flat Solid creation <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetIsSystemGeneratedBendReliefRemovedInFlatSolid
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                bool isSystemGeneratedBendReliefRemoved /** flag  */
            );
            /** RETURNS the minimum arc tolerance during Flat Solid simplification  @return  flag   <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: double GetMinimumArcToleranceInFlatSolid
            (
            );
            /** SETS the minimum arc tolerance during Flat Solid simplification  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetMinimumArcToleranceInFlatSolid
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                double minimumArcToleranceInFlatSolid /** flag  */
            );
            /** RETURNS the deviational tolerance during Flat Solid simplification  @return  flag   <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: double GetDeviationalToleranceInFlatSolid
            (
            );
            /** SETS the deviational tolerance during Flat Solid simplification  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetDeviationalToleranceInFlatSolid
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                double deviationalToleranceInFlatSolid /** flag  */
            );
            /** RETURNS the material names defined in the material standards table  @return   <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: std::vector<NXString> GetMaterialNames
            (
            );
            /** RETURNS the material name saved with the part  @return  The name of the material saved with the part <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXString GetMaterial
            (
            );
            /** RETURNS the material name saved with the part  @return  property Values  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: std::vector<NXString> GetMaterialProperties
            (
                const NXString & materialName /** material Name*/,
                std::vector<NXString> & propertyNames /** properties */
            );
            /** The material standard  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetMaterial
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately*/,
                const NXString & standardName /** The name of a material from the material standards file */
            );
            /** Returns the display data for a flat pattern object type.   @return  The display data for the flat pattern object type.  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternObjectTypeDisplay GetFlatPatternObjectTypeDisplay
            (
                NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternObjectType objectType /** The object type for which to return the display data. */
            );
            /** Sets the display data for a flat pattern object type.  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetFlatPatternObjectTypeDisplay
            (
                bool updateModel /** Specifies whether the solid model be recomputed immediately.*/,
                NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternObjectType objectType /** The object type for which to get the display data. */,
                const NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternObjectTypeDisplay & displayData /** The display data for the flat pattern object type. */
            );
            /** Returns the display data for a callout type. The name member of the
                        @link Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternCalloutTypeDisplay Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternCalloutTypeDisplay@endlink 
                        is separately allocated from the callout_type argument string.
                        In some cases the new string will contain an
                        extended form of the callout_type passed in, and that form should
                        be used for subsequent JA calls, without modification.  @return  The display data for the callout type.  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternCalloutTypeDisplay GetFlatPatternCalloutTypeDisplay
            (
                const NXString & calloutType /** The name of the callout type for which to get the display data. */
            );
            /** Sets the display data for a callout type.  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void SetFlatPatternCalloutTypeDisplay
            (
                const NXString & calloutType /** The name of the callout type for which to set the display data. */,
                const NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternCalloutTypeDisplay & displayData /** The display data for the callout type. */
            );
            /** Returns the types, colors, fonts, widths, and enabled status for all the
                        the available object types.  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void GetFlatPatternAllObjectTypeDisplay
            (
                std::vector<NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternObjectTypeDisplay> & displayData /** Array of structures with the object type display data. */
            );
            /** Returns the dialog names, identifiers, and enabled status for all the
                        available callout types.  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void GetFlatPatternAllCalloutTypeDisplay
            (
                std::vector<NXOpen::Preferences::PartFlexiblePrintedCircuitDesign::FlatPatternCalloutTypeDisplay> & displayData /** Array of structures with the callout type display data. */
            );
            /** Commits and applies all the settings done with set_callout_type_display
                        and set_object_type_display. It must be called after a sequence of calls
                        to those methods to cause the view to update.  <br> License requirements : nx_flexible_pcb ("NX Flexible PCB") */
            public: void Commit
            (
            );
            public: virtual void initialize();
        };
    }
}
#undef EXPORTLIBRARY
#endif
