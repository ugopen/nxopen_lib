//=============================================================================
//
//                   Copyright (c) 2010 Siemens PLM Solutions
//                     Unpublished - All rights reserved
//===============================================================================
//File description: Sample NX/Open Application for Block Styler Matrix Operations
//===============================================================================
//
//==============================================================================
//  WARNING!!  This file is overwritten by the Block Styler while generating
//  the automation code. Any modifications to this file will be lost after
//  generating the code again.
//==============================================================================

//==============================================================================
//  Purpose:  This TEMPLATE file contains C++ source to guide you in the
//  construction of your Block application dialog. The generation of your
//  dialog file (.dlx extension) is the first step towards dialog construction
//  within NX.  You must now create a NX Open application that
//  utilizes this file (.dlx).
//
//  The information in this file provides you with the following:
//
//  1.  Help on how to load and display your Block UI Styler dialog in NX
//      using APIs provided in NXOpen.BlockStyler namespace
//  2.  The empty callback methods (stubs) associated with your dialog items
//      have also been placed in this file. These empty methods have been
//      created simply to start you along with your coding requirements.
//      The method name, argument list and possible return values have already
//      been provided for you.
//==============================================================================

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include "MatrixOperations.hpp"
using namespace NXOpen;
using namespace NXOpen::BlockStyler;



//------------------------------------------------------------------------------
// Initialize static variables
//------------------------------------------------------------------------------
Session *(MatrixOperations::theSession) = NULL;
UI *(MatrixOperations::theUI) = NULL;

//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
MatrixOperations *theMatrixOperations;
//------------------------------------------------------------------------------
// Constructor for NX Styler class
//------------------------------------------------------------------------------
MatrixOperations::MatrixOperations()
{
    try
    {
        // Initialize the NX Open C++ API environment
        MatrixOperations::theSession = NXOpen::Session::GetSession();
        MatrixOperations::theUI = UI::GetUI();
        theDialogName = "MatrixOperations.dlx";
        theDialog = MatrixOperations::theUI->CreateDialog(theDialogName.c_str());
        // Registration of callback functions
        theDialog->AddApplyHandler(make_callback(this, &MatrixOperations::apply_cb));
        theDialog->AddOkHandler(make_callback(this, &MatrixOperations::ok_cb));
        theDialog->AddUpdateHandler(make_callback(this, &MatrixOperations::update_cb));
        theDialog->AddInitializeHandler(make_callback(this, &MatrixOperations::initialize_cb));
        theDialog->AddFocusNotifyHandler(make_callback(this, &MatrixOperations::focusNotify_cb));
        theDialog->AddKeyboardFocusNotifyHandler(make_callback(this, &MatrixOperations::keyboardFocusNotify_cb));
        theDialog->AddDialogShownHandler(make_callback(this, &MatrixOperations::dialogShown_cb));
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
        throw;
    }
}

//------------------------------------------------------------------------------
// Destructor for NX Styler class
//------------------------------------------------------------------------------
MatrixOperations::~MatrixOperations()
{
    if (theDialog != NULL)
    {
        delete theDialog;
        theDialog = NULL;
    }
}
//------------------------------- DIALOG LAUNCHING ---------------------------------
//
//    Before invoking this application one needs to open any part/empty part in NX
//    because of the behavior of the blocks.
//
//    Make sure the dlx file is in one of the following locations:
//        1.) From where NX session is launched
//        2.) $UGII_USER_DIR/application
//        3.) For released applications, using UGII_CUSTOM_DIRECTORY_FILE is highly
//            recommended. This variable is set to a full directory path to a file 
//            containing a list of root directories for all custom applications.
//            e.g., UGII_CUSTOM_DIRECTORY_FILE=$UGII_BASE_DIR\ugii\menus\custom_dirs.dat
//
//    You can create the dialog using one of the following way:
//
//    1. USER EXIT
//
//        1) Create the Shared Library -- Refer "Block UI Styler programmer's guide"
//        2) Invoke the Shared Library through File->Execute->NX Open menu.
//
//------------------------------------------------------------------------------
extern "C" DllExport void  ufusr(char *param, int *retcod, int param_len)
{
    try
    {
        theMatrixOperations = new MatrixOperations();
        // The following method shows the dialog immediately
        theMatrixOperations->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    if(theMatrixOperations != NULL)
    {
        delete theMatrixOperations;
    }
}

//------------------------------------------------------------------------------
// This method specifies how a shared image is unloaded from memory
// within NX. This method gives you the capability to unload an
// internal NX Open application or user  exit from NX. Specify any
// one of the three constants as a return value to determine the type
// of unload to perform:
//
//
//    Immediately : unload the library as soon as the automation program has completed
//    Explicitly  : unload the library from the "Unload Shared Image" dialog
//    AtTermination : unload the library when the NX session terminates
//
//
// NOTE:  A program which associates NX Open applications with the menubar
// MUST NOT use this option since it will UNLOAD your NX Open application image
// from the menubar.
//------------------------------------------------------------------------------
extern "C" DllExport int ufusr_ask_unload()
{
    //return (int)Session::LibraryUnloadOptionExplicitly;
    return (int)Session::LibraryUnloadOptionImmediately;
    //return (int)Session::LibraryUnloadOptionAtTermination;
}

//------------------------------------------------------------------------------
// Following method cleanup any housekeeping chores that may be needed.
// This method is automatically called by NX.
//------------------------------------------------------------------------------
extern "C" DllExport void ufusr_cleanup(void)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

int MatrixOperations::Show()
{
    try
    {
        theDialog->Show();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//---------------------Block UI Styler Callback Functions--------------------------
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//Callback Name: initialize_cb
//------------------------------------------------------------------------------
void MatrixOperations::initialize_cb()
{
    try
    {
        SelectOperationsGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("SelectOperationsGroup"));
        SelectOperation = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("SelectOperation"));
        Input = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("Input"));
        Matrix1Group = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("Matrix1Group"));
        Matrix1 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("Matrix1"));
        Matrix2Group = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("Matrix2Group"));
        Matrix2 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("Matrix2"));
        VectorGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("VectorGroup"));
        AllowSelection = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("AllowSelection"));
        SelectVector = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("SelectVector"));
        Vector1 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("Vector1"));
        EnterAngle = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("EnterAngle"));
        Angle1 = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("Angle1"));
        Angle = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("Angle"));
        ResultGroup = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("ResultGroup"));
        ResultMatrix = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("ResultMatrix"));
        ResultVector = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("ResultVector"));
        ResultDouble = dynamic_cast<NXOpen::BlockStyler::UIBlock* >(theDialog->TopBlock()->FindBlock("ResultDouble"));
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: dialogShown_cb
//This callback is executed just before the dialog launch. Thus any value set 
//here will take precedence and dialog will be launched showing that value. 
//------------------------------------------------------------------------------
void MatrixOperations::dialogShown_cb()
{
    try
    {
        //---- Enter your callback code here -----
        UpdateDialog();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: apply_cb
//------------------------------------------------------------------------------
int MatrixOperations::apply_cb()
{
    int errorCode = 0;
    try
    {
        //---- Enter your callback code here -----
        
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}

//------------------------------------------------------------------------------
//Callback Name: update_cb
//------------------------------------------------------------------------------
int MatrixOperations::update_cb(NXOpen::BlockStyler::UIBlock* block)
{
    try
    {

        //Getting properties of AllowSelection,SelectVector and Vector1 into propertylists
        BlockStyler::PropertyList *AllowSelectionProperties = AllowSelection->GetProperties();
        BlockStyler::PropertyList *SelectVectorProperties = SelectVector->GetProperties();
        BlockStyler::PropertyList *Vector1Properties = Vector1->GetProperties();
        NXOpen::Vector3d SelectedVec ;
        std::vector<double> vector1values(3);
        int nrows[1],ncols[3];
        


        if(block == AllowSelection)
        {
        //---------Enter your code here-----------
            vector1values = Vector1Properties->GetDoubleMatrix("Values",nrows, ncols);
            SelectedVec.X = vector1values[0];
            SelectedVec.Y = vector1values[1];
            SelectedVec.Z = vector1values[2];
            SelectVectorProperties->SetVector("Vector",SelectedVec);
            SelectVectorProperties->SetLogical("Show",AllowSelectionProperties->GetLogical("Value")); 

        }
        else if(block == SelectVector)
        {
        //---------Enter your code here-----------
            SelectedVec = SelectVectorProperties->GetVector("Vector");
            vector1values[0] = SelectedVec.X;
            vector1values[1] = SelectedVec.Y;
            vector1values[2] = SelectedVec.Z;
            Vector1Properties->SetDoubleMatrix("Values", 1, 3, vector1values);

        }        

        UpdateDialog();

        //Deleting Property list after use
        delete AllowSelectionProperties;
        delete SelectVectorProperties;
        delete Vector1Properties;

    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return 0;
}

//------------------------------------------------------------------------------
//Callback Name: ok_cb
//------------------------------------------------------------------------------
int MatrixOperations::ok_cb()
{
    int errorCode = 0;
    try
    {
        errorCode = apply_cb();
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        errorCode = 1;
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
    return errorCode;
}


//This method updates the dialog
void MatrixOperations::UpdateDialog()
{

    // Getting Properties of Matrix1Group,Matrix2Group,EnterAngle and VectorGroup
    BlockStyler::PropertyList *Matrix1GroupProperties = Matrix1Group->GetProperties();
    BlockStyler::PropertyList *Matrix2GroupProperties = Matrix2Group->GetProperties();
    BlockStyler::PropertyList *EnterAngleProperties = EnterAngle->GetProperties();
    BlockStyler::PropertyList *VectorGroupProperties = VectorGroup->GetProperties();

    // Getting Properties of Matrix1,Matrix2,Vector1 and Angle1
    BlockStyler::PropertyList *Matrix1Properties = Matrix1->GetProperties();
    BlockStyler::PropertyList *Matrix2Properties = Matrix2->GetProperties();
    BlockStyler::PropertyList *Vector1Properties = Vector1->GetProperties();
    BlockStyler::PropertyList *AngleProperties = Angle1->GetProperties();

    // Getting Properties of ResultMatrix,ResultVector and ResultDouble
    BlockStyler::PropertyList *ResultMatrixProperties = ResultMatrix->GetProperties();
    BlockStyler::PropertyList *ResultVectorProperties = ResultVector->GetProperties();
    BlockStyler::PropertyList *ResultDoubleProperties = ResultDouble->GetProperties();

    int m1nrows[3],m1ncols[3];
    int m2nrows[3],m2ncols[3];
    int v1nrows[1],v2ncols[3];
    
    

    std::vector<double > matrix1values = Matrix1Properties->GetDoubleMatrix("Values",m1nrows,m1ncols);
    std::vector<double > matrix2values = Matrix2Properties->GetDoubleMatrix("Values", m2nrows, m2ncols);
    std::vector<double> vector1values = Vector1Properties->GetDoubleMatrix("Values", v1nrows, v2ncols);
    double anglevalue = AngleProperties->GetDouble("Value");
    std::vector<double > matrixResultValues;


    double mat1values[9], mat2values[9],matResultValues[9],vec1values[3],vecproductvalues[3];


    int i = 0;    
    vector<double>::iterator it;
    for ( it = matrix1values.begin(), i = 0 ; it < matrix1values.end(); it++ )
    {
        mat1values[i++] = *it;
    }
    for ( it = matrix2values.begin(), i = 0 ; it < matrix2values.end(); it++ )
    {
        mat2values[i++] = *it;
    }
    for ( it = vector1values.begin(), i = 0 ; it < vector1values.end(); it++ )
    {
        vec1values[i++] = *it;
    }




    double  ResultValues[] = {0,0,0};
    double determinant[1];

    BlockStyler::PropertyList *SelectOperationProperties = SelectOperation->GetProperties();
    NXString matrixOperation = SelectOperationProperties->GetEnumAsString("Value");

    //If List box selection is Multiplication
    if(!(strcmp(matrixOperation.GetText(),"Multiplication")))
    {

        Matrix1GroupProperties->SetLogical("Show", true);
        Matrix2GroupProperties->SetLogical("Show", true);
        EnterAngleProperties->SetLogical("Show", false);
        VectorGroupProperties->SetLogical("Show", false);

        ResultMatrixProperties->SetLogical("Show", true);
        ResultVectorProperties->SetLogical("Show", false);
        ResultDoubleProperties->SetLogical("Show", false);



        UF_MTX3_multiply(mat1values ,mat2values,matResultValues);


        matrixResultValues.insert(matrixResultValues.begin(),matResultValues,matResultValues+9);            
        ResultMatrixProperties->SetDoubleMatrix("Values", 3, 3, matrixResultValues);
    }

    //If List box selection is Addition
    else if(!(strcmp(matrixOperation.GetText(),"Addition")))
    {
        Matrix1GroupProperties->SetLogical("Show", true);
        Matrix2GroupProperties->SetLogical("Show", true);
        EnterAngleProperties->SetLogical("Show", false);
        VectorGroupProperties->SetLogical("Show", false);

        ResultMatrixProperties->SetLogical("Show", true);
        ResultVectorProperties->SetLogical("Show", false);
        ResultDoubleProperties->SetLogical("Show", false);

        double *additionMatrix = MatrixAddition3x3(mat1values,mat2values);

        for(i=0;i<9;i++)
        {
            matResultValues[i] =  additionMatrix[i];

        }

        matrixResultValues.insert(matrixResultValues.begin(),matResultValues,matResultValues+9);            
        ResultMatrixProperties->SetDoubleMatrix("Values", 3, 3, matrixResultValues);

    }

    //If List box selection is Determinant
    else if(!(strcmp(matrixOperation.GetText(),"Determinant")))
    {
        Matrix1GroupProperties->SetLogical("Show", true);
        Matrix2GroupProperties->SetLogical("Show", false);
        EnterAngleProperties->SetLogical("Show", false);
        VectorGroupProperties->SetLogical("Show", false);

        ResultMatrixProperties->SetLogical("Show", false);
        ResultVectorProperties->SetLogical("Show", false);
        ResultDoubleProperties->SetLogical("Show", true);


        UF_MTX3_determinant(mat1values ,determinant);
        ResultDoubleProperties->SetDouble("Value", determinant[0]);



    }
    //If List box selection is Transpose
    else if(!(strcmp(matrixOperation.GetText(),"Transpose")))
    {
        Matrix1GroupProperties->SetLogical("Show", true);
        Matrix2GroupProperties->SetLogical("Show", false);
        EnterAngleProperties->SetLogical("Show", false);
        VectorGroupProperties->SetLogical("Show", false);

        ResultMatrixProperties->SetLogical("Show", true);
        ResultVectorProperties->SetLogical("Show", false);
        ResultDoubleProperties->SetLogical("Show", false);

        UF_MTX3_transpose(mat1values ,matResultValues);

        matrixResultValues.insert(matrixResultValues.begin(),matResultValues,matResultValues+9);            
        ResultMatrixProperties->SetDoubleMatrix("Values", 3, 3, matrixResultValues);



    }
    //If List box selection is OrthoNormalize    
    else if(!(strcmp(matrixOperation.GetText(),"OrthoNormalize")))
    {

        Matrix1GroupProperties->SetLogical("Show", true);
        Matrix2GroupProperties->SetLogical("Show", false);
        EnterAngleProperties->SetLogical("Show", false);
        VectorGroupProperties->SetLogical("Show", false);

        ResultMatrixProperties->SetLogical("Show", true);
        ResultVectorProperties->SetLogical("Show", false);
        ResultDoubleProperties->SetLogical("Show", false);

        UF_MTX3_ortho_normalize(mat1values);
        matrixResultValues.insert(matrixResultValues.begin(),mat1values,mat1values+9);            
        ResultMatrixProperties->SetDoubleMatrix("Values", 3, 3, matrixResultValues);


    }
    //If List box selection is RotateAboutAxis
    else if(!(strcmp(matrixOperation.GetText(),"RotateAboutAxis")))
    {
        Matrix1GroupProperties->SetLogical("Show", false);
        Matrix2GroupProperties->SetLogical("Show", false);
        EnterAngleProperties->SetLogical("Show", true);
        VectorGroupProperties->SetLogical("Show", true);

        ResultMatrixProperties->SetLogical("Show", true);
        ResultVectorProperties->SetLogical("Show", false);
        ResultDoubleProperties->SetLogical("Show", false);

        UF_MTX3_rotate_about_axis(vec1values, anglevalue, matResultValues);
        matrixResultValues.insert(matrixResultValues.begin(),matResultValues,matResultValues+9);            
        ResultMatrixProperties->SetDoubleMatrix("Values", 3, 3, matrixResultValues);

    }
    //If List box selection is VectorMultiply
    else if(!(strcmp(matrixOperation.GetText(),"VectorMultiply")))
    {

        Matrix1GroupProperties->SetLogical("Show", true);
        Matrix2GroupProperties->SetLogical("Show", false);
        EnterAngleProperties->SetLogical("Show", false);
        VectorGroupProperties->SetLogical("Show", true);

        ResultMatrixProperties->SetLogical("Show", false);
        ResultVectorProperties->SetLogical("Show", true);
        ResultDoubleProperties->SetLogical("Show", false);

        UF_MTX3_vec_multiply(vec1values, mat1values, vecproductvalues);
        matrixResultValues.insert(matrixResultValues.begin(),vecproductvalues,vecproductvalues+3);            
        ResultVectorProperties->SetDoubleMatrix("Values", 1, 3, matrixResultValues);

    }
    //If List box selection is X-direction Vector
    else if(!(strcmp(matrixOperation.GetText(),"X-direction Vector")))
    {
        Matrix1GroupProperties->SetLogical("Show", true);
        Matrix2GroupProperties->SetLogical("Show", false);
        EnterAngleProperties->SetLogical("Show", false);
        VectorGroupProperties->SetLogical("Show", false);

        ResultMatrixProperties->SetLogical("Show", false);
        ResultVectorProperties->SetLogical("Show", true);
        ResultDoubleProperties->SetLogical("Show", false);

        UF_MTX3_x_vec(mat1values, ResultValues);
        matrixResultValues.insert(matrixResultValues.begin(),ResultValues,ResultValues+3);
        ResultVectorProperties->SetDoubleMatrix("Values", 1, 3, matrixResultValues);

    }
    //If List box selection is Y-direction Vector
    else if(!(strcmp(matrixOperation.GetText(),"Y-direction Vector")))
    {
        Matrix1GroupProperties->SetLogical("Show", true);
        Matrix2GroupProperties->SetLogical("Show", false);
        EnterAngleProperties->SetLogical("Show", false);
        VectorGroupProperties->SetLogical("Show", false);

        ResultMatrixProperties->SetLogical("Show", false);
        ResultVectorProperties->SetLogical("Show", true);
        ResultDoubleProperties->SetLogical("Show", false);


        UF_MTX3_y_vec(mat1values, ResultValues);
        matrixResultValues.insert(matrixResultValues.begin(),ResultValues,ResultValues+3);
        ResultVectorProperties->SetDoubleMatrix("Values", 1, 3, matrixResultValues);

    }
    //If List box selection is Z-direction Vector
    else if(!(strcmp(matrixOperation.GetText(),"Z-direction Vector")))
    {
        Matrix1GroupProperties->SetLogical("Show", true);
        Matrix2GroupProperties->SetLogical("Show", false);
        EnterAngleProperties->SetLogical("Show", false);
        VectorGroupProperties->SetLogical("Show", false);

        ResultMatrixProperties->SetLogical("Show", false);
        ResultVectorProperties->SetLogical("Show", true);
        ResultDoubleProperties->SetLogical("Show", false);

        UF_MTX3_z_vec(mat1values, ResultValues);
        matrixResultValues.insert(matrixResultValues.begin(),ResultValues,ResultValues+3);
        ResultVectorProperties->SetDoubleMatrix("Values", 1, 3, matrixResultValues);

    }
    //Deleting all the proerties that were used
    delete SelectOperationProperties;
    delete Matrix1GroupProperties;
    delete Matrix2GroupProperties;
    delete EnterAngleProperties;
    delete VectorGroupProperties;

    delete Matrix1Properties;
    delete Matrix2Properties;
    delete Vector1Properties;
    delete AngleProperties;

    delete ResultMatrixProperties;
    delete ResultVectorProperties;
    delete ResultDoubleProperties;

}


double additionMatrix[9];

//This method performs 3x3 Matrix addition
double *  MatrixOperations::MatrixAddition3x3(double matrix1[9],double matrix2[9])
{

    for(int i=0;i<=8;i++)
    {
        additionMatrix[i] = matrix1[i] + matrix2[i];

    }
    return additionMatrix;

}






//------------------------------------------------------------------------------
//Callback Name: focusNotify_cb
//This callback is executed when any block (except the ones which receive keyboard entry such as Integer block) receives focus.
//------------------------------------------------------------------------------
void MatrixOperations::focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}

//------------------------------------------------------------------------------
//Callback Name: keyboardFocusNotify_cb
//This callback is executed when block which can receive keyboard entry, receives the focus.
//------------------------------------------------------------------------------
void MatrixOperations::keyboardFocusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus)
{
    try
    {
        //---- Enter your callback code here -----
    }
    catch(exception& ex)
    {
        //---- Enter your exception handling code here -----
        MatrixOperations::theUI->NXMessageBox()->Show("Block Styler", NXOpen::NXMessageBox::DialogTypeError, ex.what());
    }
}
