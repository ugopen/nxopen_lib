/*****************************************************************************
             Copyright (c) 2002 - 2005 UGS Inc
                       Unpublished - All Rights Reserved

====================================================================================================



File Description :

 Data Definitions for the Open API interface to Units Module.

*****************************************************************************/
#ifndef  UF_UNIT_TYPES__H_INCLUDED
#define  UF_UNIT_TYPES__H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

enum UF_UNIT_MEASURE_TYPE_e{
    UF_MEASURE_INVALID = -2,
    UF_MEASURE_UNITLESS = -1,
    UF_MEASURE_LENGTH = 0,
    UF_MEASURE_AREA,
    UF_MEASURE_VOLUME,
    UF_MEASURE_MASS,
    UF_MEASURE_MASS_DENSITY,
    UF_MEASURE_FATIGUE_STRENGTH_COEFF,
    UF_MEASURE_TIME,
    UF_MEASURE_ANGLE,
    UF_MEASURE_VELOCITY,
    UF_MEASURE_ACCELERATION,
    UF_MEASURE_FORCE,
    UF_MEASURE_FORCE_PER_LENGTH,    /* Pressure on Edge, Edge Shear */
    UF_MEASURE_FORCE_PER_AREA,      /* Pressure on Face */
    UF_MEASURE_MOMENT,
    UF_MEASURE_STRESS,
    UF_MEASURE_STRAIN,
    UF_MEASURE_STRAIN_ENERGY,
    UF_MEASURE_STRAIN_ENERGY_DENSITY,
    UF_MEASURE_TEMPERATURE,
    UF_MEASURE_HEAT_FLUX,
    UF_MEASURE_CONVECTION_COEFF,
    UF_MEASURE_THERMAL_CONDUCTIVITY,
    UF_MEASURE_THERMAL_EXPANSION_COEFF,
    UF_MEASURE_SPECIFIC_HEAT,
    UF_MEASURE_ANGULAR_VELOCITY,
    UF_MEASURE_ANGULAR_ACCELERATION,
    UF_MEASURE_FATIGUE_LIFE,
    UF_MEASURE_HEAT_FLOW,
    UF_MEASURE_THERMAL_ENERGY,
    UF_MEASURE_MASS_MOMENT_INERTIA,
    UF_MEASURE_DYNAMIC_VISCOSITY,
    UF_MEASURE_HEAT_GENERATION,
    UF_MEASURE_CONDUCTANCE,
    UF_MEASURE_LENGTH_CONDUCTANCE,
    UF_MEASURE_THERMAL_RESISTANCE,
    UF_MEASURE_MASS_FLOW,
    UF_MEASURE_VOLUME_FLOW,
    UF_MEASURE_TEMPERATURE_DIFFERENCE,
    UF_MEASURE_FREQUENCY,
    UF_MEASURE_COEFFICIENT_LENGTH,
    UF_MEASURE_MOMENT_OF_INERTIA_AREA,
    UF_MEASURE_VISCOUS_DAMPING,
    UF_MEASURE_ENERGY,
    UF_MEASURE_POWER,
    UF_MEASURE_MOMENTUM,
    UF_MEASURE_TEMPERATURE_GRADIENT,
    UF_MEASURE_ENERGY_PER_MASS,
    UF_MEASURE_DISSIPATION_RATE_OF_ENERGY_PER_MASS,
    UF_MEASURE_MASS_FLUX,
    UF_MEASURE_MASS_PER_LENGTH,
    UF_MEASURE_MASS_PER_AREA,
    UF_MEASURE_ELECTRIC_CURRENT,
    UF_MEASURE_ELECTRICAL_RESISTANCE,
    UF_MEASURE_ELECTRICAL_RESISTIVITY,
    UF_MEASURE_ELECTRICAL_CONDUCTANCE,
    UF_MEASURE_VOLTAGE,
    UF_MEASURE_VOLTAGE_PER_TEMPERATURE, /* Seebeck coefficient*/
    UF_MEASURE_DIFFUSIVITY,
    UF_MEASURE_LATENT_HEAT_PER_MASS,
    UF_MEASURE_THERMAL_ENERGY_PER_AREA,
    UF_MEASURE_THERMAL_PID_GAIN,
    UF_MEASURE_THERMAL_PID_INTEGRAL,
    UF_MEASURE_THERMAL_PID_DERIVATIVE,
    UF_MEASURE_HEADLOSS_COEFF,
    UF_MEASURE_TSAI_WU_COEFF,
    UF_MEASURE_MASS_LENGTH,
    UF_MEASURE_PER_VOLUME,
    UF_MEASURE_WARPING_CONSTANT,
    UF_MEASURE_STRESS_COMPLIANCE,
    UF_MEASURE_LENGTH_PER_PRESSURE,
    UF_MEASURE_PRESSURE_PER_LENGTH,
    UF_MEASURE_PRESSURE_PER_VELOCITY,
    UF_MEASURE_MOMENT_PER_ANGLE,
    UF_MEASURE_COUNT
};
typedef enum UF_UNIT_MEASURE_TYPE_e UF_UNIT_MEASURE_TYPE_t, *UF_UNIT_MEASURE_TYPE_p_t;

/************************************************************************************
 *      Unit Display Names defined using hash defines for easy access to
 *      System defined units from user functions
 ************************************************************************************/

#define UF_UNIT_LENGTH_m                        "Meter"
#define UF_UNIT_LENGTH_mm                       "MilliMeter"
#define UF_UNIT_LENGTH_cm                       "CentiMeter"
#define UF_UNIT_LENGTH_in                       "Inch"
#define UF_UNIT_LENGTH_ft                       "Feet"
#define UF_UNIT_LENGTH_micron                   "Micron"
#define UF_UNIT_LENGTH_nm                       "NanoMeter"
#define UF_UNIT_LENGTH_a                        "Angstrom"
#define UF_UNIT_LENGTH_km                       "KiloMeter"
#define UF_UNIT_LENGTH_mi                       "Mile"


#define UF_UNIT_AREA_m2                         "SquareMeter"
#define UF_UNIT_AREA_mm2                        "SquareMilliMeter"
#define UF_UNIT_AREA_cm2                        "SquareCentiMeter"
#define UF_UNIT_AREA_in2                        "SquareInch"
#define UF_UNIT_AREA_ft2                        "SquareFeet"

#define UF_UNIT_VOLUME_m3                       "CubicMeter"
#define UF_UNIT_VOLUME_mm3                      "CubicMilliMeter"
#define UF_UNIT_VOLUME_cm3                      "CubicCentiMeter"
#define UF_UNIT_VOLUME_in3                      "CubicInch"
#define UF_UNIT_VOLUME_ft3                      "CubicFeet"

#define UF_UNIT_MASS_kg                         "Kilogram"
#define UF_UNIT_MASS_g                          "Gram"
#define UF_UNIT_MASS_t                          "Tonne"
#define UF_UNIT_MASS_slug                       "Slug"
#define UF_UNIT_MASS_lbfsec__in2                "PoundSecondsSquaredPerInch"
#define UF_UNIT_MASS_lbm                        "PoundMass"
#define UF_UNIT_MASS_kgf_sec2__m                "KilogramForceSecondsSquaredPerMeter"
#define UF_UNIT_MASS_kgf_sec2__mm               "KilogramForceSecondsSquaredPerMilliMeter"

#define UF_UNIT_MASSDENSITY_kg__m3              "KilogramPerCubicMeter"
#define UF_UNIT_MASSDENSITY_kg__mm3             "KilogramPerCubicMilliMeter"
#define UF_UNIT_MASSDENSITY_t__m3               "TonnePerCubicMeter"
#define UF_UNIT_MASSDENSITY_t__mm3              "TonnePerCubicMilliMeter"
#define UF_UNIT_MASSDENSITY_lbfsec2__in4        "PoundsSecondSquaredPerInchFourth"
#define UF_UNIT_MASSDENSITY_slug__ft3           "SlugsPerCubicFeet"
#define UF_UNIT_MASSDENSITY_lbm__in3            "PoundMassperCubicInch"

#define UF_UNIT_FATIGUESTR_COEFF_mN__mm2        "MilliNewtonPerSquareMilliMeter"
#define UF_UNIT_FATIGUESTR_COEFF_N__mm2         "NewtonPerSquareMilliMeter"
#define UF_UNIT_FATIGUESTR_COEFF_N__m2          "Pascals"
#define UF_UNIT_FATIGUESTR_COEFF_lbf__in2       "PoundForcePerSquareInch"

#define UF_UNIT_TIME_sec                        "Second"
#define UF_UNIT_TIME_min                        "Minute"
#define UF_UNIT_TIME_hr                         "Hour"

#define UF_UNIT_ANGLE_rad                       "Radian"
#define UF_UNIT_ANGLE_deg                       "Degrees"
#define UF_UNIT_ANGLE_rev                       "Revs"

#define UF_UNIT_VELOCITY_m__sec                 "MeterPerSecond"
#define UF_UNIT_VELOCITY_mm__sec                "MilliMeterPerSecond"
#define UF_UNIT_VELOCITY_in__sec                "InchPerSecond"
#define UF_UNIT_VELOCITY_ft__sec                "FeetPerSecond"
#define UF_UNIT_VELOCITY_km__hr                 "KiloMeterPerHour"
#define UF_UNIT_VELOCITY_cm__sec                "CentiMeterPerSecond"
#define UF_UNIT_VELOCITY_mi__hr                 "MilePerHour"

#define UF_UNIT_ACCELERATION_m__sec2            "MeterPerSquareSecond"
#define UF_UNIT_ACCELERATION_mm__sec2           "MilliMeterPerSquareSecond"
#define UF_UNIT_ACCELERATION_in__sec2           "InchPerSquareSecond"
#define UF_UNIT_ACCELERATION_ft__sec2           "FeetPerSquareSecond"
#define UF_UNIT_ACCELERATION_g                  "g's"

#define UF_UNIT_FORCE_mN                        "MilliNewton"
#define UF_UNIT_FORCE_N                         "Newton"
#define UF_UNIT_FORCE_lbf                       "PoundForce"
#define UF_UNIT_FORCE_Poundal                   "Poundal"


#define UF_UNIT_PRESSUREONEDGE_mN__mm           "MilliNewtonsPerMilliMeter"
#define UF_UNIT_PRESSUREONEDGE_N__mm            "NewtonsPerMilliMeter"
#define UF_UNIT_PRESSUREONEDGE_N__m             "NewtonPerMeter"
#define UF_UNIT_PRESSUREONEDGE_lbf__in          "PoundForcePerInch"
#define UF_UNIT_PRESSUREONEDGE_lbf__ft          "PoundForcePerFoot"

#define UF_UNIT_PRESSURE_mN__mm2                "MilliNewtonPerSquareMilliMeter"
#define UF_UNIT_PRESSURE_N__mm2                 "NewtonPerSquareMilliMeter"
#define UF_UNIT_PRESSURE_N__m2                  "Pascals"
#define UF_UNIT_PRESSURE_lbf__in2               "PoundForcePerSquareInch"
#define UF_UNIT_PRESSURE_lbf__ft2               "PoundForcePerFeetSquared"
#define UF_UNIT_PRESSURE_bar                    "Bar"
#define UF_UNIT_PRESSURE_atmosphere             "Atmosphere"
#define UF_UNIT_PRESSURE_N__cm2                 "NewtonPerSquareCentiMeter"
#define UF_UNIT_PRESSURE_mm_H2O                 "MilliMeterOfWater"
#define UF_UNIT_PRESSURE_mm_Hg                  "MilliMeterOfMercury"
#define UF_UNIT_PRESSURE_in_H2O                 "InchOfWater"
#define UF_UNIT_PRESSURE_in_Hg                  "InchOfMercury"

#define UF_UNIT_MOMENT_mNmm                     "MilliNewtonMilliMeter"
#define UF_UNIT_MOMENT_Nmm                      "NewtonMilliMeter"
#define UF_UNIT_MOMENT_Nm                       "NewtonMeter"
#define UF_UNIT_MOMENT_lbfin                    "PoundForceInch"
#define UF_UNIT_MOMENT_lbfft                    "PoundForceFeet"

#define UF_UNIT_STRESS_mN__mm2                  "MilliNewtonPerSquareMilliMeter"
#define UF_UNIT_STRESS_N__mm2                   "NewtonPerSquareMilliMeter"
#define UF_UNIT_STRESS_N__m2                    "Pascals"
#define UF_UNIT_STRESS_lbf__in2                 "PoundForcePerSquareInch"
#define UF_UNIT_STRESS_N__cm2                   "NewtonPerSquareCentiMeter"
#define UF_UNIT_STRESS_lbf__ft2                 "PoundForcePerSquareFeet"

#define UF_UNIT_STRAIN_mm__mm                   "Strain_Metric1"
#define UF_UNIT_STRAIN_in__in                   "Strain_English1"

#define UF_UNIT_STRAINENERGY_mNmm               "StrainEnergy_Metric1"
#define UF_UNIT_STRAINENERGY_Nmm                "StrainEnergy_Metric2"
#define UF_UNIT_STRAINENERGY_Nm                 "StrainEnergy_Metric3"
#define UF_UNIT_STRAINENERGY_lbfin              "StrainEnergy_English1"
#define UF_UNIT_STRAINENERGY_lbfft              "StrainEnergy_English2"

#define UF_UNIT_STRAINENERGYDENSITY_mNmm__mm3   "StrainEnergyDensity_Metric1"
#define UF_UNIT_STRAINENERGYDENSITY_Nmm__m3     "StrainEnergyDensity_Metric2"
#define UF_UNIT_STRAINENERGYDENSITY_Nm__m3      "StrainEnergyDensity_Metric3"
#define UF_UNIT_STRAINENERGYDENSITY_lbfin__in3  "StrainEnergyDensity_English1"
#define UF_UNIT_STRAINENERGYDENSITY_lbfft__ft3  "StrainEnergyDensity_English2"

#define UF_UNIT_TEMPERATURE_C                   "Celsius"
#define UF_UNIT_TEMPERATURE_F                   "Fahrenheit"
#define UF_UNIT_TEMPERATURE_K                   "Kelvin"
#define UF_UNIT_TEMPERATURE_R                   "Rankine"

#define UF_UNIT_HEATFLUX_microWatt__mm2         "HeatFlux_Metric1"
#define UF_UNIT_HEATFLUX_Watt__mm2              "HeatFlux_Metric2"
#define UF_UNIT_HEATFLUX_BTU__sec__in2          "HeatFlux_English1"
#define UF_UNIT_HEATFLUX_mWatt__mm2             "HeatFlux_Metric3"
#define UF_UNIT_HEATFLUX_Watt__cm2              "HeatFlux_Metric4"
#define UF_UNIT_HEATFLUX_Watt__m2               "HeatFlux_Metric5"
#define UF_UNIT_HEATFLUX_Watt__in2              "HeatFlux_Metric6"
#define UF_UNIT_HEATFLUX_BTU__sec__ft2          "HeatFlux_English2"
#define UF_UNIT_HEATFLUX_BTU__hr__in2           "HeatFlux_English3"
#define UF_UNIT_HEATFLUX_BTU__hr__ft2           "HeatFlux_English4"
#define UF_UNIT_HEATFLUX_lbfin__sec__in2        "HeatFlux_English5"


#define UF_UNIT_HEATFLOW_microWatt              "HeatFlow_Metric1"
#define UF_UNIT_HEATFLOW_Watt                   "HeatFlow_Metric2"
#define UF_UNIT_HEATFLOW_BTU__sec               "HeatFlow_English1"
#define UF_UNIT_HEATFLOW_lbfin__sec             "HeatFlow_English2"

#define UF_UNIT_THERMALENERGY_microJ            "ThermalEnergy_Metric1"
#define UF_UNIT_THERMALENERGY_J                 "ThermalEnergy_Metric2"
#define UF_UNIT_THERMALENERGY_mJ                "ThermalEnergy_Metric3"
#define UF_UNIT_THERMALENERGY_kgfm              "ThermalEnergy_Metric4"
#define UF_UNIT_THERMALENERGY_kgfmm             "ThermalEnergy_Metric5"
#define UF_UNIT_THERMALENERGY_cJcm              "ThermalEnergy_Metric6"

#define UF_UNIT_THERMALENERGY_BTU               "ThermalEnergy_English1"
#define UF_UNIT_THERMALENERGY_lbfin             "ThermalEnergy_English2"
#define UF_UNIT_THERMALENERGY_lbfft             "ThermalEnergy_English3"
#define UF_UNIT_THERMALENERGY_pdlft             "ThermalEnergy_English4"

#define UF_UNIT_CONVECTION_COEFF_microWatt__mm2__degC       "ConvectionCoefficient_Metric1"
#define UF_UNIT_CONVECTION_COEFF_Watt__mm2__degC            "ConvectionCoefficient_Metric2"
#define UF_UNIT_CONVECTION_COEFF_BTU__sec__in2__degF        "ConvectionCoefficient_English1"
#define UF_UNIT_CONVECTION_COEFF_mWatt__mm2__degC           "ConvectionCoefficient_Metric3"
#define UF_UNIT_CONVECTION_COEFF_Watt__cm2__degC            "ConvectionCoefficient_Metric4"
#define UF_UNIT_CONVECTION_COEFF_Watt__m2__degC             "ConvectionCoefficient_Metric5"
#define UF_UNIT_CONVECTION_COEFF_Watt__in2__degC            "ConvectionCoefficient_Metric6"
#define UF_UNIT_CONVECTION_COEFF_BTU__sec__ft2__degF        "ConvectionCoefficient_English2"
#define UF_UNIT_CONVECTION_COEFF_BTU__hr__in2__degF         "ConvectionCoefficient_English3"
#define UF_UNIT_CONVECTION_COEFF_BTU__hr__ft2__degF         "ConvectionCoefficient_English4"
#define UF_UNIT_CONVECTION_COEFF_lbfin__sec__in2__degF      "ConvectionCoefficient_English5"

#define UF_UNIT_THERMALCONDUCTIVITY_microWatt__mm__degC     "ThermalConductivity_Metric1"
#define UF_UNIT_THERMALCONDUCTIVITY_Watt__mm__degC          "ThermalConductivity_Metric2"
#define UF_UNIT_THERMALCONDUCTIVITY_Watt__m__degK           "ThermalConductivity_Metric3"
#define UF_UNIT_THERMALCONDUCTIVITY_BTU__sec__in__degF      "ThermalConductivity_English1"
#define UF_UNIT_THERMALCONDUCTIVITY_BTU__hr__ft__degF       "ThermalConductivity_English2"
#define UF_UNIT_THERMALCONDUCTIVITYE_Watt__m__degC          "ThermalConductivity_Metric4"
#define UF_UNIT_THERMALCONDUCTIVITY_BTU__hr__in__degF       "ThermalConductivity_English3"
#define UF_UNIT_THERMALCONDUCTIVITY_mWatt__mm__degC         "ThermalConductivity_Metric5"
#define UF_UNIT_THERMALCONDUCTIVITY_Watt__cm__degC          "ThermalConductivity_Metric6"
#define UF_UNIT_THERMALCONDUCTIVITY_BTU__sec__ft__degF      "ThermalConductivity_English4"
#define UF_UNIT_THERMALCONDUCTIVITY_lbfin__sec__in__degF    "ThermalConductivity_English5"

#define UF_UNIT_THERMALEXPANSION_COEFF___degC   "ThermalExpansion_Metric1"
#define UF_UNIT_THERMALEXPANSION_COEFF___degF   "ThermalExpansion_English1"
#define UF_UNIT_THERMALEXPANSION_COEFF___degK   "ThermalExpansion_Metric2"

#define UF_UNIT_SPECIFICHEAT_microJ__kg__degK               "SpecificHeat_Metric1"
#define UF_UNIT_SPECIFICHEAT_J__kg__degK                    "SpecificHeat_Metric2"
#define UF_UNIT_SPECIFICHEAT_kJ__kg__degK                   "SpecificHeat_Metric3"
#define UF_UNIT_SPECIFICHEAT_BTU__lbm__degF                 "SpecificHeat_English1"
#define UF_UNIT_SPECIFICHEAT_BTU_in__lbf_sec2_degF          "SpecificHeat_English2"
#define UF_UNIT_SPECIFICHEAT_lbfin_lbm_degF                 "SpecificHeat_English3"
#define UF_UNIT_SPECIFICHEAT_lbfin_in__lbf_sec2_degF        "SpecificHeat_English4"

#define UF_UNIT_ANGULARVELOCITY_rev__sec        "RevolutionsPerSecond"
#define UF_UNIT_ANGULARVELOCITY_rev__min        "RevolutionsPerMinute"
#define UF_UNIT_ANGULARVELOCITY_deg__sec        "DegreesPerSecond"
#define UF_UNIT_ANGULARVELOCITY_rad__sec        "RadiansPerSecond"

#define UF_UNIT_ANGULARACCELERATION_rev__sec2   "RevolutionsPerSecondSquared"
#define UF_UNIT_ANGULARACCELERATION_rev__min2   "RevolutionsPerMinuteSquared"
#define UF_UNIT_ANGULARACCELERATION_deg__sec2   "DegreesPerSecondSquared"
#define UF_UNIT_ANGULARACCELERATION_rad__sec2   "RadiansPerSecondSquared"

#define UF_UNIT_FATIGUELIFE_DUTYCYCLES          "DutyCycles"

#define UF_UNIT_MASSMOMENTINERTIA_lbmin2        "PoundMassInchSquared"
#define UF_UNIT_MASSMOMENTINERTIA_kgmm2         "KilogramMilliMeterSquared"
#define UF_UNIT_MASSMOMENTINERTIA_lbfinsec2     "PoundForceInchSecondSquared"

#define UF_UNIT_DYNAMICVISC_kg__m__sec          "DynamicViscosity_Metric1"
#define UF_UNIT_DYNAMICVISC_kg__mm__sec         "DynamicViscosity_Metric2"
#define UF_UNIT_DYNAMICVISC_g__cm__sec          "DynamicViscosity_Metric3"
#define UF_UNIT_DYNAMICVISC_lbf__sec__in2       "DynamicViscosity_English1"
#define UF_UNIT_DYNAMICVISC_lbf__sec__ft2       "DynamicViscosity_English2"
#define UF_UNIT_DYNAMICVISC_lbm__in__sec        "DynamicViscosity_English3"
#define UF_UNIT_DYNAMICVISC_lbm__ft__sec        "DynamicViscosity_English4"
#define UF_UNIT_DYNAMICVISC_mN_sec__mm2         "DynamicViscosity_Metric4"
#define UF_UNIT_DYNAMICVISC_N_sec__mm2          "DynamicViscosity_Metric5"
#define UF_UNIT_DYNAMICVISC_N_sec__cm2          "DynamicViscosity_Metric6"
#define UF_UNIT_DYNAMICVISC_N_sec__m2           "DynamicViscosity_Metric7"

#define UF_UNIT_HEATGENERATION_microWatt__mm3   "HeatGeneration_Metric1"
#define UF_UNIT_HEATGENERATION_Watt__mm3        "HeatGeneration_Metric2"
#define UF_UNIT_HEATGENERATION_Watt__m3         "HeatGeneration_Metric3"
#define UF_UNIT_HEATGENERATION_BTU__sec__in3    "HeatGeneration_English1"
#define UF_UNIT_HEATGENERATION_BTU__hr__in3     "HeatGeneration_English2"
#define UF_UNIT_HEATGENERATION_BTU__hr__ft3     "HeatGeneration_English3"
#define UF_UNIT_HEATGENERATION_lbfin__sec__in3  "HeatGeneration_English4"

#define UF_UNIT_CONDUCTANCE_microWatt__degC     "ThermalConductance_Metric1"
#define UF_UNIT_CONDUCTANCE_Watt__degC          "ThermalConductance_Metric2"
#define UF_UNIT_CONDUCTANCE_BTU__sec__degF      "ThermalConductance_English1"
#define UF_UNIT_CONDUCTANCE_BTU__hr__degF       "ThermalConductance_English2"
#define UF_UNIT_CONDUCTANCE_mWatt__degC         "ThermalConductance_Metric3"
#define UF_UNIT_CONDUCTANCE_BTU__min__degF      "ThermalConductance_English3"
#define UF_UNIT_CONDUCTANCE_lbfin__sec__degF    "ThermalConductance_English4"

#define UF_UNIT_LENGTHCONDUCTANCE_microWatt__mm__degC     "ThermalConductivity_Metric1"
#define UF_UNIT_LENGTHCONDUCTANCE_Watt__mm__degC          "ThermalConductivity_Metric2"
#define UF_UNIT_LENGTHCONDUCTANCE_Watt__m__degC           "ThermalConductivity_Metric3"
#define UF_UNIT_LENGTHCONDUCTANCE_BTU__sec__in__degF      "ThermalConductivity_English1"
#define UF_UNIT_LENGTHCONDUCTANCE_BTU__hr__in__degF       "ThermalConductivity_English2"
#define UF_UNIT_LENGTHCONDUCTANCE_BTU__hr__ft__degF       "ThermalConductivity_English3"
#define UF_UNIT_LENGTHCONDUCTANCE_mWatt__mm__degC         "ThermalConductivity_Metric4"
#define UF_UNIT_LENGTHCONDUCTANCE_Watt__cm__degC          "ThermalConductivity_Metric5"
#define UF_UNIT_LENGTHCONDUCTANCE_BTU__sec__ft__degF      "ThermalConductivity_English4"
#define UF_UNIT_LENGTHCONDUCTANCE_lbfin__sec__in__degF    "ThermalConductivity_English5"

#define UF_UNIT_THERMALRESISTANCE_degC__microWatt    "ThermalResistance_Metric1"
#define UF_UNIT_THERMALRESISTANCE_degC__Watt         "ThermalResistance_Metric2"
#define UF_UNIT_THERMALRESISTANCE_degF__sec__BTU     "ThermalResistance_English1"
#define UF_UNIT_THERMALRESISTANCE_degF__hr__BTU      "ThermalResistance_English2"
#define UF_UNIT_THERMALRESISTANCE_degC__mWatt        "ThermalResistance_Metric3"
#define UF_UNIT_THERMALRESISTANCE_degF__min__BTU     "ThermalResistance_English3"
#define UF_UNIT_THERMALRESISTANCE_degF__sec__lbfin   "ThermalResistance_English4"

#define UF_UNIT_MASSFLOW_kg__sec                "KilogramPerSecond"
#define UF_UNIT_MASSFLOW_g__sec                 "GramPerSecond"
#define UF_UNIT_MASSFLOW_lbf__sec__ft           "PoundSecondPerFoot"
#define UF_UNIT_MASSFLOW_lbf__sec__in           "PoundSecondPerInch"
#define UF_UNIT_MASSFLOW_lbm__sec               "PoundMassPerSecond"
#define UF_UNIT_MASSFLOW_kg__hr                 "KilogramPerHour"
#define UF_UNIT_MASSFLOW_kg__min                "KilogramPerMinute"
#define UF_UNIT_MASSFLOW_g__hr                  "GramPerHour"
#define UF_UNIT_MASSFLOW_g__min                 "GramPerMinute"
#define UF_UNIT_MASSFLOW_lbm__hr                "PoundMassPerHour"
#define UF_UNIT_MASSFLOW_lbm__min               "PoundMassPerMinute"

#define UF_UNIT_VOLUMEFLOW_mm3__sec             "CubicMilliMeterPerSecond"
#define UF_UNIT_VOLUMEFLOW_m3__sec              "CubicMeterPerSecond"
#define UF_UNIT_VOLUMEFLOW_m3__hr               "CubicMeterPerHour"
#define UF_UNIT_VOLUMEFLOW_in3__sec             "CubicInchPerSecond"
#define UF_UNIT_VOLUMEFLOW_ft3__min             "CubicFeetPerMinute"
#define UF_UNIT_VOLUMEFLOW_l__sec               "LiterPerSecond"
#define UF_UNIT_VOLUMEFLOW_l__min               "LiterPerMinute"
#define UF_UNIT_VOLUMEFLOW_l__hr                "LiterPerHour"
#define UF_UNIT_VOLUMEFLOW_cm3__sec             "CubicCentiMeterPerSecond"
#define UF_UNIT_VOLUMEFLOW_m3__min              "CubicMeterPerMinute"
#define UF_UNIT_VOLUMEFLOW_ft3__sec             "CubicFeetPerSecond"
#define UF_UNIT_VOLUMEFLOW_ft3__hr              "CubicFeetPerHour"

#define UF_UNIT_TEMPERATUREDIFFERENCE_C         "CelsiusDifference"
#define UF_UNIT_TEMPERATUREDIFFERENCE_F         "FahrenheitDifference"
#define UF_UNIT_TEMPERATUREDIFFERENCE_K         "KelvinDifference"
#define UF_UNIT_TEMPERATUREDIFFERENCE_R         "RankineDifference"

#define UF_UNIT_MOMENT_OF_INERTIA_in4           "InchFourth"
#define UF_UNIT_MOMENT_OF_INERTIA_ft4           "FeetFourth"
#define UF_UNIT_MOMENT_OF_INERTIA_mm4           "MilliMeterFourth"
#define UF_UNIT_MOMENT_OF_INERTIA_m4            "MeterFourth"

#define UF_UNIT_FREQUENCY_hz                    "hertz"
#define UF_UNIT_FREQUENCY_kHz                   "KiloHertz"
#define UF_UNIT_FREQUENCY_MHz                   "MegaHertz"
#define UF_UNIT_FREQUENCY_GHz                   "GigaHertz"

#define UF_UNIT_COEFFICIENTLENGTH_m             "CoefficientPerMeter"
#define UF_UNIT_COEFFICIENTLENGTH_mm            "CoefficientPerMilliMeter"
#define UF_UNIT_COEFFICIENTLENGTH_in            "CoefficientPerInch"
#define UF_UNIT_COEFFICIENTLENGTH_ft            "CoefficientPerFoot"

#define UF_UNIT_VISCOUS_DAMPING_lbm__sec        "PoundMassPerSecond"
#define UF_UNIT_VISCOUS_DAMPING_lbfsec__in      "PoundForceSecondPerInch"
#define UF_UNIT_VISCOUS_DAMPING_kg__sec         "KilogramPerSecond"

#define UF_UNIT_ENERGY_lbm_ft2__sec2            "PoundMassFeetSquaredPerSecondSquared"
#define UF_UNIT_ENERGY_lbfin                    "PoundForceInch"
#define UF_UNIT_ENERGY_microJ                   "MicroJoule"
#define UF_UNIT_ENERGY_j                        "Joule"
#define UF_UNIT_ENERGY_btu                      "Btu"

#define UF_UNIT_POWER_lbm_ft2__sec3             "PoundMassFeetSquaredPerSecondCubed"
#define UF_UNIT_POWER_lbfin__sec                "PoundForceInchPerSecond"
#define UF_UNIT_POWER_microW                    "MicroWatt"
#define UF_UNIT_POWER_w                         "Watt"
#define UF_UNIT_POWER_kw                        "KiloWatt"
#define UF_UNIT_POWER_mw                        "MilliWatt"
#define UF_UNIT_POWER_BTU__hr                   "BTUPerHour"
#define UF_UNIT_POWER_BTU__min                  "BTUPerMinute"
#define UF_UNIT_POWER_BTU__sec                  "BTUPerSecond"

#define UF_UNIT_MOMENTUM_lbfsec                 "PoundForceSecond"
#define UF_UNIT_MOMENTUM_lbm_in__sec            "PoundMassInchPerSecond"
#define UF_UNIT_MOMENTUM_lbm_ft__sec            "PoundMassFeetPerSecond"
#define UF_UNIT_MOMENTUM_kg_mm__sec             "KilogramMilliMeterPerSecond"
#define UF_UNIT_MOMENTUM_kg_m__sec              "KilogramMeterPerSecond"

#define UF_UNIT_TEMPERATUREGRADIENT_C__m        "CelsiusPerMeter"
#define UF_UNIT_TEMPERATUREGRADIENT_C__mm       "CelsiusPerMilliMeter"
#define UF_UNIT_TEMPERATUREGRADIENT_F__in       "FahrenheitPerInch"
#define UF_UNIT_TEMPERATUREGRADIENT_F__ft       "FahrenheitPerFoot"

#define UF_UNIT_ENERGYPERMASS_mm2__sec2         "EnergyPerMass_Metric1"
#define UF_UNIT_ENERGYPERMASS_m2__sec2          "EnergyPerMass_Metric2"
#define UF_UNIT_ENERGYPERMASS_in2__sec2         "EnergyPerMass_English1"
#define UF_UNIT_ENERGYPERMASS_ft2__sec2         "EnergyPerMass_English2"

#define UF_UNIT_DISSIPATIONRATEOFENERGYPERMASS_mm2__sec3  "DissipationRate_Metric1"
#define UF_UNIT_DISSIPATIONRATEOFENERGYPERMASS_m2__sec3   "DissipationRate_Metric2"
#define UF_UNIT_DISSIPATIONRATEOFENERGYPERMASS_in2__sec3  "DissipationRate_English1"
#define UF_UNIT_DISSIPATIONRATEOFENERGYPERMASS_ft2__sec3  "DissipationRate_English2"

#define UF_UNIT_MASSFLUX_kg__sec__mm2            "MassFlux_Metric1"
#define UF_UNIT_MASSFLUX_kg__sec__m2             "MassFlux_Metric2"
#define UF_UNIT_MASSFLUX_lbf_sec__in3            "MassFlux_English1"
#define UF_UNIT_MASSFLUX_lbf_sec__ft3            "MassFlux_English2"
#define UF_UNIT_MASSFLUX_lbm__sec__in2           "MassFlux_English3"
#define UF_UNIT_MASSFLUX_lbm__sec__ft2           "MassFlux_English4"

#define UF_UNIT_MASSPERLENGTH_kg__mm             "KilogramPerMilliMeter"
#define UF_UNIT_MASSPERLENGTH_kg__m              "KilogramPerMeter"
#define UF_UNIT_MASSPERLENGTH_t__mm              "TonnePerMilliMeter"
#define UF_UNIT_MASSPERLENGTH_t__m               "TonnePerMeter"
#define UF_UNIT_MASSPERLENGTH_lbf_sec2__in2      "PoundForceSecondSquaredPerInchSquared"
#define UF_UNIT_MASSPERLENGTH_lbf_sec2__ft2      "PoundForceSecondSquaredPerFootSquared"
#define UF_UNIT_MASSPERLENGTH_lbm__in            "PoundMassPerInch"
#define UF_UNIT_MASSPERLENGTH_lbm__ft            "PoundMassPerFoot"

#define UF_UNIT_MASSPERAREA_kg__mm2              "KilogramPerMilliMeterSquared"
#define UF_UNIT_MASSPERAREA_kg__m2               "KilogramPerMeterSquared"
#define UF_UNIT_MASSPERAREA_t__mm2               "TonnePerMilliMeterSquared"
#define UF_UNIT_MASSPERAREA_t__m2                "TonnePerMeterSquared"
#define UF_UNIT_MASSPERAREA_lbf_sec2__in3        "PoundForceSecondSquaredPerInchCubed"
#define UF_UNIT_MASSPERAREA_lbf_sec2__ft3        "PoundForceSecondSquaredPerFootCubed"
#define UF_UNIT_MASSPERAREA_lbm__in2             "PoundPerInchSquared"
#define UF_UNIT_MASSPERAREA_lbm__ft2             "PoundPerFootSquared"

#define UF_UNIT_ELECTRICCURRENT_A                "Ampere"
#define UF_UNIT_ELECTRICCURRENT_mA               "MilliAmpere"
#define UF_UNIT_ELECTRICCURRENT_microA           "MicroAmpere"

#define UF_UNIT_ELECTRICALRESISTANCE_ohm         "Ohm"

#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_mm     "OhmMilliMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_m      "OhmMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_in     "OhmInch"
#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_ft     "OhmFoot"
#define UF_UNIT_ELECTRICALRESISTIVITY_Mohm_m      "MegaOhmMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_kohm_m      "KiloOhmMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_cm      "OhmCentiMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_kohm_ft     "KiloOhmFoot"
#define UF_UNIT_ELECTRICALRESISTIVITY_Mohm_ft     "MegaOhmFoot"

#define UF_UNIT_ELECTRICALCONDUCTANCE_mho        "Siemen"

#define UF_UNIT_VOLTAGE_V                        "Volt"
#define UF_UNIT_VOLTAGE_mV                       "MilliVolt"
#define UF_UNIT_VOLTAGE_microV                   "MicroVolt"

#define UF_UNIT_VOLTAGEPERTEMPERATURE_V__C      "VoltPerCelsius"
#define UF_UNIT_VOLTAGEPERTEMPERATURE_V__F      "VoltPerFahrenheit"
#define UF_UNIT_VOLTAGEPERTEMPERATURE_V__K      "VoltPerKelvin"
#define UF_UNIT_VOLTAGEPERTEMPERATURE_V__R      "VoltPerRankine"

#define UF_UNIT_DIFFUSIVITY_ft2__hr              "SquareFeetPerHour"
#define UF_UNIT_DIFFUSIVITY_ft2__s               "SquareFeetPerSecond"
#define UF_UNIT_DIFFUSIVITY_in2__s               "SquareInchPerSecond"
#define UF_UNIT_DIFFUSIVITY_m2__hr               "SquareMeterPerHour"
#define UF_UNIT_DIFFUSIVITY_mm2__s               "SquareMilliMeterPerSecond"
#define UF_UNIT_DIFFUSIVITY_cm2__s               "SquareCentiMeterPerSecond"
#define UF_UNIT_DIFFUSIVITY_m2__s                "SquareMeterPerSecond"

#define UF_UNIT_LATENTHEATPERMASS_microJ__kg     "MicroJoulePerKilogram"
#define UF_UNIT_LATENTHEATPERMASS_J__kg          "JoulePerKilogram"
#define UF_UNIT_LATENTHEATPERMASS_kJ__kg         "KiloJoulePerKilogram"
#define UF_UNIT_LATENTHEATPERMASS_BTU__lbm       "BritshThermalUnitsPerMassPound"
#define UF_UNIT_LATENTHEATPERMASS_cal__g         "CaloriePerGram"
#define UF_UNIT_LATENTHEATPERMASS_lbfin__lbm     "PoundForceInchPerMassPound"
#define UF_UNIT_LATENTHEATPERMASS_BTU_in__lbf_sec2       "BritshThermalUnitsInchPerPoundForceSecondSquared"
#define UF_UNIT_LATENTHEATPERMASS_lbfin_in__lbf_sec2     "PoundForceInchSquaredPerPoundForceSecondSquared"

#define UF_UNIT_THERMALPIDGAIN__C                "ThermalPIDGainMetric"
#define UF_UNIT_THERMALPIDGAIN__F                "ThermalPIDGainEnglish"

#define UF_UNIT_THERMALPIDNTEGRAL__C_sec         "ThermalPIDIntegralMetricSecond"
#define UF_UNIT_THERMALPIDNTEGRAL__F_sec         "ThermalPIDIntegralEnglishSecond"

#define UF_UNIT_THERMALPIDDERIVATIVE_sec__C      "ThermalPIDDerivativeMetricSecond"
#define UF_UNIT_THERMALPIDDERIVATIVE_sec__F      "ThermalPIDDerivativeEnglishSecond"

#define UF_UNIT_HEADLOSSCOEFF_mN_sec__mm3       "MilliNewtonSecondPerCubicMilliMeter"
#define UF_UNIT_HEADLOSSCOEFF_N_sec__m3         "NewtonSecondPerCubicMeter"
#define UF_UNIT_HEADLOSSCOEFF_lbf_sec__in3      "PoundForceSecondPerCubicInch"
#define UF_UNIT_HEADLOSSCOEFF_lbf_sec__ft3      "PoundForceSecondPerCubicFeet"

#define UF_UNIT_THERMALENERGYPERAREA_microJ__mm2 "ThermalEnergyPerArea_Metric1"
#define UF_UNIT_THERMALENERGYPERAREA_J__m2       "ThermalEnergyPerArea_Metric2"
#define UF_UNIT_THERMALENERGYPERAREA_J__cm2      "ThermalEnergyPerArea_Metric3"
#define UF_UNIT_THERMALENERGYPERAREA_BTU__in2    "ThermalEnergyPerArea_English1"
#define UF_UNIT_THERMALENERGYPERAREA_BTU__ft2    "ThermalEnergyPerArea_English2"
#define UF_UNIT_THERMALENERGYPERAREA_lbfin__in2  "ThermalEnergyPerArea_English3"

#define UF_UNIT_TSAIWUCOEFF_mm4__mN2             "TsaiWu_Metric1"
#define UF_UNIT_TSAIWUCOEFF_mm4__N2              "TsaiWu_Metric2"
#define UF_UNIT_TSAIWUCOEFF_m4__N2               "TsaiWu_Metric3"
#define UF_UNIT_TSAIWUCOEFF_in4_lbf2             "TsaiWu_English1"

#define UF_UNIT_MASSLENGTH_kg_mm                 "KilogramMilliMeter"
#define UF_UNIT_MASSLENGTH_lbm_in                "PoundMassInch"
#define UF_UNIT_MASSLENGTH_lbf__sec2             "PoundForceSecondSquared"

#define UF_UNIT_PERVOLUME__m3                   "PerCubicMeter"
#define UF_UNIT_PERVOLUME__cm3                  "PerCubicCentiMeter"
#define UF_UNIT_PERVOLUME__mm3                  "PerCubicMilliMeter"
#define UF_UNIT_PERVOLUME__ft3                  "PerCubicFeet"
#define UF_UNIT_PERVOLUME__in3                  "PerCubicInch"

#define UF_UNIT_MOMENTPERANGLE_mN_mm__deg       "MilliNewtonMilliMeterPerDegree"
#define UF_UNIT_MOMENTPERANGLE_mN_mm__rad       "MilliNewtonMilliMeterPerRadian"
#define UF_UNIT_MOMENTPERANGLE_N_mm__deg        "NewtonMilliMeterPerDegree"
#define UF_UNIT_MOMENTPERANGLE_N_mm__rad        "NewtonMilliMeterPerRadian"
#define UF_UNIT_MOMENTPERANGLE_N_m__deg         "NewtonMeterPerDegree"
#define UF_UNIT_MOMENTPERANGLE_N_m__rad         "NewtonMeterPerRadian"
#define UF_UNIT_MOMENTPERANGLE_lbf_in__deg      "PoundForceInchPerDegree"
#define UF_UNIT_MOMENTPERANGLE_lbf_in__rad      "PoundForceInchPerRadian"

#define UF_UNIT_WARPING_CONSTANT_in6           "InchSixth"
#define UF_UNIT_WARPING_CONSTANT_ft6           "FeetSixth"
#define UF_UNIT_WARPING_CONSTANT_mm6           "MilliMeterSixth"
#define UF_UNIT_WARPING_CONSTANT_m6            "MeterSixth"

#define UF_UNIT_STRESS_COMPLIANCE_mm2__mN                  "SquareMilliMeterPerMilliNewton"
#define UF_UNIT_STRESS_COMPLIANCE_mm2__N                   "SquareMilliMeterPerNewton"
#define UF_UNIT_STRESS_COMPLIANCE_m2__N                    "SquareMeterPerNewton"
#define UF_UNIT_STRESS_COMPLIANCE_in2__lbf                 "SquareInchPerPoundForce"
#define UF_UNIT_STRESS_COMPLIANCE_cm2__N                   "SquareCentiMeterPerNewton"
#define UF_UNIT_STRESS_COMPLIANCE_ft2__lbf                 "SquareFeetPerPoundForce"

#define UF_MEASURE_LENGTH_PER_PRESSURE_mm3__N          "MilliMeterCubedPerNewton"
#define UF_MEASURE_LENGTH_PER_PRESSURE_mm3__mN         "MilliMeterCubedPerMilliNewton"
#define UF_MEASURE_LENGTH_PER_PRESSURE_m3__N           "MeterCubedPerNewton"
#define UF_MEASURE_LENGTH_PER_PRESSURE_m3__mN          "MeterCubedPerMilliNewton"
#define UF_MEASURE_LENGTH_PER_PRESSURE_in3__lbf        "InchCubedPerPoundForce"
#define UF_MEASURE_LENGTH_PER_PRESSURE_ft3__lbf        "FeetCubedPerPoundForce"


#define UF_MEASURE_PRESSURE_PER_LENGTH_N__mm3          "NewtonPerMilliMeterCubed"
#define UF_MEASURE_PRESSURE_PER_LENGTH_N__m3           "NewtonPerMeterCubed"
#define UF_MEASURE_PRESSURE_PER_LENGTH_mN__mm3         "MilliNewtonPerMillimeterCubed"
#define UF_MEASURE_PRESSURE_PER_LENGTH_mN__m3          "MilliNewtonPerMeterCubed"
#define UF_MEASURE_PRESSURE_PER_LENGTH_lbf__in3        "PoundForcePerInchCubed"
#define UF_MEASURE_PRESSURE_PER_LENGTH_lbf__ft3        "PoundForcePerFootCubed"


#define UF_MEASURE_PRESSURE_PER_VELOCITY_N_sec__mm3      "Newton-SecondPerMilliMeterCubed"
#define UF_MEASURE_PRESSURE_PER_VELOCITY_N_sec__m3       "Newton-SecondPerMeterCubed"
#define UF_MEASURE_PRESSURE_PER_VELOCITY_mN_sec__mm3     "MilliNewton-SecondPerMilliMeterCubed"
#define UF_MEASURE_PRESSURE_PER_VELOCITY_mN_sec__m3      "MilliNewton-SecondPerMeterCubed"
#define UF_MEASURE_PRESSURE_PER_VELOCITY_lbf_sec__in3    "PoundForce-SecondPerInchCubed"
#define UF_MEASURE_PRESSURE_PER_VELOCITY_lbf_sec__ft3    "PoundForce-SecondPerFootCubed"

#ifdef __cplusplus
}
#endif

#endif  /*    UF_UNIT_TYPES__H_INCLUDED                                   */
