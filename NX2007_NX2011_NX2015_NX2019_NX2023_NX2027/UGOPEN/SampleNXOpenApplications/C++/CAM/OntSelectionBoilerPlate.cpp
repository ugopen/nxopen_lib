//=============================================================================
//
//                   Copyright (c) 2009 Siemens PLM Software
//                    Unpublished - All rights reserved
//=============================================================================
// 
// ===========================================================================
//   DESCRIPTION
//
//     This program is a bioler plate for editing operations selected in the Operation Navigator.
//     It must be copied and modified to suit.
//
// ============================================================================


/* Include files */
#include <uf.h>
#include <uf_cam.h>
#include <uf_obj.h>
#include <uf_ui_ont.h>
#include <uf_ncgroup.h>
#include <uf_setup.h>


// New headers
#include <NXOpen/NXObjectManager.hxx>
#include <NXOpen/Part.hxx>
#include <NXOpen/PartCollection.hxx>
#include <NXOpen/CAM_CAMSetup.hxx>
#include <NXOpen/CAM_OperationCollection.hxx>
#include <NXOpen/CAM_OperationBuilder.hxx>
#include <NXOpen/CAM_PlanarOperationBuilder.hxx>
#include <NXOpen/CAM_PlanarMillingBuilder.hxx>
#include <NXOpen/CAM_FaceMillingBuilder.hxx>
#include <NXOpen/CAM_CavityMillingBuilder.hxx>
#include <NXOpen/CAM_ZLevelMillingBuilder.hxx>
#include <NXOpen/CAM_VazlMillingBuilder.hxx>
#include <NXOpen/CAM_SurfaceContourBuilder.hxx>
#include <NXOpen/CAM_Operation.hxx>
#include <NXOpen/CAM_MillOperationBuilder.hxx>
#include <NXOpen/CAM_MillCutParameters.hxx>
#include <NXOpen/CAM_NcmPlanarBuilder.hxx>
#include <NXOpen/CAM_NcmScBuilder.hxx>
#include <NXOpen/CAM_NCGroup.hxx>
#include <NXOpen/ListingWindow.hxx>
#include <NXOpen/NXException.hxx>


//Function to set General Parameters
static logical GeneralParameters
(
    NXOpen::CAM::OperationBuilder *operationBuilder
)
{
    //What type of a builder is this?
	NXOpen::CAM::MillOperationBuilder *millOperationBuilder = dynamic_cast<NXOpen::CAM::MillOperationBuilder *>(operationBuilder);

    if( millOperationBuilder != NULL )
	{
        //Now we are ready to cahnge the parameters of cutting
		return( true );
	}
	return( false );
}

//Function to change Cutting Parameters
static logical ChangeCutParameters
(
    NXOpen::CAM::OperationBuilder *operationBuilder
)
{
    //What type of a builder is this?
	NXOpen::CAM::MillOperationBuilder *millOperationBuilder = dynamic_cast<NXOpen::CAM::MillOperationBuilder *>(operationBuilder);

    if( millOperationBuilder != NULL )
	{
        //From the Operation Builder get the Cutting Parameters Builder
		NXOpen::CAM::MillCutParameters *cutParams = millOperationBuilder->CutParameters();

        //Now we are ready to cahnge the parameters of cutting

		return( true );
	}
	return( false );
}

//Function to change Non Cutting Parameters
static logical ChangeNonCutParameters
(
    NXOpen::CAM::OperationBuilder *operationBuilder
)
{ 
	logical response = false;
	NXOpen::CAM::PlanarOperationBuilder *planarOperationBuilder = dynamic_cast<NXOpen::CAM::PlanarOperationBuilder *>(operationBuilder);

	//Is the operation Builder a Planar Operation Builder?
    if( planarOperationBuilder != NULL )
	{
        //From the Operation Builder get the Non Cutting Builder
		NXOpen::CAM::NcmPlanarBuilder *ncmBuilder = planarOperationBuilder->NonCuttingBuilder();

        //Now we are ready to change the Non Cutting Parameters

		response = true;
	}
	else
	{
	    NXOpen::CAM::SurfaceContourBuilder *scBuilder = dynamic_cast<NXOpen::CAM::SurfaceContourBuilder *>(operationBuilder);


		if( scBuilder != NULL )
		{
		    //From the Operation Builder get the Non Cutting Builder
		    NXOpen::CAM::NcmScBuilder *ncmBuilder = scBuilder->NonCuttingBuilder();

            //Now we are ready to change the Non Cutting Parameters

		    response = true;
		}
	}
	return( response );
}

//Function to save the change made
static logical CommitFunction
(
    NXOpen::CAM::Operation        *operation,
    NXOpen::CAM::OperationBuilder *operationBuilder
)
{
    try
    {
	    //Save the changes made
        operationBuilder->Commit();
    }
    catch ( const NXOpen::NXException &ex )
    {
        NXOpen::Session *session = NXOpen::Session::GetSession();
        NXOpen::ListingWindow lw = NXOpen::ListingWindow(session);
	    lw.Open();
        lw.WriteLine(operation->Name().GetLocaleText());
        lw.WriteLine("  :There is bad data in the object.");
        lw.WriteLine("EXCEPTION: " );
        lw.WriteLine( ex.Message() );
        ex.AssertErrorCode( ex.ErrorCode() );
        return false;
    }

    return true;
}

//Function to set variables in the Builder
static logical ActionFunction
(
    NXOpen::CAM::Operation        *operation,
    NXOpen::CAM::OperationBuilder *operationBuilder
)
{
    //Check if there is a valid Builder
    if( operationBuilder != NULL )
    {
	    // Change General parameters
	    GeneralParameters( operationBuilder );
	    // Change Cutting Parameters
        ChangeCutParameters( operationBuilder );
	    // Change Non Cutting Parameters
	    ChangeNonCutParameters( operationBuilder );

        //Save the change made
	    CommitFunction(operation, operationBuilder);

        // Tool path Generation, Post processing, Clsf Output all these will be done after
        // the changes have been commited

        // Prepare an array of objects
		std::vector<NXOpen::CAM::CAMObject *> objects(1);
        objects[0] = operation;

        // Get the Work Part
		NXOpen::Part *workPart = NXOpen::Session::GetSession()->Parts()->Work();

        //Get the Setup
		NXOpen::CAM::CAMSetup *setup = workPart->CAMSetup();

		//Prepare the units for CLSF output and Postprocessor output
		NXOpen::CAM::CAMSetup::OutputUnits outputUnits = NXOpen::CAM::CAMSetup::OutputUnitsInch;

		if( workPart->PartUnits() == NXOpen::BasePart::UnitsMillimeters )
			outputUnits = NXOpen::CAM::CAMSetup::OutputUnitsMetric;

		//Generate Tool Path
		setup->GenerateToolPath( objects );


        // Output CLS
        // setup->OutputClsf(objects, "CLSF_STANDARD", "test.cls", outputUnits);

		// Post Process
        // setup->Postprocess(objects, "Mill3ax", "test.ptp", outputUnits);

		return( true );
	}
	return( false );
}

//Function to get the operation builder
static NXOpen::CAM::OperationBuilder *GetOperationBuilder
(
    tag_t camObjectTag
)
{
	//Find the object associated with the Tag
	NXOpen::CAM::CAMObject *camObject = (NXOpen::CAM::CAMObject*)NXOpen::NXObjectManager().Get(camObjectTag);
	NXOpen::CAM::Operation *operation = dynamic_cast<NXOpen::CAM::Operation *>(camObject);

    //Check if the object is an Operation
    if( operation != NULL )
	{
        int operationType;
		int operationSubtype;
        NXOpen::Part *workPart = NXOpen::Session::GetSession()->Parts()->Work();
		NXOpen::CAM::OperationCollection *operationCollection = workPart->CAMSetup()->CAMOperationCollection();
            
        //Get the type and subtype of the operation
        UF_OBJ_ask_type_and_subtype(camObjectTag, &operationType, &operationSubtype);

        if( operationSubtype == 110 )      //This is a Planar Milling Operation so create a Planar Milling Builder
            return( operationCollection->CreatePlanarMillingBuilder(camObject) );
        else if( operationSubtype == 260 ) //This is a Cavity Milling Operation so create a Cavity Milling Builder
            return( operationCollection->CreateCavityMillingBuilder(camObject) );
        else if( operationSubtype == 261 ) //This is a Face Milling Operation so create a Face Milling Builder
            return( operationCollection->CreateFaceMillingBuilder(camObject) );
        else if( operationSubtype == 263 ) //This is a Z Level Milling Operation so create a Z Level Milling Builder
            return( operationCollection->CreateZlevelMillingBuilder(camObject) );
        else if( operationSubtype == 266 ) //This is a Variable Axis Z Level Milling Operation so create a Variable Axis Z Level Milling Builder
            return( operationCollection->CreateVazlMillingBuilder(camObject) );
        else if( operationSubtype == 210 ) //This is a Fixed Axis Surface Contour Operation so create a Surface Contour Builder
            return( operationCollection->CreateSurfaceContourBuilder(camObject) );
        else if( operationSubtype == 211 ) //This is a Variable Axis Surface Contour Operation so create Surface Contour Builder
            return( operationCollection->CreateSurfaceContourBuilder(camObject) );
	}
    return( NULL );
}

//This is the Funciton in which the Action is taken for an operation
static logical OperationAction
(
    tag_t camObjectTag
)
{ 
	NXOpen::CAM::CAMObject *camObject = (NXOpen::CAM::CAMObject*)NXOpen::NXObjectManager().Get(camObjectTag);
	NXOpen::CAM::Operation *operation = dynamic_cast<NXOpen::CAM::Operation *>(camObject);
	NXOpen::CAM::OperationBuilder *operationBuilder = NULL;
    logical response = true;

    //Get the proper operation builder
    operationBuilder = GetOperationBuilder(camObjectTag);

    //Now set the variables in the operation builder
    response = ActionFunction(operation,operationBuilder);

    //Commit the changes and then destroy the builder its job is done(cleanup memory)
    if( operationBuilder != NULL )
	{
        //Clean up memory
        operationBuilder->Destroy();
	}
    return( response );
}

//This is the function that is called on every object encountered in the cycling
static logical cycleCb
(
    tag_t    camObjectTag, 
	void    *ptr
)
{
    logical answer;

    //If the object is not an operation then leave without doing anything more
    UF_NCGROUP_is_group(camObjectTag, &answer);

    if( answer )
        return( answer );

    //If it is an operation then take the action
    OperationAction(camObjectTag);
    
    return( true );
}

static void action(void)
{
	NXOpen::Session *session = NXOpen::Session::GetSession();

	// Get the work part
	NXOpen::Part *workPart = NXOpen::Session::GetSession()->Parts()->Work();

    //If there is a setup only then do we have to go further
    if( workPart != NULL && workPart->CAMSetup() != NULL )
	{
		//Initialize the Cam Session
		if( !session->IsCamSessionInitialized() )
		{
            session->CreateCamSession();
		}

		tag_t *selectedTags = NULL;
		int    selectedCount = 0;

        //Get the selected nodes from the Operation Navigator
        UF_UI_ONT_ask_selected_nodes(&selectedCount, &selectedTags);

        if( selectedCount == 0 )
		{
            tag_t programRoot = NULL_TAG;
			UF_SETUP_ask_program_root( workPart->CAMSetup()->Tag(),&programRoot );
			UF_NCGROUP_cycle_members( programRoot, &cycleCb, NULL );
		}
		else
		{
			for( int ii = 0; ii < selectedCount; ii++ )
			{
				NXOpen::CAM::CAMObject *camObject = (NXOpen::CAM::CAMObject*)NXOpen::NXObjectManager().Get(selectedTags[ii]);
				NXOpen::CAM::NCGroup *ncGroup = dynamic_cast<NXOpen::CAM::NCGroup *>(camObject);
	   
				if( ncGroup != NULL )
				{
					UF_NCGROUP_cycle_members( selectedTags[ii], &cycleCb, NULL );
				}
				else
				{
					NXOpen::CAM::Operation *operation = dynamic_cast<NXOpen::CAM::Operation *>(camObject);

					if( operation != NULL )
					{
						OperationAction(operation->Tag());
					}
				}
			}
		}

		NXOpen::ListingWindow lw = NXOpen::ListingWindow(session);

		lw.Open();
        lw.WriteLine("This is a test");
	}
}

/*ARGSUSED*/
extern DllExport void ufusr( char *parm, int *returnCode, int rlen )
{
    if( UF_initialize() == 0 )
	{
        action();
        UF_terminate();
    }
}

extern int ufusr_ask_unload( void )
{
    return( UF_UNLOAD_IMMEDIATELY );
}
