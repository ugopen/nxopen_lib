/*****************************************************************************
             Copyright (c) 1995-2003 Unigraphics Solutions, Inc.
                       Unpublished - All Rights Reserved                       



File Description:
     This is the Open C API interface to creating a tool path for an operation.
 
 ******************************************************************************/

#ifndef UF_PATH_H
#define UF_PATH_H


/***************************************************************************

  ***************************************************************************/

#include <uf_defs.h>
#include <libufun_cam_exports.h>

/***************************************************************************

  ***************************************************************************/

#define ERROR_UF_PATH_base     1365000

#ifdef __cplusplus
extern "C" {
#endif

/********************************** Defines ***********************************/

#define UF_PATH_BAD_INPUT   (ERROR_UF_PATH_base + 1)


/********************************** TypeDefs **********************************/

/* UF_PATH_id_t is the identifier for referring to a UF_PATH */
typedef void   *UF_PATH_id_t;  /* is the identifier for referring to a
                                  UF_PATH. NOTE: A path identifier of
                                  the type UF_PATH_id_t has to be used
                                  as the input for all functions querying a
                                  path.
                               */  


/****************************************************************************

    A path identifier of the type UF_PATH_id_t has to be used as the
    input for all functions querying a path

*****************************************************************************/


/****************************************************************************

   CAUTION: Do not use the xxxx_LAST_ELEMENT member of the following enums. 

*****************************************************************************/ 

/*****************************************************************************

   The following two enums correspond to the CLAMP/ post command.
   Use axis type when using UF_PATH_CLAMP_AXIS_ON or UF_PATH_CLAMP_AXIS_OFF
   and UF_PATH_CLAMP_AXIS_NONE when using UF_PATH_CLAMP_ON or UF_PATH_CLAMP_OFF.
******************************************************************************/

enum UF_PATH_clamp_status_e 
        {
           UF_PATH_CLAMP_ON,                  /* Generate CLAMP/ON */
           UF_PATH_CLAMP_OFF,                 /* Generate CLAMP/OFF */
           UF_PATH_CLAMP_AXIS_ON,             /* Generate CLAMP/<axis_type>,ON
                                              */
           UF_PATH_CLAMP_AXIS_OFF,            /* Generate CLAMP/<axis_type>,OFF
                                              */
           UF_PATH_CLAMP_STATUS_LAST_ELEMENT  /* Place holder do not use. */
        } ;
typedef enum UF_PATH_clamp_status_e UF_PATH_clamp_status_t;


enum UF_PATH_axis_e 
        {
           UF_PATH_XAXIS,             /* Set axis type to X axis */
           UF_PATH_YAXIS,             /* Set axis type to Y axis */
           UF_PATH_ZAXIS,             /* Set axis type to Z axis */
           UF_PATH_AAXIS,             /* Set axis type to A axis */
           UF_PATH_BAXIS,             /* Set axis type to B axis */
           UF_PATH_CAXIS,             /* Set axis type to C axis */
           UF_PATH_AXIS_NONE,         /* Set axis type to none, to be used
                                         with UF_PATH_CLAMP_ON or
                                         UF_PATH_CLAMP_OFF */
           UF_PATH_AXIS_LAST_ELEMENT  /* Place holder, do not use */
        } ;
typedef enum UF_PATH_axis_e UF_PATH_axis_t;
/****************************************************************************

   Specify the head of the turret in a lathe. This is
   to be used in the TURRET/ (tool change) post command and the SELECT/HEAD
   (select head) post commands.

******************************************************************************/

enum UF_PATH_head_type_e 
        {
           UF_PATH_HEADTYPE_NONE,        /* For no HEAD option */
           UF_PATH_HEADTYPE_FRONT,       /* For FRONT HEAD option */
           UF_PATH_HEADTYPE_REAR,        /* For REAR HEAD option */
           UF_PATH_HEADTYPE_RIGHT,       /* For RIGHT HEAD option */
           UF_PATH_HEADTYPE_LEFT,        /* For LEFT HEAD option */
           UF_PATH_HEADTYPE_SIDE,        /* For SIDE HEAD option */
           UF_PATH_HEADTYPE_SADDLE,      /* For SADDLE HEAD option */
           UF_PATH_HEADTYPE_LAST_ELEMENT /* Placeholder, do not use */
        } ;
typedef enum UF_PATH_head_type_e UF_PATH_head_type_t;

/****************************************************************************
   Specify the plane for the CUTCOM/ post command. 
*****************************************************************************/ 

enum UF_PATH_plane_type_e 
        {
           UF_PATH_PLANE_TYPE_NONE,        /* A cutter compensation plane is
                                              not specified. */
           UF_PATH_PLANE_TYPE_XY,          /* The cutter compensation plane is
                                              in the XY plane. */
           UF_PATH_PLANE_TYPE_XZ,          /* The cutter compensation plane is
                                              in the XZ plane. */
           UF_PATH_PLANE_TYPE_YZ,          /* The cutter compensation plane is
                                              in the YZ plane. */
           UF_PATH_PLANE_TYPE_LAST_ELEMENT /* Placeholder, do not use */
        } ;
typedef enum UF_PATH_plane_type_e UF_PATH_plane_type_t;
         
/****************************************************************************

   Specify the mode for the CUTCOM/ post command. 

*****************************************************************************/ 

enum UF_PATH_cutcom_mode_e 
        {
           UF_PATH_CUTCOM_OFF,              /* Turn cutter compensation off. */
           UF_PATH_CUTCOM_ON,               /* Turn cutter compensation on. */
           UF_PATH_CUTCOM_LEFT,             /* Set cutter compensation material
                                               side to left. */
           UF_PATH_CUTCOM_RIGHT,            /* Set cutter compensation material
                                               side to right. */
           UF_PATH_CUTCOM_MODE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_cutcom_mode_e UF_PATH_cutcom_mode_t;
   
/****************************************************************************

   Specify positioning for the CUTCOM/ post command.
   Used for positioning the cutcom command in the path output relative to 
   a certain motion type. 

*****************************************************************************/ 

enum UF_PATH_cutcom_on_e 
        {
           UF_PATH_CUTCOM_ON_BEFORE_ENGAGE, /* Set cutter compensation on before
                                               engage. */
           UF_PATH_CUTCOM_ON_AFTER_ENGAGE, /* Set cutter compensation on after
                                               engage. */
           UF_PATH_CUTCOM_ON_BEFORE_MOTION, /* Set cutter compensation on before
                                               first motion. */
           UF_PATH_CUTCOM_ON_LAST_ELEMENT   /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_cutcom_on_e UF_PATH_cutcom_on_t;

/****************************************************************************

   Specify positioning for the CUTCOM/ post command.
   Used for positioning the cutcom command in the path output relative to 
   a certain motion type. 

*****************************************************************************/ 

enum UF_PATH_cutcom_off_e 
        {
           UF_PATH_CUTCOM_OFF_BEFORE_RETRACT, /* Set cutter compensation off
                                                 before retract. */
           UF_PATH_CUTCOM_OFF_AFTER_RETRACT, /* Set cutter compensation off
                                                 after retract. */
           UF_PATH_CUTCOM_OFF_AFTER_MOTION, /* Set cutter compensation off
                                                 after motion. */
           UF_PATH_CUTCOM_OFF_LAST_ELEMENT  /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_cutcom_off_e UF_PATH_cutcom_off_t;
 
/****************************************************************************

   Specify the direction of motion.

*****************************************************************************/ 

enum UF_PATH_direction_e 
        {
           UF_PATH_DIRECTION_NONE,        /* Direction not specified. */
           UF_PATH_DIRECTION_CLOCKWISE,   /* Set the direction to clockwise. */
           UF_PATH_DIRECTION_COUNTER_CLW, /* Set the direction counter clockwise
                                          */
           UF_PATH_DIRECTION_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_direction_e UF_PATH_direction_t;

/****************************************************************************

   Specify the spindle speed unit.
 
*****************************************************************************/ 
enum UF_PATH_spindle_mode_e 
        {
           UF_PATH_SPINDLE_MODE_RPM,  /* Set the spindle speed mode to RPM,
                                         revolutions per minute. */
           UF_PATH_SPINDLE_MODE_SFM,  /* Set the spindle speed to SFM, surface
                                         feet per minute. */
           UF_PATH_SPINDLE_MODE_SMM,  /* Set the spindle speed to SMM, surface
                                         meters per minute. */
           UF_PATH_SPINDLE_MODE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_spindle_mode_e UF_PATH_spindle_mode_t;

/****************************************************************************

   Specify output mode of the coolant.
 
*****************************************************************************/ 

enum UF_PATH_coolant_type_e 
        {
           UF_PATH_COOLANT_TYPE_ON,   /* Turn coolant on. */
           UF_PATH_COOLANT_TYPE_MIST,   /* Turn coolant on in mist mode. */
           UF_PATH_COOLANT_TYPE_FLOOD,  /* Turn coolant on in flood mode. */
           UF_PATH_COOLANT_TYPE_TAP,  /* Turn coolant on in tap mode. */
           UF_PATH_COOLANT_TYPE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_coolant_type_e UF_PATH_coolant_type_t;

/****************************************************************************

   Specify the units of the DELAY/ post command.
 
*****************************************************************************/ 

enum UF_PATH_dwell_unit_e 
        {
           UF_PATH_DWELL_SECONDS,          /* Set delay units to seconds. */
           UF_PATH_DWELL_REVOLUTIONS,     /* Set delay units to refolutions. */
           UF_PATH_DWELL_UNIT_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_dwell_unit_e UF_PATH_dwell_unit_t;

/****************************************************************************

   Specify the object of rotation in the ROTATE/ post command.

*****************************************************************************/ 

enum UF_PATH_rotation_object_e 
        {
           UF_PATH_ROTATION_OBJECT_TABLE, /* Set rotation object to TABLE. */
           UF_PATH_ROTATION_OBJECT_HEAD, /* Set rotation object to HEAD. */
           UF_PATH_ROTATION_OBJECT_AAXIS, /* Set rotation object to A axis. */
           UF_PATH_ROTATION_OBJECT_BAXIS, /* Set rotation object to B axis. */
           UF_PATH_ROTATION_OBJECT_CAXIS, /* Set rotation object to C axis. */
           UF_PATH_ROTATION_OBJECT_LAST_ELEMENT  /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_rotation_object_e UF_PATH_rotation_object_t;

/****************************************************************************

   Specify the mode of rotation in the ROTATE/ post command.

*****************************************************************************/ 
enum UF_PATH_rotation_type_e 
        {
           UF_PATH_ROTATION_NONE,    /* Specifies the absolute angular position
                                        in degrees. */
           UF_PATH_ROTATION_ANGLE,    /* Specifies the absolute angular 
                                         position using ATANGL. */
           UF_PATH_ROTATION_ABSOLUTE,    /* Specifies the absolute angular 
                                            position in degrees using ABSOL. */
           UF_PATH_ROTATION_INCREMENTAL,    /* Specifies the incremental angular
                                               position in degrees from its
                                               present position. */
           UF_PATH_ROTATION_TYPE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;

typedef enum UF_PATH_rotation_type_e UF_PATH_rotation_type_t;

/****************************************************************************

   Output the output mode string to the SET/MODES post command
 
*****************************************************************************/ 

enum UF_PATH_output_mode_e 
        {
           UF_PATH_OUTPUT_MODE_ABSOLUTE,    /* Output motion as absolute
                                               motion from MCS origin. */
           UF_PATH_OUTPUT_MODE_INCREMENTAL, /* Output motion as incremental
                                               motion from previous position. */
           UF_PATH_OUTPUT_MODE_NONE,        /* Do not specify an output mode. */
           UF_PATH_OUTPUT_MODE_LAST_ELEMENT /* Placeholder, do not use. */
        };
typedef enum UF_PATH_output_mode_e UF_PATH_output_mode_t;

/****************************************************************************

   Output the type of machine string to the SET/MODES post command
 
*****************************************************************************/ 
enum UF_PATH_machine_mode_e 
        {
           UF_PATH_MACHINE_MILL,    /* Specify the output to be in MILL mode. */
           UF_PATH_MACHINE_TURN,    /* Specify the output to be in TURN mode. */
           UF_PATH_MACHINE_PUNCH,  /* Specify the output to be in PUNCH mode. */
           UF_PATH_MACHINE_LASER,  /* Specify the output to be in LASER mode. */
           UF_PATH_MACHINE_TORCH,  /* Specify the output to be in plasma-arc
                                      mode. */
           UF_PATH_MACHINE_WIRE,   /* Specify the output to be in Wire EDM
                                      mode. */
           UF_PATH_MACHINE_MODE_NONE, /* Don't specify an output machine mode.*/
           UF_PATH_MACHINE_MODE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_machine_mode_e UF_PATH_machine_mode_t;

/****************************************************************************

   Output for the SET/MODES post command
 
*****************************************************************************/ 
enum UF_PATH_parallel_mode_e 
        {
           UF_PATH_PARALLEL_ZAXIS,   /* Output motion along Z axis. */
           UF_PATH_PARALLEL_WAXIS,   /* Output motion along W axis. */
           UF_PATH_PARALLEL_VAXIS,   /* Output motion along V axis. */
           UF_PATH_PARALLEL_MODE_NONE,   /* Do not specify motion axis. */
           UF_PATH_PARALLEL_MODE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_parallel_mode_e UF_PATH_parallel_mode_t;

/****************************************************************************

   Output for the SET/MODES post command
 
*****************************************************************************/ 
enum UF_PATH_arc_mode_e
        {
           UF_PATH_ARC_LINEAR,   /* Only use linear interpolation to handle
                                    contouring moves. */
           UF_PATH_ARC_CIRCULAR, /* Use circular and linear interpolation. */
           UF_PATH_ARC_MODE_NONE, /* Don't specify the interpolation mode. */
           UF_PATH_ARC_MODE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_arc_mode_e UF_PATH_arc_mode_t;

/****************************************************************************

   Output the feedrate for the SET/MODES post command
 
*****************************************************************************/ 
enum UF_PATH_feedrate_mode_e
        {
           UF_PATH_FEEDRATE_OUTPUT_OFF, /* Use the feed rate given in FEDRAT. */
           UF_PATH_FEEDRATE_OUTPUT_IPM, /* Always use IPM for the feed rate. */
           UF_PATH_FEEDRATE_OUTPUT_MMPM, /* Always use MMPM for the feed rate.
                                         */
           UF_PATH_FEEDRATE_OUTPUT_IPR, /* Always use IPR for the feed rate.
                                         */
           UF_PATH_FEEDRATE_OUTPUT_MMPR, /* Always use MMPR for the feed rate.
                                         */
           UF_PATH_FEEDRATE_OUTPUT_INVERS, /* Output feed rates as inverse time.
                                           */
           UF_PATH_FEEDRATE_OUTPUT_MODE_NONE, /* Don't specify feed rate mode.*/
           UF_PATH_FEEDRATE_MODE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;

typedef enum UF_PATH_feedrate_mode_e UF_PATH_feedrate_mode_t;

/****************************************************************************

   Used in the SEQNO/ post command. The sequence number,
   sequence frequency and the sequence increment are valid only if this enum
   is set to be UF_PATH_SEQNO_N.
 
*****************************************************************************/ 
enum UF_PATH_seqno_e
        {
           UF_PATH_SEQNO_N,   /* N is the sequencing number type. */
           UF_PATH_SEQNO_OFF, /* Terminates the output of sequence numbers
                                 for succeeding blocks. */
           UF_PATH_SEQNO_ON,  /* Resumes the output of sequence numbers for
                                 succeeding blocks. */
           UF_PATH_SEQNO_AUTO, /* Outputs the CL source record number which 
                                  caused the block of output as the sequence
                                  number. */
           UF_PATH_SEQNO_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_seqno_e UF_PATH_seqno_t;

/****************************************************************************

   Specify the flush type in the Wire EDM post commands.

*****************************************************************************/ 
enum UF_PATH_flush_type_e
        {
           UF_PATH_FLUSH_ON,   /* Begins flushing. */
           UF_PATH_FLUSH_OFF,  /* Ends flushing. */
           UF_PATH_FLUSH_TYPE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_flush_type_e UF_PATH_flush_type_t;

/****************************************************************************

   Specify the path guide type in the Wire EDM post commands.

*****************************************************************************/ 
enum UF_PATH_guide_e
        {
           UF_PATH_GUIDE_NONE,   /* Leaves the guide unspecified. */
           UF_PATH_GUIDE_UPPER,  /* Specifies upper guide flushing nozzle. */
           UF_PATH_GUIDE_LOWER,  /* Specifies lower guide flushing nozzle. */
           UF_PATH_GUIDE_ALL,    /* Specifies both upper and lower guide
                                    flushing nozzle. */
           UF_PATH_GUIDE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_guide_e UF_PATH_guide_t;

/****************************************************************************

   Specify the pressure type in the Wire EDM post commands.

*****************************************************************************/ 
enum UF_PATH_pressure_e
        {
           UF_PATH_PRESSURE_NONE,  /* Leave pressure unspecified. */
           UF_PATH_PRESSURE_LOW,   /* Specifies low flushing pressure. */
           UF_PATH_PRESSURE_MEDIUM,   /* Specifies medium flushing pressure. */
           UF_PATH_PRESSURE_HIGH,   /* Specifies high flushing pressure. */
           UF_PATH_PRESSURE_REGISTER,   /* Use the value in the flush register
                                           to specify the flushing pressure. */
           UF_PATH_PRESSURE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_pressure_e UF_PATH_pressure_t;

/****************************************************************************

   Specify the tank type in the Wire EDM post commands.

*****************************************************************************/ 
enum UF_PATH_tank_type_e
        {
           UF_PATH_TANK_IN,  /* Fill the flushing tank. */
           UF_PATH_TANK_OUT,  /* Empty the flushing tank. */
           UF_PATH_TANK_TYPE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;

typedef enum UF_PATH_tank_type_e UF_PATH_tank_type_t;

/****************************************************************************

   Specifying whether an OPSKIP/ON or an OPSKIP/OFF
   post command is to be output.

*****************************************************************************/ 
enum UF_PATH_op_skip_e
        {
           UF_PATH_OP_SKIP_ON,  /* Set OPSKIP on. */
           UF_PATH_OP_SKIP_OFF,  /* Set OPSKIP off. */
           UF_PATH_OP_SKIP_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_op_skip_e UF_PATH_op_skip_t;

/****************************************************************************

   Specify the motion shape.

*****************************************************************************/ 
enum UF_PATH_shape_e
        {
           UF_PATH_SHAPE_LINEAR=0,      /* Motion shape linear  */
           UF_PATH_SHAPE_CIRCULAR_CW=1, /* Motion shape circular clockwise. */
           UF_PATH_SHAPE_CIRCULAR_CCW=2, /* Motion shape circular counter
                                            clockwise. */
           UF_PATH_SHAPE_HELICAL_CW=5,  /* Motion shape helical clockwise. */
           UF_PATH_SHAPE_HELICAL_CCW=6,  /* Motion shape helical counter
                                            clockwise. */
           UF_PATH_SHAPE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;

typedef enum UF_PATH_shape_e UF_PATH_shape_t;
/****************************************************************************

   Specify the motion type. UF_PATH_MOTION_TYPE_DEPARTURE and 
   UF_PATH_MOTION_TYPE_THREAD_TURN are to be
   used only in specifying motion types on a lathe. 
   
*****************************************************************************/ 
enum UF_PATH_motion_type_e
        {
           UF_PATH_MOTION_TYPE_UNDEFINED=0,  /* Motion type undefined. */
           UF_PATH_MOTION_TYPE_RAPID=1, /* Motion type rapid. */
           UF_PATH_MOTION_TYPE_ENGAGE=2, /* Motion type engage. */
           UF_PATH_MOTION_TYPE_CUT=3, /* Motion type cut. */
           UF_PATH_MOTION_TYPE_RETRACT=4, /* Motion type retract. */
           UF_PATH_MOTION_TYPE_FIRST_CUT=5, /* Motion type first cut. */
           UF_PATH_MOTION_TYPE_APPROACH=6, /* Motion type approach. */
           UF_PATH_MOTION_TYPE_STEPOVER=7, /* Motion type stepover. */
           UF_PATH_MOTION_TYPE_DEPARTURE=8, /* Motion type departure.  This is
                                               only valid for a lathe. */
           UF_PATH_MOTION_TYPE_RETURN=9, /* Motion type return. */
           UF_PATH_MOTION_TYPE_TRAVERSAL=10, /* Motion type traversal. */
           UF_PATH_MOTION_TYPE_THREAD_TURN=11, /* Motion type thread.  This is
                                                  only valid for a lathe*/
           UF_PATH_MOTION_TYPE_FROM=12, /* Motion type from. */
           UF_PATH_MOTION_TYPE_GOHOME=13, /* Motion type gohome. */
           UF_PATH_MOTION_TYPE_CYCLE=14, /* Motion type cycle. */
           UF_PATH_MOTION_TYPE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_motion_type_e UF_PATH_motion_type_t;

/****************************************************************************

   Specify the material side of the tool with
   respect to the job. This is meaningful for circular motion type only.
 
*****************************************************************************/ 

enum UF_PATH_side_e
        {
           UF_PATH_SIDE_UNDEFINED = 0, /* Material side undefined. */
           UF_PATH_SIDE_RIGHT = 1, /* Material side right. */
           UF_PATH_SIDE_ON = 2, /* On material. */
           UF_PATH_SIDE_LEFT = 3, /* Material side left. */
           UF_PATH_SIDE_LAST_ELEMENT /* Placeholder, do not use. */
        } ;

typedef enum UF_PATH_side_e UF_PATH_side_t;

/****************************************************************************

   Specify the feed rate units.
 
*****************************************************************************/ 
enum UF_PATH_feed_unit_e
        {
           UF_PATH_FEED_UNIT_NONE = 0, /* No feed unit. */
           UF_PATH_FEED_UNIT_PER_MINUTE = 1, /* Feed units in minutes. */
           UF_PATH_FEED_UNIT_PER_REVOLUTION = 2, /* Feed units in revolutions.
                                                 */
           UF_PATH_FEED_UNIT_LAST_ELEMENT /* Placeholder, do not use. */
        } ;
typedef enum UF_PATH_feed_unit_e UF_PATH_feed_unit_t;

/****************************************************************************

   Specify contact data for a motion GOTO/.
   
*****************************************************************************/ 

struct UF_PATH_contact_data_s
{
    double contact_pt[3];          /*  contact point for the motion.  */
    double contact_axis[3];        /*  tool axis of contact point.  */
    double contact_arc_axis[3];    /*  Contact arc axis for circular motion.  */
    double contact_arc_center[3];  /*  Contact arc center for circular motion.  */
    double contact_arc_radius;     /*  contact arc radius for circular motion.  */
    UF_PATH_shape_t contact_shape; /*  used to describe shape of contact motion.  */
};
typedef struct UF_PATH_contact_data_s UF_PATH_contact_data_t;

/****************************************************************************

   Specify data for a linear motion GOTO/.  The position array is the 
   coordinate of the point to go to, and the feed_value is the feed rate value.
   
*****************************************************************************/ 
struct UF_PATH_linear_motion_s 
        {
           double                  position[3]; /* Coordinates of the point. */
           double                  tool_axis[3]; /* Tool axis specification. */
           double                  feed_value; /* Feed value. */
           UF_PATH_feed_unit_t     feed_unit;  /* Units of feed. */
           UF_PATH_motion_type_t   type; /* Motion type. */
        } ;
typedef struct UF_PATH_linear_motion_s UF_PATH_linear_motion_t;



/****************************************************************************

   Specify data for a circular motion CIRCLE. 

*****************************************************************************/ 
struct UF_PATH_circular_motion_s
        {
           double                  start[3]; /* this array specifies the start 
                                             point x,y,z coordinates(this should
                                             be the end point of the previous 
                                             motion)
                                             */
           double                  start_tool_axis[3]; /* This array specifies
                                             the starting tool axis. */
           double                  end[3];/* this array specifies the end
                                          point x,y,z coordinates.
                                          */

           double                  end_tool_axis[3]; /* This array specifies
                                             the ending tool axis. */
           double                  arc_axis[3]; /* this array specifies the
                                                vector which is the axis of
                                                the motion.
                                                */
           double                  arc_center[3]; /* this array specifies the
                                                  x,y,z coordinates of the 
                                                  center of the arc.
                                                  */
           double                  arc_radius; /* This is the radius of the 
                                               arc. */
           double                  tolerance; /* Tolerance to be used for arc
                                                 fits. */
           double                  feed_value; /* This is the feed rate
                                               value. 
                                               */
           UF_PATH_feed_unit_t     feed_unit; /* This specifies the units of the
                                                 feed value. */
           UF_PATH_motion_type_t   type;  /* This is the type of the motion. */
           UF_PATH_side_t          material_side; /* This specifies the material
                                                     side. */
           UF_PATH_shape_t         shape; /* This specifies the shape. */
        } ;

typedef struct UF_PATH_circular_motion_s UF_PATH_circular_motion_t;

/****************************************************************************

   Specify data for a Helical motion CIRCLE/...........,TIMES,n

*****************************************************************************/ 
struct UF_PATH_helical_motion_s
        {
           double                  start[3]; /* this array specifies the start 
                                             point x,y,z coordinates(this should
                                             be the end point of the previous 
                                             motion)
                                             */
           double                  start_tool_axis[3]; /* This array specifies
                                             the starting tool axis. */
           double                  end[3];/* this array specifies the end
                                          point x,y,z coordinates.
                                          */
           double                  end_tool_axis[3]; /* This array specifies
                                             the ending tool axis. */
           double                  arc_axis[3]; /* this array specifies the
                                                vector which is the axis of
                                                the motion.
                                                */
           double                  arc_center[3]; /* this array specifies the
                                                  x,y,z coordinates of the 
                                                  center of the helix at 
                                                  the end point.
                                                  */
           double                  arc_radius; /* This is the radius of the 
                                               helix. */
           double                  tolerance; /* Tolerance to be used for arc
                                                 fits. */
           double                  times;     /* Number of Turns including 
                                                 partial turn*/
           double                  feed_value; /* This is the feed rate
                                               value. 
                                               */
           UF_PATH_feed_unit_t     feed_unit; /* This specifies the units of the
                                                 feed value. */
           UF_PATH_motion_type_t   type;  /* This is the type of the motion. */
           UF_PATH_side_t          material_side; /* This specifies the material
                                                     side. */
           UF_PATH_shape_t         shape; /* This specifies the shape. */
        } ;

typedef struct UF_PATH_helical_motion_s UF_PATH_helical_motion_t;
/****************************************************************************

   Specify data for the tool change post command. 

*****************************************************************************/ 

struct UF_PATH_tool_change_s 
        {
           double                xoffset_value; /* offset value of the tool
                                                in the X direction.
                                                */
           double                yoffset_value; /* offset value of the tool
                                                in the Y direction.
                                                */
           double                zoffset_value; /* offset value of the tool
                                                in the Z direction.  This 
                                                value is only used by mill. */
           double                tool_angle; /* the angle at which the tool
                                             is mounted.
                                             */ 
           double                radius; /* the nose radius of the tool */
           int                   tool_number; /*The tool number */
           int                   adjust_register; /* the register to use for
                                                  tool length compensation
                                                  */
           UF_PATH_head_type_t   head_type;  /* The type of the head. */
           logical               adjust_flag; /* the adjust register is output
                                              if and only if this is TRUE.
                                              */
           logical               tool_offset_flag; /* the tool offsets are
                                                   output if and only if this
                                                   is TRUE.
                                                   */
           logical               tool_number_flag; /* the tool number is output
                                                   if and only if this is TRUE.
                                                   */
           logical               tool_angle_radius_flag; /* the tool angle and
                                                         radius are output
                                                         if and only if this
                                                         TRUE
                                                         */
           logical               manual_change_flag; /* the string MANUAL is
                                                     output if and only
                                                     if this is TRUE.
                                                     */
        } ;
typedef struct UF_PATH_tool_change_s UF_PATH_tool_change_t;

/****************************************************************************

   Specify data for the tracking point change post command. 

****************************************************************************/ 
struct UF_PATH_tracking_point_change_s 
        {
           double                xoff;
           double                yoff;
           int                   adjust_register;
           int                   cutcom_register;
        } ;
typedef struct UF_PATH_tracking_point_change_s UF_PATH_tracking_point_change_t;


/****************************************************************************

   Specify the data for the SPINDL/ post command. 

*****************************************************************************/ 
struct UF_PATH_spindle_on_s 
        {
           double                   speed; /* is the speed of the spindle */
           double                   maxrpm; /* is the maximum allowed speed
                                            of the spindle
                                            */
           char                     range[20]; /* the spindle speed range */
           UF_PATH_spindle_mode_t   mode;    
           UF_PATH_direction_t      direction;
           logical                  speed_flag; /* the speed is output if and
                                                only if this flag is TRUE.
                                                */
           logical                  maxrpm_flag; /* the maximum speed is output
                                                 if and only if this flag is 
                                                 TRUE.
                                                 */ 
           logical                  range_flag; /* the range is output if and
                                                only if this flag is TRUE.
                                                */
        } ;

typedef struct UF_PATH_spindle_on_s UF_PATH_spindle_on_t;

/****************************************************************************

   Specify data for the ROTATE/ post command.

*****************************************************************************/ 
struct UF_PATH_rotate_s 
        {
           double                      rotation_angle; /* is the angle by which
                                                       to rotate.
                                                       */
           UF_PATH_rotation_object_t   rotation_object; 
           UF_PATH_rotation_type_t     rotation_type;
           UF_PATH_direction_t         rotation_direction;
           logical                     angle_flag; /* the rotation angle is
                                                   output if and only if
                                                   this flag is TRUE.
                                                   */
           logical                     rotref_flag; /* the string ROTREF is
                                                    output if and only if this
                                                    flag is TRUE.
                                                    */
         } ;
typedef struct UF_PATH_rotate_s UF_PATH_rotate_t;


/****************************************************************************

   Specify data for the FLUSH/ post command.

*****************************************************************************/ 

struct UF_PATH_flush_s 
        {
           UF_PATH_flush_type_t   flush_type;
           UF_PATH_guide_t        flushing_guide;
           UF_PATH_pressure_t     flushing_pressure;
           logical                flush_register;
           logical                guide_flag;
           logical                pressure_flag;
        } ;
typedef struct UF_PATH_flush_s UF_PATH_flush_t;

/****************************************************************************

   Specify data for the CUTCOM/ post command.

*****************************************************************************/ 

struct UF_PATH_cutcom_s 
        {
           UF_PATH_cutcom_mode_t   cutcom_mode;
           UF_PATH_plane_type_t    plane_type;
           UF_PATH_cutcom_on_t     cutcom_on_status;  
           UF_PATH_cutcom_off_t    cutcom_off_status;
           int                     adjust_register; /* the register to use for
                                                    cutter compensation
                                                    */    
           logical                 full_cutcom_output; /* a full cutcom command
                                                       is output if and only
                                                       if this flag is TRUE.
                                                       */
           logical                 adjust_flag; /* the adjust register is
                                                output if and only if
                                                this flag is TRUE.
                                                */ 
        } ;
typedef struct UF_PATH_cutcom_s UF_PATH_cutcom_t;

struct UF_PATH_level_marker_s 
        {
           double                  tool_axis[3]; /* Tool axis specification. */
           double                  depth;       /* the depth from top */
        } ;
typedef struct UF_PATH_level_marker_s UF_PATH_level_marker_t;

/******************************* Prototypes **********************************/


/*****************************************************************************
This function initializes the tool path header.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_init_tool_path(
UF_PATH_id_t path_id  /* <I>
                      Identifier passed from UF function
                      */
);

/*****************************************************************************
This function creates a contact linear motion.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_contact_linear_motion
(
   UF_PATH_id_t             path_id,
   UF_PATH_linear_motion_t *linear_motion_data,
   UF_PATH_contact_data_t  *contact_data
);

/*****************************************************************************
This function creates a contact circular motion.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int   UF_PATH_create_contact_circular_motion
(
   UF_PATH_id_t               path_id,
   UF_PATH_circular_motion_t *motion_data,
   UF_PATH_contact_data_t    *contact_data
);

/*****************************************************************************
 This function signifies the end of the tool path. The "oper_id" is no
longer valid after this function executes.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_end_tool_path(
UF_PATH_id_t path_id  /* <I>
                      Identifier of the path to end
                      */
);

/*****************************************************************************
This function allows the creation of linear motion( GOTO/ ).

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_linear_motion(
UF_PATH_id_t path_id ,/* <I>
                      Path to perform action on
                      */
UF_PATH_linear_motion_t * linear_motion_data  /* <I>
                                              Structure specifying the linear 
                                              motion
                                              */
);

/*****************************************************************************
This function allows the creation of circular motion (CIRCLE/ ).

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_circular_motion(
UF_PATH_id_t path_id ,/* <I>
                      Path to perform action on
                      */
UF_PATH_circular_motion_t * circular_motion_data  /* <I>
                                                  Structure defining the 
                                                  circular motion.
                                                  */
);

/*****************************************************************************
This function allows the creation of helical motion (CIRCLE/.....,TIMES ).

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_helical_motion(
UF_PATH_id_t path_id ,/* <I>
                      Path to perform action on
                      */
UF_PATH_helical_motion_t * helical_motion_data  /* <I>
                                                  Structure defining the 
                                                  helical motion.
                                                  */
);
/*****************************************************************************
This function allows the creation of a post command text string.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_text(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const char * text  /* <I>
                   The post command text string
                   */
);

/*****************************************************************************
This function allows the creation of post command PPRINT/.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_pprint(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const char* text  /* <I>
                  The text to output on the PPRINT command
                  */
);

/*****************************************************************************
This function allows the creation of the post command DISPLY/.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_opmessage(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const char* text  /* <I>
                  The text to output to the operator.
                  */
);


/*****************************************************************************
This function allows the creation of the post command ORIGIN/. The
appended text is optional. If 'text' is NULL then no appended text
appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_origin(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const double origin_coordinates[3] ,/* <I>
                                    The origin x/y/z
                                    */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command SEQNO/. The
appended text is optional. If "text" is NULL then no appended text
appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_seqno(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_seqno_t seq_type ,/* <I>
                          The sequence type
                          */
int seq_number, /* <I>  
                   The sequence number, only valid if seq_type is
                   UF_PATH_SEQNO_N 
                */

int seq_incr ,/* <I>
              Only valid if seq_type is UF_PATH_SEQNO_N
              */
int seq_freq ,/* <I>
              Only valid if seq_type is UF_PATH_SEQNO_N
              */
const char * text  /* <I>
                   The post command appended text
                   */
);


/*****************************************************************************
This function allows the creation of post command SET/. The appended text is 
optional. If 'text' is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_set_mode(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_output_mode_t ouput_mode ,/* <I>
                                  The output mode for this tool path.
                                  */
UF_PATH_feedrate_mode_t feedrate_mode ,/* <I>
                                       The feedrate mode for this tool path.
                                       */
UF_PATH_arc_mode_t arc_mode ,/* <I>
                             The arc mode for this tool path.
                             */
UF_PATH_parallel_mode_t parallel_mode ,/* <I>
                                       The parallel mode for this tool path.
                                       */
UF_PATH_machine_mode_t machine_mode ,/* <I>
                                     The machine mode for this tool path.
                                     */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command SELECT/HEAD.  The appended 
text is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_select_head(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_head_type_t head_type ,/* <I>
                               The head type in the turret of the lathe.
                               */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This functions allows the creation of post command LOAD/TOOL(for mill) or 
TURRET/ (for lathe). The appended text is optional. If "text" is NULL then no 
appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_tool_change(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_tool_change_t * tool_change_data ,/* <I>
                                          Data specifying the tool change to 
                                          make.
                                          */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command TRACKING POINT CHANGE.
The appended text is optional. 
If "text" is NULL then bo appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_tracking_point_change
(
   UF_PATH_id_t                     path_id,          /* <I> The path id for this event */
   UF_PATH_tracking_point_change_t *tool_change_data  /* <I> Data specifying the tracking point change to make. */
);

/*****************************************************************************
This function allows the creation of post command SPINDL/. The appended text 
is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_spindle_on(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_spindle_on_t * spindle_on_data ,/* <I>
                                        The spindle data for the command.
                                        */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command SPINDL/OFF. The appended text
is optional. If "text" is NULL then bo appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_spindle_off(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command SPINDL/REVERSE.
The appended text is optional. 
If "text" is NULL then bo appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_spindle_reverse(
UF_PATH_id_t path_id ,/* <I> The path id for this event */
const char * text  /* <I> The post command appended text */
);

/*****************************************************************************
This function allows the creation of post command COOLNT/.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_coolant_on(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_coolant_type_t coolant_type ,/* <I>
                                     The coolant type.
                                     */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command COOLNT/OFF.  The appended 
text is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_coolant_off(
UF_PATH_id_t paht_id ,/* <I>
                      The path id for this event
                      */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command OPSTOP. The appended text is
optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_op_stop(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post comand OPSKIP/. The appended text is 
optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_op_skip(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_op_skip_t skip_option ,/* <I>
                               The skip option.
                               */
const char * text  /* <I>
                   The post command appended text
                   */
);


/*****************************************************************************
This function allows the creation of post command STOP. The appended text is 
optional. If the "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_stop(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command DELAY/. The appended text is 
optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_dwell(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
double dwell_value ,/* <I>
                    Amount of delay
                    */
UF_PATH_dwell_unit_t dwell_unit ,/* <I>
                                 The units to use for the delay.
                                 */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command AUXFUN/. The appended text 
is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_auxfun(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
int auxfun_code ,/* <I>
                 Auxfun value
                 */
const char * text  /* <I>
                   The post command appended text
                   */
);


/*****************************************************************************
This function allows the creation of post command PREFUN/. The appended text 
is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_prefun(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
int prefun_code ,/* <I>
                 Prefun value
                 */
const char * text  /* <I>
                   The post command appended text
                   */
);


/*****************************************************************************
This function allows the creation of post command CLAMP/. The appended text is
optional. If "text" is NULL then no appended test appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_clamp(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_clamp_status_t clamp_status ,/* <I>
                                     The clamp status.
                                     */
UF_PATH_axis_t axis_type ,/* <I>
                          The axis type.
                          */
const char * text  /* <I>
                   The post command appended text
                   */
);


/*****************************************************************************
This function allows the creation of post command SET/ADJUST.  The appended 
text is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_tool_length_comp(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
int tool_comp_register ,/* <I>
                        Tool length compensation register value
                        */
const char * text  /* <I>
                   The post command appended text
                   */
);


/*****************************************************************************
This function allows the creation of post command SELECT/TOOL.  The appended 
text is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_tool_preselect(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
int tool_number ,/* <I>
                 Tool number value
                 */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command ROTATE/. The appended text 
is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_rotate(
UF_PATH_id_t path_id ,/* <I>
                      The path ID for this event
                      */
UF_PATH_rotate_t * rotate_data ,/* <I>
                                The data specifying the rotation.
                                */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command LOAD/WIRE.  The appended 
text is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_thread_wire(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command UNLOAD/WIRE.  The appended 
text is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_cut_wire(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command FLUSH/. The appended text is
optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_flush(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_flush_t * flush_data ,/* <I>
                              The flush data.
                              */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command FLUSH/IN. The appended text 
is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_flush_tank(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_tank_type_t tank_type ,/* <I>
                               Specifies the tank type.
                               */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command POWER/. The appended text is 
optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_power(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
double power_value ,/* <I>
                    Value of the power register
                    */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command SET/UPPER. The appended text 
is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_wire_guides(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of the post command FEDRAT/.  The appended 
text is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_fedrat(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
double fedrat_value ,/* <I>
                     Feed rate value
                     */
const char * text  /* <I>
                   The post command appended text
                   */
);


/*****************************************************************************
This function allows the creation of post command STAN/. The appended text is 
optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_wire_angle(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
double slope_value ,/* <I>
                    Slope of the wire
                    */
double angle_value ,/* <I>
                    Angle of the wire
                    */
logical angle_flag ,/* <I>
                    Flag to indicate if angle is specified
                    */
const char * text  /* <I>
                   The post command appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command CUTCOM/. The appended text 
is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_wire_cutcom(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_cutcom_mode_t cutcom_mode ,/* <I>
                                   The mode for the CUTCOM command.
                                   */
int adjust_register ,/* <I>
                     Adjust register value
                     */
logical cutcom_off_flag ,/* <I>
                         Flag indicating if cutcom off is to be
                         output
                         */
logical adjust_flag ,/* <I>
                     Flag to indicate if the adjust register is
                     specified
                     */
const char * text  /* <I>
                   The post comand appended text
                   */
);

/*****************************************************************************
This function allows the creation of post command CUTCOM/. The appended text 
is optional. If "text" is NULL then no appended text appears.

Environment: Internal  and  External

See Also:

History:
 ******************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_cutcom(
UF_PATH_id_t path_id ,/* <I>
                      The path id for this event
                      */
UF_PATH_cutcom_t * cutcom_data ,/* <I>
                                Structure specifying the cutcom data.
                                */
const char * text  /* <I>
                   The post command appended text
                   */
);


/*****************************************************************************
This function allows the creation of level marker.

Environment: Internal  and  External

See Also:

History:
 *****************************************************************************/
extern UFUN_CAMEXPORT int UF_PATH_create_level_marker(
UF_PATH_id_t path_id ,/* <I> Path to perform action on */
UF_PATH_level_marker_t * level_marker_data  /* <I> Structure specifying the level marker data */
);

#ifdef __cplusplus
}
#endif

#undef EXPORTLIBRARY

#endif
