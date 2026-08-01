//=============================================================================
//
//   Copyright (c) 2011 Siemens Industry Software (India) Private Limited
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for PMI Example
//=============================================================================
//

import nxopen.*;


public class PMIExample
{
  public static void main(String [] args) throws NXException, java.rmi.RemoteException
  {
    Session theSession = (Session)SessionFactory.get("Session");
    Part workPart = theSession.parts().work();
    Part displayPart = theSession.parts().display();
    // ----------------------------------------------
    //   Create a diameter dimension on an arc using Menu: PMI->Dimension->Diameter...
    // ----------------------------------------------
        
    int markId1;
    markId1 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Create Dimension");
    nxopen.annotations.DimensionData dimensionData1;
    dimensionData1 = workPart.annotations().newDimensionData();
    
    nxopen.annotations.Associativity associativity1;
    associativity1 = workPart.annotations().newAssociativity();
    
    nxopen.features.Cylinder cylinder1 = ((nxopen.features.Cylinder)workPart.features().findObject("CYLINDER(0)"));
    Edge edge1 = ((Edge)cylinder1.findObject("EDGE * 1 * 3 "));
    associativity1.setFirstObject(edge1);
    
    NXObject nullNXObject = null;
    associativity1.setSecondObject(nullNXObject);
    
    nxopen.drawings.BaseView baseView1 = ((nxopen.drawings.BaseView)workPart.draftingViews().findObject("TOP@1"));
    associativity1.setObjectView(baseView1);
    
    associativity1.setPointOption(nxopen.annotations.AssociativityPointOption.NONE);
    
    associativity1.setLineOption(nxopen.annotations.AssociativityLineOption.NONE);
    
    Point3d firstDefinitionPoint1 = new Point3d(0.0, 0.0, 0.0);
    associativity1.setFirstDefinitionPoint(firstDefinitionPoint1);
    
    Point3d secondDefinitionPoint1 = new Point3d(0.0, 0.0, 0.0);
    associativity1.setSecondDefinitionPoint(secondDefinitionPoint1);
    
    Point3d originPoint1 = new Point3d(50.0, 50.0, 0);
    associativity1.setPickPoint(originPoint1);
    
    nxopen.annotations.Associativity [] associativity2  = new nxopen.annotations.Associativity[1];
    associativity2[0] = associativity1;
    dimensionData1.setAssociativity(1, associativity2);
    
    associativity1.dispose();
    associativity1 = null;
    
    Xform xform1;
    xform1 = dimensionData1.getInferredPlane(nxopen.annotations.PmiDefaultPlane.MODEL_VIEW, nxopen.annotations.DimensionType.DIAMETER);
    
    Point3d origin1 = new Point3d(100.0, 100.0, 0.0);
    nxopen.annotations.DiameterDimension diameterDimension1;
    diameterDimension1 = workPart.dimensions().createDiameterDimension(dimensionData1, origin1);
    
    dimensionData1.dispose();
    dimensionData1 = null;
    
    diameterDimension1.setOriginCentered(false);
    
    diameterDimension1.setDiameterDimensionLineAngle(0.0);
    
    Point3d origin2 = new Point3d(50, 50, 0.0);
    diameterDimension1.setAnnotationOrigin(origin2);
    
    diameterDimension1.setLeaderOrientation(nxopen.annotations.LeaderOrientation.FROM_RIGHT);

    int update=1;
    theSession.updateManager().doUpdate(update);
    
    
  }
  
  public static final int getUnloadOption() { return BaseSession.LibraryUnloadOption.IMMEDIATELY; }
  
}

