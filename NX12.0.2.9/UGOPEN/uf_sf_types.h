/*****************************************************************************
             Copyright (c) 1997-2008 Siemens PLM Software
                Unpublished - All Rights Reserved



File Description :

 Data Definitions for the Open C API interface to Scenario.

*****************************************************************************/
#ifndef  UF_SF_TYPES__H_INCLUDED
#define  UF_SF_TYPES__H_INCLUDED

#include <uf_defs.h>
#include <string.h>
#include <uf_sf_lang_names.h>
#include <uf_cfi_types.h>
#include <uf_unit_types.h>
#include <uf_sf_enums.h>

#ifdef __cplusplus
extern "C" {
#endif


#define UF_SF_MIDSRF_NON_EXIST       (-1)
#define UF_SF_MIDSRF_FACEPAIR_METHOD  0
#define UF_SF_MIDSRF_OFFSET_METHOD    1
#define UF_SF_MIDSRF_USER_DEF_METHOD  2


#define UF_SF_SECTION_UNINITIALIZED     -777777.
#define UF_SF_USER_DEFINED_TW_THICKNESS "USER_DEFINED_THIN_WALL_THICKNESS"


struct UF_SF__fixed_s
{
    UF_SF_fem_coord_type_t  type;        /* Coordinate type. */
    double                  origin[3];   /* origin point            */
    double                  x_dir[3];    /* x direction vector      */
    double                  y_dir[3];    /* y direction vector      */
    double                  z_dir[3];    /* z direction vector      */
};
typedef struct UF_SF__fixed_s UF_SF__fixed_t;

union UF_SF_matl_orient_u
{
    UF_SF__fixed_t fixed;
};
typedef union UF_SF_matl_orient_u  UF_SF_matl_orient_t,
                                  *UF_SF_matl_orient_p_t;

union UF_SF_table_u
{
    double                       pair[2]; /* A pair of values for the tabular
                                             form of variable material
                                             properties. The first value is the
                                             independent variable where as the
                                             second one is dependent on the
                                             first. */
};
typedef union UF_SF_table_u  UF_SF_table_t,
                            *UF_SF_table_p_t;

struct UF_SF_table_prop_s
{
    int                          size;  /* The number of pairs in the table. */
    UF_SF_table_p_t              array_ptr; /* Pointer to the table that has
                                               the data. */
};
typedef struct UF_SF_table_prop_s  UF_SF_table_prop_t,
                                  *UF_SF_table_prop_p_t;


union UF_SF__multi_u
{
    UF_SF_table_prop_p_t     table_ptr;      /* pointer to the table property
                                                structure. */
    tag_t                    expression_tag; /* Tag of the expression if
                                                type of property is through
                                                expression. */
};
typedef union UF_SF__multi_u UF_SF__multi_t;


struct UF_SF_multi_prop_s
{
    UF_SF_multi_prop_type_t      type;          /* Type of property, tabular or through
                                                   expression. */
    UF_SF__multi_t               multi;         /* Union containing pointer to the table
                                                   and tag of the expression. */
    UF_UNIT_MEASURE_TYPE_t       measure_type;  /* Type of measure - Eg. MEASURE_FORCE, MEASURE_MASS_DENSITY..etc*/
    tag_t                        unit_type_tag; /* Tag to pointer of unit type - Eg Newton, kg/m3 ..etc */
};
typedef struct UF_SF_multi_prop_s  UF_SF_multi_prop_t,
                                  *UF_SF_multi_prop_p_t;


/* The array sizes in UF_SF_extend_matl_prop                            */
#define UF_SF_extend_matl_aniso_G1                      6
#define UF_SF_extend_matl_aniso_G2                      6
#define UF_SF_extend_matl_aniso_thermal_coeff           6
#define UF_SF_extend_matl_aniso_thermal_conduct1        3
#define UF_SF_extend_matl_aniso_thermal_conduct2        3
#define UF_SF_extend_matl_ortho_youngs_modulus          3
#define UF_SF_extend_matl_ortho_poissons_ratio          3
#define UF_SF_extend_matl_ortho_shear_modulus           3
#define UF_SF_extend_matl_ortho_thermal_coeff           3
#define UF_SF_extend_matl_ortho_thermal_conduct         3

struct UF_SF__isotropic_s
{
    UF_SF_multi_prop_t       youngs_modulus;
    UF_SF_multi_prop_t       poissons_ratio;
    UF_SF_multi_prop_t       shear_modulus;
    UF_SF_multi_prop_t       mass_density;
    UF_SF_multi_prop_t       thermal_coeff;
    UF_SF_multi_prop_t       reference_temperature;
    UF_SF_multi_prop_t       plastic_strain_ratio;
    UF_SF_multi_prop_t       thermal_conduct;
    UF_SF_multi_prop_t       specific_heat;
    UF_SF_multi_prop_t       latent_heat;
    UF_SF_multi_prop_t       phase_temperature;
    UF_SF_multi_prop_t       phase_temperature_range;
    UF_SF_multi_prop_t       phase_specific_heat;
    UF_SF_multi_prop_t       ir_scattering_coeff;
    UF_SF_multi_prop_t       solar_scattering_coeff;
    UF_SF_multi_prop_t       ir_extinction_coeff;
    UF_SF_multi_prop_t       solar_extinction_coeff;
    UF_SF_multi_prop_t       electrical_resistivity;
    UF_SF_multi_prop_t       max_stress_tension;
    UF_SF_multi_prop_t       max_stress_compression;
    UF_SF_multi_prop_t       max_in_plane_shear_stress;
    UF_SF_multi_prop_t       max_strain_tension;
    UF_SF_multi_prop_t       max_strain_compression;
    UF_SF_multi_prop_t       max_in_plane_shear_strain;
    UF_SF_multi_prop_t       tsai_wu_interaction;
    UF_SF_multi_prop_t       damping_coeff;
};
typedef struct UF_SF__isotropic_s UF_SF__isotropic_t;

struct UF_SF__anisotropic_s
{
    UF_SF_multi_prop_t       G  [6] [6];
    UF_SF_multi_prop_t       mass_density;
    UF_SF_multi_prop_t       thermal_coeff  [6];
    UF_SF_multi_prop_t       reference_temperature;
    UF_SF_multi_prop_t       thermal_conduct [3][3];
    UF_SF_multi_prop_t       specific_heat;
    UF_SF_multi_prop_t       damping_coeff;
};
typedef struct UF_SF__anisotropic_s UF_SF__anisotropic_t;

struct UF_SF__orthotropic_s
{
    UF_SF_multi_prop_t       youngs_modulus  [3];
    UF_SF_multi_prop_t       poissons_ratio  [3];
    UF_SF_multi_prop_t       mass_density;
    UF_SF_multi_prop_t       shear_modulus   [3];
    UF_SF_multi_prop_t       thermal_coeff   [3];
    UF_SF_multi_prop_t       reference_temperature;
    UF_SF_multi_prop_t       thermal_conduct [3];
    UF_SF_multi_prop_t       specific_heat;
    UF_SF_multi_prop_t       latent_heat;
    UF_SF_multi_prop_t       phase_temperature;
    UF_SF_multi_prop_t       phase_temperature_range;
    UF_SF_multi_prop_t       phase_specific_heat;
    UF_SF_multi_prop_t       ir_scattering_coeff;
    UF_SF_multi_prop_t       solar_scattering_coeff;
    UF_SF_multi_prop_t       ir_extinction_coeff;
    UF_SF_multi_prop_t       solar_extinction_coeff;
    UF_SF_multi_prop_t       electrical_resistivity;
    UF_SF_multi_prop_t       max_stress_tension[3];
    UF_SF_multi_prop_t       max_stress_compression[3];
    UF_SF_multi_prop_t       max_in_plane_shear_stress;
    UF_SF_multi_prop_t       max_strain_tension[3];
    UF_SF_multi_prop_t       max_strain_compression[3];
    UF_SF_multi_prop_t       max_in_plane_shear_strain;
    UF_SF_multi_prop_t       tsai_wu_interaction;
    UF_SF_multi_prop_t       damping_coeff;
};
typedef struct UF_SF__orthotropic_s UF_SF__orthotropic_t;

struct UF_SF__fluid_s
{
    UF_SF_multi_prop_t       mass_density;
    UF_SF_multi_prop_t       thermal_conduct;
    UF_SF_multi_prop_t       thermal_coeff;
    UF_SF_multi_prop_t       dynamic_viscosity;
    UF_SF_multi_prop_t       specific_heat_pressure;
    UF_SF_multi_prop_t       gas_constant;
    UF_SF_multi_prop_t       bulk_modulus;
    UF_SF_multi_prop_t       sound_speed;
    UF_SF_multi_prop_t       damping_coeff;
    UF_SF_multi_prop_t       molar_mass;
};
typedef struct UF_SF__fluid_s UF_SF__fluid_t;

union UF_SF_material_prop_u
{
    UF_SF__isotropic_t   isotropic;
    UF_SF__anisotropic_t anisotropic;
    UF_SF__orthotropic_t orthotropic;
    UF_SF__fluid_t       fluid;
};
typedef union UF_SF_material_prop_u  UF_SF_material_prop_t,
                                    *UF_SF_material_prop_p_t;

struct UF_SF_material_formability_s
{
    UF_SF_multi_prop_t       work_hardening;
    UF_SF_multi_prop_t       flc;
    UF_SF_multi_prop_t       stress_strain_curve;
};
typedef struct UF_SF_material_formability_s UF_SF_material_formability_prop_t,
                                           *UF_SF_material_formability_prop_p_t;

struct UF_SF_material_strength_s
{
    UF_SF_multi_prop_t       yield;
    UF_SF_multi_prop_t       ultimate_tensile;
};
typedef struct UF_SF_material_strength_s UF_SF_material_strength_prop_t,
                                        *UF_SF_material_strength_prop_p_t;
struct UF_SF_material_fatigue_s
{
    UF_SF_multi_prop_t       fatigue_strength_coef;
    UF_SF_multi_prop_t       fatigue_strength_exp;
    UF_SF_multi_prop_t       fatigue_ductility_coef;
    UF_SF_multi_prop_t       fatigue_ductility_exp;
};
typedef struct UF_SF_material_fatigue_s UF_SF_material_fatigue_prop_t,
                                        *UF_SF_material_fatigue_prop_p_t;

#define UF_SF_MATERIAL_LABELS                                               \
    /* Isotropic items.                                         */          \
    LABEL_TEXT i_mass_density_label = "Mass Density";                  \
    LABEL_TEXT i_reference_temp_label = "Reference Temperature";         \
    LABEL_TEXT i_plastic_strain_label = "Plastic Strain Ratio";          \
    /*                    */       \
    LABEL_TEXT i_youngs_label = "Young`s Modulus";               \
    LABEL_TEXT i_poisson_label = "Poisson`s Ratio";               \
    LABEL_TEXT i_shear_mod_label = "Shear Modulus";                 \
    LABEL_TEXT i_therm_coeff_label = "Thermal Expansion Coefficient"; \
    LABEL_TEXT i_therm_conduct_label = "Thermal Conductivity";          \
    LABEL_TEXT i_specific_heat_label = "Specific Heat";                 \
    LABEL_TEXT i_latent_heat_label = "Latent Heat"; \
    LABEL_TEXT i_phase_temperature_label = "Phase Change Temperature"; \
    LABEL_TEXT i_phase_temperature_range_label = "Phase Change Temperature Range"; \
    LABEL_TEXT i_phase_specific_heat_label = "Specific Heat above Phase Change"; \
    LABEL_TEXT i_ir_scattering_coeff_label = "IR Scattering Coefficient"; \
    LABEL_TEXT i_solar_scattering_coeff_label = "Solar Scattering Coefficient"; \
    LABEL_TEXT i_ir_extinction_coeff_label = "IR Extinction Coefficient"; \
    LABEL_TEXT i_solar_extinction_coeff_label = "Solar Extinction Coefficient"; \
    LABEL_TEXT i_electrical_resistivity_label = "Electrical Resistivity";   \
    LABEL_TEXT i_yield_label = "Yield Strength";                \
    LABEL_TEXT i_ultimate_tensile_label = "Ultimate Tensile Strength";              \
    LABEL_TEXT i_max_stress_tension_label = "Max Allowable Stress in Tension";        \
    LABEL_TEXT i_max_stress_compression_label = "Max Allowable Stress in Compression";    \
    LABEL_TEXT i_max_in_plane_shear_stress_label = "Max Allowable in plane Shear Stress"; \
    LABEL_TEXT i_max_strain_tension_label = "Max Allowable Strain in Tension";        \
    LABEL_TEXT i_max_strain_compression_label = "Max Allowable Strain in Compression";    \
    LABEL_TEXT i_max_in_plane_shear_strain_label = "Max Allowable in plane Shear Strain"; \
    LABEL_TEXT i_tsai_wu_interaction_label = "Tsai-Wu Interaction Coefficient (F12)";     \
    LABEL_TEXT i_damping_coeff_label = "Damping Coefficient";           \
    LABEL_TEXT i_work_harden_label = "Work Hardening";                \
    LABEL_TEXT i_forming_limit_label = "Forming Limit";                 \
    LABEL_TEXT i_stress_strain_label = "Stress/Strain";                 \
    LABEL_TEXT i_fatigue_strength_coef_label = "Fatigue Strength Coefficient";  \
    LABEL_TEXT i_fatigue_strength_exp_label = "Fatigue Strength Exponent";     \
    LABEL_TEXT i_fatigue_ductility_coef_label = "Fatigue Ductility Coefficient"; \
    LABEL_TEXT i_fatigue_ductility_exp_label = "Fatigue Ductility Exponent";    \
    \
    /* Orthotropic items.                                       */          \
    LABEL_TEXT o_mass_density_label = "Mass Density";                  \
    LABEL_TEXT o_reference_temp_label = "Reference Temperature";         \
    /*                    */       \
    LABEL_TEXT o_youngs_label = "Young`s Modulus";               \
    LABEL_TEXT o_poisson_label = "Poisson`s Ratio";               \
    LABEL_TEXT o_shear_mod_label = "Shear Modulus";                 \
    LABEL_TEXT o_therm_coeff_label = "Thermal Expansion Coefficient"; \
    LABEL_TEXT o_therm_conduct_label = "Thermal Conductivity";          \
    LABEL_TEXT o_specific_heat_label = "Specific Heat";                 \
    LABEL_TEXT o_latent_heat_label = "Latent Heat";             \
    LABEL_TEXT o_phase_temperature_label = "Phase Change Temperature"; \
    LABEL_TEXT o_phase_temperature_range_label = "Phase Change Temperature Range"; \
    LABEL_TEXT o_phase_specific_heat_label = "Specific Heat above Phase Change"; \
    LABEL_TEXT o_ir_scattering_coeff_label = "IR Scattering Coefficient";        \
    LABEL_TEXT o_solar_scattering_coeff_label = "Solar Scattering Coefficient";     \
    LABEL_TEXT o_ir_extinction_coeff_label = "IR Extinction Coefficient";        \
    LABEL_TEXT o_solar_extinction_coeff_label = "Solar Extinction Coefficient";     \
    LABEL_TEXT o_electrical_resistivity_label = "Electrical Resistivity";           \
    LABEL_TEXT o_max_stress_tension_label = "Max Stress in Tension";     \
    LABEL_TEXT o_max_stress_compression_label = "Max Stress in Compression"; \
    LABEL_TEXT o_max_in_plane_shear_stress_label = "Max in plane Shear Stress"; \
    LABEL_TEXT o_max_strain_tension_label = "Max Strain in Tension";     \
    LABEL_TEXT o_max_strain_compression_label = "Max Strain in Compression"; \
    LABEL_TEXT o_max_in_plane_shear_strain_label = "Max in plane Shear Strain"; \
    LABEL_TEXT o_tsai_wu_interaction_label = "Tsai-Wu Interaction Coefficient (F12)";  \
    LABEL_TEXT o_damping_coeff_label = "Damping Coefficient";                          \
    \
    /* Anisotropic items.                                       */          \
    LABEL_TEXT mass_density_label = "Mass Density";                  \
    LABEL_TEXT reference_temp_label = "Reference Temperature";         \
    LABEL_TEXT shear_moduli_label = "Material Moduli";               \
    LABEL_TEXT therm_expan_coeff_label = "Thermal Expansion Coefficient"; \
    LABEL_TEXT therm_conduct_label = "Thermal Conductivity";          \
    LABEL_TEXT specific_heat_label = "Specific Heat";                 \
    LABEL_TEXT damping_coeff_label = "Damping Coefficient";           \
    \
    /* Fluid items. */                                                      \
    LABEL_TEXT f_mass_density_label = "Mass Density";                    \
    LABEL_TEXT f_therm_conduct_label = "Thermal Conductivity";            \
    LABEL_TEXT f_therm_coeff_label = "Thermal Expansion Coefficient";   \
    LABEL_TEXT f_dynamic_visc_label = "Dynamic Viscosity";               \
    LABEL_TEXT f_spec_heat_press_label = "Specific Heat Constant Pressure"; \
    LABEL_TEXT f_gas_constant_label = "Gas Constant";                    \
    LABEL_TEXT f_bulk_modulus_label = "Bulk Modulus";                    \
    LABEL_TEXT f_sound_speed_label = "Speed of Sound";                  \
    LABEL_TEXT f_damping_coeff_label = "Damping Coefficient";             \
    LABEL_TEXT f_molar_mass_label = "Molar Mass";

/* Names of each type shown to the user. */
#define UF_SF_LANG_ANALYSIS_STRUCTURAL_STR              "Structural"
#define UF_SF_LANG_ANALYSIS_THERMAL_STR                 "Thermal"
#define UF_SF_LANG_ANALYSIS_FLOW_STR                    "Flow"
#define UF_SF_LANG_ANALYSIS_COUPLED_STR                 "Coupled"
#define UF_SF_LANG_ANALYSIS_MAPPING_STR                 "Mapping"


/* Names of each type shown to the user. */
#define UF_SF_LANG_ANALYSIS_SIMPLE_STR          "Simple"
#define UF_SF_LANG_ANALYSIS_AXISYM_STR          "Axisymmetric"


/* Names of each type shown to the user. */
#define UF_SF_LANG_ANALYSIS_LINEAR_STR          "Linear"
#define UF_SF_LANG_ANALYSIS_NONLINEAR_STR       "Non-Linear"


/* Names of each type shown to the user. */
#define UF_SF_LANG_ANALYSIS_STEADY_STR          "Steady-state"



#define  UF_SF__MAX_EXP_TAGS 10

/***********************************************************************
       This Structure contains the data required to define/describe
       a beam/bar section.  Sections are define in the YZ plane.
**********************************************************************/
struct UF_SF_section_data_s
{
    UF_SF_section_type_t type; /* indicates the type of section described,
                                  UF_SF_SECTION_TWREC = Thin wall, rectangle
                                  UF_SF_SECTION_TWCYL = Thin wall, cylinder
                                  UF_SF_SECTION_TWCHA = Thin wall, channel
                                  UF_SF_SECTION_TWHAT = Thin wall, hat
                                  UF_SF_SECTION_TWIBE = Thin wall, I beam
                                  UF_SF_SECTION_SOCYL = Solid, cylinder
                                  UF_SF_SECTION_SOREC = Solid, rectangle
                                  UF_SF_SECTION_KEYIN = User defined
                                  UF_SF_SECTION_USER_TW
                                                      = User Defined TW
                                  UF_SF_SECTION_USER_SOLID
                                                      = User Defined Solid*/
    double origin[3]; /* Location of section origin */
    double x_dir[3]; /* Orientation of sections x directions (along elm) */
    double y_dir[3]; /* Orientation of sections y directions
                        z_dir = x_dir X y_dir */
    logical offset_set[3]; /* Indicates if the coresponding offset was
                              set (TRUE) or was given the default (FALSE).
                             [0] == x offset of section, always = FALSE */
    double offset[3]; /* (y,z) offset of section
                         [0] == x offset of section, always = 0.0 */
    tag_t geometry;     /* Tag of geometry on which section is defined
                             (i.e the curve tag along which beams are defined
                             in the case where elements are created between
                             geometry "geometry" will be the mesh_recipe. */
    tag_t exp_tag[UF_SF__MAX_EXP_TAGS]; /* An array of tags to Expression
                                           defining the sections dimension or
                                           section properties depending on
                                           the type of section */
};
typedef struct UF_SF_section_data_s  UF_SF_section_data_t,
                                    *UF_SF_section_data_p_t;

/************************************************************************
       This Structure contains the data required to define the edge
       density for a curve/edge object
************************************************************************/
struct UF_SF_edge_density_data_s
{
    UF_SF_edge_density_type_t type; /* indicates the type of density (size or
                                       number). */
    double size; /* The number of elements on the edge/curve is calculated
                    automatically from the length of the edge/curve and the
                    element size. If this option is set, the value of number
                    is disregarded. */
    int number; /* The number of elements on the edge/curve is calculated
                   automatically from the length of the edge/curve and the
                   element size. If this option is set, the value of number is
                   disregarded. */
};
typedef struct UF_SF_edge_density_data_s  UF_SF_edge_density_data_t,
                                         *UF_SF_edge_density_data_p_t;

/**************************************************************************
       This structure contains the data required to define/describe
       a smart point.
**************************************************************************/
struct UF_SF_HPT_location_data_s
{
    UF_SF_HPT_method_t method; /* Indicates the how the smart point is defined.
                                  UF_SF_HPT_ON_CURVE
                                  UF_SF_HPT_BASEPT_AND_OFFSET
                                  UF_SF_HPT_CENTER_OF_CONIC
                                  UF_SF_HPT_CURVE_INTERSECTION
                                  UF_SF_HPT_ON_SURFACE */
    UF_SF_section_type_t type; /* How the base is defined:
                                  UF_SF_numeric_method_t. */
    double origin[3]; /* Location of base point
                         when baseMethod = UF_SF_NUMERIC. */
    double x_dir[3]; /* when baseMethod = UF_SF_EXPRESSION. */
    double y_dir[3]; /* How the offset is defined:
                        when method = SFEM_HPT_BASEPT_AND_OFFSET */
    logical offset_set[3]; /* Offset vector,
                              when baseMethod = UF_SF_NUMERIC. */
    double offset[3]; /* Offset vector, when baseMethod = UF_SF_EXPRESSION. */
    tag_t geometry; /* First object tag.
                       Curve tag when method = SFEM_HPT_ON_CURVE
                       First curve tag when method = SFEM_HPT_CURVE_INTERSECTION
                       Conic tag when method = SFEM_HPT_CENTER_OF_CONIC */
    tag_t exp_tag[UF_SF__MAX_EXP_TAGS]; /* Second curve tag when method = SFEM_HPT_CURVE_INTERSECTION */

};
typedef struct UF_SF_HPT_location_data_s  UF_SF_HPT_location_data_t,
                                         *UF_SF_HPT_location_data_p_t;


/********************************* ATM parameters *****************************/


struct UF_SF_atm_mesh_parameters_data_s
{
    UF_SF_atm_element_types_t     element_type;   /*  TETRA or TETRA_10   */
    UF_SF_atm_edge_shape_types_t  edge_shape;     /*  LINEAR, CURVED or MIXED */
    double                      def_elem_size;    /*  Default Element Size*/
    double                      target_angle;     /*  0. < ang <= 90.     */
    int                         curvature_scaling;/*  1 = OFF  , 0 = ON   */
    int                         auto_constraining;/*  1 = OFF  , 0 = ON   */
    tag_t                       elem_desc_tag; /* element descri(p)tor tag*/
};
typedef struct UF_SF_atm_mesh_parameters_data_s
                                             UF_SF_atm_mesh_parameters_data_t,
                                            *UF_SF_atm_mesh_parameters_data_p_t;



struct UF_SF_sfqm_param_data_s
{
    double    edge_match_tol; /* Distance tolerance value used to find the
                                 matched edges. The distance is measured from
                                 the mid point location of one edge to the mid
                                 point of the other edge.  The default value
                                 is 0.02. */
    double    node_uniq_tol;  /* Specifies the maximum distance allowed between
                                 nodes before they are merged when uniqueness
                                 testing is active.  The default is 0.0001. */
    double    smooth_tol;     /* Distance in model units from old position to
                                 new position for the node moved the farthest
                                 during one iteration of the smoothing
                                 algorithm.  The default value is 0.01. */
    double    on_surf_tol;    /* Controls the maximum distance in model units
                                 that a node created during Scenario Shell
                                 Mesher may lie from its closest point on the
                                 surface.  The default value is 0.001. */
    int       trans_rows;     /* Allows to control the number of rows that will
                                 be used to bridge the gap between elements of
                                 different sizes.  The default value is 3. */
};
typedef struct UF_SF_sfqm_param_data_s  UF_SF_sfqm_param_data_t,
                                       *UF_SF_sfqm_param_data_p_t;

struct UF_SF_sfqm_mesh_data_s
{
    UF_SF_sfqm_elem_type_t     elem_type;  /* The type of element chosen. */
    double                  elem_size;     /* The size of the element. */
    int                     smart_edge_seeding;
    UF_SF_sfqm_param_data_p_t  mesh_param_data_p; /* Pointer to the mesh
                                         parameter data structure, containing
                                         the values for the given parameters. */
    int                     format_mesh;  /* 0 = OFF  , 1 = ON      */
    int                     mapped_mesh;         /* 0 = OFF  , 1 = ON      */
    int                     mesh_transition;  /* 0 = OFF  , 1 = ON      */
    int                     mesh_method;  /* 0 = Automatic, 1 = Paver   */
};
typedef struct UF_SF_sfqm_mesh_data_s  UF_SF_sfqm_mesh_data_t,
                                      *UF_SF_sfqm_mesh_data_p_t;

struct UF_SF_1d_mesh_data_s
{
    UF_SF_1D_element_type_t  element_type; /* Type of element for solid meshing.
                                              The following tetrahedral elements
                                              are supported:
                                                UF_SF_ATM_SYSTEM_DEFAULT_TYPE
                                                UF_SF_ATM_TETRA
                                                UF_SF_ATM_TETRA_10 */
    UF_SF_1D_density_type_t  density_type; /* Type of edge density
                                                UF_SF_1D_EDGE_DENSITY_NUMBER
                                                UF_SF_1D_EDGE_DENSITY_SIZE
                                                UF_SF_1D_EDGE_DENSITY_SMART
                                           */
    double                     edge_density; /* Value of edge density. */
    int                        merge_node_option; /* 0 - OFF, 1 - ON */
    double                     node_unique_tol; /* Value of node unique
                                                   tolerance. */
};
typedef struct UF_SF_1d_mesh_data_s  UF_SF_1d_mesh_data_t,
                                    *UF_SF_1d_mesh_data_p_t;

struct UF_SF_ef_conn_info_s
{
    tag_t                element_des_tag; /* Set to NULL_TAG */
    UF_SF_1D_density_type_t  density_type; /* Type of edge density
                                                UF_SF_1D_EDGE_DENSITY_NUMBER
                                                UF_SF_1D_EDGE_DENSITY_SIZE
                                                UF_SF_1D_EDGE_DENSITY_SMART
                                           */
    double               edge_density; /* Value of edge density. */
    int                  mesh_option; /* 0 for Glue mesh
                                         1 for Match mesh */
    int                  num_edges; /* Number of edges */
    tag_p_t              edge_tags; /* <len:num_edges> Edge tags array */
    int                  num_faces; /* Number of faces */
    tag_p_t              face_tags; /* <len:num_faces> Face tags array */
};
typedef struct UF_SF_ef_conn_info_s UF_SF_ef_conn_info_t,
                                    *UF_SF_ef_conn_info_p_t;


struct UF_SF_contact_mesh_data_s
{
    char  *element_name;                 /* refer to uf_sf_lang_names.h */
    tag_t element_descritor_tag;         /* Set it to NULL_TAG */
    int align_target_edge_node;        /* 0 - Equal Distance
                                           1 - Minimum Distance or Normal To */
    int target_edge_node_align_method; /* 0 - Minimum Distance
                                           1 - Normal To */
    int number_of_elms;                 /* required */
    int gap_tol_option;                 /* 0 - Do not apply tol
                                           1 - Apply gap tolerance */
    double gap_tolerance;               /* Gap tolerance option
                                           0: Don't apply tolerance
                                           1: Apply tolerance
                                        */
    tag_t contact_edge;                 /* Tag of the contact edge. */
    UF_SF_mesh_geom_meshdir_t  contact_edge_mesh_dir;
                                        /* Direction of the mesh for the
                                           contact edge:
                                              UF_SF_MG_MESHDIR_FROM_START
                                              UF_SF_MG_MESHDIR_FROM_END
                                        */
    double contact_edge_start_limit;    /* Limit of edge starting for the
                                           contact edge. */
    double contact_edge_end_limit;      /* Limit of edge ending for the contact
                                           edge. */
    tag_t  target_edge;                 /* Tag of the target edge. */
    UF_SF_mesh_geom_meshdir_t  target_edge_mesh_dir;
                                        /* Direction of the mesh for the target
                                           edge:
                                             UF_SF_MG_MESHDIR_FROM_START
                                             UF_SF_MG_MESHDIR_FROM_END
                                        */
    double target_edge_start_limit;     /* set start limits to 0 and end limits
                                           to 1 to build contact mesh between
                                           entire length of the edges. */
    double target_edge_end_limit;       /* Limit of edge ending for the target
                                           edge. */

};
typedef struct UF_SF_contact_mesh_data_s  UF_SF_contact_mesh_data_t,
                                         *UF_SF_contact_mesh_data_p_t;

struct UF_SF_orientation_data_s
{
    tag_t face_tag;      /* tag of a solid face.
                         The y vector will be defined normal to this face.
                         If this is a NULL_TAG use origin, x_dir, and y_dir
                         to create csys and use it to define y orientation. */
    double origin[3];    /* origin info */
    double x_dir[3];     /* x direction vector */
    double y_dir[3];     /* y direction vector */
};
typedef struct UF_SF_orientation_data_s  UF_SF_orientation_data_t,
                                        *UF_SF_orientation_data_p_t;

struct  UF_SF_section_prop_list_s
{
   int      section_type; /* Type of section:
                               UF_SF_SECTION_TWREC for Thin wall, rectangle
                               UF_SF_SECTION_TWCYL for Thin wall, cylinder
                               UF_SF_SECTION_TWCHA for Thin wall, channel
                               UF_SF_SECTION_TWHAT for Thin wall, hat
                               UF_SF_SECTION_TWIBE for  Thin wall, I beam
                               UF_SF_SECTION_SOCYL for Solid, cylinder
                               UF_SF_SECTION_SOREC for  Solid, rectangle
                               UF_SF_SECTION_KEYIN  for User defined.
                               UF_SF_SECTION_USER_TW forUser Defined TW
                               UF_SF_SECTION_USER_SOLID for User Defined Solid
                           */
   double   bcenter;      /* Breadth of section.                        */
   double   hcenter;      /* Height of section.                         */
   double   thicknesst;   /* Thickness of section.                      */
   double   b1center;     /* Flange breadth of hat & ibeam sections.    */
   double   thicknesstw;  /* Web thickness of ibeam section.            */
   double   radius;       /* Radius of TWCYL and SOCYL sections.        */
   double   area;         /* Area of section.                           */
   double   Izz;          /* Moment of Inertia about x-axis.            */
   double   Iyy;          /* Moment of Inertia about y-axis.            */
   double   Izy;          /* Moment of Inertia about xy-axis.           */
   double   torsion;      /* Torsional coefficient.                     */
   double   warp;         /* Warping coefficient.                       */
   double   y_eccentricity; /* Y Eccentricity.                          */
   double   z_eccentricity; /* Z Eccentricity.                          */
   double   hydro_diameter; /* Hydraulic Diameter of section.           */
   double   perimeter;      /* Perimeter of section.                    */
   double   wall_thickness; /* Wall Thickness of section.               */
};
typedef struct UF_SF_section_prop_list_s  UF_SF_section_prop_list_t,
                                         *UF_SF_section_prop_list_p_t;



   /* General properties of 1D Element Sections.
      First are the numeric values, followed by corresponding expressions
      tags, when any property has an expression.
      If there is no expression, then the tag is NULL_TAG.
    */
struct  UF_SF_section_properties_s
{
   int      section_type; /* Type of section:
                               UF_SF_SECTION_TWREC for Thin wall, rectangle
                               UF_SF_SECTION_TWCYL for Thin wall, cylinder
                               UF_SF_SECTION_TWCHA for Thin wall, channel
                               UF_SF_SECTION_TWHAT for Thin wall, hat
                               UF_SF_SECTION_TWIBE for  Thin wall, I beam
                               UF_SF_SECTION_SOCYL for Solid, cylinder
                               UF_SF_SECTION_SOREC for  Solid, rectangle
                               UF_SF_SECTION_KEYIN  for User defined.
                               UF_SF_SECTION_USER_TW forUser Defined TW
                               UF_SF_SECTION_USER_SOLID for User Defined Solid
                           */
   double   bcenter;      /* Breadth of section.                        */
   double   hcenter;      /* Height of section.                         */
   double   thicknesst;   /* Thickness of section.                      */
   double   b1center;     /* Flange breadth of hat & ibeam sections.    */
   double   thicknesstw;  /* Web thickness of ibeam section.            */
   double   radius;       /* Radius of TWCYL and SOCYL sections.        */
   double   area;         /* Area of section.                           */
   double   Izz;          /* Moment of Inertia about x-axis.            */
   double   Iyy;          /* Moment of Inertia about y-axis.            */
   double   Izy;          /* Moment of Inertia about xy-axis.           */
   double   torsion;      /* Torsional coefficient.                     */
   double   warp;         /* Warping coefficient.                       */
   double   y_eccentricity; /*Y Eccenctricity                           */
   double   z_eccentricity; /*Z Eccenctricity                           */
   double   hydro_diameter; /*Hydraulic Diameter of section.            */
   double   perimeter;      /*Perimeter of section.                     */
   double   wall_thickness; /*Wall Thickness of section.                */
   tag_t    bcenter_exp;  /* Breadth of section.                        */
   tag_t    hcenter_exp;  /* Height of section.                         */
   tag_t    thicknesst_exp; /* Thickness of section.                    */
   tag_t    b1center_exp; /* Flange breadth of hat & ibeam sections.    */
   tag_t    thicknesstw_exp; /* Web thickness of ibeam section.         */
   tag_t    radius_exp;   /* Radius of TWCYL and SOCYL sections.        */
   tag_t    area_exp;     /* Area of section.                           */
   tag_t    Izz_exp;      /* Moment of Inertia about x-axis.            */
   tag_t    Iyy_exp;      /* Moment of Inertia about y-axis.            */
   tag_t    Izy_exp;      /* Moment of Inertia about xy-axis.           */
   tag_t    torsion_exp;  /* Torsional coefficient.                     */
   tag_t    warp_exp;     /* Warping coefficient.                       */
   tag_t    y_eccentricity_exp; /*Y Eccentricity                        */
   tag_t    z_eccentricity_exp; /*Z Eccentricity                        */
   tag_t    hydro_diameter_exp; /*Hydraulic Diameter of section.        */
   tag_t    perimeter_exp;      /*Perimeter of section.                 */
   tag_t    wall_thickness_exp; /*Wall Thickness of section.            */
   tag_t    sketch_tag;   /* For user defined thin wall.                */
   tag_t    face_tag;     /* For user defined solid.                    */
   tag_t    vector_tag;   /* For user defined solid horizonal direction.*/
};
typedef struct UF_SF_section_properties_s  UF_SF_section_properties_t,
                                         *UF_SF_section_properties_p_t;

   /* Properties unique to user defined sections which are
      not passed to the FEA solver. These are user feedback
      only.
    */
struct  UF_SF_user_defined_section_properties_s
{
   double   principal_angle;   /* Principal angle in degrees.           */
   double   principal_mom_inertia[2]; /*Principal Moment of Inertia.    */
   double   centroid[2];  /* Centroid location in global coordinates.   */
   double   shear_center[2]; /* Shear center in global coordinates.     */

};
typedef struct UF_SF_user_defined_section_properties_s
               UF_SF_user_defined_section_properties_t,
              *UF_SF_user_defined_section_properties_p_t;


struct UF_SF_section_src_list_s
{
   double     C1;  /* Y location of the first stress recovery point.    */
   double     C2;  /* Z location of the first stress recovery point.    */
   double     D1;  /* Y location of the second stress recovery point.   */
   double     D2;  /* Z location of the second stress recovery point.   */
   double     E1;  /* Y location of the third stress recovery point.    */
   double     E2;  /* Z location of the third stress recovery point.    */
   double     F1;  /* Y location of the fourth stress recovery point.   */
   double     F2;  /* Z location of the fourth stress recovery point.   */
};
typedef struct UF_SF_section_src_list_s  UF_SF_section_src_list_t,
                                        *UF_SF_section_src_list_p_t;

   /* Stress recovery locations of 1D Element Sections.
      First are the numeric values, followed by corresponding expressions
      tags, when any location has an expression.
      If there is no expression, then the tag is NULL_TAG.
    */
struct UF_SF_section_src_properties_s
{
   double     C1;  /* Y location of the first stress recovery point.    */
   double     C2;  /* Z location of the first stress recovery point.    */
   double     D1;  /* Y location of the second stress recovery point.   */
   double     D2;  /* Z location of the second stress recovery point.   */
   double     E1;  /* Y location of the third stress recovery point.    */
   double     E2;  /* Z location of the third stress recovery point.    */
   double     F1;  /* Y location of the fourth stress recovery point.   */
   double     F2;  /* Z location of the fourth stress recovery point.   */
   tag_t    C1_exp; /* Y location of the first stress recovery point.   */
   tag_t    C2_exp; /* Z location of the first stress recovery point.   */
   tag_t    D1_exp; /* Y location of the second stress recovery point.  */
   tag_t    D2_exp; /* Z location of the second stress recovery point.  */
   tag_t    E1_exp; /* Y location of the third stress recovery point.   */
   tag_t    E2_exp; /* Z location of the third stress recovery point.   */
   tag_t    F1_exp; /* Y location of the fourth stress recovery point.  */
   tag_t    F2_exp; /* Z location of the fourth stress recovery point.  */
};
typedef struct UF_SF_section_src_properties_s  UF_SF_section_src_properties_t,
                                        *UF_SF_section_src_properties_p_t;


/****************************************************************************
 * Structure defining mesh visualization attributes.                        *
 ****************************************************************************/
struct UF_SF_mesh_visuals_s
{
    int       color;              /* Primary element color */
    int       shade_mode;         /* Different modes of shading:
                                       0 - never shade
                                       1 - shade when any shade mode is on
                                       2 - shade when partial shaded mode is on
                                       3 - shade when fully shaded mode is on */
    int       shade_edge_color;   /* Element edge color when shaded */
    int       shrink_factor;      /* Element shrink percentage  0 -> 100
                                         0 - no shrinking
                                       100 - shrinks elements to a point  */
    int       normals;            /* Valid for 2D elements
                                       0 - no element normals
                                       1 - element directional tails
                                       2 - element vectors */
    int       normals_color;      /* Normal display color */
    int       edge_visibility_sw; /* Element edge visibility switch:
                                       0 - do not show elemement edges
                                       1 - show element edges  */
    int       text_display_sw;    /* Element text display switch:
                                       0 - do not show text
                                       1 - show text  */

    int       thick_shell_sw;     /* Element thick shell display switch:
                                       0 - do not show 2D elements as thick shells
                                       1 - show 2D elements as thick shells  */

    /* The following only apply to meshes created by a call to UF_SF_create_disp_mesh */
    int       show_analysis;      /* Show analysis results or not
                                   * 0 - do not show analysis results
                                   * 1 - show analysis results  */
    int       show_deformed;      /* Show deformation or not .
                                   * 0 - do not show deformed results
                                   * 1 - show deformed results  */
    double    deformed_scale;     /* Scale value for the deformation magnitude
                                   * if show deformation is requested */
};
typedef struct UF_SF_mesh_visuals_s UF_SF_mesh_visuals_t, *UF_SF_mesh_visuals_p_t;

typedef struct  UF_SF_AMM_mesh_parameters_s  *UF_SF_AMM_mesh_parameters_p_t;


/* Idealize types */
typedef void *UF_SF_idealize_parms_p_t;
typedef void *UF_SF_idealize_region_p_t;

/*****************************************************************************
  Structure defining the parameters of a defeature feature.
******************************************************************************/
struct  UF_SF_defeature_parms_s
{
    int                 num_ret_faces;        /* Number of retained faces in the
                                                 retained_faces array.  Can be 0
                                              */
    tag_t              *retained_faces;       /* Array of retained faces.
                                                 Will be NULL if  num_ret_faces == 0
                                              */
    int                 num_rem_faces;        /* Number of removed faces in the
                                                 removed_faces array.  Can be 0
                                              */
    tag_t              *removed_faces;        /*  Array of removed faces.
                                                  Will be NULL if num_rem_faces == 0
                                              */

    UF_SF_idealize_region_p_t region_parms_p; /* Pointer to an instance of
                                                 UF_SF_idealize_region_t structure
                                                 that defines a region on the
                                                 body or NULL.
                                              */
};
typedef struct  UF_SF_defeature_parms_s UF_SF_defeature_parms_t, * UF_SF_defeature_parms_p_t;


struct UF_SF_resulting_face_pairs_s
{
   tag_t                        face1;
   tag_t                        face2;
   UF_SF_face_subdiv_status_t   relative_status;
};

typedef struct UF_SF_resulting_face_pairs_s  UF_SF_resulting_face_pairs_t,
                                             *UF_SF_resulting_face_pairs_p_t;

struct UF_SF_SURFACE_CONTACT_ANS_data_s {
    int                  closed_stiff_opt;  /* closed stiffness option */
    double               closed_stiff;      /* closed stiffness */
    int                  open_stiff_opt;    /* open   stiffness option */
    double               open_stiff;        /* open stiffness */
    int                  init_closure_opt;  /* initial closure option  */
    double               init_closure;      /* initial closure */
    int                  norm_toler_opt;    /* normal tolerance option */
    double               norm_toler;        /* normal tolerance */
    double               surf_cont_offset;  /* surface contact offset  */
    double               mu;                /* Coefficient of friction */
    int                  cont_type;         /* Contact type Standard,Rough*/

} ;

typedef struct UF_SF_SURFACE_CONTACT_ANS_data_s UF_SF_SURFACE_CONTACT_ANS_data_t,
                                                *UF_SF_SURFACE_CONTACT_ANS_data_p_t;

struct UF_SF_SURFACE_CONTACT_NAS_data_s {

    double               pre_load;       /* pre load */
    double               closed_stiff;   /* closed stiffness */
    double               open_stiff;     /* open stiffness */
    double               kinetic_fric;   /* kenetic friction coefficient */
    double               static_fric;    /* static friction coefficient  */
    double               max_pen;        /* maximum peneration           */
    int                  cont_type;      /* Contact type - Standard,Rough*/
} ;

typedef struct UF_SF_SURFACE_CONTACT_NAS_data_s UF_SF_SURFACE_CONTACT_NAS_data_t,
                                         *UF_SF_SURFACE_CONTACT_NAS_data_p_t;


struct UF_SF_SURFACE_CONTACT_UGFEA_data_s{

    double               pre_load;
    double               closed_stiff;
    double               open_stiff;
    double               kinetic_fric;
    double               static_fric;
    double               max_pen;
    int                  cont_type;
};

typedef struct UF_SF_SURFACE_CONTACT_UGFEA_data_s UF_SF_SURFACE_CONTACT_UGFEA_data_t,
                                           *UF_SF_SURFACE_CONTACT_UGFEA_data_p_t;

/* Defines are left for campatability
   Please use UF_SFANS_algorithm_t instead */
#define   FRONTAL_SOLVER    0
#define   PCG_SOLVER        1
#define   JCG_SOLVER        2
#define   SPARSE_SOLVER     3
#define   JCG_PCG_SOLVER    4
#define   JCG_FRONTAL_SOLVER 5
#define   SUBSPACE_MODOPT    6
#define   LANCZOS_MODOPT     7
#define   POWERDYN_MODOPT    8


#define  UF_SFFEA_ALGORITHM_NUM_TYPES   5


struct UF_SFANS_solver_data_s
{
    int formatChoice;
    int algoChoice;
    int num_roots;
    double upper_limit;
    double lower_limit;
    double temperature;
};
typedef struct UF_SFANS_solver_data_s UF_SFANS_solver_data_t, *UF_SFANS_solver_data_p_t;


#ifdef __cplusplus
}
#endif

struct UF_SFAS_solver_data_s
{
    int algolChoice;
    int typeChoice;
    int codeChoice;
    int echoChoice;
    int num_roots;
    int densityChoice;
    int formatChoice;
    int job_time;
    double temperature;
    tag_t  temperature_unit_tag;
    double upper_limit;
    int    max_iter;
    double err_tol_percent;
    int    min_pvalue;
    int    max_pvalue;
    double lower_limit;
    double sol_tol_val ;
    char jobname[ MAX_FSPEC_BUFSIZE ];
    char titlestring[ MAX_FSPEC_BUFSIZE ];
    char scratch_path[ MAX_FSPEC_BUFSIZE ];
    int  memory_requested ;
    int  num_design_cycles;
    int  frequency_mode_number;
    int  optimizationChoice;
    int  AdaptOpt; /* Added to handle Opt in Adaptivity */
    int  OptTypeChoice;
    UF_SFOPT_solver_type_t solver_types[(int)UF_MAX_NUM_SOLVER_TYPES];
    int  reset_node_elm_id_Choice;
    int  save_after_reset_Choice;
    int  prt_displacements;
    int  prt_stresses;
    int  prt_strains;
    int  prt_strain_energies;
    int  prt_elforces;
    int  prt_reactforces;
    int  prt_applied_loads;
    int  prt_fluxes;
    int  prt_temps;
    double plate_stiffness;
    int inrelChoice;
    int inrel_support_node_id[3];
    SFNAS_inter_output_types_t  intout_flag;
    int componentChoice ;
    int nl_ninc;
    int adaptChoice;
    int adapt_max_itr;
    double adapt_per_error;
    double adapt_dev_error;
    double adapt_elem_size;
    int  PrintOutputLevel;
    int start_elem_id;
    int start_node_id;
    int largeDispChoice;
    logical thermstruct;
    /* Flag set to indicate whether thermostruct env.. this is needed since during solution time
    the env will be changed to structures and then to thermal */
    int     modeChoice;
    int     fatigueChoice;
    int     fatigue_analysis;
    int     fatigue_stress_crit;
    int     fatigue_stress_type;
    int     fatigue_fatigue_crit;
    int     fatigue_cycles;
    double  fatigue_k_factor;
    int     fatigue_life_crit;

};
typedef struct UF_SFAS_solver_data_s UF_SFAS_solver_data_t, *UF_SFAS_solver_data_p_t;



#ifdef __cplusplus
extern "C" {
#endif




/*****************************************************************************
  Structure defining the parameters of a user defined midsurface feature.
******************************************************************************/
struct UF_SF_midsrf_user_parms_s
{
   tag_t   solid_body;       /* Tag of the target solid body. */
   int     num_sheet_bodies; /* Number of sheet bodies.           */
   tag_t  *sheet_bodies_a;   /* <len:num_sheet_bodies>  Array of sheet body tags that will define the
                                midsurface of the selected target solid body.
                                The size of the array is num_sheet_bodies */
   double  thickness;        /* Thickness value to be used at formatting time
                                 whenever the automatic thickness extraction fails. */
   double  const_thickness;  /* Constant thickness of all nodes of the midsurface.
                                If this is provided by the user then this is will be
                                the value used for all nodes at format time in which
                                case the value of the thickness field will be unused.
                                This field is not currently used.  */
};
typedef struct UF_SF_midsrf_user_parms_s UF_SF_midsrf_user_parms_t, *UF_SF_midsrf_user_parms_p_t;


struct UF_SF_geom_options_s
{
    logical     fSyncPoints;
    logical     fSyncCsys;
    logical     fSyncLines;
    logical     fSyncArcs;
    logical     fSyncSplines;
    logical     fSyncSketchCurves;
    logical     fSyncConics;
};
typedef struct UF_SF_geom_options_s UF_SF_geom_options_t, *UF_SF_geom_options_p_t;

/*
UF_SF_MAX_STRING_LEN is being deprecated because NX is moving to support 
multibyte characters. User written programs should start using the 
new definitions:
MAX_LINE_BUFSIZE should be used for buffer allocations and memory 
allocations, e.g. char my_data[MAX_LINE_BUFSIZE]; 
MAX_LINE_NCHARS should be used to limit the number of characters in 
a buffer. NX code will enforce these limits. 
New routines have been added which will help in this transition: 
UF_TEXT_count_characters() will count the number of characters in a buffer. 
UF_TEXT_terminate_chars() will terminate a C string after the given number of characters.
*/

/*  */
#define UF_SF_MAX_STRING_LEN (MAX_LINE_BUFSIZE)
/*  */ 

#ifdef __cplusplus
}
#endif

#endif  /*    UF_SF_TYPES__H_INCLUDED                                   */
