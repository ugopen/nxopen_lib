/*==============================================================================

             Copyright (c) 2002 Unigraphics Solutions Inc.
                     Unpublished - All rights reserved

================================================================================*/

/******************************************************************************
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *         UF_DRF_create_custom_symbol_instance                               *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   The following example requires a blank, open part. The code generates a  *
 *   custom symbol instance from newly created geometry, adding several       *
 *   lines, a mandatory note, and a controlled note.                          *
 *                                                                            *
              
 *                                                                            *
 ******************************************************************************/


#include <stdio.h>
#include <uf.h>
#include <uf_csys.h>
#include <uf_ui.h>
#include <uf_curve.h>
#include <uf_drf.h>
#include <uf_drf_types.h>
#include <uf_disp.h>


/* This macro allows us to automatically report User Function errors via
   the function report_error */
#define UF_CALL(X) (report_error( __FILE__, __LINE__, #X, (X)))

/***********************************************************************
 *
 * DESCRIPTION:  This function is used for reporting errors from User
 *               Function to the listing window.
 *
 ***********************************************************************/
static int report_error( char *file, int line, char *call, int irc)
{
    if (irc)
    {
        char err[133],
             msg[133];

        UF_get_fail_message(irc, err);
        sprintf(msg, "error %d at line %d in %s", irc, line, file);

        if (!UF_UI_open_listing_window())
        {
            UF_UI_write_listing_window(err);
            UF_UI_write_listing_window("\n");
            UF_UI_write_listing_window(msg);
            UF_UI_write_listing_window("\n");
            UF_UI_write_listing_window(call);
            UF_UI_write_listing_window(";\n\n");
        }
        else
        {
#ifdef _USRDLL
            uc1601(err, TRUE);
            uc1601(msg, TRUE);
#else
            fprintf(stderr, "%s\n", err);
            fprintf(stderr, "%s\n", msg);
            fprintf(stderr, "%s;\n\n", call);
#endif
        }
    }
    return(irc);
}

/**************************************************************************
 *
 * DESCRIPTION:  This function will ask the user for a screen pick and
 *               return the position of the screen pick to the calling
 *               function.  In this example the screen pick is used to
 *               describe a location for the custom symbol.
 *
 ************************************************************************/
static logical specify_position(char *prompt, double pos[3])
{
    int
        resp = uc1615(prompt, pos);

    if (resp == 5) return TRUE;
    else return FALSE;

}

/*****************************************************************************
 *
 * DESCRIPTION:  This routine will create the geometry pieces which will later
 *               be incorporated into a custom symbol.  For the purpose of
 *               this example, we will only include two lines and a circle.
 *               Note, however, that many other objects may be included:
 *               splines, parabolas, hyperbolas, b-curves, crosshatching,
 *               and area fill are all valid consituent geometry for a
 *               custom symbol.
 *
 ****************************************************************************/
static void create_symbol_geometry(UF_DRF_custom_symbol_p_t symbol_definition)
{
    UF_CURVE_line_t
        line_data[2] = {{{ -0.5,0,0 }, { 0.5,0,0}}, {{0,-0.5,0}, {0,0.5,0}}};
    UF_CURVE_arc_t
        arc_data;
    double
        matrix_values[9] = {1.0, 0.0, 0.0,
                         0.0, 1.0, 0.0,
                            0.0, 0.0, 1.0},
        arc_center[3] = {0.0, 0.0, 0.0};
    tag_t
        matrix_tag = NULL_TAG;
    int irc;

    /*Create space for the tags to be stored*/
    symbol_definition->geometry = (tag_t *)UF_allocate_memory(sizeof(tag_t)*3, &irc);
    if (irc != 0)
    {
        symbol_definition->geometry = NULL;
        symbol_definition->num_geometry = 0;
        return;
    }
    else
        symbol_definition->num_geometry = 3;

    /*Create the two lines in a vertical "cross" shape*/
    UF_CALL(UF_CURVE_create_line(&line_data[0],
                                 &(symbol_definition->geometry[0])));
    UF_CALL(UF_CURVE_create_line(&line_data[1],
                                 &(symbol_definition->geometry[1])));

    /*Create the arc*/
    UF_CALL(UF_CSYS_create_matrix(matrix_values, &matrix_tag));
    arc_data.matrix_tag = matrix_tag;
    arc_data.start_angle = 0.0;
    arc_data.end_angle = TWOPI;
    arc_data.arc_center[0] = arc_center[0];
    arc_data.arc_center[1] = arc_center[1];
    arc_data.arc_center[2] = arc_center[2];
    arc_data.radius = 0.5;
    UF_CALL(UF_CURVE_create_arc(&arc_data, &(symbol_definition->geometry[2])));

    return;
}

/**********************************************************************
 *
 * DESCRIPTION:  This function will create three points which will be
 *               used as part of the custom symbol definition.
 *               The minimum number of required points for a custom
 *               symbol is one -- the anchor point.  However, you
 *               may also specify left and right leader terminator
 *               points as an option.  If you intend to create a
 *               custom symbol with a leader, you must create at
 *               least one leader terminator point.  If you create
 *               both left and right leader terminator points, the
 *               system will use these points to infer a leader side.
 *
 ********************************************************************/
static void create_symbol_points(UF_DRF_custom_symbol_p_t symbol_definition)
{
    double
        anchor_point[3] = {0.0, 0.0, 0.0},
        left_leader_point[3] = {-0.5, 0.0, 0.0},
        right_leader_point[3] = {0.5, 0.0, 0.0};
    UF_DRF_symbol_connection_t
        left_leader_connection,
        right_leader_connection;
    int
        irc;

    /*Create the anchor point*/
    /*Note that the relationship between the anchor point and the rest of
      the symbol geometry at creation time defines the origin of the object.
      When changing the position of the symbol interactively, this point
      will act as the "drag point" around which all the other symbol pieces
      orient themselves.  When changing symbol scale, this point will act
      as an invariant point (unless changing the symbol scale interactively
      via drag handles on the object).*/
    UF_CALL(UF_CURVE_create_point(anchor_point,
                                  &(symbol_definition->anchor_point)));

    /*Create the leader attachment points*/
    symbol_definition->connections = (UF_DRF_symbol_connection_t *)UF_allocate_memory(sizeof(UF_DRF_symbol_connection_t)*2, &irc);
    if (irc != 0)
    {
        symbol_definition->connections = NULL;
        symbol_definition->num_connections = 0;
        return;
    }
    else
        symbol_definition->num_connections = 2;

    left_leader_connection.connection_type = UF_DRF_LEFT_LEADER_CONNECTION;
    UF_CALL(UF_CURVE_create_point(left_leader_point,
                                  &(left_leader_connection.connection_point)));
    symbol_definition->connections[0] = left_leader_connection;

    right_leader_connection.connection_type = UF_DRF_RIGHT_LEADER_CONNECTION;
    UF_CALL(UF_CURVE_create_point(right_leader_point,
                                  &(right_leader_connection.connection_point)));
    symbol_definition->connections[1] = right_leader_connection;

    return;
}

/************************************************************************
 *
 * DESCRIPTION: This function will create all the note objects necessary
 *              to define the text fields in the custom symbol.  For the
 *              purposes of this example, we will create one mandatory
 *              piece of text and one controlled piece of text.  In
 *              general, however, you may create as many notes as you want
 *              using the following types:
 *                Mandatory:  The text cannot be edited
 *                Controlled: The text may only be edited from a list of
 *                            predefined strings.
 *                Partially controlled:  The text may be edited from a list
 *                                       of predefined strings, or it can
 *                                       be arbitrary.
 *                Arbitrary: The text may be edited arbitrarily
 *                Integer: The text may only be an integer number within
 *                         certain boundaries.
 *                Real: The text may only be a real number within certain
 *                      boundaries.
 *
 *************************************************************************/
static void create_symbol_text(UF_DRF_custom_symbol_p_t symbol_definition)
{
    int
        integer_draft_prefs[100],
        original_integer_draft_prefs[100],
        num_strings = 5,
        inx = 0,
        irc;
    double
        real_draft_prefs[70],
        original_real_draft_prefs[70],
        upper_right_note_origin[3] = {0.125, 0.125, 0.0},
        lower_left_note_origin[3] = {-0.125, -0.125, 0.0};
    char
        diameter[27],
        radius[27],
        *note_text[1] = { "DUMMY TEXT" },
        *mandatory_note_title = "My mandatory note",
        *mandatory_text_string = "AA",
        *controlled_note_title = "My controlled note",
        *controlled_note_strings[5] = {"BB", "CC", "DD", "EE", "FF"};
    tag_t
        upper_right_note,
        lower_left_note;


    /*Set up the preferences that we will use to create the notes.  Also,
      save a copy of the original preferences so that we can change back
      to the original preferences after creating the notes.*/
    UF_CALL(UF_DRF_ask_preferences(integer_draft_prefs, real_draft_prefs,
                                   radius, diameter));
    UF_CALL(UF_DRF_ask_preferences(original_integer_draft_prefs,
                                   original_real_draft_prefs, radius,
                                   diameter));
    /*Set the entity site to be lower left.  This will enable the note in
      the upper right portion of the symbol to grow up and to the right
      when the text size changes.*/
    integer_draft_prefs[30] = 7;

    /*Save the changes to drafting preferences.*/
    /*Although for this example we are only changing the text alignment
      position, notice that the text objects in the symbol definition
      will display using all of the preferences of the note at the time
      of symbol creation.  Thus, if you are interested in maintaining
      text at a certain size, font, or color different from the current
      drafting preferences, make sure the drafting preferences you
      desire are applied to the notes before the custom symbol is created.*/
    UF_CALL(UF_DRF_set_preferences(integer_draft_prefs, real_draft_prefs,
                                   radius, diameter));

    /*Create the notes.  Be aware that the system will use the note origin
      with respect to the other symbol pieces to define the shape of the
      symbol.  Also be aware that the text alignment position of the note
      will affect how the note moves when the text size is changed.  The
      text alignment position will be an invariant point with respect to
      the rest of the symbol pieces if the text size changes.*/
    /*The first note we create will be located in the upper right quadrant,
      with its lower left point slightly above and to the right of the
      symbol origin*/
    UF_CALL(UF_DRF_create_note(1, note_text, upper_right_note_origin, 0,
                               &upper_right_note));

    /*Change the text alignment location for the second note:
      Set the entity site to be upper right.  This will enable the note
      in the lower left portion of the symbol to grow down and to the
      left when the text size changes.*/
    integer_draft_prefs[30] = 3;
    /*Save the changes to drafting preferences.*/
    UF_CALL(UF_DRF_set_preferences(integer_draft_prefs, real_draft_prefs,
                                   radius, diameter));

    /*Create the second note.  This note will be located with its upper
      right corner slightly below and to the left of the symbol origin.*/
    UF_CALL(UF_DRF_create_note(1, note_text, lower_left_note_origin, 0,
                               &lower_left_note));

    symbol_definition->num_text = 2;
    symbol_definition->text = (UF_DRF_custom_symbol_text_t *)UF_allocate_memory(sizeof(UF_DRF_custom_symbol_text_t)*2, &irc);
    if (irc != 0)
        return;

    /*Create the text objects.  Now that the note objects have been
      created, we can specify note type information as well as the
      predefined text strings for controlled text types or upper and lower
      bounds for numerical text types.  In this example we will use the
      upper right note to create a mandatory text object with the text
      "AA" and use the lower left note to create a controlled text object
      with the default text "BB", but also define the text strings "CC",
      "DD", "EE", and "FF" as valid choices.*/
    UF_CALL(UF_DRF_initialize_custom_symbol_text_data(&(symbol_definition->text[0])));
    (symbol_definition->text[0]).note_tag = upper_right_note;
    (symbol_definition->text[0]).text_type = UF_DRF_MANDATORY_TEXT;
    (symbol_definition->text[0]).title = mandatory_note_title;
    (symbol_definition->text[0]).simple_text = mandatory_text_string;

    UF_CALL(UF_DRF_initialize_custom_symbol_text_data(&(symbol_definition->text[1])));
    (symbol_definition->text[1]).note_tag = lower_left_note;
    (symbol_definition->text[1]).text_type = UF_DRF_FULLY_CONTROLLED_TEXT;
    (symbol_definition->text[1]).title = controlled_note_title;
    (symbol_definition->text[1]).num_optional_strings = num_strings;
    (symbol_definition->text[1]).optional_strings = (char **)UF_allocate_memory((sizeof(char*) * num_strings), &irc);
    if (irc != 0)
        return;
    for (inx = 0; inx < num_strings; inx++)
    {
        (symbol_definition->text[1]).optional_strings[inx] = controlled_note_strings[inx];
    }
    (symbol_definition->text[1]).current_option = 0;

    /*Reset drafting preferences since we are done creating the notes*/
    UF_CALL(UF_DRF_set_preferences(original_integer_draft_prefs,
                                   original_real_draft_prefs, radius,
                                   diameter));
}

/************************************************************************
 *
 * DESCRIPTION:  This function will initialize the data structure and
 *               set the appropriate information to add a leader to the
 *               custom symbol.
 *
 ***********************************************************************/
static void create_symbol_leader(UF_DRF_custom_symbol_p_t symbol_definition)
{
    UF_DRF_leader_p_t
        leader;
    double
        leader_terminator_point_coords[3] = {-4.0, -3.0, 0.0};
    int irc;

    symbol_definition->leader = (UF_DRF_leader_p_t)UF_allocate_memory(sizeof(UF_DRF_leader_t), &irc);
    if (irc != 0)
    {
        symbol_definition->leader = NULL;
        return;
    }
    else
        leader = symbol_definition->leader;

    /*We can add more than one leader to a single leader structure.
      However, for purposes of this example we will only use one.*/
    leader->num_leaders = 1;

    /*Create the terminator point for the leader and add it to the
      structure*/
    leader->leader_terminators = (tag_t *)UF_allocate_memory(sizeof(tag_t), &irc);
    if (irc != 0)
        return;
    UF_CALL(UF_CURVE_create_point(leader_terminator_point_coords,
                                  &(leader->leader_terminators[0])));

    /*Define the leader to be from the left.*/
    leader->leader_orientation = UF_DRF_LEADER_LEFT;

    /*Create an intermediate points structure.  This structure contains
      a list of point coordinates for any intermediate points between
      the leader terminator and the stub.  In this example, there are
      no intermediate points.*/
    leader->intermediate_points = (UF_DRF_intermediate_points_t *)UF_allocate_memory(sizeof(UF_DRF_intermediate_points_t), &irc);
    if (irc != 0)
        return;
    leader->intermediate_points[0].num_points = 0;
    leader->intermediate_points[0].points = NULL;

    return;
}

static void clean_up_memory(UF_DRF_custom_symbol_p_t symbol_definition)
{
    int
        inx = 0;

    /*Clean up the geometry array*/
    UF_free(symbol_definition->geometry);

    /*Clean up the connection array*/
    UF_free(symbol_definition->connections);

    /*Clean up the text array*/
    for (inx = 0; inx < symbol_definition->num_text; inx ++)
    {
        UF_free(symbol_definition->text[inx].optional_strings);
    }
    UF_free(symbol_definition->text);

    /*Clean up the leader data*/
    for (inx = 0; inx < symbol_definition->leader->num_leaders; inx ++)
    {
        UF_free(symbol_definition->leader->leader_terminators);

        UF_free(symbol_definition->leader->intermediate_points[inx].points);
    }
    UF_free(symbol_definition->leader->intermediate_points);
    UF_free(symbol_definition->leader);

}

/********************************************************************
 *
 * DESCRIPTION:  This function is the driving function for the
 *               creation of a custom symbol.  This function will
 *               initialize the data, fill in the appropriate data
 *               structures, and pass the data into the API to create
 *               the custom symbol.
 *
 * NOTES:
 * 1) The API currently does not support the creation of custom symbol
 *    instances from master symbol definitions.  This demonstration
 *    program will only show how to create individual custom symbol
 *    instances from non-reusable sets of geometry.
 *
 * 2) The API currently does not support editing of Custom Symbols
 *    similar to the functionality provided by selecting a Custom
 *    Symbol in the Insert->Custom Symbol dialog in Drafting.
 *    Until support is added in UG/Open, the only way to edit Custom
 *    Symbols (apart from editing symbol scale, angle, color,
 *    line font, and line width) is to edit them interactively.
 *    The ability to switch between a predefined set of text strings
 *    with controlled notes is one of the types of edits that is only
 *    available interactively.
 *
 ********************************************************************/
static void create_custom_symbol(void)
{
    tag_t
        symbol;
    UF_DRF_custom_symbol_t
        symbol_definition;

    /*Initialize the custom symbol data structures.*/
    UF_CALL(UF_DRF_initialize_custom_symbol_data(&symbol_definition));

    /*Create the geometry objects which will constitute the custom symbol.*/
    create_symbol_geometry(&symbol_definition);

    /*Create the points of the symbol. (Includes the symbol anchor point
      and the leader attachment points)*/
    create_symbol_points(&symbol_definition);

    /*Create the symbol text objects.*/
    create_symbol_text(&symbol_definition);

    /*Create the symbol leader*/
    create_symbol_leader(&symbol_definition);

    /*Get the actual location for the symbol from a screen pick*/
    specify_position("Place custom symbol", symbol_definition.origin);

    /*Create the custom symbol object*/
    UF_CALL(UF_DRF_create_custom_symbol_instance(&symbol_definition,
                                                 &symbol));

    /*Clean up dynamically allocated memory*/
    clean_up_memory(&symbol_definition);

}

/****************************************************************************
 *
 * DESCRIPTION:  This function is the entry point for internal User Function.
 *
 ****************************************************************************/
void ufusr(char *param, int *retcode, int paramLen)
{
    if (UF_CALL(UF_initialize())) return;
    create_custom_symbol();
    UF_terminate();
}

int ufusr_ask_unload(void)
{
    return (UF_UNLOAD_IMMEDIATELY);
}
