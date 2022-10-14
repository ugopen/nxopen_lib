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

#ifndef MATRIXOPERATIONS_H_INCLUDED
#define MATRIXOPERATIONS_H_INCLUDED

//------------------------------------------------------------------------------
//These includes are needed for the following template code
//------------------------------------------------------------------------------
#include <uf_defs.h>
#include <uf_ui_types.h>
#include <uf.h>
#include <uf_ui.h>
#include <uf_mtx.h>
#include <iostream>
#include <string.h>
#include <NXOpen/Session.hxx>
#include <NXOpen/UI.hxx>
#include <NXOpen/NXMessageBox.hxx>
#include <NXOpen/Callback.hxx>
#include <NXOpen/NXException.hxx>
#include <NXOpen/BlockStyler_UIBlock.hxx>
#include <NXOpen/BlockStyler_BlockDialog.hxx>
#include <NXOpen/BlockStyler_PropertyList.hxx>
//------------------------------------------------------------------------------
//Bit Option for Property: SnapPointTypesOnByDefault
//------------------------------------------------------------------------------
#define          SnapPointTypesOnByDefault_UserDefined (1 << 0);
#define             SnapPointTypesOnByDefault_Inferred (1 << 1);
#define       SnapPointTypesOnByDefault_ScreenPosition (1 << 2);
#define             SnapPointTypesOnByDefault_EndPoint (1 << 3);
#define             SnapPointTypesOnByDefault_MidPoint (1 << 4);
#define         SnapPointTypesOnByDefault_ControlPoint (1 << 5);
#define         SnapPointTypesOnByDefault_Intersection (1 << 6);
#define            SnapPointTypesOnByDefault_ArcCenter (1 << 7);
#define        SnapPointTypesOnByDefault_QuadrantPoint (1 << 8);
#define        SnapPointTypesOnByDefault_ExistingPoint (1 << 9);
#define         SnapPointTypesOnByDefault_PointonCurve (1 <<10);
#define       SnapPointTypesOnByDefault_PointonSurface (1 <<11);
#define     SnapPointTypesOnByDefault_PointConstructor (1 <<12);
#define SnapPointTypesOnByDefault_TwocurveIntersection (1 <<13);
#define         SnapPointTypesOnByDefault_TangentPoint (1 <<14);
#define                SnapPointTypesOnByDefault_Poles (1 <<15);
#define     SnapPointTypesOnByDefault_BoundedGridPoint (1 <<16);
//------------------------------------------------------------------------------
// Namespaces needed for following template
//------------------------------------------------------------------------------
using namespace std;
using namespace NXOpen;
using namespace NXOpen::BlockStyler;

//------------------------------------------------------------------------------
// Forward declaration for Class
//------------------------------------------------------------------------------
class MatrixOperations;
//
//------------------------------------------------------------------------------
// Declaration of global variables
//------------------------------------------------------------------------------
extern MatrixOperations *theMatrixOperations;

class MatrixOperations
{
    // class members
public:
    static Session *theSession;
    static UI *theUI;
    MatrixOperations();
    ~MatrixOperations();
    int Show();
    
    //----------------------- BlockStyler Callback Prototypes ---------------------
    // The following member function prototypes define the callbacks 
    // specified in your BlockStyler dialog.  The empty implementaiton
    // of these prototypes is provided in the MatrixOperations.cpp file. 
    // You are REQUIRED to write the implementation for these funtions.
    //------------------------------------------------------------------------------
    void initialize_cb();
    void dialogShown_cb();
    int apply_cb();
    int ok_cb();
    int update_cb(NXOpen::BlockStyler::UIBlock* block);
    void focusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus);
    void keyboardFocusNotify_cb(NXOpen::BlockStyler::UIBlock* block, bool focus);
    
private:
    std::string theDialogName;
    NXOpen::BlockStyler::BlockDialog* theDialog;
    NXOpen::BlockStyler::UIBlock* SelectOperationsGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* SelectOperation;// Block type: Enumeration
    NXOpen::BlockStyler::UIBlock* Input;// Block type: Group
    NXOpen::BlockStyler::UIBlock* Matrix1Group;// Block type: Group
    NXOpen::BlockStyler::UIBlock* Matrix1;// Block type: Double Table
    NXOpen::BlockStyler::UIBlock* Matrix2Group;// Block type: Group
    NXOpen::BlockStyler::UIBlock* Matrix2;// Block type: Double Table
    NXOpen::BlockStyler::UIBlock* VectorGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* AllowSelection;// Block type: Toggle
    NXOpen::BlockStyler::UIBlock* SelectVector;// Block type: Specify Vector
    NXOpen::BlockStyler::UIBlock* Vector1;// Block type: Double Table
    NXOpen::BlockStyler::UIBlock* EnterAngle;// Block type: Group
    NXOpen::BlockStyler::UIBlock* Angle1;// Block type: Angular Dim
    NXOpen::BlockStyler::UIBlock* Angle;// Block type: Double
    NXOpen::BlockStyler::UIBlock* ResultGroup;// Block type: Group
    NXOpen::BlockStyler::UIBlock* ResultMatrix;// Block type: Double Table
    NXOpen::BlockStyler::UIBlock* ResultVector;// Block type: Double Table
    NXOpen::BlockStyler::UIBlock* ResultDouble;// Block type: Double
	void UpdateDialog();
	double * MatrixAddition3x3(double[9] ,double[9]);    
};
#endif //MATRIXOPERATIONS_H_INCLUDED
