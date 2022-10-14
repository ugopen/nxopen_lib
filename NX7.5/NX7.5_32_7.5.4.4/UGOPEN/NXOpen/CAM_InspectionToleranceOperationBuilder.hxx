#ifndef NXOpen_CAM_INSPECTIONTOLERANCEOPERATIONBUILDER_HXX_INCLUDED
#define NXOpen_CAM_INSPECTIONTOLERANCEOPERATIONBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAM_InspectionToleranceOperationBuilder.ja
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
#include <NXOpen/CAM_InspectionToleranceOperationBuilder.hxx>
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/SelectObject.hxx>
#include <NXOpen/libnxopencpp_exports.hxx>
namespace NXOpen
{
    namespace CAM
    {
        class InspectionToleranceOperationBuilder;
    }
    namespace CAM
    {
        class OperationBuilder;
    }
    class Direction;
    class SelectNXObject;
    namespace CAM
    {
        class _InspectionToleranceOperationBuilderBuilder;
        class InspectionToleranceOperationBuilderImpl;
        /** this class creates the tolerance operation  <br> To create a new instance of this class, use @link CAM::InspectionOperationCollection::CreateInspectionToleranceOperationBuilder CAM::InspectionOperationCollection::CreateInspectionToleranceOperationBuilder@endlink  <br> */
        class NXOPENCPPEXPORT  InspectionToleranceOperationBuilder : public CAM::OperationBuilder
        {
            /** Tolerance types */
            public: enum TolType
            {
                TolTypeDistanceBetween/** Distance Between */,
                TolTypeAngleBetween/** Angle Between */,
                TolTypeCoordinateTolerance/** Coordinate */,
                TolTypeDiameter/** Diameter */,
                TolTypeRadius/** Radius */,
                TolTypeWidth/** Width */,
                TolTypeConeAngle/** Angle of Cone */,
                TolTypeDatumDefinition/** Datum Definition */,
                TolTypeFlatness/** Flatness */,
                TolTypeStraightness/** Straightness */,
                TolTypeCircularity/** Circularity */,
                TolTypeCylindricity/** Cylindricity */,
                TolTypeLineProfile/** Profile of Line */,
                TolTypeSurfaceProfile/** Profile of Surface */,
                TolTypeAngularity/** Angularity */,
                TolTypeParallelism/** Parallelism */,
                TolTypePerpendicularity/** Perpendicularity */,
                TolTypePosition/** Position */,
                TolTypeConcentricity/** Concentricity */,
                TolTypeSymmetry/** Symmetry */,
                TolTypeCircularRunout/** Circular Runout */,
                TolTypeTotalRunout/** Total Runout */,
                TolTypeDatumTarget/** datum target */ 
            };

            /** X/Y/Z axis */
            public: enum ParamXYZAxis
            {
                ParamXYZAxisXAxis/** X Axis */,
                ParamXYZAxisYAxis/** Y Axis */,
                ParamXYZAxisZAxis/** Z Axis */,
                ParamXYZAxisMajorAxis/** Major Axis */,
                ParamXYZAxisMinorAxis/** Minor Axis */
            };

            /** Subtypes */
            public: enum ParamSubType
            {
                ParamSubTypeSurface/** Surface */,
                ParamSubTypeAxis/** Axis */
            };

            /** Extent */
            public: enum ParamExtent
            {
                ParamExtentTotal/** Total */,
                ParamExtentUnitAreaLength/** Unit Area Length */
            };

            /** Tolerance zone shape */
            public: enum ParamTolZoneShape
            {
                ParamTolZoneShapeNone/** None */,
                ParamTolZoneShapeCylindrical/** Cylindrical */,
                ParamTolZoneShapeCircular/** Circular */,
                ParamTolZoneShapeSpherical/** Spherical */,
                ParamTolZoneShapeRadial/** Radial */,
                ParamTolZoneShapeAngular/** Angular */
            };

            /** Material Condition modifiers */
            public: enum ParamTolMatModifier
            {
                ParamTolMatModifierNone/** None */,
                ParamTolMatModifierMmc/** Maximum Material Condition */,
                ParamTolMatModifierLmc/** Least Material Condition */,
                ParamTolMatModifierRfs/** Regardless of Feature Size */
            };

            /** Material Condition modifiers */
            public: enum ParamTolMatModifierDup
            {
                ParamTolMatModifierDupNone/** None */,
                ParamTolMatModifierDupMmc/** Maximum Material Condition */,
                ParamTolMatModifierDupLmc/** Least Material Condition */,
                ParamTolMatModifierDupRfs/** Regardless of Feature Size */
            };

            /** Default datum symbols */
            public: enum ParamPriDatum
            {
                ParamPriDatumA/** A */,
                ParamPriDatumB/** B */,
                ParamPriDatumC/** C */
            };

            /** Primary datum material modifiers */
            public: enum ParamPriDatumModifier
            {
                ParamPriDatumModifierNone/** None */,
                ParamPriDatumModifierMmc/** Maximum Material Condition */,
                ParamPriDatumModifierLmc/** Least Material Condition */,
                ParamPriDatumModifierRfs/** Regardless of Feature Size */
            };

            /** Default datum symbols */
            public: enum ParamSecDatum
            {
                ParamSecDatumA/** A */,
                ParamSecDatumB/** B */,
                ParamSecDatumC/** C */
            };

            /** Secondary datum material modifiers */
            public: enum ParamSecDatumModifier
            {
                ParamSecDatumModifierNone/** None */,
                ParamSecDatumModifierMmc/** Maximum Material Condition */,
                ParamSecDatumModifierLmc/** Least Material Condition */,
                ParamSecDatumModifierRfs/** Regardless of Feature Size */
            };

            /** Default datum symbols */
            public: enum ParamTerDatum
            {
                ParamTerDatumA/** A */,
                ParamTerDatumB/** B */,
                ParamTerDatumC/** C */
            };

            /** Tertiary datum material modifiers */
            public: enum ParamTerDatumModifier
            {
                ParamTerDatumModifierNone/** None */,
                ParamTerDatumModifierMmc/** Maximum Material Condition */,
                ParamTerDatumModifierLmc/** Least Material Condition */,
                ParamTerDatumModifierRfs/** Regardless of Feature Size */
            };

            /** PCS or absolute coordinate sysytem */
            public: enum SirVecPCSABS
            {
                SirVecPCSABSRelativetoPCS/** Relative to PCS */,
                SirVecPCSABSAbsolute/** Absolute */
            };

            /** Angle format */
            public: enum AngleFormat
            {
                AngleFormatDecimalDegree/** Decimal Degrees */,
                AngleFormatDegMinSec/** Degrees/Minutes/Seconds */
            };

            private: InspectionToleranceOperationBuilderImpl * m_inspectiontoleranceoperationbuilder_impl;
            private: friend class  _InspectionToleranceOperationBuilderBuilder;
            protected: InspectionToleranceOperationBuilder();
            public: ~InspectionToleranceOperationBuilder();
            /**Returns  the tolerance type  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::TolType TolOpType
            (
            );
            /**Sets  the tolerance type  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetTolOpType
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::TolType tolOpType /** toloptype */ 
            );
            /**Returns  the is composite flag  <br> License requirements : None */
            public: bool IsComposite
            (
            );
            /**Sets  the is composite flag  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetComposite
            (
                bool isComposite /** iscomposite */ 
            );
            /**Returns  the PMI selection  <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectionPMI
            (
            );
            /**Returns  the string datum letter  <br> License requirements : None */
            public: NXString StringDatumLetter
            (
            );
            /**Sets  the string datum letter  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringDatumLetter
            (
                const NXString & stringDatumLetter /** stringdatumletter */ 
            );
            /**Returns  the enum parameter xyzaxis  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamXYZAxis EnumParamXYZAxis
            (
            );
            /**Sets  the enum parameter xyzaxis  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamXYZAxis
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamXYZAxis enumParamXYZAxis /** enumparamxyzaxis */ 
            );
            /**Returns  the enum torus characteristic  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamXYZAxis EnumTorusCharacteristic
            (
            );
            /**Sets  the enum torus characteristic  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumTorusCharacteristic
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamXYZAxis enumTorusCharacteristic /** enumtoruscharacteristic */ 
            );
            /**Returns  the nominal tolerance  <br> License requirements : None */
            public: double DoubleNominal
            (
            );
            /**Sets  the nominal tolerance  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleNominal
            (
                double doubleNominal /** doublenominal */ 
            );
            /**Returns  the upper tolerance  <br> License requirements : None */
            public: double DoubleUpper
            (
            );
            /**Sets  the upper tolerance  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleUpper
            (
                double doubleUpper /** doubleupper */ 
            );
            /**Returns  the lower tolerance  <br> License requirements : None */
            public: double DoubleLower
            (
            );
            /**Sets  the lower tolerance  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleLower
            (
                double doubleLower /** doublelower */ 
            );
            /**Returns  the enum parameter sub type  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamSubType EnumParamSubType
            (
            );
            /**Sets  the enum parameter sub type  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamSubType
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamSubType enumParamSubType /** enumparamsubtype */ 
            );
            /**Returns  the enum parameter extent  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamExtent EnumParameterExtent
            (
            );
            /**Sets  the enum parameter extent  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParameterExtent
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamExtent enumParameterExtent /** enumparameterextent */ 
            );
            /**Returns  the double parameter extent length  <br> License requirements : None */
            public: double DoubleParamExtLength
            (
            );
            /**Sets  the double parameter extent length  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleParamExtLength
            (
                double doubleParamExtLength /** doubleparamextlength */ 
            );
            /**Returns  the double parameter extent area  <br> License requirements : None */
            public: double DoubleParamExtArea
            (
            );
            /**Sets  the double parameter extent area  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleParamExtArea
            (
                double doubleParamExtArea /** doubleparamextarea */ 
            );
            /**Returns  the enum parameter tolerance zone shape  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolZoneShape EnumParamTolZoneShape
            (
            );
            /**Sets  the enum parameter tolerance zone shape  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamTolZoneShape
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolZoneShape enumParamTolZoneShape /** enumparamtolzoneshape */ 
            );
            /**Returns  the double parameter tolerance value  <br> License requirements : None */
            public: double DoubleParamTolValue
            (
            );
            /**Sets  the double parameter tolerance value  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleParamTolValue
            (
                double doubleParamTolValue /** doubleparamtolvalue */ 
            );
            /**Returns  the enum parameter tolerance material modifier  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolMatModifier EnumParamTolMatModifier
            (
            );
            /**Sets  the enum parameter tolerance material modifier  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamTolMatModifier
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolMatModifier enumParamTolMatModifier /** enumparamtolmatmodifier */ 
            );
            /**Returns  the enum parameter tolerance material modifier dup  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolMatModifierDup EnumParamTolMatModifierDup
            (
            );
            /**Sets  the enum parameter tolerance material modifier dup  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamTolMatModifierDup
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolMatModifierDup enumParamTolMatModifierDup /** enumparamtolmatmodifierdup */ 
            );
            /**Returns  the double parameter outer profile  <br> License requirements : None */
            public: double DoubleParamOuterProfile
            (
            );
            /**Sets  the double parameter outer profile  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleParamOuterProfile
            (
                double doubleParamOuterProfile /** doubleparamouterprofile */ 
            );
            /**Returns  the string primary datum  <br> License requirements : None */
            public: NXString StringPriDatum
            (
            );
            /**Sets  the string primary datum  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringPriDatum
            (
                const NXString & stringPriDatum /** stringpridatum */ 
            );
            /**Returns  the enum parameter primary material modifier  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamPriDatumModifier EnumParamPriMatModifier
            (
            );
            /**Sets  the enum parameter primary material modifier  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamPriMatModifier
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamPriDatumModifier enumParamPriMatModifier /** enumparamprimatmodifier */ 
            );
            /**Returns  the string secondary datum  <br> License requirements : None */
            public: NXString StringSecDatum
            (
            );
            /**Sets  the string secondary datum  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringSecDatum
            (
                const NXString & stringSecDatum /** stringsecdatum */ 
            );
            /**Returns  the enum parameter secondary material modifier  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamSecDatumModifier EnumParamSecMatModifier
            (
            );
            /**Sets  the enum parameter secondary material modifier  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamSecMatModifier
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamSecDatumModifier enumParamSecMatModifier /** enumparamsecmatmodifier */ 
            );
            /**Returns  the string tertiary datum  <br> License requirements : None */
            public: NXString StringTerDatum
            (
            );
            /**Sets  the string tertiary datum  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringTerDatum
            (
                const NXString & stringTerDatum /** stringterdatum */ 
            );
            /**Returns  the enum parameter tertiary material modifier  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTerDatumModifier EnumParamTerMatModifier
            (
            );
            /**Sets  the enum parameter tertiary material modifier  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamTerMatModifier
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTerDatumModifier enumParamTerMatModifier /** enumparamtermatmodifier */ 
            );
            /**Returns  the enum parameter tolerance zone shape1  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolZoneShape EnumParamTolZoneShape1
            (
            );
            /**Sets  the enum parameter tolerance zone shape1  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamTolZoneShape1
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolZoneShape enumParamTolZoneShape1 /** enumparamtolzoneshape1 */ 
            );
            /**Returns  the double parameter tolerance value1  <br> License requirements : None */
            public: double DoubleParamTolValue1
            (
            );
            /**Sets  the double parameter tolerance value1  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleParamTolValue1
            (
                double doubleParamTolValue1 /** doubleparamtolvalue1 */ 
            );
            /**Returns  the double lower parameter outer profile  <br> License requirements : None */
            public: double DoubleLowerParamOuterProfile
            (
            );
            /**Sets  the double lower parameter outer profile  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleLowerParamOuterProfile
            (
                double doubleLowerParamOuterProfile /** doublelowerparamouterprofile */ 
            );
            /**Returns  the enum parameter tolerance material modifier1  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolMatModifier EnumParamTolMatModifier1
            (
            );
            /**Sets  the enum parameter tolerance material modifier1  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamTolMatModifier1
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTolMatModifier enumParamTolMatModifier1 /** enumparamtolmatmodifier1 */ 
            );
            /**Returns  the string primary datum1  <br> License requirements : None */
            public: NXString StringPriDatum1
            (
            );
            /**Sets  the string primary datum1  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringPriDatum1
            (
                const NXString & stringPriDatum1 /** stringpridatum1 */ 
            );
            /**Returns  the enum parameter primary material modifier1  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamPriDatumModifier EnumParamPriMatModifier1
            (
            );
            /**Sets  the enum parameter primary material modifier1  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamPriMatModifier1
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamPriDatumModifier enumParamPriMatModifier1 /** enumparamprimatmodifier1 */ 
            );
            /**Returns  the string secondary datum1  <br> License requirements : None */
            public: NXString StringSecDatum1
            (
            );
            /**Sets  the string secondary datum1  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringSecDatum1
            (
                const NXString & stringSecDatum1 /** stringsecdatum1 */ 
            );
            /**Returns  the enum parameter secondary material modifier1  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamSecDatumModifier EnumParamSecMatModifier1
            (
            );
            /**Sets  the enum parameter secondary material modifier1  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamSecMatModifier1
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamSecDatumModifier enumParamSecMatModifier1 /** enumparamsecmatmodifier1 */ 
            );
            /**Returns  the string tertiary datum1  <br> License requirements : None */
            public: NXString StringTerDatum1
            (
            );
            /**Sets  the string tertiary datum1  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringTerDatum1
            (
                const NXString & stringTerDatum1 /** stringterdatum1 */ 
            );
            /**Returns  the enum parameter tertiary material modifier1  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTerDatumModifier EnumParamTerMatModifier1
            (
            );
            /**Sets  the enum parameter tertiary material modifier1  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumParamTerMatModifier1
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::ParamTerDatumModifier enumParamTerMatModifier1 /** enumparamtermatmodifier1 */ 
            );
            /**Returns  the vector view vec  <br> License requirements : None */
            public: NXOpen::Direction * VectorViewVec
            (
            );
            /**Sets  the vector view vec  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVectorViewVec
            (
                NXOpen::Direction * vectorViewVec /** vectorviewvec */ 
            );
            /**Returns  the double view vec i  <br> License requirements : None */
            public: double DoubleViewVecI
            (
            );
            /**Sets  the double view vec i  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleViewVecI
            (
                double doubleViewVecI /** doubleviewveci */ 
            );
            /**Returns  the double view vec j  <br> License requirements : None */
            public: double DoubleViewVecJ
            (
            );
            /**Sets  the double view vec j  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleViewVecJ
            (
                double doubleViewVecJ /** doubleviewvecj */ 
            );
            /**Returns  the double view vec k  <br> License requirements : None */
            public: double DoubleViewVecK
            (
            );
            /**Sets  the double view vec k  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleViewVecK
            (
                double doubleViewVecK /** doubleviewveck */ 
            );
            /**Returns  the selection toleranced feature  <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectionTolerancedFeature
            (
            );
            /**Returns  the string toleranced feat  <br> License requirements : None */
            public: NXString StringTolerancedFeat
            (
            );
            /**Sets  the string toleranced feat  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringTolerancedFeat
            (
                const NXString & stringTolerancedFeat /** stringtolerancedfeat */ 
            );
            /**Returns  the selection origin feature  <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectionOriginFeature
            (
            );
            /**Returns  the string origin feat name  <br> License requirements : None */
            public: NXString StringOriginFeatName
            (
            );
            /**Sets  the string origin feat name  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringOriginFeatName
            (
                const NXString & stringOriginFeatName /** stringoriginfeatname */ 
            );
            /**Returns  the vector direction  <br> License requirements : None */
            public: NXOpen::Direction * VectorDirection
            (
            );
            /**Sets  the vector direction  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetVectorDirection
            (
                NXOpen::Direction * vectorDirection /** vectordirection */ 
            );
            /**Returns  the enum pcsabs  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::SirVecPCSABS EnumPCSABS
            (
            );
            /**Sets  the enum pcsabs  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetEnumPCSABS
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::SirVecPCSABS enumPCSABS /** enumpcsabs */ 
            );
            /**Returns  the double dir vec i  <br> License requirements : None */
            public: double DoubleDirVecI
            (
            );
            /**Sets  the double dir vec i  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleDirVecI
            (
                double doubleDirVecI /** doubledirveci */ 
            );
            /**Returns  the double dir vec j  <br> License requirements : None */
            public: double DoubleDirVecJ
            (
            );
            /**Sets  the double dir vec j  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleDirVecJ
            (
                double doubleDirVecJ /** doubledirvecj */ 
            );
            /**Returns  the double dir vec k  <br> License requirements : None */
            public: double DoubleDirVecK
            (
            );
            /**Sets  the double dir vec k  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetDoubleDirVecK
            (
                double doubleDirVecK /** doubledirveck */ 
            );
            /**Returns  the selection feature  <br> License requirements : None */
            public: NXOpen::SelectNXObject * SelectionFeature
            (
            );
            /**Returns  the string datum feat name  <br> License requirements : None */
            public: NXString StringDatumFeatName
            (
            );
            /**Sets  the string datum feat name  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringDatumFeatName
            (
                const NXString & stringDatumFeatName /** stringdatumfeatname */ 
            );
            /**Returns  the string tolerance name  <br> License requirements : None */
            public: NXString StringTolName
            (
            );
            /**Sets  the string tolerance name  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetStringTolName
            (
                const NXString & stringTolName /** stringtolname */ 
            );
            /**Returns  the deg/min flag for angle between  <br> License requirements : None */
            public: NXOpen::CAM::InspectionToleranceOperationBuilder::AngleFormat UseDegMin
            (
            );
            /**Sets  the deg/min flag for angle between  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetUseDegMin
            (
                NXOpen::CAM::InspectionToleranceOperationBuilder::AngleFormat useDegMinSec /** usedegminsec */ 
            );
            /**Returns  the string for anglb nominal DMS  <br> License requirements : None */
            public: NXString NominalDMS
            (
            );
            /**Sets  the string for anglb nominal DMS  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetNominalDMS
            (
                const NXString & stringNominalDMS /** stringnominaldms */ 
            );
            /**Returns  the string for anglb upper DMS  <br> License requirements : None */
            public: NXString UpperDMS
            (
            );
            /**Sets  the string for anglb upper DMS  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetUpperDMS
            (
                const NXString & stringUpperDMS /** stringupperdms */ 
            );
            /**Returns  the string for anglb upper DMS  <br> License requirements : None */
            public: NXString LowerDMS
            (
            );
            /**Sets  the string for anglb upper DMS  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void SetLowerDMS
            (
                const NXString & stringLowerDMS /** stringlowerdms */ 
            );
            /** Updates Inspection tolerance parameters based on selected annotation.  <br> License requirements : insp_programming ("INSPECTION PROGRAMMING") */
            public: void UpdateParameters
            (
            );
        };
    }
}
#undef EXPORTLIBRARY
#endif