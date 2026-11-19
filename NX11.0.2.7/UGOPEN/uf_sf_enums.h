/*****************************************************************************
             Copyright (c) 1997-2008 Siemens PLM Software
                Unpublished - All Rights Reserved



File Description :

 Enumeration Definitions for the Open C API interface to Advanced Simulation

*****************************************************************************/
#ifndef  UF_SF_ENUMS__H_INCLUDED
#define  UF_SF_ENUMS__H_INCLUDED


#ifdef __cplusplus
extern "C" {
#endif

enum UF_SFNAS_inter_output_types_e
{
        INTOUT_YES = 0,
        INTOUT_NO,
        INTOUT_ALL
};

typedef enum UF_SFNAS_inter_output_types_e UF_SFNAS_inter_output_types_t;
typedef enum UF_SFNAS_inter_output_types_e SFNAS_inter_output_types_t;

enum UF_SF_node_btype_e
{
    UF_SF_NODE_BODYINTERIOR, /* Node on the interior of a body. */
    UF_SF_NODE_EDGE,         /* Node on an edge. */
    UF_SF_NODE_FACEINTERIOR, /* Node on the interior of a face. */
    UF_SF_NODE_INTERIOR,     /* Interior node. */
    UF_SF_NODE_NO_GEOMETRY,  /* Node not on any geometry. */
    UF_SF_NODE_POINT         /* Node on point. The point could be on
                                Edge or Face, but the node on point
                                is not a part of mesh on edge/face.  */
};

typedef enum UF_SF_node_btype_e  UF_SF_node_btype_t,
                                *UF_SF_node_btype_p_t;


enum UF_SF_node_switch_e
{
    UF_SF_SWITCH_ON_BOUNDARY,  /* Switch to nodes only on the boundary. */
    UF_SF_SWITCH_IN_INTERIOR,  /* Switch to nodes only in the interior. */
    UF_SF_SWITCH_ALL           /* Switch to all nodes, independent of the
                                  location. */
};
typedef enum UF_SF_node_switch_e  UF_SF_node_switch_t,
                                 *UF_SF_node_switch_p_t;

enum UF_SF_mid_node_type_e
{
    UF_SF_NODE_CORNER,    /* Node on the corner. */
    UF_SF_NODE_DISABLED,  /* Node disabled. */
    UF_SF_NODE_MID,       /* Node on the middle. */
    UF_SF_NODE_ORIENTATION /* Node with an orientation. */
};
typedef enum UF_SF_mid_node_type_e  UF_SF_mid_node_type_t,
                                   *UF_SF_mid_node_type_p_t;


/* meshdir codes associated with mesh geometry in a mesh recipe */
enum UF_SF_mesh_geom_meshdir_e
{
    UF_SF_MG_MESHDIR_UNINITIALIZED = 0, /* Uninitialized mesh direction.   */
    UF_SF_MG_MESHDIR_UNDEFINED,         /* Undefined mesh direction. */
    UF_SF_MG_MESHDIR_FROM_START,        /* Mesh direction from line start */
    UF_SF_MG_MESHDIR_FROM_END,          /* Mesh direction from line end   */
    UF_SF_MG_MESHDIR_REVERSE,           /* Reverse the mesh direction */
    UF_SF_MG_MESHDIR_DONT_REVERSE       /* Do not reverse the mesh direction. */
};
typedef enum UF_SF_mesh_geom_meshdir_e  UF_SF_mesh_geom_meshdir_t,
                                       *UF_SF_mesh_geom_meshdir_p_t;

enum UF_SF_mesh_recipe_adaptivity_e
{
    UF_SF_MESH_RECIPE_ADAPT_HELMS, /* Adaptivity of elements is H-type. */
    UF_SF_MESH_RECIPE_ADAPT_PELMS /* Adaptivity of elements is P-type. */
};
typedef enum UF_SF_mesh_recipe_adaptivity_e  UF_SF_mesh_recipe_adaptivity_t,
                                            *UF_SF_mesh_recipe_adaptivity_p_t;

enum UF_SF_elm_adaptivity_type_e
{
    UF_SF_ELEMENT_ADAPT_HELMS = (int)UF_SF_MESH_RECIPE_ADAPT_HELMS,
                                /* Adaptivity of elements is H-type. */
    UF_SF_ELEMENT_ADAPT_PELMS = (int)UF_SF_MESH_RECIPE_ADAPT_PELMS
                                /* Adaptivity of elements is P-type. */
};
typedef enum UF_SF_elm_adaptivity_type_e  UF_SF_elm_adaptivity_type_t,
                                         *UF_SF_elm_adaptivity_type_p_t;


enum UF_SF_element_type_e
{
     UF_SF_UNDEFINED = 0,/* Generic undefined type. */
     UF_SF_CMASS = 1,    /* Concentrated mass element. */
     UF_SF_BAR = 2,      /* Bar element. */
     UF_SF_BEAM = 3,     /* Beam element. */
     UF_SF_ROD = 4,      /* Rod element. */
     UF_SF_RBE2 = 5,     /* Rigid link element. */
     UF_SF_SPRING = 6,   /* Spring element. */
     UF_SF_MASS = 7,     /* Distributed mass element. */
     UF_SF_HBDY = 8,     /* Heat body element. */
     UF_SF_QUAD4 = 9,    /* Quadrilateral element with 4 nodes. */
     UF_SF_TRIA3 = 10,   /* Triangular element with 3 nodes. */
     UF_SF_QUAD8 = 11,   /* Quadrilateral element with 8 nodes. */
     UF_SF_TRIA6 = 12,   /* Triangular element with 6 nodes. */
     UF_SF_TET4 = 13,    /* Tetrahedral element with 4 nodes. */
     UF_SF_TET10 = 14,    /* Tetrahedral element with 10 nodes. */
     UF_SF_1D_CONTACT=15, /* 1D contact elements between 2 bodies. */
     UF_SF_HEX8 = 16,     /* Hexahedral element with 8 nodes. */
     UF_SF_HEX20 = 17,    /* Hexahedral element with 20 nodes. */
     UF_SF_WDG6  = 18,    /* Wedge element with 6 nodes. */
     UF_SF_WDG15 = 19,    /* Wedge element with 15 nodes. */
     UF_SF_2D_CONTACT = 20, /* 2D Contact elements between 2 faces */
     UF_SF_WELD = 21,        /* weld elements */
     UF_SF_EF_CONN = 22,  /* Edge-Face connection element */
     UF_SF_MM_FREE = 23,  /* Not an element type but useful as connection. */
     UF_SF_MM_GLUE = 24,  /* Not an element type but useful as connection. */
     UF_SF_RBE3 = 25,     /* rbe3 element with 1 core node (first node) and multiple leg nodes. */
     UF_SF_PYR5 = 26,     /* Pyramid element with 5 nodes. */
     UF_SF_PYR9 = 27,     /* Pyramid element with 9 nodes. */
     UF_SF_PYR13 = 28,    /* Pyramid element with 13 nodes. */
     UF_SF_1D_NG = 29,    /* 1D Node to Ground elements with 1 node. */
     UF_SF_1D_PLOTEL = 30,/* 1D plotel element with 2 nodes. */
     UF_SF_1D_MASS = 31,  /* 1D mass element with 2 nodes. */
     UF_SF_PYR_MIXED_ORDER = 32, /* Pyramid element mixed order. */
     UF_SF_TET_MIXED_ORDER = 33, /* Tetrahedral element mixed order. */
     UF_SF_1D_BEARING = 34,
     UF_SF_HEXCOHES8 = 35,     /* cohesive element with 8 nodes. */
     UF_SF_HEXCOHES20 = 36,    /* cohesive element with 20 nodes. */
     UF_SF_WDGCOHES6 = 37,     /* cohesive element with 6 nodes. */
     UF_SF_WDGCOHES15 = 38,    /* cohesive element with 15 nodes. */

/*   
*/

     UF_SF_TOTAL_COUNT = 39 /* This last member represents the total
                               number of members in this enum */
};
typedef enum UF_SF_element_type_e  UF_SF_element_type_t,
                                  *UF_SF_element_type_p_t;

enum UF_SF_mesh_dimension_e
{
  UF_SF_DIMENSION_0D,    /* Element dimension is 0 - CMASS or MASS */
  UF_SF_DIMENSION_1D,    /* Element dimension is 1 - Bar, beam, rods, rigid
                            links, springs and contact elements. */
  UF_SF_DIMENSION_2D,    /* Element dimension is 2 - quad4, quad8, tri3, tri6 */
  UF_SF_DIMENSION_3D,    /* Element dimension is 3 - tet4, tet10. */
  UF_SF_DIMENSION_ANY    /* Element of any dimension. */
};
typedef enum UF_SF_mesh_dimension_e  UF_SF_mesh_dimension_t,
                                    *UF_SF_mesh_dimension_p_t;


enum UF_SF_elm_dimension_type_e
{
    UF_SF_ELEMENT_POINT = (int)UF_SF_DIMENSION_0D, /* Element type is point - CMASS
                                                      or MASS. */
    UF_SF_ELEMENT_BEAM  = (int)UF_SF_DIMENSION_1D, /* Element type is beam - Bar,
                                                      beam, rods, rigid links,
                                                      springs and contact elements.*/
    UF_SF_ELEMENT_SHELL = (int)UF_SF_DIMENSION_2D, /* Element type is shell - quad4,
                                                      quad8, tri3, tri6. */
    UF_SF_ELEMENT_SOLID = (int)UF_SF_DIMENSION_3D, /* Element type is solid - tet4,
                                                      tet10. */
    UF_SF_ELEMENT_ALL                         /* Element of any of the 4 above
                                                 types. */
};
typedef enum UF_SF_elm_dimension_type_e  UF_SF_elm_dimension_type_t,
                                        *UF_SF_elm_dimension_type_p_t;


enum UF_SF_section_type_e
{
  UF_SF_SECTION_TWREC = 0,    /* Thin wall, rectangle                 */
  UF_SF_SECTION_TWCYL,        /* Thin wall, cylinder                  */
  UF_SF_SECTION_TWCHA,        /* Thin wall, channel                   */
  UF_SF_SECTION_TWHAT,        /* Thin wall, hat                       */
  UF_SF_SECTION_TWIBE,        /* Thin wall, I beam                    */
  UF_SF_SECTION_SOCYL,        /* Solid, cylinder                      */
  UF_SF_SECTION_SOREC,        /* Solid, rectangle                     */
  UF_SF_SECTION_KEYIN,        /* User defined.                        */
  UF_SF_SECTION_USER_TW,      /* User Defined TW                      */
  UF_SF_SECTION_USER_SOLID,   /* User Defined Solid                   */
  UF_SF_SECTION_NUM_TYPES
};
typedef enum UF_SF_section_type_e  UF_SF_section_type_t,
                                  *UF_SF_section_type_p_t;

/*  */
enum UF_SF_neutral_material_types_e
{
    UF_SF_MATERIAL_ISOTROPIC = 0,           /* Material is isotropic.               */
    UF_SF_MATERIAL_ORTHOTROPIC = 1,         /* Material is orthotropic.             */
    UF_SF_MATERIAL_ANISOTROPIC = 2,         /* Material is anisotropic.             */
    UF_SF_MATERIAL_FORMABILITY = 3,         /* Formability properties.              */
    UF_SF_MATERIAL_FLUID = 4,               /* Fluid material.                      */
    UF_SF_MATERIAL_HYPERELASTIC = 5,        /* General Hyperelastic Material        */
    UF_SF_MATERIAL_MOONEYRIVLIN=6,          /* Mooney Rivlin                        */
    UF_SF_MATERIAL_MOONEYRIVLINTESTDATA=7,  /* Mooney Rivlin - test data option     */
    UF_SF_MATERIAL_POLYNOMIAL=8,            /* Polynomial                           */
    UF_SF_MATERIAL_REDUCEDPOLYNOMIAL=9,     /* Reduced Polynomial                   */
    UF_SF_MATERIAL_OGDEN=10,                /* Ogden                                */
    UF_SF_MATERIAL_OGDENTESTDATA=11,        /* Ogden - test data option             */
    UF_SF_MATERIAL_FOAM=12,                 /* Foam                                 */
    UF_SF_MATERIAL_FOAMTESTDATA=13,         /* Foam - test data option              */
    UF_SF_MATERIAL_BLATZ=14,                /* Blatz-Ko                             */
    UF_SF_MATERIAL_ARRUDABOYCE=15,          /* Arruda-Boyce                         */
    UF_SF_MATERIAL_ARRUDABOYCETESTDATA=16,  /* Arruda-Boyce - test data option      */
    UF_SF_MATERIAL_NEOHOOKE=17,             /* Neo Hooke                            */
    UF_SF_MATERIAL_NEOHOOKETESTDATA=18,     /* Neo Hooke - test data option         */
    UF_SF_MATERIAL_MARLOW=19,               /* Marlow                               */
    UF_SF_MATERIAL_VANDERWAALS=20,          /* Van Der Waals                        */
    UF_SF_MATERIAL_YEOH=21,                 /* Yeoh                                 */
    UF_SF_MATERIAL_YEOHTESTDATA=22,         /* Yeoh - test data option              */
    UF_SF_MATERIAL_GENT=23,                 /* Gent                                 */
    UF_SF_MATERIAL_GASKET=24,               /* Gasket                               */
    UF_SF_MATERIAL_GASKETBEHAVIOR=25,       /* Gasket Behavior                      */
    UF_SF_MATERIAL_SHAPEMEMORYALLOY=26,     /* Shape Memory Alloy                   */
    UF_SF_MATERIAL_SUSSMANBATHE=27,         /* Sussman-Bathe hyperelastic material  */
    UF_SF_MATERIAL_GASKETDISPLACEMENT=28,   /* Gasket with length-based loading     */
    UF_SF_MATERIAL_DAMAGEINTERFACE=29,      /* Damage interface material            */
    UF_SF_MATERIAL_MULTIPLEFLUID=30,        /* Multiple fluid material              */
    UF_SF_MATERIAL_HARTSMITH=31,            /* Hart-Smith material                  */
    UF_SF_MATERIAL_ALEXANDER=32,            /* Alexander material                   */
    UF_SF_MATERIAL_CURING=33,               /* Curing material                      */
    UF_SF_MATERIAL_POROUS=35              /* Porous material                      */
};
typedef enum UF_SF_neutral_material_types_e  UF_SF_neutral_material_types_t,
                                            *UF_SF_neutral_material_types_p_t;

/* Extended material types.                                            */
enum UF_SF_matl_orient_option_e
{
    UF_SF_MATL_ORIENT_FIXED,        /* Origin/vectors option           */
    UF_SF_MATL_ORIENT_WCS           /* Create an orientation based
                                       upon the current WCS.           */
};
typedef enum UF_SF_matl_orient_option_e  UF_SF_matl_orient_option_t,
                                        *UF_SF_matl_orient_option_p_t;

/* Coordinate system type.                                              */
enum UF_SF_fem_coord_type_e
{
    UF_SF_RECT_COORD
};
typedef enum UF_SF_fem_coord_type_e  UF_SF_fem_coord_type_t,
                                    *UF_SF_fem_coord_type_p_t;


enum UF_SF_multi_prop_type_e
{
    UF_SF_MULTI_PROP_TABLE,   /* Tabular form of variable material properties.*/
    UF_SF_MULTI_PROP_EXPRESSION /* Variation of material properties is through
                                   an expression. */
};
typedef enum UF_SF_multi_prop_type_e  UF_SF_multi_prop_type_t,
                                     *UF_SF_multi_prop_type_p_t;


enum UF_SF_library_material_e
{
    UF_SF_MATL_IS_READ_ONLY,        /* User not allowed to edit in NX. */
    UF_SF_MATL_IS_EDITABLE          /* User allowed to edit within NX. */
};
typedef enum UF_SF_library_material_e  UF_SF_library_material_t,
                                      *UF_SF_library_material_p_t;

enum UF_SF_mesh_geom_usage_e
{
    UF_SF_GEOM_ANY,           /* all geometry                          */
    UF_SF_GEOM_HARD,          /* hard geometry                         */
    UF_SF_GEOM_CONNECT_A,     /* group1 geometry                       */
    UF_SF_GEOM_CONNECT_B      /* group2 geometry                       */
};
typedef enum UF_SF_mesh_geom_usage_e  UF_SF_mesh_geom_usage_t,
                                      *UF_SF_mesh_geom_usage_p_t;

enum UF_SF_edge_density_type_e
{
  UF_SF_EDGE_DENSITY_SIZE,    /* Edge density defined by elm size      */
  UF_SF_EDGE_DENSITY_NUMBER,  /* Edge density defined by number of elms. */
  UF_SF_EDGE_DENSITY_SMART = 4,  /* Edge density defined by smart option. */
  UF_SF_NOT_EDGE_DENSITY_DEFINED /* Edge density not defined. */
};
typedef enum UF_SF_edge_density_type_e  UF_SF_edge_density_type_t,
                                       *UF_SF_edge_density_type_p_t;


/* The definition method for numeric values.                            */
enum UF_SF_numeric_method_e
{
  UF_SF_NUMERIC,              /* Numeric value                        */
  UF_SF_EXPRESSION            /* Expression string used.              */
};
typedef enum UF_SF_numeric_method_e  UF_SF_numeric_method_t,
                                    *UF_SF_numeric_method_p_t;


/* The smart point definition method.                                   */
enum UF_SF_HPT_method_e
{
    UF_SF_HPT_NO_METHOD,          /* Smart point created with no method. */
    UF_SF_HPT_ON_CURVE,           /* Smart point created on curve. */
    UF_SF_HPT_BASEPT_AND_OFFSET,  /* Smart point created as offset to some base
                                     point. */
    UF_SF_HPT_CENTER_OF_CONIC,    /* Smart point created at the center of a
                                     conic. */
    UF_SF_HPT_CURVE_INTERSECTION, /* Smart point created at the intersection of
                                     two curves. */
    UF_SF_HPT_ON_SURFACE          /* Smart point created on a surface. */
};
typedef enum UF_SF_HPT_method_e  UF_SF_HPT_method_t,
                                *UF_SF_HPT_method_p_t;

/* The 0d mesher element types.                                         */
enum UF_SF_0D_element_type_e
{
    UF_SF_0D_CONMASS = (int)UF_SF_CMASS /* 0D element type - concentrated mass. */
};
typedef enum UF_SF_0D_element_type_e  UF_SF_0D_element_type_t,
                                     *UF_SF_0D_element_type_p_t;


/* The 0d mesher element density.                                       */
enum UF_SF_0D_density_type_e
{
    UF_SF_0D_EDGE_DENSITY_SIZE,     /* Edge density given as size of the
                                       elements. */
    UF_SF_0D_EDGE_DENSITY_NUMBER,   /* Edge density given as number of the
                                       elements. */
    UF_SF_0D_EDGE_DENSITY_SMART = 4
};
typedef enum UF_SF_0D_density_type_e  UF_SF_0D_density_type_t,
                                     *UF_SF_0D_density_type_p_t;

/* The 1d mesher element types.                                         */
enum UF_SF_1D_element_type_e
{
    UF_SF_1D_SPRING_TYPE = (int)UF_SF_SPRING,   /* Spring elements. */
    UF_SF_1D_BAR_TYPE = (int)UF_SF_BAR,         /* Bar elements. */
    UF_SF_1D_BEAM_TYPE = (int)UF_SF_BEAM,       /* Beam elements. */
    UF_SF_1D_ROD_TYPE = (int)UF_SF_ROD,         /* Rod elements. */
    UF_SF_1D_RIGID_TYPE = (int)UF_SF_RBE2       /* Rigid link elements. */
};
typedef enum UF_SF_1D_element_type_e  UF_SF_1D_element_type_t,
                                     *UF_SF_1D_element_type_p_t;


/* The 1d mesher element density.                                       */
enum UF_SF_1D_density_type_e
{
    UF_SF_1D_EDGE_DENSITY_SIZE,      /* Edge density given as a size of the
                                        elements. */
    UF_SF_1D_EDGE_DENSITY_NUMBER,    /* Edge density given as number of the
                                        elements. */
    UF_SF_1D_EDGE_DENSITY_SMART = 4

};
typedef enum UF_SF_1D_density_type_e  UF_SF_1D_density_type_t,
                                     *UF_SF_1D_density_type_p_t;


/* The Load functions mode_type parameter.                              */
enum UF_SF_load_mode_e
{
    UF_SF_LOAD_FORCE =  1,         /* Force. */
    UF_SF_LOAD_DISTRIBUTED =  2,   /* Uniform pressure, applicable only normal
                                      to the face. */
    UF_SF_LOAD_SPACIAL =  3,
    UF_SF_LOAD_GRAVITY =  4,       /* Gravity load. */
    UF_SF_LOAD_PRESSURE =  5,      /* Pressure load, can be appied in any
                                      direction. */
    UF_SF_LOAD_MOMENT =  6,        /* Moment. */
    UF_SF_LOAD_SHEAR =  7,         /* Edge shear. */
    UF_SF_LOAD_FLUX =  8,          /* Heat flux. */
    UF_SF_LOAD_TEMPERATURE =  9,  /* Temperature load. */
    UF_SF_LOAD_CENTRIFUGAL = 10,    /* Centrifugal load. */
    UF_SF_LOAD_TORQUE = 11,         /* Torque */
    UF_SF_LOAD_BEARING = 12,         /* Bearing */

    UF_SF_LOAD_UNKNOWN_MODE = -99999   /* Unknown load mode type */
};
typedef enum UF_SF_load_mode_e  UF_SF_load_mode_t,
                               *UF_SF_load_mode_p_t;


/* The Load functions load_class parameter.                             */
enum UF_SF_load_class_e
{
    UF_SF_LOAD_NODE_ELEMENT_CLASS = 1,  /* Load applied on a node. */
    UF_SF_LOAD_EDGE_ELEMENT_CLASS = 2,  /* Load applied on an edge. */
    UF_SF_LOAD_FACE_CLASS = 3,          /* Load applied on a face. */
    UF_SF_LOAD_PART_CLASS = 4,          /* Load applied to the whole part. */
    UF_SF_LOAD_BODY_CLASS = 5,          /* Load applied on a body. */
    UF_SF_LOAD_CURVE_CLASS = 6          /* Load applied on a curve. */
};
typedef enum UF_SF_load_class_e  UF_SF_load_class_t,
                                *UF_SF_load_class_p_t;

/* The BC functions class parameter.                                    */
enum UF_SF_bc_class_e
{
    UF_SF_BC_ERROR_CLASS = -1, /* To indicate error */
    UF_SF_BC_NODE_ELEMENT_CLASS = 1, /* BC applied on a node. */
    UF_SF_BC_EDGE_ELEMENT_CLASS = 2, /* BC applied on an edge. */
    UF_SF_BC_FACE_CLASS = 3,         /* BC applied on a face. */
    UF_SF_BC_CURVE_CLASS = 4         /* BC applied on a curve. */
};
typedef enum UF_SF_bc_class_e  UF_SF_bc_class_t,
                              *UF_SF_bc_class_p_t;


/* The Load functions load_disp_symbol parameter.                       */
enum UF_SF_load_disp_symbol_e
{
    UF_SF_LOAD_SINGLE_HEADED_ARROW = 1,
    UF_SF_LOAD_DOUBLE_HEADED_ARROW = 2,
    UF_SF_LOAD_HALF_ARROW = 3,
    UF_SF_LOAD_Q_ARROW = 4,
    UF_SF_BC_PYRAMID = 101,
    UF_SF_BC_ARROW = 102,
    UF_SF_BC_DOUBLE_HEADED_ARROW = 103,
    UF_SF_BC_SMALL_CIRCLE = 104,
    UF_SF_BC_SMALL_ARROW = 105,
    UF_SF_BC_S_ON_ENTITY = 106,
    UF_SF_BC_M_ON_ENTITY = 107
};
typedef enum UF_SF_load_disp_symbol_e  UF_SF_load_disp_symbol_t,
                                      *UF_SF_load_disp_symbol_p_t;



/* The Load functions component_type parameter.                         */
enum UF_SF_LBC_component_type_e
{
    UF_SF_NULL_COMP = -1,
    UF_SF_LBC_XYZ = 0,   /* Having XYZ components - rectangular coordinates. */
    UF_SF_LBC_RTZ,       /* Having RTZ components - Cylindrical coordinates. */
    UF_SF_LBC_RTP,       /* Having RTP components - Spherical coordinates. */
    UF_SF_LBC_NORMAL_TO, /* Applicable normal to a face only. */
    UF_SF_LBC_EDGE_CSYS  /* Applicable along an edge only. */
};
typedef enum UF_SF_LBC_component_type_e  UF_SF_LBC_component_type_t,
                                        *UF_SF_LBC_component_type_p_t;

enum UF_SF_load_dimension_e
{
    UF_SF_NULL_LOAD = 0,    /* Load value is 0. */
    UF_SF_SCALAR_LOAD,      /* Load is a scalar - temperature. */
    UF_SF_VECTOR_LOAD,      /* Having RTP components - Spherical coordinates. */
    UF_SF_AXIS_LOAD         /* Applicable normal to a face only. */
};
typedef enum UF_SF_load_dimension_e  UF_SF_load_dimension_t,
                                    *UF_SF_load_dimention_p_t;


/* The BC functions mode parameter.                                     */
enum UF_SF_bc_mode_e
{
    UF_SF_BC_CONSTRAINT = 1,            /* Both linear displacement and rotation
                                           are available. */
    UF_SF_BC_DISPLACEMENT = 2,          /* Only displacement is available,
                                           rotation is free. */
    UF_SF_BC_ROTATION = 3,              /* Only rotation is available,
                                           displacement is free. */
    UF_SF_BC_TEMPERATURE = 4,           /* Temperature BC is available. */
    UF_SF_BC_CONVECTION_COEFFICIENT = 5,/* Convection coefficient BC is
                                           available. */

    UF_SF_BC_UNKNOWN_MODE = -99999      /* Unknown BC mode type */
};
typedef enum UF_SF_bc_mode_e  UF_SF_bc_mode_t,
                             *UF_SF_bc_mode_p_t;


/* The Durability Event mode parameter.                                     */
enum UF_SF_dur_event_mode_e
{
    UF_SF_DUR_EVENT_STATIC = 1    /* Currently we only have Static Durability Events */
};
typedef enum UF_SF_dur_event_mode_e  UF_SF_dur_event_mode_t,
                             *UF_SF_dur_event_mode_p_t;

/* geometry types */
enum UF_SF_mesh_geometry_types_e
{
    UF_SF_GEOM_OTHER,  /* Geometry does not fall into any of the categories
                          listed below. */
    UF_SF_GEOM_ASSEM,  /* Geometry is an assembly. */
    UF_SF_GEOM_COMPON, /* Geometry is a component. */
    UF_SF_GEOM_OCC,    /* Geometry is an occurrence. */
    UF_SF_GEOM_BODY,   /* Geometry is a body. */
    UF_SF_GEOM_FACE,   /* Geometry is a face. */
    UF_SF_GEOM_EDGE,   /* Geometry is an edge. */
    UF_SF_GEOM_SURF ,   /* Geometry is a surface. */
    UF_SF_GEOM_CURVE,   /* Geometry is a curve. */
    UF_SF_GEOM_POINT,  /* Geometry is a point. */
    UF_SF_GEOM_VERTEX,  /* Geometry is a vertex. */
    UF_SF_GEOM_COMPOSITE_BODY, /* Geometry is a composite body */
    UF_SF_GEOM_COMPOSITE_FACE, /* Geometry is a composite face */
    UF_SF_GEOM_COMPOSITE_EDGE  /* Geometry is a composite edge */
};
typedef enum UF_SF_mesh_geometry_types_e  UF_SF_mesh_geometry_types_t,
                                         *UF_SF_mesh_geometry_types_p_t;

enum UF_SF_LANG_analysis_type_e
{
    UF_SF_LANG_ANALYSIS_UNKNOWN    = 0,     /* unknown language type */
    UF_SF_LANG_ANALYSIS_STRUCTURAL = 1,     /* Structural analysis */
    UF_SF_LANG_ANALYSIS_THERMAL = 2,        /* Thermal analysis */
    UF_SF_LANG_ANALYSIS_FLOW = 3,           /* CFD analysis */
    UF_SF_LANG_ANALYSIS_COUPLED = 4,        /* Flow-Thermal analysis */
    UF_SF_LANG_ANALYSIS_MAPPING = 5         /* Mapping analysis */
};
typedef enum UF_SF_LANG_analysis_type_e  UF_SF_LANG_analysis_type_t,
                                        *UF_SF_LANG_analysis_type_p_t;


enum UF_SF_LANG_problem_abstract_e
{
    UF_SF_LANG_SIMPLE_PROB_ABSTRACT = 1,
    UF_SF_LANG_AXISYM_PROB_ABSTRACT = 2,
    UF_SF_LANG_MIXED_PROB_ABSTRACT  = 3
};
typedef enum UF_SF_LANG_problem_abstract_e  UF_SF_LANG_problem_abstract_t,
                                           *UF_SF_LANG_problem_abstract_p_t;

enum UF_SF_LANG_linearity_e
{
    UF_SF_LANG_LINEAR_LINEARITY = 1,
    UF_SF_LANG_NONLINEAR_LINEARITY = 2
};
typedef enum UF_SF_LANG_linearity_e  UF_SF_LANG_linearity_t,
                                    *UF_SF_LANG_linearity_p_t;


enum UF_SF_LANG_time_depend_e
{
    UF_SF_LANG_STEADY_TIME_DEPEND = 1  /* Analysis will be steady-state. */
};
typedef enum UF_SF_LANG_time_depend_e  UF_SF_LANG_time_depend_t,
                                      *UF_SF_LANG_time_depend_p_t;


/*  Element types supported by Aries Tet Mesher  */
enum UF_SF_atm_element_types_e
{
    UF_SF_ATM_SYSTEM_DEFAULT_TYPE = 0, /* Element will be system default,
                                          either tet4 or tet10, depending on the
                                          enviroment. */
    UF_SF_ATM_TETRA,                   /* Element will be tetrahedral, with 4
                                          nodes. */
    UF_SF_ATM_TETRA_10                 /* Element will be tetrahedral, with 10
                                          nodes. */
};
typedef enum UF_SF_atm_element_types_e UF_SF_atm_element_types_t;

/*  Aries Tet Mesher edge shapes  */
enum UF_SF_atm_edge_shape_types_e
{
    UF_SF_ATM_LINEAR = 0, /* Type of element is linear. */
    UF_SF_ATM_CURVED,     /* Type of element is curved. */
    UF_SF_ATM_MIXED       /* Both curved and linear elements can form. */
};
typedef enum UF_SF_atm_edge_shape_types_e UF_SF_atm_edge_shape_types_t;



/********************************* ATM parameters *****************************/

enum UF_SF_sfqm_elem_type_e
{
  UF_SF_SFQM_QUAD4,
  UF_SF_SFQM_TRIA3,
  UF_SF_SFQM_QUAD8,
  UF_SF_SFQM_TRIA6
};
typedef enum UF_SF_sfqm_elem_type_e  UF_SF_sfqm_elem_type_t,
                                    *UF_SF_sfqm_elem_type_p_t;


/* Distribution type */
typedef enum
{
   UF_SF_SINUSOIDAL = 0,
   UF_SF_PARABOLIC
} UF_SF_dist_type_t;


/* Mating Type */
enum UF_SF_mate_type_e
{
    UF_SF_NOT_SUPPORT_MATE_TYPE = 0,
    UF_SF_ASSEMBLY_MESH
};
typedef enum UF_SF_mate_type_e  UF_SF_mate_type_t,
                               *UF_SF_mate_type_p_t;

/* Assembly Mesh Type */
enum UF_SF_assembly_type_e
{
    UF_SF_NOT_SUPPORT_ASSEM_TYPE = 0,
    UF_SF_ASSEM_BY_GLUE,
    UF_SF_ASSEM_BY_SLIDE_CONTACT,
    UF_SF_ASSEM_BY_GAP_CONTACT,
    UF_SF_ASSEM_FREE
};
typedef enum UF_SF_assembly_type_e  UF_SF_assembly_type_t,
                                   *UF_SF_assembly_type_p_t;

enum UF_SF_edge_matching_type_e
{
    UF_SF_EDGE_MATCHING_TYPE_ND,
    UF_SF_EDGE_MATCHING_BY_LOCATION,
    UF_SF_EDGE_MATCHING_BY_ESIZE,
    UF_SF_EDGE_MATCHING_BY_COLLAPSE,
    UF_SF_EDGE_MATCHING_MM_GLUE,
    UF_SF_EDGE_MATCHING_MM_FREE,
    UF_SF_EDGE_MATCHING_ANY
};

typedef enum UF_SF_edge_matching_type_e  UF_SF_edge_matching_type_t,
                                        *UF_SF_edge_matching_type_p_t;


typedef enum
{
     UF_SF_IDEALIZE_HOLE_DIAMETER,
     UF_SF_IDEALIZE_BLEND_RADIUS,
     UF_SF_IDEALIZE_TINY_FACE_AREA,
     UF_SF_IDEALIZE_THIN_FACE_WIDTH,
     UF_SF_IDEALIZE_FACE_COLLECTOR,
     UF_SF_IDEALIZE_SCREEN_SELECTED_FACE
} UF_SF_idealize_parm_exp_t;

typedef enum
{
     UF_SF_IDEALIZE_RETAINED_FACES,
     UF_SF_IDEALIZE_REMOVED_FACES
} UF_SF_idealize_parm_face_t;
#define UF_SF_SEPERATE_FACES UF_SF_SEPARATE_FACES
enum UF_SF_face_subdiv_status_e
{
   UF_SF_IDENTICAL_FACES_EQ_EDGES,  /* Both faces identical with eq. num of edges   */
   UF_SF_IDENTICAL_FACES_UNEQ_EDGES,/* Both faces identical with uneq. num of edges */
   UF_SF_NOT_IDENTICAL,             /* Both faces are not identical                 */
   UF_SF_OVERLAPPING_FACES,         /* Both faces overlapping                       */
   UF_SF_SEPARATE_FACES             /* Both faces are separate                      */
};

typedef enum UF_SF_face_subdiv_status_e UF_SF_face_subdiv_status_t,
                                        *UF_SF_face_subdiv_status_p_t;


typedef enum
{
    UF_SFANS_NULL_SOLVER = -1,
    UF_SFANS_FRONTAL_SOLVER = 0,
    UF_SFANS_PCG_SOLVER,
    UF_SFANS_JCG_SOLVER,
    UF_SFANS_SPARSE_SOLVER,
    UF_SFANS_JCG_PCG_SOLVER,
    UF_SFANS_JCG_FRONTAL_SOLVER,
    UF_SFANS_SUBSPACE_MODOPT_SOLVER,
    UF_SFANS_LANCZOS_MODOPT_SOLVER,
    UF_SFANS_POWERDYN_MODOPT_SOLVER,
    UF_SFANS_NUM_ALGORITHM_TYPES
} UF_SFANS_algorithm_t, *UF_SFANS_algorithm_p_t;

typedef enum
{
    UF_SFFEA_AUTOMATIC                               = -1,
    UF_SFFEA_DIRECT_IN_CORE                          = 0,
    UF_SFFEA_DIRECT_OUT_OF_CORE                      = 2,
    UF_SFFEA_ITERATIVE_IN_CORE                       = 6,
    UF_SFFEA_ITERATIVE_OUT_OF_CORE                   = 8,
    UF_SFFEA_SPARSE                                  = 10,
    UF_SFFEA_ITERATIVE                               = 11
} UF_SFFEA_algorithm_t, *UF_SFFEA_algorithm_p_t;

typedef enum
{
    UF_SFOPT_NULL_SOLVER_TYPE = -1,
    UF_SFOPT_GENERIC_SOLVER_TYPE = 0,
    UF_SFOPT_SENSITIVITY_SOLVER_TYPE = 1,
    UF_SFOPT_HYPEROPT_SOLVER_TYPE = 2,
    UF_MAX_NUM_SOLVER_TYPES = 3
} UF_SFOPT_solver_type_t, *UF_SFOPT_solver_type_p_t;

#ifdef __cplusplus
}
#endif

/* The Load functions mode_type parameter.                              */
enum UF_SF_lv_function_mode_e
{
    UF_SF_HALF_UNIT_CYCLE =  0,   /* Half Unit Cycle */
    UF_SF_FULL_UNIT_CYCLE =  1    /* Full Unit Cycle */
};
typedef enum UF_SF_lv_function_mode_e  UF_SF_lv_function_mode_t,
                                      *UF_SF_lv_function_mode_p_t;


#ifdef __cplusplus
extern "C" {
#endif

typedef enum
{
    UF_MODE_TYPE = 0,
    UF_MODE_AND_FREQUENCY_RANGE_TYPE,
    UF_FREQUENCY_RANGE_TYPE,
    UF_SFAS_MAX_MODE_CHOICES
} UF_SFAS_mode_type_t, *UF_SFAS_mode_type_p_t;

typedef enum
{
    UF_SF_mesh_info = 0,                  /* export info about meshes */
    UF_SF_load_info = 1,                  /* export info about loads */
    UF_SF_solution_info = 2,              /* export info about solutions */
    UF_SF_step_info = 3,                  /* export info about steps */
    UF_SF_boundary_condition_info = 4,    /* export info about boundary
                                             conditions. */
    UF_SF_material_info = 5,              /* export info about materials
                                             Assigned to a specified entity. */
    UF_SF_section_info = 6,               /* export info about sections */
    UF_SF_mesh_mating_condition_info = 7, /* export info about a mesh mating
                                             condition. */
    UF_SF_fea_summary_info = 8,           /* export a summary including all
                                             fea entities. */
    UF_SF_dur_event_info = 9,             /* export a summary including all
                                             load variations for the event. */
    UF_SF_load_case_info = 10,            /* export info about load cases */
    UF_SF_sim_summary_info = 11           /* export a summary of simulation
                                             entities. */
} UF_SF_scenario_info_t;


/* FEM Property types. */

#define UF_SF_LANG_NIL_VAL_TYPE                   0
#define UF_SF_LANG_INT_VAL_TYPE                   1
#define UF_SF_LANG_SCALAR_VAL_TYPE                2
#define UF_SF_LANG_TEXT_VAL_TYPE                  3
#define UF_SF_LANG_ENUM_VAL_TYPE                  4
#define UF_SF_LANG_COORD_VAL_TYPE                 5
#define UF_SF_LANG_MATERIAL_VAL_TYPE              6
#define UF_SF_LANG_SECTION_VAL_TYPE               7
#define UF_SF_LANG_VECTOR_VAL_TYPE                8
#define UF_SF_LANG_TABLE_VAL_TYPE                 9
#define UF_SF_LANG_LOAD_VAL_TYPE                 10
#define UF_SF_LANG_BNDCOND_VAL_TYPE              11
#define UF_SF_LANG_BOOL_VAL_TYPE                 12
#define UF_SF_LANG_MULTI_STRING_VAL_TYPE         13
#define UF_SF_LANG_FILENAME_VAL_TYPE             14
#define UF_SF_LANG_DIRPATH_VAL_TYPE              15
#define UF_SF_LANG_SSMO_VAL_TYPE                 16
#define UF_SF_LANG_FIELD_VAL_TYPE                17
#define UF_SF_LANG_AXIS_VAL_TYPE                 18
#define UF_SF_LANG_DOF_VAL_TYPE                  19
#define UF_SF_LANG_POINT_VAL_TYPE                20
/*=================================================================

================================================================= */
#define UF_SF_LANG_MULTI_STRING_ITI_VAL_TYPE     23
#define UF_SF_LANG_CAE_SECTION_VAL_TYPE          24
#define UF_SF_LANG_EDGES_ON_FACE_VAL_TYPE        25
#define UF_SF_LANG_SFEM_VECTOR_VAL_TYPE          26
#define UF_SF_LANG_SCALAR_ARRAY_VAL_TYPE         27
#define UF_SF_LANG_ACTION_VAL_TYPE               28
#define UF_SF_LANG_PPT_VAL_TYPE                  29
#define UF_SF_LANG_SSMO_ARRAY_VAL_TYPE           30
#define UF_SF_LANG_TIME_VAL_TYPE                 31
#define UF_SF_LANG_PLYMAT_VAL_TYPE               32
#define UF_SF_LANG_INT_ARRAY_VAL_TYPE            33
#define UF_SF_LANG_EXT_MENU_VAL_TYPE             34
#define UF_SF_LANG_CATALOG_VAL_TYPE              35
#define UF_SF_LANG_GENERAL_FIELD_VAL_TYPE        36
#define UF_SF_LANG_SCALAR_FIELD_VAL_TYPE         37
#define UF_SF_LANG_VECTOR_FIELD_VAL_TYPE         38
#define UF_SF_LANG_MATRIX_VAL_TYPE               39
#define UF_SF_LANG_REGION_VAL_TYPE               40
#define UF_SF_LANG_GROUPREF_VAL_TYPE             41
#define UF_SF_LANG_SELECTREF_VAL_TYPE            42
#define UF_SF_LANG_CAE_SECTION_ORIENT_VAL_TYPE   43
#define UF_SF_LANG_CAE_SECTION_OFFSET_VAL_TYPE   44
#define UF_SF_LANG_TARGETSET_VAL_TYPE            45
#define UF_SF_LANG_CAE_SECTION_REF_VAL_TYPE      46
#define UF_SF_LANG_DOFSETREF_VAL_TYPE            47
#define UF_SF_LANG_ALTERNATE_REP_ARRAY_VAL_TYPE  48
#define UF_SF_LANG_LBCREF_VAL_TYPE               49
#define UF_SF_LANG_PHYSICAL_ARRAY_VAL_TYPE       50
#define UF_SF_LANG_SOLUTIONREF_VAL_TYPE          51
#define UF_SF_LANG_GROUPREF_ARRAY_VAL_TYPE       52
#define UF_SF_LANG_SCALAR_FIELD_TABLE_VAL_TYPE   53
#define UF_SF_LANG_COMPLEX_SCALAR_FIELD_VAL_TYPE 54
#define UF_SF_LANG_SOLUTIONSTEPREF_VAL_TYPE      55
#define UF_SF_LANG_POINT_ARRAY_VAL_TYPE          56
/* FEM Property type parameter. */

typedef enum
{
    UF_SF_FEM_VALUE_NIL                = UF_SF_LANG_NIL_VAL_TYPE,
    UF_SF_FEM_VALUE_INT                = UF_SF_LANG_INT_VAL_TYPE,
    UF_SF_FEM_VALUE_SCALAR             = UF_SF_LANG_SCALAR_VAL_TYPE,
    UF_SF_FEM_VALUE_TEXT               = UF_SF_LANG_TEXT_VAL_TYPE,
    UF_SF_FEM_VALUE_ENUM               = UF_SF_LANG_ENUM_VAL_TYPE,
    UF_SF_FEM_VALUE_COORD              = UF_SF_LANG_COORD_VAL_TYPE ,
    UF_SF_FEM_VALUE_MATERIAL           = UF_SF_LANG_MATERIAL_VAL_TYPE,
    UF_SF_FEM_VALUE_SECTION            = UF_SF_LANG_SECTION_VAL_TYPE,
    UF_SF_FEM_VALUE_VECTOR             = UF_SF_LANG_VECTOR_VAL_TYPE,
    UF_SF_FEM_VALUE_TABLE              = UF_SF_LANG_TABLE_VAL_TYPE,
    UF_SF_FEM_VALUE_LOAD               = UF_SF_LANG_LOAD_VAL_TYPE,
    UF_SF_FEM_VALUE_BNDCOND            = UF_SF_LANG_BNDCOND_VAL_TYPE,
    UF_SF_FEM_VALUE_BOOL               = UF_SF_LANG_BOOL_VAL_TYPE,
    UF_SF_FEM_VALUE_MULTI_STRING       = UF_SF_LANG_MULTI_STRING_VAL_TYPE,
    UF_SF_FEM_VALUE_MULTI_STRING_ITI   = UF_SF_LANG_MULTI_STRING_ITI_VAL_TYPE,
    UF_SF_FEM_VALUE_FILENAME_VAL_TYPE  = UF_SF_LANG_FILENAME_VAL_TYPE,
    UF_SF_FEM_VALUE_DIRPATH_VAL_TYPE   = UF_SF_LANG_DIRPATH_VAL_TYPE,
    UF_SF_FEM_VALUE_SSMO_VAL_TYPE      = UF_SF_LANG_SSMO_VAL_TYPE ,
    UF_SF_FEM_VALUE_PPT_VAL_TYPE       = UF_SF_LANG_PPT_VAL_TYPE ,
    UF_SF_FEM_VALUE_PLYMAT_VAL_TYPE    = UF_SF_LANG_PLYMAT_VAL_TYPE ,
    UF_SF_FEM_VALUE_FIELD_VAL_TYPE     = UF_SF_LANG_FIELD_VAL_TYPE ,
    UF_SF_FEM_VALUE_AXIS_VAL_TYPE      = UF_SF_LANG_AXIS_VAL_TYPE ,
    UF_SF_FEM_VALUE_DOF_VAL_TYPE       = UF_SF_LANG_DOF_VAL_TYPE ,
    UF_SF_FEM_VALUE_POINT_VAL_TYPE     = UF_SF_LANG_POINT_VAL_TYPE,
    UF_SF_FEM_VALUE_EDGES_ON_FACE      = UF_SF_LANG_EDGES_ON_FACE_VAL_TYPE,
    UF_SF_FEM_VALUE_SCALAR_ARRAY       = UF_SF_LANG_SCALAR_ARRAY_VAL_TYPE,
    UF_SF_FEM_VALUE_ACTION             = UF_SF_LANG_ACTION_VAL_TYPE,
    UF_SF_FEM_VALUE_SSMO_ARRAY         = UF_SF_LANG_SSMO_ARRAY_VAL_TYPE,
    UF_SF_FEM_VALUE_TIME               = UF_SF_LANG_TIME_VAL_TYPE,
    UF_SF_FEM_VALUE_INT_ARRAY          = UF_SF_LANG_INT_ARRAY_VAL_TYPE,
    UF_SF_FEM_VALUE_EXT_MENU           = UF_SF_LANG_EXT_MENU_VAL_TYPE,
    UF_SF_FEM_VALUE_CATALOG            = UF_SF_LANG_CATALOG_VAL_TYPE,
    UF_SF_FEM_VALUE_GENERAL_FIELD      = UF_SF_LANG_GENERAL_FIELD_VAL_TYPE,
    UF_SF_FEM_VALUE_SCALAR_FIELD       = UF_SF_LANG_SCALAR_FIELD_VAL_TYPE,
    UF_SF_FEM_VALUE_VECTOR_FIELD       = UF_SF_LANG_VECTOR_FIELD_VAL_TYPE,
    UF_SF_FEM_VALUE_COMPLEX_SCALAR_FIELD = UF_SF_LANG_COMPLEX_SCALAR_FIELD_VAL_TYPE,
    UF_SF_FEM_VALUE_MATRIX             = UF_SF_LANG_MATRIX_VAL_TYPE,
    UF_SF_FEM_VALUE_REGION             = UF_SF_LANG_REGION_VAL_TYPE,
    UF_SF_FEM_VALUE_GROUPREF           = UF_SF_LANG_GROUPREF_VAL_TYPE,
    UF_SF_FEM_VALUE_SELECTREF          = UF_SF_LANG_SELECTREF_VAL_TYPE,
    UF_SF_FEM_VALUE_SECTION_ORIENT     = UF_SF_LANG_CAE_SECTION_ORIENT_VAL_TYPE,
    UF_SF_FEM_VALUE_SECTION_OFFSET     = UF_SF_LANG_CAE_SECTION_OFFSET_VAL_TYPE,
    UF_SF_FEM_VALUE_TARGETSET          = UF_SF_LANG_TARGETSET_VAL_TYPE,
    UF_SF_FEM_VALUE_SECTION_REF        = UF_SF_LANG_CAE_SECTION_REF_VAL_TYPE,
    UF_SF_FEM_VALUE_DOFSET_REF         = UF_SF_LANG_DOFSETREF_VAL_TYPE,
    UF_SF_FEM_VALUE_ALTREP_ARRAY_REF   = UF_SF_LANG_ALTERNATE_REP_ARRAY_VAL_TYPE,
    UF_SF_FEM_VALUE_LBCREF             = UF_SF_LANG_LBCREF_VAL_TYPE,
    UF_SF_FEM_VALUE_PPT_ARRAY          = UF_SF_LANG_PHYSICAL_ARRAY_VAL_TYPE,
    UF_SF_FEM_VALUE_SOLUTIONREF        = UF_SF_LANG_SOLUTIONREF_VAL_TYPE,
    UF_SF_FEM_VALUE_GROUPREF_ARRAY     = UF_SF_LANG_GROUPREF_ARRAY_VAL_TYPE,
    UF_SF_FEM_VALUE_SCALAR_FIELD_TABLE = UF_SF_LANG_SCALAR_FIELD_TABLE_VAL_TYPE,
    UF_SF_FEM_VALUE_SOLUTIONSTEPREF    = UF_SF_LANG_SOLUTIONSTEPREF_VAL_TYPE,
    UF_SF_FEM_VALUE_POINT_ARRAY_VAL_TYPE = UF_SF_LANG_POINT_ARRAY_VAL_TYPE


} UF_SF_fem_value_type_t, * UF_SF_fem_value_type_p_t;

/* Durability Solution type parameter. */

typedef enum
{
    UF_SF_ULTIMATE_STRENGTH = 0,
    UF_SF_YIELD_STRENGTH = 1

} UF_SF_dursol_stress_criterion_t, * UF_SF_dursol_stress_criterion_p_t;

typedef enum
{
    UF_SF_VON_MISES = 0,
    UF_SF_TRESCA = 1,
    UF_SF_MAXIMUM_PRINCIPLE = 2,
    UF_SF_MINIMUM_PRINCIPLE = 3

} UF_SF_dursol_stress_type_t, * UF_SF_dursol_stress_type_p_t;

typedef enum
{
    UF_SF_INFINITE_LIFE = 0,
    UF_SF_CYCLES_TO_FAILURE = 1

} UF_SF_dursol_design_life_criterion_t, * UF_SF_design_life_criterion_p_t;

typedef enum
{
    UF_SF_SMITH_WATSON_TOPPER = 0,
    UF_SF_STRAIN_LIFE_MAX_PRINCIPLE = 1,
    UF_SF_STRAIN_LIFE_MAX_SHEAR = 2,
    UF_SF_STRESS_LIFE = 3

} UF_SF_dursol_fatigue_life_criterion_t, * UF_SF_dursol_fatigue_life_criterion_p_t;

#ifdef __cplusplus
}
#endif

#endif  /*    UF_SF_TYPES__H_INCLUDED                                   */
