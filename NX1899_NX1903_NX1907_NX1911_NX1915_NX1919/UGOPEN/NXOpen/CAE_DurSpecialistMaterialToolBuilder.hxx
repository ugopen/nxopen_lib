#ifndef NXOpen_CAE_DURSPECIALISTMATERIALTOOLBUILDER_HXX_INCLUDED
#define NXOpen_CAE_DURSPECIALISTMATERIALTOOLBUILDER_HXX_INCLUDED
//--------------------------------------------------------------------------
//  Header for C++ interface to JA API
//--------------------------------------------------------------------------
//
//  Source File:
//     CAE_DurSpecialistMaterialToolBuilder.ja
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
#include <NXOpen/CAE_DurSpecialistSimulationObjectTable.hxx>
#include <NXOpen/Expression.hxx>
#include <NXOpen/Builder.hxx>
#include <NXOpen/libnxopencpp_cae_exports.hxx>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable:4996)
#endif
#ifdef __GNUC__
#pragma GCC diagnostic ignored "-Wdeprecated-declarations"
#endif

namespace NXOpen
{
    namespace CAE
    {
        class DurSpecialistMaterialToolBuilder;
    }
    class Builder;
    namespace CAE
    {
        class DurSpecialistSimulationObjectTable;
    }
    class Expression;
    class PhysicalMaterial;
    namespace CAE
    {
        class _DurSpecialistMaterialToolBuilderBuilder;
        class DurSpecialistMaterialToolBuilderImpl;
        /** This class is used to generate a material to be used with Specialist Durability, based on an existing material  <br> To create a new instance of this class, use @link NXOpen::CAE::DurSpecialistManager::CreateMaterialToolBuilder  NXOpen::CAE::DurSpecialistManager::CreateMaterialToolBuilder @endlink  <br> 
         <br>  Created in NX1847.0.0.  <br>  
        */
        class NXOPENCPP_CAEEXPORT  DurSpecialistMaterialToolBuilder : public NXOpen::Builder
        {
            /** Definition Type */
            public: enum DefinitionType
            {
                DefinitionTypeUniversalSlope/** universal slope */ ,
                DefinitionTypeUniversalMaterialLaw/** universal material law */ ,
                DefinitionTypeSyntheticSNCurveFromStrainLife/** synthetic sncurve from strain life */ 
            };

            /** Universal Slope Material Type */
            public: enum USlopeMaterialType
            {
                USlopeMaterialTypeSteel/** steel */ ,
                USlopeMaterialTypeSteelFKMConservative/** steel fkmconservative */ ,
                USlopeMaterialTypeIronCasts/** iron casts */ ,
                USlopeMaterialTypeIronCastsFKMConservative/** iron casts fkmconservative */ ,
                USlopeMaterialTypeAluminum/** aluminum */ ,
                USlopeMaterialTypeMagnesium/** magnesium */ ,
                USlopeMaterialTypeAluminumMagnesiumFKMConservative/** aluminum magnesium fkmconservative */ ,
                USlopeMaterialTypeTitanium/** titanium */ ,
                USlopeMaterialTypeCopperNickel/** copper nickel */ 
            };

            /** Universal Slope Tensile Strength */
            public: enum USlopeTensileStrength
            {
                USlopeTensileStrengthInheritFromMaterial/** inherit from material */ ,
                USlopeTensileStrengthSpecify/** specify */ 
            };

            /** Uniform Material Law Material Type */
            public: enum ULawMaterialType
            {
                ULawMaterialTypeSteel/** steel */ ,
                ULawMaterialTypeAluminum/** aluminum */ ,
                ULawMaterialTypeGrayCast/** gray cast */ 
            };

            /** Uniform Material Law Tensile Strength */
            public: enum ULawTensileStrength
            {
                ULawTensileStrengthInheritFromMaterial/** inherit from material */ ,
                ULawTensileStrengthSpecify/** specify */ 
            };

            /** Uniform Material Law Young's Modulus */
            public: enum ULawYoungsModulus
            {
                ULawYoungsModulusInheritFromMaterial/** inherit from material */ ,
                ULawYoungsModulusSpecify/** specify */ 
            };

            private: DurSpecialistMaterialToolBuilderImpl * m_durspecialistmaterialtoolbuilder_impl;
            private: friend class  _DurSpecialistMaterialToolBuilderBuilder;
            protected: DurSpecialistMaterialToolBuilder();
            public: ~DurSpecialistMaterialToolBuilder();
            /**Returns  the name. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : None */
            public: NXString Name
            (
            );
            /**Sets  the name. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetName
            (
                const NXString & name /** name given to the material to be created */
            );
            /**Sets  the name. 
             <br>  Created in NX1899.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            void SetName
            (
                const char * name /** name given to the material to be created */
            );
            /**Returns  the selected material. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PhysicalMaterial * SourceMaterial
            (
            );
            /**Sets  the selected material. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetSourceMaterial
            (
                NXOpen::PhysicalMaterial * material /** @link NXOpen::PhysicalMaterial NXOpen::PhysicalMaterial@endlink  to assign  */
            );
            /**Returns  the newly created material. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::PhysicalMaterial * CreatedMaterial
            (
            );
            /**Returns  the enum definition type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistMaterialToolBuilder::DefinitionType EnumDefinitionType
            (
            );
            /**Sets  the enum definition type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetEnumDefinitionType
            (
                NXOpen::CAE::DurSpecialistMaterialToolBuilder::DefinitionType enumDefinitionType /** enumdefinitiontype */ 
            );
            /**Returns  the enum uslope material type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistMaterialToolBuilder::USlopeMaterialType EnumUSlopeMaterialType
            (
            );
            /**Sets  the enum uslope material type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetEnumUSlopeMaterialType
            (
                NXOpen::CAE::DurSpecialistMaterialToolBuilder::USlopeMaterialType enumUSlopeMaterialType /** enumuslopematerialtype */ 
            );
            /**Returns  the enum uslope tensile strength 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistMaterialToolBuilder::USlopeTensileStrength EnumUSlopeTensileStrength
            (
            );
            /**Sets  the enum uslope tensile strength 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetEnumUSlopeTensileStrength
            (
                NXOpen::CAE::DurSpecialistMaterialToolBuilder::USlopeTensileStrength enumUSlopeTensileStrength /** enumuslopetensilestrength */ 
            );
            /**Returns  the expression uslope tensile strength 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ExpressionUSlopeTensileStrength
            (
            );
            /**Returns  the enum ulaw material type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistMaterialToolBuilder::ULawMaterialType EnumULawMaterialType
            (
            );
            /**Sets  the enum ulaw material type 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetEnumULawMaterialType
            (
                NXOpen::CAE::DurSpecialistMaterialToolBuilder::ULawMaterialType enumULawMaterialType /** enumulawmaterialtype */ 
            );
            /**Returns  the enum ulaw tensile strength 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistMaterialToolBuilder::ULawTensileStrength EnumULawTensileStrength
            (
            );
            /**Sets  the enum ulaw tensile strength 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetEnumULawTensileStrength
            (
                NXOpen::CAE::DurSpecialistMaterialToolBuilder::ULawTensileStrength enumULawTensileStrength /** enumulawtensilestrength */ 
            );
            /**Returns  the expression ulaw tensile strength 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ExpressionULawTensileStrength
            (
            );
            /**Returns  the enum ulaw youngs modulus 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistMaterialToolBuilder::ULawYoungsModulus EnumULawYoungsModulus
            (
            );
            /**Sets  the enum ulaw youngs modulus 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetEnumULawYoungsModulus
            (
                NXOpen::CAE::DurSpecialistMaterialToolBuilder::ULawYoungsModulus enumULawYoungsModulus /** enumulawyoungsmodulus */ 
            );
            /**Returns  the expression ulaw youngs modulus 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::Expression * ExpressionULawYoungsModulus
            (
            );
            /**Returns  the strain life damage simulation object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSimulationObjectTable * StrainLifeDamage
            (
            );
            /**Sets  the strain life damage simulation object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetStrainLifeDamage
            (
                NXOpen::CAE::DurSpecialistSimulationObjectTable * strainLifeDamage /** strain life damage simulation object to assign  */
            );
            /**Returns  the load notch strain relation simulation object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : None */
            public: NXOpen::CAE::DurSpecialistSimulationObjectTable * LoadNotchStrainRelation
            (
            );
            /**Sets  the load notch strain relation simulation object 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: void SetLoadNotchStrainRelation
            (
                NXOpen::CAE::DurSpecialistSimulationObjectTable * loadNotchStrainRelation /** load notch strain relation simulation object to assign  */
            );
            /** Check if the material has its ultimate tensile strength defined or not. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: bool IsUltimateTensileStrengthDefined
            (
                NXOpen::PhysicalMaterial * materialTag /** @link NXOpen::PhysicalMaterial NXOpen::PhysicalMaterial@endlink  to check  */
            );
            /** Check if the material has its Young's modulus defined or not. 
             <br>  Created in NX1847.0.0.  <br>  
             <br> License requirements : sc_dur_specialist ("Simcenter Specialist Durability") */
            public: bool IsYoungsModulusDefined
            (
                NXOpen::PhysicalMaterial * materialTag /** @link NXOpen::PhysicalMaterial NXOpen::PhysicalMaterial@endlink  to check  */
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