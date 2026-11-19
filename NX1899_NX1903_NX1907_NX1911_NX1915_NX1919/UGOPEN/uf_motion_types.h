/*****************************************************************************

                    Copyright (c) 2001-2004 Unigraphics Solutions Inc. 
                             Unpublished - All rights reserved
==============================================================================



File description:

Data types that are used in the Open API interface for Scenario for Motion+.
For each structure that is defined in this file, there is a corresponding 
initialization routine that will assign default values to the members of the 
structure.  It is highly recommended that all structures are initialized 
before they are used.

*****************************************************************************/

#ifndef UF_MOTION_TYPES_H_INCLUDED
#define UF_MOTION_TYPES_H_INCLUDED

#include <uf_defs.h>
#include <uf_obj_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/* UF_MOTION_angular_units_type_s defines the possible values of angular
   input values.  This includes drives for joints and other motion inputs. */
enum UF_MOTION_angular_units_type_e
{
    UF_MOTION_degree_units,    /* motion inputs are assumed to be in degrees */
    UF_MOTION_radian_units     /* motion inputs are assumed to be in radians */
};
typedef enum UF_MOTION_angular_units_type_e
             UF_MOTION_angular_units_type_t;

enum UF_MOTION_measurement_type_e
{
    UF_MOTION_unknown_measurement = 0,   /* This type is used to signify that
                                          the measurement type is not set. */
    UF_MOTION_distance_measurement,      /* This type is for measuring 
                                          distances.  If this type is used
                                          with solid bodies, the minimum
                                          distance between the body is 
                                          calculated. */
    UF_MOTION_angle_measurement          /* This type is for measuring angles
                                          between lines or linear edges. */
};
typedef enum UF_MOTION_measurement_type_e
             UF_MOTION_measurement_type_t;

struct UF_MOTION_measurement_s
{
    UF_MOTION_measurement_type_t type;     /* The type of measurement.  See the
                                            enum definition. */
    tag_t object_1;                      /* The object to measure from.  It 
                                            must be a geometric object that
                                            belongs to a link.  If type is
                                            an angle measurement, it must be 
                                            a linear edge or line.  If type 
                                            is a minimum distance measurement,
                                            it can be either a solid body,
                                            sheet body, curve, or marker. */
    tag_t object_2;                      /* The object to measure to.  It must
                                            be on a different link than
                                            object_1.  If this is an angle
                                            measurement, object_2 must be a 
                                            linear edge or line.  If this is
                                            a distance measurement, it can be
                                            any geometric object. */
};
typedef struct UF_MOTION_measurement_s
               UF_MOTION_measurement_t;

struct UF_MOTION_trace_s
{
    tag_t object;                        /* The geometric object to be traced.
                                            It must belong to a link (not
                                            ground). */
    int target_layer;                    /* The layer that the traced objects
                                            will be created on. */
};
typedef struct UF_MOTION_trace_s
               UF_MOTION_trace_t;

enum UF_MOTION_reference_frame_e
{
    UF_MOTION_absolute = 0,   /* This type is used for objects and operations
                               in the absolute coordinate system.  This is
                               the ground coordinate system and does not move
                               with the mechanism. */
    UF_MOTION_first_link,     /* This type is used for objects and operations
                               in the coordinate system of the first link.
                               This reference frame moves with the link. */
    UF_MOTION_second_link     /* This type is used for objects and operations
                               in the coordinate system of the second link.
                               This reference frame moves with the link. */
};
typedef enum UF_MOTION_reference_frame_e
             UF_MOTION_reference_frame_t;

struct UF_MOTION_interference_s
{
    tag_t solid_1;                       /* The first solid body of the 
                                            interference check. */
    tag_t solid_2;                       /* The second solid body of the
                                            interference check. */
};
typedef struct UF_MOTION_interference_s
               UF_MOTION_interference_t;

enum UF_MOTION_solver_e
{
   UF_MOTION_unknown_solver = 0,   /* This type is used to signify that no
                                      solver has been set yet. */
   UF_MOTION_kinematic_solver,     /* This is the solver for kinematic
                                      analysis. */
   UF_MOTION_static_dynamic_solver /* This is the sovler for dynamic 
                                      (inertial) and static analyses. */
};
typedef enum UF_MOTION_solver_e
             UF_MOTION_solver_t;

struct UF_MOTION_solver_parameters_s
{
    UF_MOTION_solver_t solver;   /* The solver to be used.  See the solver 
                                    enum definition. */
    double max_step_size;      /* The maximum allowed step size of the 
                                  solver.  For more detailed results, decrease
                                  this number.  For quicker results, increase
                                  this number. */
    double max_solver_error;   /* The maximum integration error allowed by the
                                  solver.  For more accurate results, decrease
                                  this number.  For quicker results, increase
                                  this number. */
    int max_integrator_iterations; /* The maximum number of iterations allowed for 
                                   the solver's integrator to converge 
                                   to the solution in a dynamic analysis.If the
                                   solver integrator has problems in converging 
                                   during a dynamic analysis then increase 
                                   this number */
    int max_kinematics_iterations; /* The maximum number of iterations allowed for 
                                     the solver to converge to the 
                                     solution in a kinematic  analysis.If the
                                     motion model has problems in converging during a
                                     kinematic analysis then increase this number */
    int max_statics_iterations; /* The maximum number of iterations allowed for 
                                  the solver to converge to the 
                                  solution in a static analysis. If the
                                  motion model has problems in converging during a
                                  static analysis then increase this number */
    int use_mass_properties;   /* A flag to determine whether or not to use
                                  mass properties in the analysis.  If FALSE,
                                  no dynamic analyses can be performed and 
                                  kinematic results will not have inertial
                                  loads.  */
};
typedef struct UF_MOTION_solver_parameters_s
               UF_MOTION_solver_parameters_t;

enum UF_MOTN_motion_type_e
{
    UF_MOTION_translation = 0,  /* The motion described by this type is a pure
                                 translation.  It could be a translation of a
                                 joint or link or a component of the 
                                 translation along an axis of a specific 
                                 coordinate system. */
    UF_MOTION_rotation          /* The motion described by this type is a pure
                                 rotation.  It could be a rotation of a joint
                                 or link or a component of the rotation about
                                 an axis of a specific coordinate system. */
};
typedef enum UF_MOTN_motion_type_e
             UF_MOTION_motion_type_t;

enum UF_MOTION_vector_component_e
{
    UF_MOTION_magnitude = 0,   /* This value represents the full magnitude of
                                the vector in question.  It is not a valid
                                entry for functions that need to set the 
                                direction of the vector.  */
    UF_MOTION_x_component,     /* This value represents the x component of the
                                vector.  */
    UF_MOTION_y_component,     /* This value represents the y component of the
                                vector.  */
    UF_MOTION_z_component      /* This value represents the z component of the
                                vector.  */
};
typedef enum UF_MOTION_vector_component_e
             UF_MOTION_vector_component_t;

enum UF_MOTION_disp_angle_e
{
    UF_MOTION_euler_one = 0,   /* This is the first Euler angle displacement in
                                the body 3-1-3 system.  It is the rotation 
                                about the z axis of the original coordinate 
                                system. */
    UF_MOTION_euler_two,       /* This is the second Euler angle displacement in
                                the body 3-1-3 system.  It is the rotation 
                                about the NEW x axis that exists after the 
                                first Euler angle rotation. */
    UF_MOTION_euler_three     /* This is the third Euler angle displacement in
                                the body 3-1-3 system.  It is the rotation 
                                about the NEW z axis that exists after the 
                                second Euler angle rotation. */
   
};
typedef enum UF_MOTION_disp_angle_e
             UF_MOTION_disp_angle_t;

enum UF_MOTION_PV_export_type_e
{
    UF_MOTION_PV_EXPORT_VFM = 0,   /* This type is used to create vfm file only */
    UF_MOTION_PV_EXPORT_VFM_AND_JT      /* This type is used to create vfm and jt file */
 
};
typedef enum UF_MOTION_PV_export_type_e
             UF_MOTION_PV_export_type_t;

struct UF_MOTION_link_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the link.  If NULL,
                                            a default name will be created. */
    int num_geometry_tags;               /* The number of valid geometry tags
                                            in the tag array */
    tag_t *geometry;                     /* <len:num_geometry_tags> The array of geometry tags that
                                            make up the link.  These can be
                                            solid bodies, lines, curves,
                                            points, etc. */
};
typedef struct UF_MOTION_link_s
               UF_MOTION_link_t;

struct UF_MOTION_link_mass_properties_s
{
    tag_t mass_center;               /* Smart point at the center of mass.
                                        If the mass properties are automatically
                                        calculated, this will be the same 
                                        as the origin of the marker below.
                                        These origins can be different
                                        for user defined mass properties. */
    tag_t inertia_marker;            /* Internal marker that defines the 
                                        origin and orientation of the inertia
                                        values.  If the mass properties are
                                        automatically generated, the origin
                                        will be the same as the mass_center
                                        above and the orientation will be the
                                        principle axes. */
    double mass;                     /* The mass of the link */
    double products_of_inertia[6];   /* The products of inertia of the link
                                        in the following order:  Ixx, Ixy,
                                        Ixz, Iyy, Iyz, Iyz */
    logical user_defined;            /* TRUE if overriding default mass
                                        properties with user defined values. */
};
typedef struct UF_MOTION_link_mass_properties_s
               UF_MOTION_link_mass_properties_t;

struct UF_MOTION_link_initial_vel_s
{
    tag_t linear_dir;         /* A smart DIRR describing the linear
                                 initial velocity direction. */
    double magnitude;         /* The magnitude of the linear velocity. */

    tag_t rotation_dir;       /* A smart DIRR describing the axis of rotation
                                 for the initial rotational veloctiy. */
    double angular_mag;       /* The magnitude of the angular velocity. */

    tag_t rotation_csys;      /* The CSYS for a fully defined initial angular
                                 velocity.  The components below are about
                                 each of the corresponding axis of this CSYS */
    double rotation_vel[3];   /* The components of rotation about each axis 
                                 of rotation_csys. */
};
typedef struct UF_MOTION_link_initial_vel_s
               UF_MOTION_link_initial_velocity_t;

enum UF_MOTION_joint_type_e
{
    UF_MOTION_unknown_joint = 0,   /* This type is used to signify that the type
                                      has not been set yet. */
    UF_MOTION_revolute_joint,      /* This joint type is a single axis rotation.
                                      This joint removes 5 degrees of freedom.
                                      The origins of csys_1 and csys_2 are
                                      identical and the z axes of csys_1 and
                                      csys_2 are colinear and codirected. */
    UF_MOTION_slider_joint,        /* This joint type is a single translation.
                                      This joint removes 5 degrees of freedom.
                                      The orientations of csys_1 and csys_2 are
                                      identical and the z axes are colinear and
                                      codirected. */
    UF_MOTION_cylinder_joint,      /* This joint type is a single rotation and
                                      a single translation.  This joint removes
                                      4 degrees of freedom.  The z axes of csys_1
                                      and csys_2 are colinear and codirected. */
    UF_MOTION_screw_joint,         /* This joint type is used to couple the 
                                      rotation and translation of a cylindrical
                                      joint to remove one degree of freedom.  
                                      It should be created on the same pair
                                      of links as the cylindrical joint.  If 
                                      the screw joint needs to be driven, it
                                      may be coupled with a revolute joint and 
                                      a slider joint instead. */
    UF_MOTION_universal_joint,     /* This joint type allows two rotations.  It
                                      removes 4 degrees of freedom.  The origins
                                      of csys_1 and csys_2 are identical.  The
                                      rotations about the x axis of csys_2 are
                                      equal and opposite to the rotations about
                                      the x axis of csys_1. */
    UF_MOTION_spherical_joint,     /* This joint type allows three rotations.
                                      It removes 3 degrees of freedom.  The
                                      origins of csys_1 and csys_2 are
                                      identical. */
    UF_MOTION_planar_joint,         /* This joint type allows a single rotation
                                      and two translations.  It removes three
                                      degrees of freedom.  The z axes of csys_1
                                      and csys_2 are parallel and codirected.
                                      The origins of csys_1 and csys_2 are in
                                      a common x-y plane. */
    UF_MOTION_fixed_joint           /* This Joint fixes a link or weld two links, 
                                      It removes 6 degrees of freedom */
};
typedef enum UF_MOTION_joint_type_e
             UF_MOTION_joint_type_t;

struct UF_MOTION_joint_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the joint.  If NULL,
                                            a default name will be created. */
    UF_MOTION_joint_type_t jt_type;      /* The type of the joint.  See the
                                            UF_MOTION_joint_type_t enum. */
    logical snap_links;                  /* If TRUE, the joint "snaps" the two
                                            links into position using the link
                                            orientations. */
    tag_t link_1;                        /* The first link associated with
                                            the joint. */
    tag_t link_2;                        /* The second link associated with
                                            the joint.  It can be NULL_TAG
                                            for grounded joints. */
    tag_t direction_1;                   /* Smart direction tag that defines
                                            the direction of link_1.  See
                                            uf_so.h for creation methods. */
    tag_t direction_2;                   /* Smart direction tag that defines
                                            the direction of link_2.  It can
                                            be NULL_TAG for grounded joints.
                                            See uf_so.h for creation methods. */
    tag_t origin_1;                      /* Optional point location on link_1.
                                            This point should be defined if link_1
                                            has no center of mass. */
    tag_t origin_2;                      /* Optional point location on link_2.
                                            This point should be defined if link_2
                                            has no center of mass. */
    double screw_ratio;                  /* Used only for UF_MOTION_screw_joint.
                                            This is the pitch of the screw's
                                            threads.  It defines how much 
                                            link_2 translates along the joint's
                                            Z axis relative to link_1 for each
                                            full turn of rotation. */
};
typedef struct UF_MOTION_joint_s
               UF_MOTION_joint_t;

struct UF_MOTION_joint_limits_s
{
    double min;   /* The minimum allowed value of the joint. It is an angle
                     for revolute joints and a length for slider joints. */
    double max;   /* The maximum allowed value of the joint. It is an angle
                     for revolute joints and a length for slider joints. */
};
typedef struct UF_MOTION_joint_limits_s
               UF_MOTION_joint_limits_t;

enum UF_MOTION_joint_motion_input_type_e
{
    UF_MOTION_unknown_input = 0,   /* This type is used to signify that the
                                      motion input type is unset. */
    UF_MOTION_function_input,      /* This type is a user-defined function that
                                      describes the position of the joint as a
                                      function of other measurable values. */
    UF_MOTION_constant_input,      /* This type is a motion input of constant
                                      displacement, velocity, and/or
                                      acceleration. */
    UF_MOTION_harmonic_input,      /* This type is a harmonic oscillating motion
                                      with specified amplitude, frequency,
                                      phase angle, and offset displacement. */
    UF_MOTION_articulation_input   /* This type is strictly for articulation and
                                      the motion input is defined incrmentally
                                      using the articulation functions. */
};
typedef enum UF_MOTION_joint_motion_input_type_e
             UF_MOTION_joint_motion_input_type_t;

struct UF_MOTION_joint_motion_input_s
{
    UF_MOTION_joint_motion_input_type_t input_type;  /* The type of the motion input.
                                                        See the enum definition. */
    tag_t function;                  /* The tag to the function.  It is used
                                        if type is UF_MOTION_function_input. */
    double displacement;             /* The constant displacement input.
                                        Used if type is UF_MOTION_constant_input. */
    double velocity;                 /* The constant velocity input.
                                        Used if type is UF_MOTION_constant_input. */
    double acceleration;             /* The constant acceleration input.
                                        Used if type is UF_MOTION_constant_input. */
    double amplitude;                /* The harmonic amplitude input.
                                        Used if type is UF_MOTION_harmonic_input. */
    double frequency;                /* The harmonic frequency input.
                                        Used if type is UF_MOTION_harmonic_input. */
    double phase_angle;              /* The harmonic phase angle input.
                                        Used if type is UF_MOTION_harmonic_input. */
    double harm_disp;                /* The harmonic offset displacement input.
                                        This is the distance from the design
                                        position to the center of the harmonic wave.
                                        If the wave is to be centered at the
                                        design position, this value should be zero.
                                        Used if type is UF_MOTION_harmonic_input. */
};
typedef struct UF_MOTION_joint_motion_input_s
               UF_MOTION_joint_motion_input_t;

enum UF_MOTION_joint_coupler_type_e
{
    UF_MOTION_unknown_coupler = 0,       /* This type is used to signify that
                                            the coupler type is not yet set. */
    UF_MOTION_rack_and_pinion_coupler,   /* This coupler is used to couple a
                                            revolute and slider whose z axes
                                            will remain nearly prependicular
                                            throughout the motion. */
    UF_MOTION_gear_coupler,              /* This coupler is used to couple two
                                            revolute joints.  */
    UF_MOTION_cable_coupler              /* This coupler is used to couple two
                                            slider joints.  */
};
typedef enum UF_MOTION_joint_coupler_type_e
             UF_MOTION_joint_coupler_type_t;

struct UF_MOTION_joint_coupler_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the joint coupler.  If
                                            NULL, a default name will be created. */
    UF_MOTION_joint_coupler_type_t jtc_type;  /* The type of the joint coupler.
                                                 See the enum definition. */
    tag_t joint_1;                       /* The first joint of the coupler.
                                            It can be a revolute, slider, or
                                            cylindrical joint depending on the
                                            coupler type. */
    tag_t joint_2;                       /* The second joint of the coupler.
                                            If joint_1 is a revolute or
                                            slider joint, this joint can also
                                            be a revolute or slider joint
                                            depending on the coupler type.  If
                                            joint_1 is a cylindrical joint,
                                            then this joint is ignored.  If
                                            the type is gear or rack and
                                            pinion, the joints must have a
                                            common link.  */
    double ratio;                        /* The constraint ratio between the
                                            joints. It determines how far
                                            joint_2 moves for a unit movement
                                            of joint_1.  If ratio is defined,
                                            the contact point will be calculated
                                            for gear and rack/pinion couplers,
                                            otherwise, if the contact point is
                                            defined, the ratio will be calculated. */
    tag_t origin_tag;                    /* The smart point that defines the
                                            origin of the contact point between
                                            the joints.  This is only used for
                                            gear and rack/pinion couplers
                                            currently.  If defined, the ratio
                                            will be calculated, otherwise, the
                                            contact point will be calculated
                                            if the ratio is defined.  See uf.so.h 
                                            for creation of this object. */
    tag_t orientation_tag;               /* The orientation matrix that defines
                                            the orientation at the contact
                                            point between the two joints.
                                            This is only used for gear and
                                            rack/pinion couplers and is strictly
                                            optional.  A default orientation matrix
                                            will be calculated if not defined.
                                            Use UF_CSYS_create_matrix for the 
                                            creation of object. */
};
typedef struct UF_MOTION_joint_coupler_s
               UF_MOTION_joint_coupler_t;

struct UF_MOTION_point_curve_constraint_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the point curve
                                            constraint.  If NULL, a default
                                            name will be created. */
    int num_curve_tags;                  /* The number of tags in the curve
                                            tag array. */
    tag_t *curve;                        /* <len:num_curve_tags> The tags of the constraint
                                            curves.  All curves must be on
                                            same link (or no link). */
    tag_t point;                         /* The tag of the constrained point.
                                            It cannot belong to the same link
                                            as the curves.  See uf_so.h for
                                            smart point creation methods.*/
};
typedef struct UF_MOTION_point_curve_constraint_s
               UF_MOTION_point_curve_constraint_t;

struct UF_MOTION_curve_curve_constraint_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the curve curve
                                            constraint.  If NULL, a default
                                            name will be created. */
    int num_curve_1_tags;                /* The number of tags in the first
                                            curve tag array. */
    tag_t *curve_1;                      /* <len:num_curve_1_tags> The tags of the first constraint
                                            curves.  All curves must be on
                                            same link (or no link). */
    int num_curve_2_tags;                /* The number of tags in the second
                                            curve tag array. */
    tag_t *curve_2;                      /* <len:num_curve_2_tags> The tags of the second constraint
                                            curves.  All curves must be on
                                            same link (or no link) and the
                                            link must be different from the
                                            link of the first curve. */
};
typedef struct UF_MOTION_curve_curve_constraint_s
               UF_MOTION_curve_curve_constraint_t;

/* Enum definition for use with both springs and dampers. */
enum UF_MOTION_spring_damper_type_e
{
    UF_MOTION_unknown_spring_damper = 0, /* This type is used to signify
                                            that the spring-damper type is
                                            not set yet. */
    UF_MOTION_revolute_spring_damper,    /* This type of spring-damper is
                                            rotational and must be applied
                                            to a revolute joint. */
    UF_MOTION_slider_spring_damper,      /* This type of spring-damper is
                                            translational and must be
                                            applied to a slider joint. */
    UF_MOTION_link_spring_damper         /* This type of spring-damper is
                                            translational and can be
                                            applied generally to two
                                            independent links. */
};
typedef enum UF_MOTION_spring_damper_type_e
             UF_MOTION_spring_damper_type_t;

/* Data structure definition for use with both springs and
   dampers since they share many of the same attributes. */
struct UF_MOTION_spring_damper_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the spring damper.
                                            If NULL, a default name will be
                                            created. */
    UF_MOTION_spring_damper_type_t spr_dmp_type;  /* The type of spring/damper.
                                                    See the enum definition. */
    tag_t joint;                         /* The joint owning the spring/damper
                                            if the spring/damper type is
                                            UF_MOTION_revolute_spring_damper or
                                            UF_MOTION_slider_spring_damper. */
    tag_t link_1;                        /* Link one of the spring/damper if
                                            the spring/damper type is
                                            UF_MOTION_link_spring_damper. */
    tag_t point_1;                       /* The point of the spring/damper
                                            attachment on the first link.
                                            See uf_so.h for smart point creation.
                                            If the spring/damper type is
                                            UF_MOTION_slider_spring_damper or
                                            UF_MOTION_revolute_spring_damper,
                                            this will automatically be set
                                            with the joint origin. */
    double pt1_coord[3];                 /* The coordinates of the attachment
                                            point of the spring/damper on the
                                            first link.  Not required for creation
                                            or edit.  If a smart point is not
                                            provided for point_1, a dumb point will
                                            automatically be created from input
                                            coordinates (not recommended).*/
    tag_t link_2;                        /* Link two of the spring/damper, or
                                            NULL_TAG if ground.  This is only
                                            for a spring/damper type of
                                            UF_MOTION_link_spring_damper. */
    tag_t point_2;                       /* The point of the spring/damper
                                            attachment on the second link,
                                            or the point of attachment to
                                            ground if link_2 is NULL_TAG. 
                                            See uf_so.h for smart point creation.
                                            If the spring/damper type is
                                            UF_MOTION_slider_spring_damper,
                                            this will automatically be set
                                            with the joint origin. */
    double pt2_coord[3];                 /* The coordinates of the attachment
                                            point of the spring/damper to the
                                            second link, or to ground.  Not required
                                            for creation or edit.  If a smart
                                            point is not provided for point_2,
                                            a dumb point will automatically be
                                            created from input coordinates 
                                            (not recommended). */
    double spring_rate;                  /* The spring rate for both rotational
                                            and translational springs. */
    double spring_preload;               /* The spring preload at the reference length or angle*/
    double spring_ref_length;            /* The reference length of the spring
                                            is used to calculate either the 
                                            preload force on the spring or the
                                            free length.  This is used for
                                            linear springs. */
    double spring_ref_angle;             /* The reference angle of the spring
                                            at zero displacement.  This is used
                                            for rotational springs. */
    double spring_init_length;           /* The initial length of the spring at assembly
                                            position; used for spring defined on slide
                                            joint */
    double damping_rate;                 /* The linear damping rate of the
                                            damper. */
};
typedef struct UF_MOTION_spring_damper_s
               UF_MOTION_spring_damper_t;

/* Data structure definition for use with both scalar forces and torques. */
struct UF_MOTION_scalar_force_torque_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the force or torque.
                                            If NULL, a default name will be
                                            created. */
    tag_t attach_body;                   /* The link the force is acting on,
                                            or the revolute joint the torque
                                            is acting on. */
    tag_t origin_1;                      /* The point that defines the location
                                            the force is acting from.  Not
                                            needed for torque. */
    tag_t origin_2;                      /* The point that defines the location
                                            the force is acting to.  Not needed
                                            for torque. */
    tag_t force_function;                /* The function describing the force
                                            magnitude. */
    tag_t torque_function;               /* The function describing the torque
                                            magnitude. */
    tag_t reaction_link;                 /* The optional link that receives an
                                            equal and opposite reaction force.
                                            If fixed to ground, this should be
                                            NULL_TAG.  Not needed for torque. */
};
typedef struct UF_MOTION_scalar_force_torque_s
               UF_MOTION_scalar_force_torque_t;

/* Enum definition to designate vector force or vector torque. */
enum UF_MOTION_vector_type_e
{
    UF_MOTION_vector_force = 0,
    UF_MOTION_vector_torque
};
typedef enum UF_MOTION_vector_type_e
             UF_MOTION_vector_type_t;

/* Data structure definition for use with both vector forces and torques. */
struct UF_MOTION_vector_force_torque_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the force or torque.
                                            If NULL, a default name will be
                                            created. */
    UF_MOTION_vector_type_t vtype;       /* Either UF_MOTION_vector_force
                                            or UF_MOTION_vector_torque. */ 
    tag_t link;                          /* The link that the force or torque
                                            is acting on. */
    tag_t origin;                        /* The point that defines the location
                                            the force or torque is acting on. */
    tag_t direction;                     /* The vector that defines the
                                            orientation of the force or torque
                                            if reference frame is
                                            UF_MOTION_first_link.  If reference
                                            frame is UF_MOTION_absolute, this
                                            should be NULL_TAG. */
    UF_MOTION_reference_frame_t frame;   /* The reference frame of the force
                                            or torque:  UF_MOTION_absolute means
                                            the orientation of the force/torque
                                            is constant with respect to the
                                            absolute CSYS regardless of the
                                            motion of the link.
                                            UF_MOTION_first_link means the
                                            orientation of the force/torque
                                            is constant with respect to the
                                            link CSYS and the force/torque
                                            rotates with the link.  No other
                                            reference frames are considered. */
    tag_t comp_functions[3];             /* For reference frame of
                                            UF_MOTION_absolute:  The functions
                                            describing the X, Y, and Z components
                                            of the force or torque.  If there
                                            is no force/torque along an axis,
                                            enter a NULL_TAG. */
    tag_t magnitude_function;            /* For reference frame of
                                            UF_MOTION_first_link:  A single
                                            function tag describing the force 
                                            or torque magnitude. */ 
    tag_t reaction_link;                 /* The optional link that receives an
                                            equal and opposite reaction force
                                            or torque. If fixed to ground, this
                                            should be NULL_TAG. */
};
typedef struct UF_MOTION_vector_force_torque_s
               UF_MOTION_vector_force_torque_t;

struct UF_MOTION_cylindrical_bushing_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the bushing.  If NULL,
                                            a default name will be created. */
    tag_t link_1;                        /* The first link of the bushing. */
    tag_t origin_1;                      /* The point that defines the location
                                            of the bushing on link_1. */
    tag_t direction_1;                   /* The direction vector that defines
                                            the orientation of the bushing on
                                            link_1. */
    tag_t link_2;                        /* The second link of the bushing or
                                            NULL_TAG to attach to ground. */
    tag_t origin_2;                      /* The point that defines the location
                                            of the bushing on link_2,
                                            or NULL_TAG if ground. */
    tag_t direction_2;                   /* The direction vector that defines
                                            the orientation of the bushing on
                                            link_2, or NULL_TAG if ground. */
    double radial_stiffness;             /* The radial stiffness with respect
                                            to the bushing orientation on
                                            link_1. */
    double longitudinal_stiffness;       /* The longitudinal stiffness with
                                            respect to the bushing orientation
                                            on link_1. */
    double conical_stiffness;            /* The conical stiffness with respect
                                            to the bushing orientation on
                                            link_1. */
    double torsional_stiffness;          /* The torsional stiffness with 
                                            respect to the bushing orientation
                                            on link_1. */
    double radial_damping;               /* The radial damping with respect to
                                            the bushing orientation on link_1. */
    double longitudinal_damping;         /* The longitudinal damping with 
                                            respect to the bushing orientation
                                            on link_1. */
    double conical_damping;              /* The conical damping with respect
                                            to the bushing orientation on
                                            link_1. */
    double torsional_damping;            /* The torsional damping with respect
                                            to the bushing orientation on
                                            link_1. */
};
typedef struct UF_MOTION_cylindrical_bushing_s
               UF_MOTION_cylindrical_bushing_t;

struct UF_MOTION_general_bushing_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the bushing.  If NULL,
                                            a default name will be created. */
    tag_t link_1;                        /* The first link of the bushing. */
    tag_t origin_1;                      /* The point that defines the location
                                            of the bushing on link_1. */
    tag_t direction_1;                   /* The direction vector that defines
                                            the orientation of the bushing on
                                            link_1. */
    tag_t link_2;                        /* The second link of the bushing or
                                            NULL_TAG to attach to ground. */
    tag_t origin_2;                      /* The point that defines the location
                                            of the bushing on link_2,
                                            or NULL_TAG if ground. */
    tag_t direction_2;                   /* The direction vector that defines
                                            the orientation of the bushing on
                                            link_2, or NULL_TAG if ground. */
    double translational_stiffness[3];   /* The x, y, and z components of the
                                            translational stiffness with
                                            respect to the bushing orientation
                                            on link_1. */
    double translational_damping[3];     /* The x, y, and z components of the
                                            translational damping with respect
                                            to the bushing orientatation on
                                            link_1. */
    double translational_preload[3];     /* The x, y, and z components of the
                                            translational preload with respect
                                            to the bushing orientation on 
                                            link_1. */
    double torsional_stiffness[3];       /* The x, y, and z components of the
                                            torsional stiffness with respect
                                            to the bushing orientation on 
                                            link_1. */
    double torsional_damping[3];         /* The x, y, and z components of the
                                            torsional damping with respect to
                                            the bushing orientation on link_1. */
    double torsional_preload[3];         /* The x, y, and z components of the
                                            torsional preload with respect to
                                            the bushing orientation on link_1. */
};
typedef struct UF_MOTION_general_bushing_s
               UF_MOTION_general_bushing_t;

struct UF_MOTION_contact_parameters_s
{
    double force_exponent;                  /* The exponent of non-linear
                                               stiffness. (Force is not
                                               proportional to penetration
                                               depth.) */
    double material_damping;                /* The linear damping rate
                                               relative to the penetration
                                               depth. */
    double penetration_depth;               /* The maximum overlap distance
                                               between contact objects. */
    double static_friction;                 /* The coefficient of static
                                               friction at the static slip
                                               velocity.  It is usually
                                               greater than the dynamic
                                               friction coefficient. */
    double slip_velocity;                   /* The slip velocity of static
                                               friction where the static
                                               coefficient is maximum.  It is
                                               always less than the dynamic
                                               transition velocity. */
    double dynamic_friction;                /* The coefficient of dynamic
                                               friction above the transition
                                               velocity.   It is usually less
                                               than the static friction
                                               coefficient. */
    double transition_velocity;             /* The dynamic transition velocity
                                               is the velocity at which the
                                               static friction effects
                                               disappear.  It is always
                                               greater than the static slip
                                               velocity. */
};
typedef struct UF_MOTION_contact_parameters_s
               UF_MOTION_contact_parameters_t;

enum UF_MOTION_3D_contact_force_e
{
    UF_MOTION_3D_CONTACT_IMPACT = 0,
    UF_MOTION_3D_CONTACT_POISSON
}; 
typedef enum UF_MOTION_3D_contact_force_e
             UF_MOTION_3D_contact_force_t;

enum UF_MOTION_3D_contact_friction_e
{
    UF_MOTION_3D_CONTACT_NO_FRICTION = 0,
    UF_MOTION_3D_CONTACT_ALL_FRICTION
    /* UF_MOTION_3D_CONTACT_DYNAMIC_FRICTION_ONLY  No longer used(PR#4987406) */
};
typedef enum UF_MOTION_3D_contact_friction_e
             UF_MOTION_3D_contact_friction_t;

struct UF_MOTION_3D_contact_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];       /* The name of the 3D contact.
                                                If NULL, a default name wil be
                                                created. */
    int num_contact_side_1;                  /* The number of solid bodies
                                                on side 1 to be in contact.
                                                All the solid bodies must
                                                belong to the same link. */
    tag_t *contact_side_1;                   /* <len:num_contact_side_1> The tag array of the bodies
                                                on side 1 to be in contact.
                                                All the solid bodies must
                                                belong to the same link. */
    int num_contact_side_2;                  /* The number of solid bodies
                                                on side 2 to be in contact.
                                                All the solid bodies must
                                                belong to the same link. */
    tag_t *contact_side_2;                   /* <len:num_contact_side_2> The tag array of the bodies
                                                on side 2 to be in contact.
                                                All the solid bodies must
                                                belong to the same link. */
    UF_MOTION_3D_contact_force_t force_model_type;  /* The type of force
                                                model to be used during
                                                contact analysis. See enum
                                                definition. */
    UF_MOTION_3D_contact_friction_t friction_option;  /* The friction option
                                                to be used during contact
                                                analysis.  See enum definition. */ 
    double stiffness;                        /* The contact stiffness.  */             
    UF_MOTION_contact_parameters_t advanced; /* The advanced parameters of the
                                                contact.  See the structure
                                                definition. */
    double restitution_coefficient;          /* The coefficient that measures
                                                how much kinetic energy of the
                                                contact objects remain after
                                                the collision. */
};
typedef struct UF_MOTION_3D_contact_s
               UF_MOTION_3D_contact_t;

struct UF_MOTION_2D_contact_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];       /* The name of the 2D contact.
                                                If NULL, a default name will
                                                be created. */
    int num_curve_1;                         /* The number of curve tags in
                                                the curve_1 list. */
    tag_t *curve_1;                          /* <len:num_curve_1> The curve tags of the first
                                                link.  All of these curves
                                                must be coplanar and on the
                                                same link (or ground). */
    int num_curve_2;                         /* The number of curve tags in
                                                the curve_2 list. */
    tag_t *curve_2;                          /* <len:num_curve_2> The curve tags of the second
                                                link.  All of these curves
                                                must be coplanar with curve_1,
                                                on the same link (or ground),
                                                and on a different link than
                                                curve_1 list. */
    int max_num_contact_points;              /* The maximum number of contact
                                                points along the curve. */
    logical switch_material_side_1;          /* The material direction for
                                                side 1 is automatically
                                                determined based on the input
                                                curves.  Set this parameter
                                                to TRUE to reverse the default
                                                material direction. */
    logical switch_material_side_2;          /* The material direction for
                                                side 2 is automatically
                                                determined based on the input
                                                curves.  Set this parameter
                                                to TRUE to reverse the default
                                                material direction. */
    double stiffness;                        /* The contact stiffness.  */
    UF_MOTION_contact_parameters_t advanced; /* The advanced parameters of the
                                                contact.  See the structure
                                                definition. */
};
typedef struct UF_MOTION_2D_contact_s
               UF_MOTION_2D_contact_t;

enum UF_MOTION_marker_type_e
{
    UF_MOTION_undefined_marker = 0,
    UF_MOTION_inertia_marker,            /* This type defines the center of
                                            inertia for a link.  It will be
                                            automatically created for a link. */ 
    UF_MOTION_cofm_marker,               /* This type defines the center of
                                            mass for a link.  It will be 
                                            automatically created for a link. */
    UF_MOTION_user_defined_marker        /* This is a user created marker.
                                            This marker can be attached to
                                            any mechanism object. */
};
typedef enum UF_MOTION_marker_type_e
             UF_MOTION_marker_type_t;

struct UF_MOTION_marker_s
{
    char name[ UF_OBJ_NAME_BUFSIZE ];   /* The name of the marker.  If NULL,
                                            a default name will be created. */
    UF_MOTION_marker_type_t marker_type; /* Type of marker.  See enum definition. */ 
    tag_t attachment_tag;                /* The mechanism object that this marker is
                                            attached to.  User defined markers can
                                            be attached to any mechanism object. */
    tag_t orientation_tag;               /* Orientation matrix that defines the
                                            orientation of the marker.  Use 
                                            UF_CSYS_create_matrix for creation of
                                            this object. */
    tag_t origin_tag;                    /* Smart point that defines the origin
                                            of the marker.  Note that this object
                                            is currently not saved in the database  
                                            with the marker, it is included here
                                            for future enhancement.  However, it 
                                            is used to extract the coordinates in
                                            lieu of the user manually supplying or
                                            determining the coordinates of the marker. */
    double location[3];                  /* Coordinates that define the location of
                                            the marker. */
};
typedef struct UF_MOTION_marker_s
               UF_MOTION_marker_t;


struct UF_MOTION_point_on_surface_data_s 
{
    tag_t point_on_surface_tag; /* Tag of the created/edited entity */
    tag_t point_tag;            /* The point tag of the point on surface constraint.
                                   If the point tag is NOT on  a link, then the 
                                   point is considered to be on a grounded link */
    tag_t point_link_tag;       /* Optional: The user need not specify this data. However,
                                   user will be returned with this data when user queries
                                   for the data on the point_on_surface constraint tag */

    int num_face_tags;          /* Number of face tags for the constraint */
    tag_p_t face_tags;          /* <len:num_face_tags> 
                                   Group of faces that can be have a parameterized UV
                                   space. User can select faces of a single sheet or
                                   solid body. If the body is NOT on a link, then the faces
                                   are considered to be on a grounded link */
                                
    tag_t face_link_tag;        /* Optional: The user need not specify this data. However,
                                   user will be returned with this data when user queries
                                   for the data on the point_on_surface constraint tag */

                                /* BOTH THE point_tag and the face_tags cannot be on a 
                                   grounded link. Atleast one has to have a non-grounded
                                   link */
                                   
    double display_scale;       /* This scale is used in UI for displaying the object */
    char entity_name[ UF_OBJ_NAME_BUFSIZE ];          /* <len:MAX_ENTITY_NAME_SIZE +1> 
                                                           A unique name for the object */
};
typedef struct UF_MOTION_point_on_surface_data_s 
               UF_MOTION_point_on_surface_data_t,
              *UF_MOTION_point_on_surface_data_p_t;

enum UF_MOTION_anl_geometry_format_e
{
    UF_MOTION_stl_format = 0,           /* For exporting the Adams data in STL Format      */
    UF_MOTION_parasolid_format,         /* For exporting the Adams data in Parasolid Format*/
    UF_MOTION_no_format,                /* For exporting the Adams data in No Format       */
    UF_MOTION_unknown_geometry_format   /* Used in case of raising ERROR */

};
typedef enum UF_MOTION_anl_geometry_format_e
             UF_MOTION_anl_geometry_format_t;

struct UF_MOTION_stl_parameters_s
{
    double minimum_facet_length;   /* Minimum Facet Length for exporting the STL Data*/
    double maximum_facet_length;   /* Maximum Facet Length for exporting the STL Data*/
    double facet_tolerance;        /* Facet Tolerance Value for exporting the STL Data*/
};
typedef struct UF_MOTION_stl_parameters_s
               UF_MOTION_stl_parameters_t,
              *UF_MOTION_stl_parameters_p_t;

enum UF_MOTION_3d_contact_method_e
{
    UF_MOTION_faceted_contact = 0,     /* For Faceted Contact Algorithm      */
    UF_MOTION_precise_contact,         /* For Precise Contact Algorithm      */
    UF_MOTION_unknown_contact_method  /* For Undefined type       */
};
typedef enum UF_MOTION_3d_contact_method_e
             UF_MOTION_3d_contact_method_t;

struct UF_MOTION_function_s
{
    char  *name;                         /* The name of the function object.  There is
                                            no automatic default naming, a new name
                                            must be input for creation of function. */
    char **definition;                   /* <len:num_lines>
                                            String of the function definition.  Function
                                            string can contain standard math functions,
                                            Adams variables and functions, and derived
                                            functions of motion object results.  It is
                                            the responsibility of the user to know the
                                            correct strings and usage of standard math
                                            functions and Adams variables/functions.
                                            To get the derived function string of a
                                            motion object for a result type, use
                                            UF_MOTION_get_object_derived_function.
                                            It is highly recommended that the syntax
                                            of a function definition be validated
                                            before creating the function object.  See
                                            UF_MOTION_validate_function_syntax. */
    int    num_lines;                    /* Number of lines in the function definition. */

};
typedef struct UF_MOTION_function_s
               UF_MOTION_function_t;

/* Motion result type for a derived function. */
typedef enum
{
    UF_MOTION_func_displacement = 0,     /* Displacement result for derived function. */
    UF_MOTION_func_velocity,             /* Velocity result for derived function. */
    UF_MOTION_func_acceleration,         /* Acceleration result for derived function. */
    UF_MOTION_func_force                 /* Force result for derived function. */
} UF_MOTION_func_result_type_t;

/* Motion result component type for derived function. */
typedef enum
{
    UF_MOTION_func_linear_mag = 0,       /* Linear magnitude component of result type
                                            for derived function. */
    UF_MOTION_func_x_comp,               /* X component of result type for derived
                                            function. */
    UF_MOTION_func_y_comp,               /* Y component of result type for derived
                                            function. */
    UF_MOTION_func_z_comp,               /* Z component of result type for derived
                                            function. */
    UF_MOTION_func_angular_mag,          /* Angular magnitude component of result type
                                            for derived function.  This component is
                                            not allowed for UF_MOTION_func_displacement. */
    UF_MOTION_func_euler1_comp,          /* First Euler angle component of result type
                                            for derived function.  It is the rotation 
                                            about the z axis of the original coordinate 
                                            system. */
    UF_MOTION_func_euler2_comp,          /* Second Euler angle component of result type
                                            for derived function.  It is the rotation 
                                            about the NEW x axis that exists after the 
                                            first Euler angle rotation. */
    UF_MOTION_func_euler3_comp           /* Third Euler angle component of result type
                                            for derived function.  It is the rotation 
                                            about the NEW z axis that exists after the 
                                            second Euler angle rotation. */
} UF_MOTION_func_component_type_t;

typedef enum
{
    UF_MOTION_func_absolute_frame = 0,   /* Derived function in absolute coordinate system. */
    UF_MOTION_func_relative_frame        /* Derived function is relative to j-marker of
                                            referenced motion object. */
} UF_MOTION_func_ref_frame_type_t;


#ifdef __cplusplus
}
#endif

#endif /* UF_MOTION_TYPES_H_INCLUDED */
