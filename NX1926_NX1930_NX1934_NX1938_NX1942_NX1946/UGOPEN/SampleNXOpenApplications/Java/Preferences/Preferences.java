//=============================================================================
//
//   Copyright (c) 2011 Siemens Industry Software (India) Private Limited
//                    Unpublished - All rights reserved
//=============================================================================
//File description: Sample NX/Open Application for Preferences
//=============================================================================
//
//
import nxopen.*;

public class Preferences
{
  public static void main(String [] args) throws NXException, java.rmi.RemoteException
  {
    Session theSession = (Session)SessionFactory.get("Session");
    // ----------------------------------------------
    //   Menu: File->New...
    // ----------------------------------------------
    Part part1;
    part1 = theSession.parts().newDisplay("prefs", nxopen.Part.Units.MILLIMETERS);
    
    Part workPart = theSession.parts().work();
    Part displayPart = theSession.parts().display();
    Part part2;
    part2 = theSession.parts().work();
    
    Part part3;
    part3 = theSession.parts().display();
    // ----------------------------------------------
    //   Menu: preferences->Sketch...
    // ----------------------------------------------
    
    theSession.preferences().sketch().setDefaultSketchNamePrefix("SKT_");
    
    theSession.preferences().sketch().setDefaultVertexNamePrefix("VRT_");
    
    theSession.preferences().sketch().setDefaultLineNamePrefix("LIN_");
    
    theSession.preferences().sketch().setDefaultArcNamePrefix("ARC_");
    
    theSession.preferences().sketch().setDefaultConicNamePrefix("CON_");
    
    theSession.preferences().sketch().setDefaultSplineNamePrefix("SPL_");
    // ----------------------------------------------
    //   Menu: preferences->Grid...
    // ----------------------------------------------
    nxopen.preferences.WorkPlane workPlane1;
    workPlane1 = workPart.preferences().workplane();
    
    workPlane1.setGridType(nxopen.preferences.WorkPlane.Grid.POLAR);
    
    nxopen.preferences.WorkPlane.PolarGridSize polarGridSize1 = new nxopen.preferences.WorkPlane.PolarGridSize();
    polarGridSize1.radialGridSize.majorGridSpacing = 75.0;
    polarGridSize1.radialGridSize.minorLinesPerMajor = 3;
    polarGridSize1.radialGridSize.snapPointsPerMinor = 5;
    polarGridSize1.angularGridSize.majorGridSpacing = 45.0;
    polarGridSize1.angularGridSize.minorLinesPerMajor = 4;
    polarGridSize1.angularGridSize.snapPointsPerMinor = 2;
    workPlane1.setPolarGridSize(polarGridSize1);
    
    workPlane1.setShowGrid(true);
    
    workPlane1.setShowLabels(false);
    
    workPlane1.setSnapToGrid(false);
    
    workPlane1.setGridOnTop(false);
    
    workPlane1.setRectangularShowMajorLines(false);
    
    workPlane1.setPolarShowMajorLines(true);
    
    workPlane1.setGridColor(130);
    
    int markId1;
    markId1 = theSession.setUndoMark(nxopen.Session.MarkVisibility.VISIBLE, "Enter Gateway");
    
    // ----------------------------------------------
    //   Menu: Tools->Journal->Stop 
    // ----------------------------------------------
  
  }
  
  public static final int getUnloadOption() { return BaseSession.LibraryUnloadOption.IMMEDIATELY; }
  
}
