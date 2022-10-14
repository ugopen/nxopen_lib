/*
 *
 *
  
 */
#ifndef GEOMASSIGNMENT_H
#define GEOMASSIGNMENT_H

#include <stdio.h>
#include <string.h>

#include <NXOpen/CAE_FEModel.hxx>

namespace NXOpen
{

    class geomAssignment
    {
    public:

        geomAssignment();
        virtual  ~geomAssignment();

        void mesh_control_processing_module ( FILE *batchmesher_logger_file, tag_t partTag, CAE::FEModel *fEModel1, int nCAEBodies, tag_t *CAEBodies_p );

    private:

        geomAssignment( const geomAssignment &X);
        geomAssignment& operator= ( const geomAssignment &X);
    };
}
#endif

