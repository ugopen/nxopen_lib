
/*=============================================================================
                        Copyright (c) 2004 UGS Corp.
                            All Rights Reserved
=============================================================================*/
/******************************************************************************
 *                                                                            *
 * FILE NAME - ufd_cam_ita_query.c  ufd_tai_sample.prt                        *
 *                                                                            *
 * DESCRIPTION -                                                              *
 *   This program shows how to use the following UG/Open API routine(s):      *
 *                                                                            *
 *   UF_SCOP_ask_tx_intp_data_type                                            *
 *   UF_SCOP_set_tx_intp_data_type                                            *
 *   UF_SCOP_ask_tx_intp_method                                               *
 *   UF_SCOP_set_tx_intp_method                                               *
 *   UF_SCOP_ask_tx_intp_vector_data                                          *
 *   UF_SCOP_set_tx_intp_vector_data                                          *
 *                                                                            *
 * PROGRAM DESCRIPTION -                                                      *
 *   This example uses the above part file, a manufacturing setup, and        *
 *   three Surface Contour operations with Surface Area Drive methods.        *
 *   The operations have Drive Surface(s) defined and the Interpolation       *
 *   Method initialized based on the Drive Surface parameters.                *
 *   Each operation will be queried and have the Interpolation Method reset   *
 *   to Linear, Cubic Spline and Smooth respectively. Each operation will be  *
 *   generated in order. An visual inspection of the tool paths will show     *
 *   better results are achieved when the Interpolation method is Smooth.     *
 *                                                                            *
              
 *                                                                            *
 *****************************************************************************/

/***************************** Include Files *********************************/

#include <uf.h>
#include <uf_disp.h>
#include <uf_part.h>
#include <uf_ui.h>
#include <uf_ui_ont.h>
#include <uf_scop.h>
#include <uf_param.h>
#include <string.h>

/*******************************************************************/
#if 0
static UF_SCOP_vector_data_p_t create_and_init_vector_data(void);
#endif
/*******************************************************************/
static void do_scop_ita_api(void)
{
    tag_t  part_tag, *objects;
    int object_count, jj=0, knt=1;
    logical generate;

    /* Get the displayed part. */
    part_tag = UF_PART_ask_display_part( );

    UF_UI_open_listing_window( );
    
    if( part_tag != null_tag )
    {
        /* Get the highlighted/selected objects from Navigation Tool. */
        UF_UI_ONT_ask_selected_nodes( &object_count, &objects );

            UF_UI_open_listing_window( );
            uc4404( "Total object count is ", object_count );

        while (jj <= object_count)
        {
            int error_code = 0, err_code=0;
            UF_SCOP_tx_intp_data_type_t tx_intp_data_type 
                        = UF_SCOP_TX_INTP_DATYPE_VECTOR;
            UF_SCOP_tx_intp_method_t tx_intp_method 
                        = UF_SCOP_TX_INTP_SMOOTH_METHOD;
            int ii, count = -1, count2=0;
            UF_SCOP_vector_data_t  *vector_data = NULL, 
                                   *vector_data_2 = NULL;
            logical all_on_surface = FALSE;

            /***************************************************/
            /* UF_SCOP_ask_tx_intp_data_type                   */
            /***************************************************/
            error_code = 
                UF_SCOP_ask_tx_intp_data_type(objects[jj], &tx_intp_data_type);
            if ( ! error_code)
            {
                tx_intp_data_type = UF_SCOP_TX_INTP_DATYPE_VECTOR;
                /***************************************************/
                /* UF_SCOP_set_tx_intp_data_type                   */
                /***************************************************/
                error_code = 
                    UF_SCOP_set_tx_intp_data_type(objects[jj], 
                                                  tx_intp_data_type);
            }
            /***************************************************/
            /* UF_SCOP_ask_tx_intp_method                      */
            /***************************************************/
            error_code = 
                UF_SCOP_ask_tx_intp_method(objects[jj], &tx_intp_method);
            if ( ! error_code )
            {
            switch(knt)
            {
            case 1:
                if ( tx_intp_method == UF_SCOP_TX_INTP_CUBIC_SPLINE_METHOD || 
                     tx_intp_method == UF_SCOP_TX_INTP_SMOOTH_METHOD)
                {
                UF_UI_write_listing_window("Interpolation Method is not LINEAR.\n");
                UF_UI_write_listing_window("Resetting Interpolation Method to LINEAR.\n");
                tx_intp_method = UF_SCOP_TX_INTP_LINEAR_METHOD;         /* 0 */
                }
            break;

            case 2:
                if ( tx_intp_method == UF_SCOP_TX_INTP_LINEAR_METHOD || 
                     tx_intp_method == UF_SCOP_TX_INTP_SMOOTH_METHOD)
                {
                UF_UI_write_listing_window("Interpolation Method is not CUBIC SPLINE.\n");
                UF_UI_write_listing_window("Resetting Interpolation Method to CUBIC SPLINE.\n");
                tx_intp_method = UF_SCOP_TX_INTP_CUBIC_SPLINE_METHOD;   /* 1 */
                }
            break;

            case 3:
                if ( tx_intp_method == UF_SCOP_TX_INTP_LINEAR_METHOD ||
                     tx_intp_method == UF_SCOP_TX_INTP_CUBIC_SPLINE_METHOD )
                {
                UF_UI_write_listing_window("Interpolation Method is not SMOOTH.\n");
                UF_UI_write_listing_window("Resetting Interpolation Method to SMOOTH.\n");
                tx_intp_method = UF_SCOP_TX_INTP_SMOOTH_METHOD;         /* 2 */
                }
            break;

            default:
                break;
            }

                /***************************************************/
                /* UF_SCOP_set_tx_intp_method                      */
                /***************************************************/
                error_code = 
                    UF_SCOP_set_tx_intp_method(objects[jj], tx_intp_method);
            }
            /***************************************************/
            /* UF_SCOP_ask_tx_intp_vector_data                 */
            /***************************************************/
            error_code = 
                UF_SCOP_ask_tx_intp_vector_data(objects[jj], 
                                                &count, &vector_data);
            if ( ! error_code && count > 0 )
            {
                count2 = 0;
                vector_data_2 = (UF_SCOP_vector_data_p_t) 
                    UF_allocate_memory(sizeof(UF_SCOP_vector_data_t)*count, 
                                       &err_code);
                if ( ! err_code)
                {
                    for (ii=0; ii < count; ii++)
                    {
                    /*******************************************************/
                    /* If the vector_data with is_corner_vector = TRUE,    */
                    /* it must be set back to system. It can not be        */
                    /* discarded.                                          */
                    /*******************************************************/
                        if (vector_data[ii].is_corner_vector == TRUE)
                        {
                            vector_data_2[count2] = vector_data[ii];
                            count2++;
                        }
                    }
                }
                /***************************************************/
                /* UF_SCOP_set_tx_intp_vector_data                 */
                /***************************************************/
                error_code = UF_SCOP_set_tx_intp_vector_data(objects[jj], 
                                 count2, vector_data_2, &all_on_surface);

                error_code = UF_PARAM_generate( objects[jj], &generate );
                     if ( generate == TRUE )
                       {
                       UF_UI_write_listing_window( "Generated the operation successfully...\n" );
                       }
                       UF_DISP_refresh ();
            }
            if ( vector_data != NULL )
                UF_free ( vector_data );
            if ( vector_data_2 != NULL )
                UF_free (vector_data_2 );
    
            ++knt;

            ++jj;
                        
        }
        
    }
            

    return;
}

#if 0
static UF_SCOP_vector_data_p_t create_and_init_vector_data(void)
{
    UF_SCOP_vector_data_p_t  vector_data; 
    int                      err_code;

    vector_data = (UF_SCOP_vector_data_p_t) UF_allocate_memory(
                       sizeof(UF_SCOP_vector_data_t), &err_code);

    if (err_code)
return(NULL);

    /* Set flags. */
    vector_data->xyz[0] = 0.0;
    vector_data->xyz[0] = 0.0;
    vector_data->xyz[0] = 0.0;
    vector_data->ijk[0] = 0.0;
    vector_data->ijk[0] = 0.0;
    vector_data->ijk[0] = 1.0;
    vector_data->is_corner_vector = FALSE;

    return(vector_data);
}
#endif

/*ARGSUSED*/
void ufusr(char *param, int *retcode, int param_len)
{
    UF_initialize();

    do_scop_ita_api();

    UF_terminate();
}

int ufusr_ask_unload(void)
{
 return (UF_UNLOAD_IMMEDIATELY);
}
