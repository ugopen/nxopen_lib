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

#define UF_MEASURE_NAME_UNITLESS "Unitless"
#define UF_MEASURE_NAME_LENGTH "Length"
#define UF_MEASURE_NAME_AREA "Area"
#define UF_MEASURE_NAME_VOLUME "Volume"
#define UF_MEASURE_NAME_MASS "Mass"
#define UF_MEASURE_NAME_MASS_DENSITY "Mass Density"
#define UF_MEASURE_NAME_FATIGUE_STRENGTH_COEFF "Fatigue Strength Coefficient"
#define UF_MEASURE_NAME_TIME "Time"
#define UF_MEASURE_NAME_ANGLE "Angle"
#define UF_MEASURE_NAME_VELOCITY "Velocity"
#define UF_MEASURE_NAME_ACCELERATION "Acceleration"
#define UF_MEASURE_NAME_FORCE "Force"
#define UF_MEASURE_NAME_FORCE_PER_LENGTH "Force Per Unit Length"
#define UF_MEASURE_NAME_FORCE_PER_AREA "Pressure"
#define UF_MEASURE_NAME_MOMENT "Moment"
#define UF_MEASURE_NAME_STRESS "Stress"
#define UF_MEASURE_NAME_STRAIN "Strain"
#define UF_MEASURE_NAME_STRAIN_ENERGY "Strain Energy"
#define UF_MEASURE_NAME_STRAIN_ENERGY_DENSITY "Strain Energy Density"
#define UF_MEASURE_NAME_TEMPERATURE "Temperature"
#define UF_MEASURE_NAME_HEAT_FLUX "Heat Flux"
#define UF_MEASURE_NAME_CONVECTION_COEFF "Convection Coefficient"
#define UF_MEASURE_NAME_THERMAL_CONDUCTIVITY "Thermal Conductivity"
#define UF_MEASURE_NAME_THERMAL_EXPANSION_COEFF "Thermal Expansion Coefficient"
#define UF_MEASURE_NAME_SPECIFIC_HEAT "Specific Heat"
#define UF_MEASURE_NAME_ANGULAR_VELOCITY "Angular Velocity"
#define UF_MEASURE_NAME_ANGULAR_ACCELERATION "Angular Acceleration"
#define UF_MEASURE_NAME_FATIGUE_LIFE "Fatigue Life"
#define UF_MEASURE_NAME_HEAT_FLOW "Heat Flow Rate"
#define UF_MEASURE_NAME_THERMAL_ENERGY "Thermal Energy"
#define UF_MEASURE_NAME_MASS_MOMENT_INERTIA "Mass Moment of Inertia"
#define UF_MEASURE_NAME_DYNAMIC_VISCOSITY "Dynamic Viscosity"
#define UF_MEASURE_NAME_HEAT_GENERATION "Heat Generation"
#define UF_MEASURE_NAME_CONDUCTANCE "Thermal Conductance"
#define UF_MEASURE_NAME_LENGTH_CONDUCTANCE "Conductance per Unit Length"
#define UF_MEASURE_NAME_THERMAL_RESISTANCE "Thermal Resistance"
#define UF_MEASURE_NAME_MASS_FLOW "Mass Flow Rate"
#define UF_MEASURE_NAME_VOLUME_FLOW "Volume Flow Rate"
#define UF_MEASURE_NAME_TEMPERATURE_DIFFERENCE "Temperature Difference"
#define UF_MEASURE_NAME_FREQUENCY "Frequency"
#define UF_MEASURE_NAME_COEFFICIENT_LENGTH "Coefficient per Unit Length"
#define UF_MEASURE_NAME_MOMENT_OF_INERTIA_AREA "Moment of Inertia (Area)"
#define UF_MEASURE_NAME_VISCOUS_DAMPING "Viscous Damping"
#define UF_MEASURE_NAME_ENERGY "Energy"
#define UF_MEASURE_NAME_POWER "Power"
#define UF_MEASURE_NAME_MOMENTUM "Momentum"
#define UF_MEASURE_NAME_TEMPERATURE_GRADIENT "Temperature Gradient"
#define UF_MEASURE_NAME_ENERGY_PER_MASS "Energy per Unit Mass"
#define UF_MEASURE_NAME_DISSIPATION_RATE_OF_ENERGY_PER_MASS "Dissipation Rate of Energy per Unit Mass"
#define UF_MEASURE_NAME_MASS_FLUX "Mass Flux"
#define UF_MEASURE_NAME_MASS_PER_LENGTH "Mass per Unit Length"
#define UF_MEASURE_NAME_MASS_PER_AREA "Mass per Unit Area"
#define UF_MEASURE_NAME_ELECTRIC_CURRENT "Electric Current"
#define UF_MEASURE_NAME_ELECTRICAL_RESISTANCE "Electrical Resistance"
#define UF_MEASURE_NAME_ELECTRICAL_RESISTIVITY "Electrical Resistivity"
#define UF_MEASURE_NAME_ELECTRICAL_CONDUCTANCE "Electrical Conductance"
#define UF_MEASURE_NAME_VOLTAGE "Voltage"
#define UF_MEASURE_NAME_VOLTAGE_PER_TEMPERATURE "Voltage per Temperature"
#define UF_MEASURE_NAME_DIFFUSIVITY "Diffusivity"
#define UF_MEASURE_NAME_LATENT_HEAT_PER_MASS "Latent Heat per Mass"
#define UF_MEASURE_NAME_THERMAL_ENERGY_PER_AREA "Thermal Energy per Area"
#define UF_MEASURE_NAME_THERMAL_PID_GAIN "Thermal PID Gain"
#define UF_MEASURE_NAME_THERMAL_PID_INTEGRAL "Thermal PID Integral Term Constant"
#define UF_MEASURE_NAME_THERMAL_PID_DERIVATIVE "Thermal PID Derivative Term Constant"
#define UF_MEASURE_NAME_HEADLOSS_COEFF "Head Loss Coefficient"
#define UF_MEASURE_NAME_TSAI_WU_COEFF "Tsai-Wu Coefficient"
#define UF_MEASURE_NAME_MASS_LENGTH "Mass Length"
#define UF_MEASURE_NAME_PER_VOLUME "Per Volume"
#define UF_MEASURE_NAME_WARPING_CONSTANT "Warping constant"
#define UF_MEASURE_NAME_STRESS_COMPLIANCE "Stress Compliance"
#define UF_MEASURE_NAME_LENGTH_PER_PRESSURE "Length Per Unit Pressure"
#define UF_MEASURE_NAME_PRESSURE_PER_LENGTH "Pressure Per Unit Length"
#define UF_MEASURE_NAME_PRESSURE_PER_VELOCITY "Pressure Per Unit Velocity"
#define UF_MEASURE_NAME_MOMENT_PER_ANGLE "Moment Per Angle"
#define UF_MEASURE_NAME_COEFFICIENT_PER_TIME "Coefficient Per Unit Time"
#define UF_MEASURE_NAME_ANGULAR_MOMENTUM_PER_ANGLE "Angular Momentum Per Unit Angle"
#define UF_MEASURE_NAME_THERMAL_CAPACITANCE "Thermal Capacitance"
#define UF_MEASURE_NAME_INDUCTANCE "Inductance"
#define UF_MEASURE_NAME_VOLTAGE_PER_ANGULAR_VELOCITY "Voltage per Angular Velocity"
#define UF_MEASURE_NAME_PER_AREA "Per Area"
#define UF_MEASURE_NAME_TEMPERATURE_CHANGE_RATE "Temperature Change Rate"
#define UF_MEASURE_NAME_JERK "Jerk"
#define UF_MEASURE_NAME_ANGULAR_JERK "Angular Jerk"
#define UF_MEASURE_NAME_MAGNETIC_FIELD_STRENGTH "Magnetic Field Strength"
#define UF_MEASURE_NAME_MAGNETIC_FLUX_DENSITY "Magnetic Flux Density"
#define UF_MEASURE_NAME_ANGULAR_MOMENTUM "Angular Momentum"
#define UF_MEASURE_NAME_VELOCITY_PER_PRESSURE "Velocity Per Pressure"
#define UF_MEASURE_NAME_COEFFICIENT_PER_TIME_SQUARED "Coefficient Per Unit Time Squared"
#define UF_MEASURE_NAME_COEFFICIENT_PER_TIME_CUBED "Coefficient Per Unit Time Cubed"
#define UF_MEASURE_NAME_FLOW_RESISTIVITY "Static Flow Resistivity"
#define UF_MEASURE_NAME_CURRENT_DENSITY "Current Density"
#define UF_MEASURE_NAME_FORCE_PER_ANGLE "Force Per Unit Angle"
#define UF_MEASURE_NAME_LENGTH_PER_ANGLE "Length Per Angle"
#define UF_MEASURE_NAME_CURRENT_DENSITY_AREA "Current Density Area"
#define UF_MEASURE_NAME_ELECTRIC_FIELD_STRENGTH "ElectricFieldStrength"
#define UF_MEASURE_NAME_ELECTRIC_FLUX_DENSITY "Electric Flux Density"
#define UF_MEASURE_NAME_ELECTRIC_CHARGE "Electric Charge"
#define UF_MEASURE_NAME_LUMINOUS_INTENSITY "Luminous Intensity"
#define UF_MEASURE_NAME_LUMINOUS_FLUX "Luminous Flux"
#define UF_MEASURE_NAME_LUMINANCE "Luminance"
#define UF_MEASURE_NAME_ILLUMINANCE "Illuminance"
#define UF_MEASURE_NAME_AMOUNT_OF_SUBSTANCE "Amount Of Substance"
#define UF_MEASURE_NAME_MOLALITY "Molality"
#define UF_MEASURE_NAME_MOLAR_CONCENTRATION "Molar Concentration"
#define UF_MEASURE_NAME_PER_FREQUENCY "Per Frequency"
#define UF_MEASURE_NAME_DIFFUSION_RESISTANCE "Diffusion Resistance"
#define UF_MEASURE_NAME_TRANSMISSION_LOSS "Transmission Loss"
#define UF_MEASURE_NAME_ELECTRICAL_CONDUCTIVITY "Electrical Conductivity"
#define UF_MEASURE_NAME_POWER_TO_MASS_RATIO "Power to Mass Ratio"
#define UF_MEASURE_NAME_ELECTRICAL_CAPACITANCE "Electrical Capacitance"
#define UF_MEASURE_NAME_FREQUENCY_SQUARED "Frequency Squared"
#define UF_MEASURE_NAME_PER_ANGLE "Per Angle"
#define UF_MEASURE_NAME_PER_ANGLE_SQUARED "Per Angle Squared"
#define UF_MEASURE_NAME_FREQUENCY_CUBED "Frequency Cubed"
#define UF_MEASURE_NAME_MASS_MOMENT_INERTIA_PER_ANGLE "Mass Moment of Inertia Per Angle"
#define UF_MEASURE_NAME_MAGNETIC_CONDUCTIVITY "Magnetic Conductivity"
#define UF_MEASURE_NAME_MAGNETIC_FLUX "Magnetic Flux"
#define UF_MEASURE_NAME_MAGNETIC_VECTOR_POTENTIAL "Magnetic Vector Potential"
#define UF_MEASURE_NAME_VOLUME_CHARGE_DENSITY "Volume Charge Density"
#define UF_MEASURE_NAME_APPARENT_POWER "Apparent Power"
#define UF_MEASURE_NAME_ENERGY_CONTENT "Energy Content"
#define UF_MEASURE_NAME_VOLUMETRIC_STRAIN "Volumetric Strain"
#define UF_MEASURE_NAME_VOLUME_ACCELERATION "Volume Acceleration"
 
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
    UF_MEASURE_COEFFICIENT_PER_TIME,
    UF_MEASURE_ANGULAR_MOMENTUM_PER_ANGLE,
    UF_MEASURE_THERMAL_CAPACITANCE,
    UF_MEASURE_INDUCTANCE,
    UF_MEASURE_VOLTAGE_PER_ANGULAR_VELOCITY,
    UF_MEASURE_PER_AREA,
    UF_MEASURE_TEMPERATURE_CHANGE_RATE,
    UF_MEASURE_JERK,
    UF_MEASURE_ANGULAR_JERK,
    UF_MEASURE_MAGNETIC_FIELD_STRENGTH,
    UF_MEASURE_MAGNETIC_FLUX_DENSITY,
    UF_MEASURE_ANGULAR_MOMENTUM,
    UF_MEASURE_VELOCITY_PER_PRESSURE,
    UF_MEASURE_COEFFICIENT_PER_TIME_SQUARED,
    UF_MEASURE_COEFFICIENT_PER_TIME_CUBED,
    UF_MEASURE_FLOW_RESISTIVITY,
    UF_MEASURE_CURRENT_DENSITY,
    UF_MEASURE_FORCE_PER_ANGLE,      /* Force per unit angle */
    UF_MEASURE_LENGTH_PER_ANGLE,
    UF_MEASURE_CURRENT_DENSITY_AREA,
    UF_MEASURE_ELECTRIC_FIELD_STRENGTH,
    UF_MEASURE_ELECTRIC_FLUX_DENSITY,
    UF_MEASURE_ELECTRIC_CHARGE,
    UF_MEASURE_LUMINOUS_INTENSITY,
    UF_MEASURE_LUMINOUS_FLUX,
    UF_MEASURE_LUMINANCE,
    UF_MEASURE_ILLUMINANCE,
    UF_MEASURE_AMOUNT_OF_SUBSTANCE,
    UF_MEASURE_MOLALITY,
    UF_MEASURE_MOLAR_CONCENTRATION,
    UF_MEASURE_PER_FREQUENCY,
    UF_MEASURE_DIFFUSION_RESISTANCE,
    UF_MEASURE_TRANSMISSION_LOSS,
    UF_MEASURE_ELECTRICAL_CONDUCTIVITY,
    UF_MEASURE_POWER_TO_MASS_RATIO, 
    UF_MEASURE_ELECTRICAL_CAPACITANCE,
    UF_MEASURE_FREQUENCY_SQUARED,
    UF_MEASURE_PER_ANGLE,
    UF_MEASURE_PER_ANGLE_SQUARED,
    UF_MEASURE_FREQUENCY_CUBED,
    UF_MEASURE_MASS_MOMENT_INERTIA_PER_ANGLE,
    UF_MEASURE_MAGNETIC_CONDUCTIVITY,
    UF_MEASURE_MAGNETIC_FLUX, 
    UF_MEASURE_MAGNETIC_VECTOR_POTENTIAL, 
    UF_MEASURE_VOLUME_CHARGE_DENSITY,
    UF_MEASURE_APPARENT_POWER,
    UF_MEASURE_ENERGY_CONTENT,
    UF_MEASURE_VOLUMETRIC_STRAIN,
    UF_MEASURE_VOLUME_ACCELERATION,
    UF_MEASURE_COUNT,

    UF_MEASURE_CUSTOM = 5000
    /* The UF_MEASURE_CUSTOM here is for user-defined measures, which cannot be identified by enumerations.
       If/when your application requires the use of such measures, it will need to handle them separately.
    */
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
#define UF_UNIT_MASS_Mg                         "MegaGram"
#define UF_UNIT_MASS_mg                         "MilliGram"
#define UF_UNIT_MASS_t                          "Tonne"
#define UF_UNIT_MASS_slug                       "Slug"
#define UF_UNIT_MASS_lbf_sec2__in               "PoundSecondsSquaredPerInch"
#define UF_UNIT_MASS_lbm                        "PoundMass"
#define UF_UNIT_MASS_oz                         "Ounce"
#define UF_UNIT_MASS_kgf_sec2__m                "KilogramForceSecondsSquaredPerMeter"
#define UF_UNIT_MASS_kgf_sec2__mm               "KilogramForceSecondsSquaredPerMilliMeter"
#define UF_UNIT_MASS_kgf_sec2__cm               "KilogramForceSecondsSquaredPerCentiMeter"

/************************************************************************************
* 
* UF_UNIT_MASS_lbfsec__in2 should have been UF_UNIT_MASS_lbf_sec2__in.
*  The correct #define was added in NX9.
*  The old #define remains so that changes are not required to
*  existing customer programs.
************************************************************************************/
#define UF_UNIT_MASS_lbfsec__in2                "PoundSecondsSquaredPerInch" /* remains here for legacy only purposes */

#define UF_UNIT_MASSDENSITY_lbm__ft3            "PoundMassperCubicFoot"
#define UF_UNIT_MASSDENSITY_Mg__mm3             "MegaGramPerCubicMilliMeter"
#define UF_UNIT_MASSDENSITY_g__mm3              "GramPerCubicMilliMeter"
#define UF_UNIT_MASSDENSITY_g__cm3              "GramPerCubicCentiMeter"
#define UF_UNIT_MASSDENSITY_kg__m3              "KilogramPerCubicMeter"
#define UF_UNIT_MASSDENSITY_kg__mm3             "KilogramPerCubicMilliMeter"
#define UF_UNIT_MASSDENSITY_t__m3               "TonnePerCubicMeter"
#define UF_UNIT_MASSDENSITY_t__mm3              "TonnePerCubicMilliMeter"
#define UF_UNIT_MASSDENSITY_lbfsec2__in4        "PoundsSecondSquaredPerInchFourth"
#define UF_UNIT_MASSDENSITY_slug__ft3           "SlugsPerCubicFeet"
#define UF_UNIT_MASSDENSITY_lbm__in3            "PoundMassperCubicInch"
#define UF_UNIT_MASSDENSITY_g__l                "GramPerLiter"
#define UF_UNIT_MASSDENSITY_g__m3               "GramPerCubicMeter"
#define UF_UNIT_MASSDENSITY_kg__l               "KiloGramPerLiter"

#define UF_UNIT_FATIGUESTR_COEFF_mN__mm2        "MilliNewtonPerSquareMilliMeter"
#define UF_UNIT_FATIGUESTR_COEFF_N__mm2         "NewtonPerSquareMilliMeter"
#define UF_UNIT_FATIGUESTR_COEFF_N__m2          "Pascals"
#define UF_UNIT_FATIGUESTR_COEFF_lbf__in2       "PoundForcePerSquareInch"

#define UF_UNIT_TIME_sec                        "Second"
#define UF_UNIT_TIME_min                        "Minute"
#define UF_UNIT_TIME_hr                         "Hour"
#define UF_UNIT_TIME_millisec                   "millisecond"
#define UF_UNIT_TIME_microsec                   "microsecond"
#define UF_UNIT_TIME_day                        "Day"

#define UF_UNIT_ANGLE_rad                       "Radian"
#define UF_UNIT_ANGLE_pi_rad                    "PiRadian"
#define UF_UNIT_ANGLE_deg                       "Degrees"
#define UF_UNIT_ANGLE_rev                       "Revs"

#define UF_UNIT_VELOCITY_m__sec                 "MeterPerSecond"
#define UF_UNIT_VELOCITY_mm__sec                "MilliMeterPerSecond"
#define UF_UNIT_VELOCITY_in__sec                "InchPerSecond"
#define UF_UNIT_VELOCITY_ft__sec                "FeetPerSecond"
#define UF_UNIT_VELOCITY_ft__min                "FeetPerMinute"
#define UF_UNIT_VELOCITY_km__hr                 "KiloMeterPerHour"
#define UF_UNIT_VELOCITY_cm__sec                "CentiMeterPerSecond"
#define UF_UNIT_VELOCITY_mi__hr                 "MilePerHour"

#define UF_UNIT_ACCELERATION_m__sec2            "MeterPerSquareSecond"
#define UF_UNIT_ACCELERATION_mm__sec2           "MilliMeterPerSquareSecond"
#define UF_UNIT_ACCELERATION_cm__sec2           "CentiMeterPerSquareSecond"
#define UF_UNIT_ACCELERATION_in__sec2           "InchPerSquareSecond"
#define UF_UNIT_ACCELERATION_ft__sec2           "FeetPerSquareSecond"
#define UF_UNIT_ACCELERATION_g                  "g's"

#define UF_UNIT_FORCE_mN                        "MilliNewton"
#define UF_UNIT_FORCE_N                         "Newton"
#define UF_UNIT_FORCE_lbf                       "PoundForce"
#define UF_UNIT_FORCE_Poundal                   "Poundal"
#define UF_UNIT_FORCE_kgf                       "kgf"
#define UF_UNIT_FORCE_cN                        "CentiNewton"
#define UF_UNIT_FORCE_kN                        "KiloNewton"
#define UF_UNIT_FORCE_dyn                       "Dyne"
#define UF_UNIT_FORCE_microN                    "MicroNewton"

#define UF_UNIT_FORCE_PER_ANGLE_mN__deg         "MilliNewtonPerDeg"
#define UF_UNIT_FORCE_PER_ANGLE_N__deg          "NewtonPerDeg"
#define UF_UNIT_FORCE_PER_ANGLE_lbf__deg        "PoundForcePerDeg"
#define UF_UNIT_FORCE_PER_ANGLE_Poundal__deg    "PoundalPerDeg"
#define UF_UNIT_FORCE_PER_ANGLE_kgf__deg        "KgfPerDeg"
#define UF_UNIT_FORCE_PER_ANGLE_cN__deg         "CentiNewtonPerDeg"
#define UF_UNIT_FORCE_PER_ANGLE_mN__rad         "MilliNewtonPerRad"
#define UF_UNIT_FORCE_PER_ANGLE_N__rad          "NewtonPerRad"
#define UF_UNIT_FORCE_PER_ANGLE_lbf__rad        "PoundForcePerRad"
#define UF_UNIT_FORCE_PER_ANGLE_Poundal__rad    "PoundalPerRad"
#define UF_UNIT_FORCE_PER_ANGLE_kgf__rad        "KgfPerRad"
#define UF_UNIT_FORCE_PER_ANGLE_cN__rad         "CentiNewtonPerRad"

#define UF_UNIT_PRESSUREONEDGE_mN__mm           "MilliNewtonsPerMilliMeter"
#define UF_UNIT_PRESSUREONEDGE_N__mm            "NewtonsPerMilliMeter"
#define UF_UNIT_PRESSUREONEDGE_N__m             "NewtonPerMeter"
#define UF_UNIT_PRESSUREONEDGE_cN__cm           "CentiNewtonPerCentiMeter"
#define UF_UNIT_PRESSUREONEDGE_kgf__m           "KilogramForcePerMeter"
#define UF_UNIT_PRESSUREONEDGE_kgf__cm          "KilogramForcePerCentiMeter"
#define UF_UNIT_PRESSUREONEDGE_kgf__mm          "KilogramForcePerMilliMeter"
#define UF_UNIT_PRESSUREONEDGE_lbf__in          "PoundForcePerInch"
#define UF_UNIT_PRESSUREONEDGE_lbf__ft          "PoundForcePerFoot"
#define UF_UNIT_PRESSUREONEDGE_J__m2            "JoulePerMeterSquared"

#define UF_UNIT_PRESSURE_mN__mm2                "PressureMilliNewtonPerSquareMilliMeter"
#define UF_UNIT_PRESSURE_N__mm2                 "PressureNewtonPerSquareMilliMeter"
#define UF_UNIT_PRESSURE_N__m2                  "PressurePascals"
#define UF_UNIT_PRESSURE_cN__cm2                "PressureCentiNewtonPerSquareCentiMeter"
#define UF_UNIT_PRESSURE_kgf__m2                "PressureKilogramForcePerSquareMeter"
#define UF_UNIT_PRESSURE_kgf__cm2               "PressureKilogramForcePerSquareCentiMeter"
#define UF_UNIT_PRESSURE_kgf__mm2               "PressureKilogramForcePerSquareMilliMeter"
#define UF_UNIT_PRESSURE_lbf__in2               "PressurePoundForcePerSquareInch"
#define UF_UNIT_PRESSURE_lbf__ft2               "PoundForcePerFeetSquared"
#define UF_UNIT_PRESSURE_bar                    "Bar"
#define UF_UNIT_PRESSURE_atmosphere             "Atmosphere"
#define UF_UNIT_PRESSURE_N__cm2                 "NewtonPerSquareCentiMeter"
#define UF_UNIT_PRESSURE_mm_H2O                 "MilliMeterOfWater"
#define UF_UNIT_PRESSURE_mm_Hg                  "MilliMeterOfMercury"
#define UF_UNIT_PRESSURE_in_H2O                 "InchOfWater"
#define UF_UNIT_PRESSURE_in_Hg                  "InchOfMercury"
#define UF_UNIT_PRESSURE_pdl__ft2               "PressurePoundalPerSquareFoot"
#define UF_UNIT_PRESSURE_mbar                   "PressureMillibar"
#define UF_UNIT_PRESSURE_mPa                    "PressureMilliPascal"
#define UF_UNIT_PRESSURE_hPa                    "PressureHectoPascal"

#define UF_UNIT_MOMENT_mNmm                     "MilliNewtonMilliMeter"
#define UF_UNIT_MOMENT_Nmm                      "NewtonMilliMeter"
#define UF_UNIT_MOMENT_Nm                       "NewtonMeter"
#define UF_UNIT_MOMENT_kNm                      "KiloNewtonMeter"
#define UF_UNIT_MOMENT_cNcm                     "CentiNewtonCentiMeter"
#define UF_UNIT_MOMENT_kgfm                     "KilogramForceMeter"
#define UF_UNIT_MOMENT_kgfmm                    "KilogramForceMilliMeter"
#define UF_UNIT_MOMENT_kgfcm                    "KilogramForceCentiMeter"
#define UF_UNIT_MOMENT_lbfin                    "PoundForceInch"
#define UF_UNIT_MOMENT_lbfft                    "PoundForceFeet"
#define UF_UNIT_MOMENT_pdlft                    "PoundalFeet"
#define UF_UNIT_MOMENT_dyncm                    "DyneCentiMeter"

#define UF_UNIT_STRESS_mN__mm2                  "StressMilliNewtonPerSquareMilliMeter"
#define UF_UNIT_STRESS_N__mm2                   "StressNewtonPerSquareMilliMeter"
#define UF_UNIT_STRESS_N__m2                    "StressPascals"
#define UF_UNIT_STRESS_N__cm2                   "StressNewtonPerSquareCentiMeter"
#define UF_UNIT_STRESS_cN__cm2                  "StressCentiNewtonPerSquareCentiMeter"
#define UF_UNIT_STRESS_kgf__m2                  "StressKilogramForcePerSquareMeter"
#define UF_UNIT_STRESS_kgf__mm2                 "StressKilogramForcePerSquareMilliMeter"
#define UF_UNIT_STRESS_kgf__cm2                 "StressKilogramForcePerSquareCentiMeter"
#define UF_UNIT_STRESS_lbf__in2                 "StressPoundForcePerSquareInch"
#define UF_UNIT_STRESS_lbf__ft2                 "PoundForcePerSquareFeet"

#define UF_UNIT_STRAIN_mm__mm                   "Strain_Metric1"
#define UF_UNIT_STRAIN_m__m                     "Strain_MeterPerMeter"
#define UF_UNIT_STRAIN_cm__cm                   "Strain_CentiMeterPerCentiMeter"
#define UF_UNIT_STRAIN_in__in                   "Strain_English1"

#define UF_UNIT_STRAINENERGY_mNmm               "StrainEnergy_Metric1"
#define UF_UNIT_STRAINENERGY_Nmm                "StrainEnergy_Metric2"
#define UF_UNIT_STRAINENERGY_Nm                 "StrainEnergy_Metric3"
#define UF_UNIT_STRAINENERGY_cNcm               "StrainEnergy_Metric4"
#define UF_UNIT_STRAINENERGY_kgfm               "StrainEnergy_Metric5"
#define UF_UNIT_STRAINENERGY_kgfmm              "StrainEnergy_Metric6"
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
#define UF_UNIT_HEATFLOW_mWatt                  "HeatFlow_Metric3"
#define UF_UNIT_HEATFLOW_BTU__sec               "HeatFlow_English1"
#define UF_UNIT_HEATFLOW_lbfin__sec             "HeatFlow_English2"
#define UF_UNIT_HEATFLOW_BTU__hr                "HeatFlow_BTUPerHour"
#define UF_UNIT_HEATFLOW_BTU__min               "HeatFlow_BTUPerMinute"
#define UF_UNIT_HEATFLOW_kw                     "HeatFlow_KiloWatt"
#define UF_UNIT_HEATFLOW_lbfft__sec             "HeatFlow_PoundForceFeetPerSecond"
#define UF_UNIT_HEATFLOW_hp                     "HeatFlow_Hp"

#define UF_UNIT_THERMALENERGY_microJ            "ThermalEnergy_Metric1"
#define UF_UNIT_THERMALENERGY_J                 "ThermalEnergy_Metric2"
#define UF_UNIT_THERMALENERGY_mJ                "ThermalEnergy_Metric3"
#define UF_UNIT_THERMALENERGY_kgfm              "ThermalEnergy_Metric4"
#define UF_UNIT_THERMALENERGY_kgfmm             "ThermalEnergy_Metric5"
#define UF_UNIT_THERMALENERGY_cNcm              "ThermalEnergy_Metric6"

/************************************************************************************
* 
* UF_UNIT_THERMALENERGY_cJcm should have been UF_UNIT_THERMALENERGY_cNcm.
*  The correct #define was added in NX11.
*  The old #define remains so that changes are not required to
*  existing customer programs.
************************************************************************************/
#define UF_UNIT_THERMALENERGY_cJcm              "ThermalEnergy_Metric6" /* remains here for legacy only purposes */
#define UF_UNIT_THERMALENERGY_erg               "ThermalEnergy_Erg"

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
#define UF_UNIT_CONVECTION_COEFF_mWatt__mm2__degK           "ConvectionCoefficient_Metric7"
#define UF_UNIT_CONVECTION_COEFF_BTU__sec__ft2__degF        "ConvectionCoefficient_English2"
#define UF_UNIT_CONVECTION_COEFF_BTU__hr__in2__degF         "ConvectionCoefficient_English3"
#define UF_UNIT_CONVECTION_COEFF_BTU__hr__ft2__degF         "ConvectionCoefficient_English4"
#define UF_UNIT_CONVECTION_COEFF_lbfin__sec__in2__degF      "ConvectionCoefficient_English5"
#define UF_UNIT_CONVECTION_COEFF_Watt__m2__degK             "ConvectionCoefficient_Metric8"

#define UF_UNIT_THERMALCONDUCTIVITY_microWatt__mm__degC     "ThermalConductivity_Metric1"
#define UF_UNIT_THERMALCONDUCTIVITY_Watt__mm__degC          "ThermalConductivity_Metric2"
#define UF_UNIT_THERMALCONDUCTIVITY_Watt__m__degK           "ThermalConductivity_Metric3"
#define UF_UNIT_THERMALCONDUCTIVITY_BTU__sec__in__degF      "ThermalConductivity_English1"
#define UF_UNIT_THERMALCONDUCTIVITY_BTU__hr__ft__degF       "ThermalConductivity_English2"
#define UF_UNIT_THERMALCONDUCTIVITYE_Watt__m__degC          "ThermalConductivity_Metric4"
#define UF_UNIT_THERMALCONDUCTIVITY_BTU__hr__in__degF       "ThermalConductivity_English3"
#define UF_UNIT_THERMALCONDUCTIVITY_mWatt__mm__degC         "ThermalConductivity_Metric5"
#define UF_UNIT_THERMALCONDUCTIVITY_Watt__cm__degC          "ThermalConductivity_Metric6"
#define UF_UNIT_THERMALCONDUCTIVITY_mWatt__mm__degK         "ThermalConductivity_Metric7"
#define UF_UNIT_THERMALCONDUCTIVITY_BTU__sec__ft__degF      "ThermalConductivity_English4"
#define UF_UNIT_THERMALCONDUCTIVITY_lbfin__sec__in__degF    "ThermalConductivity_English5"

#define UF_UNIT_THERMALEXPANSION_COEFF___degC   "ThermalExpansion_Metric1"
#define UF_UNIT_THERMALEXPANSION_COEFF___degF   "ThermalExpansion_English1"
#define UF_UNIT_THERMALEXPANSION_COEFF___degK   "ThermalExpansion_Metric2"

#define UF_UNIT_SPECIFICHEAT_microJ__kg__degK               "SpecificHeat_Metric1"
#define UF_UNIT_SPECIFICHEAT_J__kg__degK                    "SpecificHeat_Metric2"
#define UF_UNIT_SPECIFICHEAT_kJ__kg__degK                   "SpecificHeat_Metric3"
#define UF_UNIT_SPECIFICHEAT_mJ__Mg__degK                   "SpecificHeat_Metric4"
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
#define UF_UNIT_MASSMOMENTINERTIA_lbmft2        "PoundMassFeetSquared"
#define UF_UNIT_MASSMOMENTINERTIA_gmm2          "GramMilliMeterSquared"
#define UF_UNIT_MASSMOMENTINERTIA_gcm2          "GramCentiMeterSquared"
#define UF_UNIT_MASSMOMENTINERTIA_kgm2          "KilogramMeterSquared"
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
#define UF_UNIT_DYNAMICVISC_mPa_sec             "DynamicViscosity_MilliPascalSecond"
#define UF_UNIT_DYNAMICVISC_Pa_sec              "DynamicViscosity_PascalSecond"

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
#define UF_UNIT_CONDUCTANCE_Watt__degK          "ThermalConductance_Metric4"

#define UF_UNIT_LENGTHCONDUCTANCE_microWatt__mm__degC     "LengthConductance_Metric1"
#define UF_UNIT_LENGTHCONDUCTANCE_Watt__mm__degC          "LengthConductance_Metric2"
#define UF_UNIT_LENGTHCONDUCTANCE_Watt__m__degC           "LengthConductance_Metric3"
#define UF_UNIT_LENGTHCONDUCTANCE_BTU__sec__in__degF      "LengthConductance_English1"
#define UF_UNIT_LENGTHCONDUCTANCE_BTU__hr__in__degF       "LengthConductance_English2"
#define UF_UNIT_LENGTHCONDUCTANCE_BTU__hr__ft__degF       "LengthConductance_English3"
#define UF_UNIT_LENGTHCONDUCTANCE_mWatt__mm__degC         "LengthConductance_Metric4"
#define UF_UNIT_LENGTHCONDUCTANCE_Watt__cm__degC          "LengthConductance_Metric5"
#define UF_UNIT_LENGTHCONDUCTANCE_BTU__sec__ft__degF      "LengthConductance_English4"
#define UF_UNIT_LENGTHCONDUCTANCE_lbfin__sec__in__degF    "LengthConductance_English5"
#define UF_UNIT_LENGTHCONDUCTANCE_Watt__m__degK           "LengthConductance_Metric6"

#define UF_UNIT_THERMALRESISTANCE_degC__microWatt    "ThermalResistance_Metric1"
#define UF_UNIT_THERMALRESISTANCE_degC__Watt         "ThermalResistance_Metric2"
#define UF_UNIT_THERMALRESISTANCE_degF__sec__BTU     "ThermalResistance_English1"
#define UF_UNIT_THERMALRESISTANCE_degF__hr__BTU      "ThermalResistance_English2"
#define UF_UNIT_THERMALRESISTANCE_degC__mWatt        "ThermalResistance_Metric3"
#define UF_UNIT_THERMALRESISTANCE_degF__min__BTU     "ThermalResistance_English3"
#define UF_UNIT_THERMALRESISTANCE_degF__sec__lbfin   "ThermalResistance_English4"
#define UF_UNIT_THERMALRESISTANCE_degK__Watt         "ThermalResistance_Metric4"

#define UF_UNIT_MASSFLOW_Mg__sec                "MegagramPerSecond"
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
#define UF_UNIT_VOLUMEFLOW_ml__sec              "MilliLiterPerSecond"
#define UF_UNIT_VOLUMEFLOW_dm3__min             "CubicDeciMeterPerMinute"

#define UF_UNIT_VOLUMEACCELERATION_mm3__sec2    "CubicMilliMeterPerSecondSquared"
#define UF_UNIT_VOLUMEACCELERATION_m3__sec2     "CubicMeterPerSecondSquared"
#define UF_UNIT_VOLUMEACCELERATION_m3__hr2      "CubicMeterPerHourSquared"
#define UF_UNIT_VOLUMEACCELERATION_in3__sec2    "CubicInchPerSecondSquared"
#define UF_UNIT_VOLUMEACCELERATION_ft3__min2    "CubicFeetPerMinuteSquared"
#define UF_UNIT_VOLUMEACCELERATION_l__sec2      "LiterPerSecondSquared"
#define UF_UNIT_VOLUMEACCELERATION_l__min2      "LiterPerMinuteSquared"
#define UF_UNIT_VOLUMEACCELERATION_l__hr2       "LiterPerHourSquared"
#define UF_UNIT_VOLUMEACCELERATION_cm3__sec2    "CubicCentiMeterPerSecondSquared"
#define UF_UNIT_VOLUMEACCELERATION_m3__min2     "CubicMeterPerMinuteSquared"
#define UF_UNIT_VOLUMEACCELERATION_ft3__sec2    "CubicFeetPerSecondSquared"
#define UF_UNIT_VOLUMEACCELERATION_ft3__hr2     "CubicFeetPerHourSquared"

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
#define UF_UNIT_COEFFICIENTLENGTH_cm            "CoefficientPerCentiMeter"
#define UF_UNIT_COEFFICIENTLENGTH_in            "CoefficientPerInch"
#define UF_UNIT_COEFFICIENTLENGTH_ft            "CoefficientPerFoot"
#define UF_UNIT_COEFFICIENTLENGTH_micron        "CoefficientPerMicron"
#define UF_UNIT_COEFFICIENTLENGTH_nm            "CoefficientPerNanoMeter"
#define UF_UNIT_COEFFICIENTLENGTH_angstrom      "CoefficientPerAngstrom"
#define UF_UNIT_COEFFICIENTLENGTH_km            "CoefficientPerKiloMeter"
#define UF_UNIT_COEFFICIENTLENGTH_mi            "CoefficientPerMile"

#define UF_UNIT_VISCOUS_DAMPING_lbm__sec        "ViscousDampingPoundMassPerSecond"
#define UF_UNIT_VISCOUS_DAMPING_lbfsec__in      "PoundForceSecondPerInch"
#define UF_UNIT_VISCOUS_DAMPING_kg__sec         "ViscousDampingKilogramPerSecond"
#define UF_UNIT_VISCOUS_DAMPING_N_sec__m        "NewtonSecondPerMeter"
#define UF_UNIT_VISCOUS_DAMPING_N_sec__mm       "NewtonSecondPerMilliMeter"
#define UF_UNIT_VISCOUS_DAMPING_mN_sec__mm      "MilliNewtonSecondPerMilliMeter"

#define UF_UNIT_ENERGY_lbm_ft2__sec2            "PoundMassFeetSquaredPerSecondSquared"
#define UF_UNIT_ENERGY_lbfin                    "EnergyPoundForceInch"
#define UF_UNIT_ENERGY_microJ                   "MicroJoule"
#define UF_UNIT_ENERGY_j                        "Joule"
#define UF_UNIT_ENERGY_btu                      "Btu"
#define UF_UNIT_ENERGY_mj                       "MilliJoule"
#define UF_UNIT_ENERGY_erg                      "Erg"
#define UF_UNIT_ENERGY_lbfft                    "EnergyPoundForceFoot"

#define UF_UNIT_POWER_lbm_ft2__sec3             "PoundMassFeetSquaredPerSecondCubed"
#define UF_UNIT_POWER_lbfin__sec                "PoundForceInchPerSecond"
#define UF_UNIT_POWER_microW                    "MicroWatt"
#define UF_UNIT_POWER_w                         "Watt"
#define UF_UNIT_POWER_kw                        "KiloWatt"
#define UF_UNIT_POWER_mw                        "MilliWatt"
#define UF_UNIT_POWER_Mw                        "MegaWatt"
#define UF_UNIT_POWER_BTU__hr                   "BTUPerHour"
#define UF_UNIT_POWER_BTU__min                  "BTUPerMinute"
#define UF_UNIT_POWER_BTU__sec                  "BTUPerSecond"
#define UF_UNIT_POWER_lbfft__sec                "PoundForceFeetPerSecond"
#define UF_UNIT_POWER_hp                        "Hp"

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
#define UF_UNIT_MASSPERLENGTH_g__cm              "GramsPerCentimeter"

#define UF_UNIT_MASSPERAREA_kg__mm2              "KilogramPerMilliMeterSquared"
#define UF_UNIT_MASSPERAREA_kg__m2               "KilogramPerMeterSquared"
#define UF_UNIT_MASSPERAREA_g__cm2               "GramPerCentiMeterSquared"
#define UF_UNIT_MASSPERAREA_g__mm2               "GramPerMilliMeterSquared"
#define UF_UNIT_MASSPERAREA_t__mm2               "TonnePerMilliMeterSquared"
#define UF_UNIT_MASSPERAREA_t__m2                "TonnePerMeterSquared"
#define UF_UNIT_MASSPERAREA_lbf_sec2__in3        "PoundForceSecondSquaredPerInchCubed"
#define UF_UNIT_MASSPERAREA_lbf_sec2__ft3        "PoundForceSecondSquaredPerFootCubed"
#define UF_UNIT_MASSPERAREA_lbm__in2             "PoundPerInchSquared"
#define UF_UNIT_MASSPERAREA_lbm__ft2             "PoundPerFootSquared"

#define UF_UNIT_ELECTRICCURRENT_A                "Ampere"
#define UF_UNIT_ELECTRICCURRENT_mA               "MilliAmpere"
#define UF_UNIT_ELECTRICCURRENT_kA               "KiloAmpere"
#define UF_UNIT_ELECTRICCURRENT_microA           "MicroAmpere"

#define UF_UNIT_ELECTRICALRESISTANCE_ohm         "Ohm"
#define UF_UNIT_ELECTRICALRESISTANCE_microOhm    "microOhm"
#define UF_UNIT_ELECTRICALRESISTANCE_mOhm        "MilliOhm"
#define UF_UNIT_ELECTRICALRESISTANCE_kOhm        "KiloOhm"
#define UF_UNIT_ELECTRICALRESISTANCE_MOhm        "MegaOhm"
#define UF_UNIT_ELECTRICALRESISTANCE_English1    "ElectricalResistance_English1"

#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_mm     "OhmMilliMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_m      "OhmMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_in     "OhmInch"
#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_ft     "OhmFoot"
#define UF_UNIT_ELECTRICALRESISTIVITY_Mohm_m      "MegaOhmMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_kohm_m      "KiloOhmMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_ohm_cm      "OhmCentiMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_kohm_ft     "KiloOhmFoot"
#define UF_UNIT_ELECTRICALRESISTIVITY_Mohm_ft     "MegaOhmFoot"
#define UF_UNIT_ELECTRICALRESISTIVITY_microOhm_mm "MicroOhmMilliMeter"
#define UF_UNIT_ELECTRICALRESISTIVITY_English1    "ElectricalResistivity_English1"

#define UF_UNIT_ELECTRICALCONDUCTANCE_mho        "Siemen"
#define UF_UNIT_ELECTRICALCONDUCTANCE_Mmho       "MegaSiemen"
#define UF_UNIT_ELECTRICALCONDUCTANCE_English1   "ElectricalConductance_English1"

#define UF_UNIT_VOLTAGE_V                        "Volt"
#define UF_UNIT_VOLTAGE_mV                       "MilliVolt"
#define UF_UNIT_VOLTAGE_kV                       "KiloVolt"
#define UF_UNIT_VOLTAGE_microV                   "MicroVolt"
#define UF_UNIT_VOLTAGE_English1                 "Voltage_English1"

#define UF_UNIT_VOLTAGEPERTEMPERATURE_V__C      "VoltPerCelsius"
#define UF_UNIT_VOLTAGEPERTEMPERATURE_V__F      "VoltPerFahrenheit"
#define UF_UNIT_VOLTAGEPERTEMPERATURE_V__K      "VoltPerKelvin"
#define UF_UNIT_VOLTAGEPERTEMPERATURE_V__R      "VoltPerRankine"
#define UF_UNIT_VOLTAGEPERTEMPERATURE_microV__C "MicroVoltPerCelsius"
#define UF_UNIT_VOLTAGEPERTEMPERATURE_English1  "VoltagePerTemperature_English1"

#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_V_min__rev       "VoltMinutePerRevolution"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_V_sec__deg       "VoltSecondPerDegree"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_V_sec__rad       "VoltSecondPerRadians"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_mV_min__rev      "MilliVoltMinutePerRevolution"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_mV_sec__deg      "MilliVoltSecondPerDegree"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_mV_sec__rad      "MilliVoltSecondPerRadians"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_microV_min__rev  "MicroVoltMinutePerRevolution"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_microV_sec__deg  "MicroVoltSecondPerDegree"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_microV_sec__rad  "MicroVoltSecondPerRadians"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_English1         "PoundForceInchDegreePerAmp"
#define UF_UNIT_VOLTAGEPERANGULARVELOCITY_English2         "PoundForceInchRadiansPerAmp"

#define UF_UNIT_INDUCTANCE_H                     "Henry"
#define UF_UNIT_INDUCTANCE_mH                    "MilliHenry"
#define UF_UNIT_INDUCTANCE_microH                "MicroHenry"
#define UF_UNIT_INDUCTANCE_nanoH                 "NanoHenry"
#define UF_UNIT_INDUCTANCE_English1              "Inductance_English1"

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
#define UF_UNIT_LATENTHEATPERMASS_mJ__Mg          "MilliJoulePerMegagram"

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

#define UF_UNIT_MASSLENGTH_lbm_in                "PoundMassInch"
#define UF_UNIT_MASSLENGTH_lbm_ft                "PoundMassFeet"
#define UF_UNIT_MASSLENGTH_g_mm                  "GramMilliMeter"
#define UF_UNIT_MASSLENGTH_g_cm                  "GramCentiMeter"
#define UF_UNIT_MASSLENGTH_kg_m                  "KilogramMeter"
#define UF_UNIT_MASSLENGTH_kg_mm                 "KilogramMilliMeter"
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
#define UF_UNIT_MOMENTPERANGLE_lbf_ft__deg      "PoundForceFootPerDegree"
#define UF_UNIT_MOMENTPERANGLE_lbf_ft__rad      "PoundForceFootPerRadian"

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

#define UF_UNIT_LENGTH_PER_PRESSURE_mm3__N          "MilliMeterCubedPerNewton"
#define UF_UNIT_LENGTH_PER_PRESSURE_mm3__mN         "MilliMeterCubedPerMilliNewton"
#define UF_UNIT_LENGTH_PER_PRESSURE_m3__N           "MeterCubedPerNewton"
#define UF_UNIT_LENGTH_PER_PRESSURE_m3__mN          "MeterCubedPerMilliNewton"
#define UF_UNIT_LENGTH_PER_PRESSURE_in3__lbf        "InchCubedPerPoundForce"
#define UF_UNIT_LENGTH_PER_PRESSURE_ft3__lbf        "FeetCubedPerPoundForce"


#define UF_UNIT_PRESSURE_PER_LENGTH_N__mm3          "NewtonPerMilliMeterCubed"
#define UF_UNIT_PRESSURE_PER_LENGTH_N__m3           "NewtonPerMeterCubed"
#define UF_UNIT_PRESSURE_PER_LENGTH_mN__mm3         "MilliNewtonPerMillimeterCubed"
#define UF_UNIT_PRESSURE_PER_LENGTH_mN__m3          "MilliNewtonPerMeterCubed"
#define UF_UNIT_PRESSURE_PER_LENGTH_lbf__in3        "PoundForcePerInchCubed"
#define UF_UNIT_PRESSURE_PER_LENGTH_lbf__ft3        "PoundForcePerFootCubed"
#define UF_UNIT_PRESSURE_PER_LENGTH_J__m4           "JoulePerMeterFourth"
#define UF_UNIT_PRESSURE_PER_LENGTH_kg__m2__sec2    "KilogramPerMeterSquaredPerSecondSquared"
#define UF_UNIT_PRESSURE_PER_LENGTH_kg__mm2__sec2   "KilogramPerMilliMeterSquaredPerSecondSquared"
#define UF_UNIT_PRESSURE_PER_LENGTH_lbm__in2__sec2  "PoundMassPerInchSquaredPerSecondSquared"
#define UF_UNIT_PRESSURE_PER_LENGTH_lbm__ft2__sec2  "PoundMassPerFeetSquaredPerSecondSquared"

#define UF_UNIT_PRESSURE_PER_VELOCITY_N_sec__mm3      "Newton-SecondPerMilliMeterCubed"
#define UF_UNIT_PRESSURE_PER_VELOCITY_N_sec__m3       "Newton-SecondPerMeterCubed"
#define UF_UNIT_PRESSURE_PER_VELOCITY_mN_sec__mm3     "MilliNewton-SecondPerMilliMeterCubed"
#define UF_UNIT_PRESSURE_PER_VELOCITY_mN_sec__m3      "MilliNewton-SecondPerMeterCubed"
#define UF_UNIT_PRESSURE_PER_VELOCITY_lbf_sec__in3    "PoundForce-SecondPerInchCubed"
#define UF_UNIT_PRESSURE_PER_VELOCITY_lbf_sec__ft3    "PoundForce-SecondPerFootCubed"
#define UF_UNIT_PRESSURE_PER_VELOCITY_kg__m2__sec     "KilogramPerMeterSquaredPerSecond"
#define UF_UNIT_PRESSURE_PER_VELOCITY_kg__mm2__sec    "KilogramPerMilliMeterSquaredPerSecond"
#define UF_UNIT_PRESSURE_PER_VELOCITY_lbm__in2__sec   "PoundMassPerInchSquaredPerSecond"
#define UF_UNIT_PRESSURE_PER_VELOCITY_lbm__ft2__sec   "PoundMassPerFeetSquaredPerSecond"

#define UF_UNIT_COEFFICIENTPERTIME__sec                  "CoefficientPerSec"
#define UF_UNIT_COEFFICIENTPERTIME__min                  "CoefficientPerMin"
#define UF_UNIT_COEFFICIENTPERTIME__hr                   "CoefficientPerHr"
#define UF_UNIT_COEFFICIENTPERTIMESQUARED__sec2          "CoefficientPerSecSquared"
#define UF_UNIT_COEFFICIENTPERTIMESQUARED__min2          "CoefficientPerMinSquared"
#define UF_UNIT_COEFFICIENTPERTIMESQUARED__hr2           "CoefficientPerHrSquared"
#define UF_UNIT_COEFFICIENTPERTIMECUBED__sec3            "CoefficientPerSecCubed"
#define UF_UNIT_COEFFICIENTPERTIMECUBED__min3            "CoefficientPerMinCubed"
#define UF_UNIT_COEFFICIENTPERTIMECUBED__hr3             "CoefficientPerHrCubed"

#define UF_UNIT_ANGULARMOMENTUM_mN_mm_sec__deg       "MilliNewtonMilliMeterSecondPerDegree"
#define UF_UNIT_ANGULARMOMENTUM_mN_mm_sec__rad       "MilliNewtonMilliMeterSecondPerRadian"
#define UF_UNIT_ANGULARMOMENTUM_N_mm_sec__deg        "NewtonMilliMeterSecondPerDegree"
#define UF_UNIT_ANGULARMOMENTUM_N_mm_sec__rad        "NewtonMilliMeterSecondPerRadian"
#define UF_UNIT_ANGULARMOMENTUM_N_m_sec__deg         "NewtonMeterSecondPerDegree"
#define UF_UNIT_ANGULARMOMENTUM_N_m_sec__rad         "NewtonMeterSecondPerRadian"
#define UF_UNIT_ANGULARMOMENTUM_lbf_in_sec__deg      "PoundForceInchSecondPerDegree"
#define UF_UNIT_ANGULARMOMENTUM_lbf_in_sec__rad      "PoundForceInchSecondPerRadian"
#define UF_UNIT_ANGULARMOMENTUM_lbf_ft_sec__deg      "PoundForceFootSecondPerDegree"
#define UF_UNIT_ANGULARMOMENTUM_lbf_ft_sec__rad      "PoundForceFootSecondPerRadian"

#define UF_UNIT_THERMALCAPACITANCE_microJ__C         "MicroJoulePerCelsius"
#define UF_UNIT_THERMALCAPACITANCE_J__C              "JoulePerCelsius"
#define UF_UNIT_THERMALCAPACITANCE_KJ__C             "KiloJoulePerCelsius"
#define UF_UNIT_THERMALCAPACITANCE_BTU__F            "BritshThermalUnitsPerDegreeFahrenheit"
#define UF_UNIT_THERMALCAPACITANCE_lbf_in__F         "PoundForceInchPerDegreeFahrenheit"
#define UF_UNIT_THERMALCAPACITANCE_lbf_ft__F         "PoundForceFootPerDegreeFahrenheit"
#define UF_UNIT_THERMALCAPACITANCE_cal__F            "CaloriePerDegreeFahrenheit"

#define UF_UNIT_PERAREA__m2                          "PerSquareMeter"
#define UF_UNIT_PERAREA__cm2                         "PerSquareCentiMeter"
#define UF_UNIT_PERAREA__mm2                         "PerSquareMilliMeter"
#define UF_UNIT_PERAREA__ft2                         "PerSquareFeet"
#define UF_UNIT_PERAREA__in2                         "PerSquareInch"

#define UF_UNIT_TEMPERATURECHANGERATE_C__sec         "CelsiusPerSecond"
#define UF_UNIT_TEMPERATURECHANGERATE_C__min         "CelsiusPerMinute"
#define UF_UNIT_TEMPERATURECHANGERATE_C__hr          "CelsiusPerHour"
#define UF_UNIT_TEMPERATURECHANGERATE_F__sec         "FahrenheitPerSecond"
#define UF_UNIT_TEMPERATURECHANGERATE_F__min         "FahrenheitPerMinute"
#define UF_UNIT_TEMPERATURECHANGERATE_F__hr          "FahrenheitPerHour"
#define UF_UNIT_TEMPERATURECHANGERATE_K__sec         "KelvinPerSecond"
#define UF_UNIT_TEMPERATURECHANGERATE_K__min         "KelvinPerMinute"
#define UF_UNIT_TEMPERATURECHANGERATE_K__hr          "KelvinPerHour"
#define UF_UNIT_TEMPERATURECHANGERATE_R__sec         "RankinePerSecond"
#define UF_UNIT_TEMPERATURECHANGERATE_R__min         "RankinePerMinute"
#define UF_UNIT_TEMPERATURECHANGERATE_R__hr          "RankinePerHour"

#define UF_UNIT_JERK_m__sec3                         "MeterPerCubeSecond"
#define UF_UNIT_JERK_mm__sec3                        "MilliMeterPerCubeSecond"
#define UF_UNIT_JERK_in__sec3                        "InchPerCubeSecond"
#define UF_UNIT_JERK_ft__sec3                        "FeetPerCubeSecond"

#define UF_UNIT_ANGULARJERK_rev__sec3                "RevolutionsPerSecondCubed"
#define UF_UNIT_ANGULARJERK_rev__min3                "RevolutionsPerMinuteCubed"
#define UF_UNIT_ANGULARJERK_deg__sec3                "DegreesPerSecondCubed"
#define UF_UNIT_ANGULARJERK_rad__sec3                "RadiansPerSecondCubed"

#define UF_UNIT_MAGNETICFIELDSTRENGTH_A__mm          "AmpPerMilliMeter"
#define UF_UNIT_MAGNETICFIELDSTRENGTH_A__in          "AmpPerInch"
#define UF_UNIT_MAGNETICFIELDSTRENGTH_A__m           "AmpPerMeter"
#define UF_UNIT_MAGNETICFIELDSTRENGTH_mA__mm         "MilliAmpPerMilliMeter"
#define UF_UNIT_MAGNETICFIELDSTRENGTH_kA__m          "KiloAmpPerMeter"
#define UF_UNIT_MAGNETICFIELDSTRENGTH_Oe             "Oersted"

#define UF_UNIT_MAGNETICFLUXDENSITY_N__A_m           "NewtonPerAmpPerMeter"
#define UF_UNIT_MAGNETICFLUXDENSITY_lbf__A_in        "PoundForcePerAmpPerInch"
#define UF_UNIT_MAGNETICFLUXDENSITY_Tesla            "Tesla"
#define UF_UNIT_MAGNETICFLUXDENSITY_G                "Gauss"
#define UF_UNIT_MAGNETICFLUXDENSITY_mG               "MilliGauss"
#define UF_UNIT_MAGNETICFLUXDENSITY_mT               "MilliTesla"
#define UF_UNIT_MAGNETICFLUXDENSITY_microT           "MicroTesla"
#define UF_UNIT_MAGNETICFLUXDENSITY_Wb__m2           "WeberPerMeterSquared"
#define UF_UNIT_MAGNETICFLUXDENSITY_mN__A_mm         "MilliNewtonPerAmpPerMilliMeter"

#define UF_UNIT_ANGULARMOMENTUM_mN_mm_sec    "MilliNewtonMilliMeterSecond"
#define UF_UNIT_ANGULARMOMENTUM_N_mm_sec     "NewtonMilliMeterSecond"
#define UF_UNIT_ANGULARMOMENTUM_N_m_sec      "NewtonMeterSecond"
#define UF_UNIT_ANGULARMOMENTUM_lbf_in_sec   "PoundForceInchSecond"
#define UF_UNIT_ANGULARMOMENTUM_lbf_ft_sec   "PoundForceFootSecond"

#define UF_UNIT_VELOCITY_PER_PRESSURE_mm3__N__sec     "MilliMeterCubedPerNewtonPerSecond"
#define UF_UNIT_VELOCITY_PER_PRESSURE_m3__N__sec      "MeterCubedPerNewtonPerSecond"
#define UF_UNIT_VELOCITY_PER_PRESSURE_mm3__mN__sec    "MilliMeterCubedPerMilliNewtonPerSecond"
#define UF_UNIT_VELOCITY_PER_PRESSURE_m3__mN__sec     "MeterCubedPerMilliNewtonPerSecond"
#define UF_UNIT_VELOCITY_PER_PRESSURE_in3__lbf__sec   "InchCubedPerPoundForcePerSecond"
#define UF_UNIT_VELOCITY_PER_PRESSURE_ft3__lbf__sec   "FeetCubedPerPoundForcePerSecond"
#define UF_UNIT_VELOCITY_PER_PRESSURE_m2_sec__kg      "MeterSquaredSecondPerKilogram"
#define UF_UNIT_VELOCITY_PER_PRESSURE_mm2_sec__kg     "MilliMeterSquaredSecondPerKilogram"
#define UF_UNIT_VELOCITY_PER_PRESSURE_in2_sec__lbm    "InchSquaredSecondPerPoundMass"
#define UF_UNIT_VELOCITY_PER_PRESSURE_ft2_sec__lbm    "FeetSquaredSecondPerPoundMass"

#define UF_UNIT_FLOW_RESISTIVITY_N_sec__m4   "NewtonSecondPerMeterFourth"
#define UF_UNIT_FLOW_RESISTIVITY_mN_sec__mm4 "MilliNewtonSecondPerMilliMeterFourth"
#define UF_UNIT_FLOW_RESISTIVITY_N_sec__mm4 "NewtonSecondPerMilliMeterFourth"
#define UF_UNIT_FLOW_RESISTIVITY_lbf_sec__in4 "PoundForceSecondPerInchFourth"
#define UF_UNIT_FLOW_RESISTIVITY_N_sec__cm4 "NewtonSecondPerCentiMeterFourth"
#define UF_UNIT_FLOW_RESISTIVITY_kg__sec_mm3 "KilogramsPerSecondMilliMeterCubed"
#define UF_UNIT_FLOW_RESISTIVITY_lbm__sec_in3 "PoundMassPerSecondInchCubed"
#define UF_UNIT_FLOW_RESISTIVITY_g__sec_mm3 "GramsPerSecondMilliMeterCubed"
#define UF_UNIT_FLOW_RESISTIVITY_g__sec_cm3 "GramsPerSecondCentiMeterCubed"

#define UF_UNIT_CURRENT_DENSITY_A__m3           "AmperePerMeterCubed"
#define UF_UNIT_CURRENT_DENSITY_A__mm3          "AmperePerMilliMeterCubed"
#define UF_UNIT_CURRENT_DENSITY_A__in3          "AmperePerInchCubed"
#define UF_UNIT_CURRENT_DENSITY_A__micron3      "AmperePerMicronCubed"
#define UF_UNIT_CURRENT_DENSITY_A__nm3          "AmperePerNanoMeterCubed"
#define UF_UNIT_CURRENT_DENSITY_mA__m3          "MilliAmperePerMeterCubed"
#define UF_UNIT_CURRENT_DENSITY_mA__mm3         "MilliAmperePerMilliMeterCubed"
#define UF_UNIT_CURRENT_DENSITY_mA__in3         "MilliAmperePerInchCubed"
#define UF_UNIT_CURRENT_DENSITY_mA__micron3     "MilliAmperePerMicronCubed"

#define UF_UNIT_LENGTH_PER_ANGLE_mm__rev         "MillimeterPerRevolution"
#define UF_UNIT_LENGTH_PER_ANGLE_mm__radian      "MillimeterPerRadian"
#define UF_UNIT_LENGTH_PER_ANGLE_mm__degree      "MillimeterPerDegree"
#define UF_UNIT_LENGTH_PER_ANGLE_inch__rev       "InchPerRevolution"
#define UF_UNIT_LENGTH_PER_ANGLE_inch__radian    "InchPerRadian"
#define UF_UNIT_LENGTH_PER_ANGLE_inch__degree    "InchPerDegree"
#define UF_UNIT_LENGTH_PER_ANGLE_cm__rev         "CentimeterPerRevolution"
#define UF_UNIT_LENGTH_PER_ANGLE_cm__radian      "CentimeterPerRadian"
#define UF_UNIT_LENGTH_PER_ANGLE_cm__degree      "CentimeterPerDegree"
#define UF_UNIT_LENGTH_PER_ANGLE_meter__rev      "MeterPerRevolution"
#define UF_UNIT_LENGTH_PER_ANGLE_meter__radian   "MeterPerRadian"
#define UF_UNIT_LENGTH_PER_ANGLE_meter__degree   "MeterPerDegree"
#define UF_UNIT_LENGTH_PER_ANGLE_feet__rev       "FeetPerRevolution"
#define UF_UNIT_LENGTH_PER_ANGLE_feet__radian    "FeetPerRadian"
#define UF_UNIT_LENGTH_PER_ANGLE_feet__degree    "FeetPerAngle"

#define UF_UNIT_CURRENT_DENSITY_AREA_A__m2           "AmperePerMeterSquared"
#define UF_UNIT_CURRENT_DENSITY_AREA_A__mm2          "AmperePerMilliMeterSquared"
#define UF_UNIT_CURRENT_DENSITY_AREA_A__in2          "AmperePerInchSquared"
#define UF_UNIT_CURRENT_DENSITY_AREA_A__micron2      "AmperePerMicronSquared"
#define UF_UNIT_CURRENT_DENSITY_AREA_A__nm2          "AmperePerNanoMeterSquared"
#define UF_UNIT_CURRENT_DENSITY_AREA_mA__m2          "MilliAmperePerMeterSquared"
#define UF_UNIT_CURRENT_DENSITY_AREA_mA__mm2         "MilliAmperePerMilliMeterSquared"
#define UF_UNIT_CURRENT_DENSITY_AREA_mA__in2         "MilliAmperePerInchSquared"
#define UF_UNIT_CURRENT_DENSITY_AREA_mA__micron2     "MilliAmperePerMicronSquared"

#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_V__m           "VoltPerMeter"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_V__mm          "VoltPerMillimeter"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_V__in          "VoltPerInch"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_V__micron      "VoltPerMicron"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_V__nm          "VoltPerNanometer"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_mV__m          "MilliVoltPerMeter"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_mV__mm         "MilliVoltPerMillimeter"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_mV__in         "MilliVoltPerInch"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_mV__micron     "MilliVoltPerMicron"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_microV__mm     "MicroVoltPerMillimeter"
#define UF_UNIT_ELECTRIC_FIELD_STRENGTH_lbf__A_s       "ElectricFieldStrength_English1"

#define UF_UNIT_ELECTRIC_FLUX_DENSITY_A_sec__m2        "AmpereSecondPerMeterSquared"
#define UF_UNIT_ELECTRIC_FLUX_DENSITY_A_sec__mm2       "AmpereSecondPerMilimeterSquared"
#define UF_UNIT_ELECTRIC_FLUX_DENSITY_A_sec__in2       "AmpereSecondPerInchSquared"
#define UF_UNIT_ELECTRIC_FLUX_DENSITY_A_sec__micron2   "AmpereSecondPerMicronSquared"
#define UF_UNIT_ELECTRIC_FLUX_DENSITY_A_sec__nm2       "AmpereSecondPerNanometerSquared"
#define UF_UNIT_ELECTRIC_FLUX_DENSITY_mA_sec__m2       "MilliAmpereSecondPerMeterSquared"
#define UF_UNIT_ELECTRIC_FLUX_DENSITY_mA_sec__mm2      "MilliAmpereSecondPerMillimeterSquared"
#define UF_UNIT_ELECTRIC_FLUX_DENSITY_mA_sec__in2      "MilliAmpereSecondPerInchSquared"
#define UF_UNIT_ELECTRIC_FLUX_DENSITY_mA_sec__micron2  "MilliAmpereSecondPerMicronSquared"

#define UF_UNIT_ELECTRIC_CHARGE_A_sec           "Coulomb"
#define UF_UNIT_ELECTRIC_CHARGE_kA_sec          "KiloCoulomb"
#define UF_UNIT_ELECTRIC_CHARGE_mA_sec          "MilliCoulomb"
#define UF_UNIT_ELECTRIC_CHARGE_A_hr            "AmpereHour"
#define UF_UNIT_ELECTRIC_CHARGE_kA_hr           "KiloAmpereHour"
#define UF_UNIT_ELECTRIC_CHARGE_mA_hr           "MilliAmpereHour"

#define UF_UNIT_LUMINOUS_INTENSITY_cd       "Candela"
#define UF_UNIT_LUMINOUS_INTENSITY_kcd      "KiloCandela"
#define UF_UNIT_LUMINOUS_INTENSITY_mcd      "MilliCandela"

#define UF_UNIT_LUMINOUS_FLUX_lm   "Lumen"
#define UF_UNIT_LUMINOUS_FLUX_klm  "KiloLumen"
#define UF_UNIT_LUMINOUS_FLUX_mlm  "MilliLumen"

#define UF_UNIT_LUMINANCE_cd__m2   "CandelaPerMeterSquared"
#define UF_UNIT_LUMINANCE_cd__mm2  "CandelaPerMilliMeterSquared"
#define UF_UNIT_LUMINANCE_cd__in2  "CandelaPerInchSquared"
#define UF_UNIT_LUMINANCE_cd__ft2  "CandelaPerFootSquared"

#define UF_UNIT_ILLUMINANCE_lx   "Lux"
#define UF_UNIT_ILLUMINANCE_Mlx  "MegaLux"
#define UF_UNIT_ILLUMINANCE_lm__in2  "LumenPerInchSquared"
#define UF_UNIT_ILLUMINANCE_lm__ft2  "LumenPerFootSquared"

#define UF_UNIT_AMOUNT_OF_SUBSTANCE_mol    "Mole"
#define UF_UNIT_AMOUNT_OF_SUBSTANCE_kmol   "KiloMole"
#define UF_UNIT_AMOUNT_OF_SUBSTANCE_mmol   "MilliMole"

#define UF_UNIT_MOLALITY_mol__kg    "MolePerKilogram"
#define UF_UNIT_MOLALITY_mol__lbm   "MolePerPoundMass"
#define UF_UNIT_MOLALITY_mol_in__lbf_sec2   "MoleInchPerPoundForceSecondSquared"

#define UF_UNIT_MOLAR_CONCENTRATION_mol__m3    "MolePerMeterCubed"
#define UF_UNIT_MOLAR_CONCENTRATION_mol__mm3   "MolePerMilliMeterCubed"
#define UF_UNIT_MOLAR_CONCENTRATION_mol__in3   "MolePerInchCubed"
#define UF_UNIT_MOLAR_CONCENTRATION_mol__ft3   "MolePerFootCubed"

#define UF_UNIT_PER_FREQUENCY__hz   "PerHertz"
#define UF_UNIT_PER_FREQUENCY__kHz  "PerKiloHertz"
#define UF_UNIT_PER_FREQUENCY__MHz  "PerMegaHertz"
#define UF_UNIT_PER_FREQUENCY__GHz  "PerGigaHertz"

/* UF_MEASURE_DIFFUSION_RESISTANCE */

#define UF_UNIT_DIFFUSION_RESISTANCE_sec__m      "SecondPerMeter"
#define UF_UNIT_DIFFUSION_RESISTANCE_sec__cm     "SecondPerCentiMeter"
#define UF_UNIT_DIFFUSION_RESISTANCE_sec__mm     "SecondPerMilliMeter"
#define UF_UNIT_DIFFUSION_RESISTANCE_sec__in     "SecondPerInch"
#define UF_UNIT_DIFFUSION_RESISTANCE_sec__ft     "SecondPerFoot"
#define UF_UNIT_DIFFUSION_RESISTANCE_min__ft     "MinutePerFoot"
#define UF_UNIT_DIFFUSION_RESISTANCE_hr__km      "HourPerKiloMeter"
#define UF_UNIT_DIFFUSION_RESISTANCE_hr__mi      "HourPerMile"

#define UF_UNIT_TRANSMISSION_LOSS_microW__microW "MicroWattPerMicroWatt"
#define UF_UNIT_TRANSMISSION_LOSS_W__W "WattPerWatt"
#define UF_UNIT_TRANSMISSION_LOSS_lbf_in__sec__lbf_in__sec "PoundForceInchPerSecondPerPoundForceInchPerSecond"


#define UF_UNIT_ELECTRICAL_CONDUCTIVITY_mho__m           "SiemenPerMeter"
#define UF_UNIT_ELECTRICAL_CONDUCTIVITY_Mmho__m          "MegaSiemenPerMeter"
#define UF_UNIT_ELECTRICAL_CONDUCTIVITY_Mmho__mm         "MegaSiemenPerMilliMeter"
#define UF_UNIT_ELECTRICAL_CONDUCTIVITY_Mmho__cm         "MegaSiemenPerCentiMeter"
#define UF_UNIT_ELECTRICAL_CONDUCTIVITY_English1         "ELECTRICAL_CONDUCTIVITY_English1" 

#define UF_UNIT_POWER_TO_MASS_RATIO_in2__sec3            "InchSquaredPerSecondCubed"
#define UF_UNIT_POWER_TO_MASS_RATIO_w__lbm               "WattPerPoundMass"
#define UF_UNIT_POWER_TO_MASS_RATIO_BTU__hr__lbm         "BtuPerHourPerPoundMass"
#define UF_UNIT_POWER_TO_MASS_RATIO_BTU__min__lbm        "BtuPerMinPerPoundMass"
#define UF_UNIT_POWER_TO_MASS_RATIO_BTU__sec__lbm        "BtuPerSecPerPoundMass"
#define UF_UNIT_POWER_TO_MASS_RATIO_microW__kg           "MicroWattPerKilogram"
#define UF_UNIT_POWER_TO_MASS_RATIO_w__kg                "WattPerKilogram"
#define UF_UNIT_POWER_TO_MASS_RATIO_kw__kg               "KiloWattPerKilogram"
#define UF_UNIT_POWER_TO_MASS_RATIO_microW__g            "MicroWattPerGram"
#define UF_UNIT_POWER_TO_MASS_RATIO_w__g                 "WattPerGram"

#define UF_UNIT_ELECTRICAL_CAPACITANCE_picofarad         "PicoFarad"
#define UF_UNIT_ELECTRICAL_CAPACITANCE_nanofarad         "NanoFarad"
#define UF_UNIT_ELECTRICAL_CAPACITANCE_microfarad        "MicroFarad"
#define UF_UNIT_ELECTRICAL_CAPACITANCE_millifarad        "MilliFarad"
#define UF_UNIT_ELECTRICAL_CAPACITANCE_farad             "Farad"
#define UF_UNIT_ELECTRICAL_CAPACITANCE_megafarad         "MegaFarad"
#define UF_UNIT_ELECTRICAL_CAPACITANCE_English1          "ELECTRICAL_CAPACITANCE_English1"

#define UF_UNIT_FREQUENCY_SQUARED_hz2                    "HertzSquared"
#define UF_UNIT_FREQUENCY_SQUARED_kHz2                   "KiloHertzSquared"
#define UF_UNIT_FREQUENCY_SQUARED_MHz2                   "MegaHertzSquared"
#define UF_UNIT_FREQUENCY_SQUARED_GHz2                   "GigaHertzSquared"

#define UF_UNIT_PER_ANGLE_radian                         "PerRadian"
#define UF_UNIT_PER_ANGLE_degree                         "PerDegree"
#define UF_UNIT_PER_ANGLE_pi_rad                         "PerPiRadian"
#define UF_UNIT_PER_ANGLE_rev                            "PerRev"

#define UF_UNIT_PER_ANGLE_SQUARED_radian2                "PerRadianSquared"
#define UF_UNIT_PER_ANGLE_SQUARED_degree2                "PerDegreeSquared"
#define UF_UNIT_PER_ANGLE_SQUARED_pi_rad2                "PerPiRadianSquared"
#define UF_UNIT_PER_ANGLE_SQUARED_rev2                   "PerRevSquared"

#define UF_UNIT_FREQUENCY_CUBED_hz3                      "HertzCubed"
#define UF_UNIT_FREQUENCY_CUBED_kHz3                     "KiloHertzCubed"
#define UF_UNIT_FREQUENCY_CUBED_MHz3                     "MegaHertzCubed"
#define UF_UNIT_FREQUENCY_CUBED_GHz3                     "GigaHertzCubed"

#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_lbmin2__deg        "PoundMassInchSquaredPerDegree"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_lbmft2__deg        "PoundMassFeetSquaredPerDegree"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_gmm2__deg          "GramMilliMeterSquaredPerDegree"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_gcm2__deg          "GramCentiMeterSquaredPerDegree"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_kgm2__deg          "KilogramMeterSquaredPerDegree"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_kgmm2__deg         "KilogramMilliMeterSquaredPerDegree"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_lbfinsec2__deg     "PoundForceInchSecondSquaredPerDegree"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_lbmin2__rad        "PoundMassInchSquaredPerRadian"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_lbmft2__rad        "PoundMassFeetSquaredPerRadian"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_gmm2__rad          "GramMilliMeterSquaredPerRadian"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_gcm2__rad          "GramCentiMeterSquaredPerRadian"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_kgm2__rad          "KilogramMeterSquaredPerRadian"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_kgmm2__rad         "KilogramMilliMeterSquaredPerRadian"
#define UF_UNIT_MASSMOMENTINERTIAPERANGLE_lbfinsec2__rad     "PoundForceInchSecondSquaredPerRadian"

#define UF_UNIT_MAGNETIC_CONDUCTIVITY_ohm         "OhmPerMeter"
#define UF_UNIT_MAGNETIC_CONDUCTIVITY_microOhm    "MicroOhmPerMillimeter"
#define UF_UNIT_MAGNETIC_CONDUCTIVITY_English1    "MagneticConductivity_English1"

#define UF_UNIT_MAGNETIC_FLUX_weber                     "weber"
#define UF_UNIT_MAGNETIC_FLUX_microWeber                "MicroWeber"
#define UF_UNIT_MAGNETIC_FLUX_milliWeber                "MilliWeber"
#define UF_UNIT_MAGNETIC_FLUX_nanoWeber                 "NanoWeber"
#define UF_UNIT_MAGNETIC_FLUX_maxwell                   "maxwell"
#define UF_UNIT_MAGNETIC_FLUX_lbfin__A                  "PoundForceInchPerAmp"

#define UF_UNIT_MAGNETIC_VECTOR_POTENTIAL_weber__m       "weberPerMeter"
#define UF_UNIT_MAGNETIC_VECTOR_POTENTIAL_microWeber__mm "MicroWeberPerMillimeter"
#define UF_UNIT_MAGNETIC_VECTOR_POTENTIAL_N__A           "NewtonPerAmp"
#define UF_UNIT_MAGNETIC_VECTOR_POTENTIAL_lbf__A         "PoundForcePerAmp"

#define UF_UNIT_VOLUME_CHARGE_DENSITY_C__m3      "CoulombPerMeterCubed"
#define UF_UNIT_VOLUME_CHARGE_DENSITY_C__mm3     "CoulombPerMillimeterCubed"
#define UF_UNIT_VOLUME_CHARGE_DENSITY_C__cm3     "CoulombPerCentimeterCubed"
#define UF_UNIT_VOLUME_CHARGE_DENSITY_C__in3     "CoulombPerInchCubed"
#define UF_UNIT_VOLUME_CHARGE_DENSITY_C__ft3     "CoulombPerFootCubed"

#define UF_UNIT_VOLUMETRIC_STRAIN_mm3__mm3                   "VolumetricStrain_MilliMeterCubedPerMilliMeterCubed"
#define UF_UNIT_VOLUMETRIC_STRAIN_m3__m3                     "VolumetricStrain_MeterCubedPerMeterCubed"
#define UF_UNIT_VOLUMETRIC_STRAIN_cm3__cm3                   "VolumetricStrain_CentiMeterCubedPerCentiMeterCubed"
#define UF_UNIT_VOLUMETRIC_STRAIN_in3__in3                   "VolumetricStrain_InchCubedPerInchCubed"

#define UF_UNIT_APPARENT_POWER_lbfin__sec        "ApparentPowerPoundForceInchPerSecond"
#define UF_UNIT_APPARENT_POWER_microVA           "ApparentPowerMicroVoltAmp"
#define UF_UNIT_APPARENT_POWER_kVA               "ApparentPowerKiloVoltAmp"
#define UF_UNIT_APPARENT_POWER_VA                "ApparentPowerVoltAmp"
#define UF_UNIT_APPARENT_POWER_MVA               "ApparentPowerMegaVoltAmp"

#define UF_UNIT_ENERGY_CONTENT_lbfin             "EnergyContentPoundForceInch"
#define UF_UNIT_ENERGY_CONTENT_microW_sec        "EnergyContentMicroWattSecond"
#define UF_UNIT_ENERGY_CONTENT_W_sec             "EnergyContentWattSecond"
#define UF_UNIT_ENERGY_CONTENT_kW_hr             "EnergyContentKiloWattHour"
#define UF_UNIT_ENERGY_CONTENT_W_hr              "EnergyContentWattHour"

#ifdef __cplusplus
}
#endif
#endif  /*    UF_UNIT_TYPES__H_INCLUDED                                   */

