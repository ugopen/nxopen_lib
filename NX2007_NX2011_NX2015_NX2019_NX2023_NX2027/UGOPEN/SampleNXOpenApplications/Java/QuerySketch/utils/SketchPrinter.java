/*==================================================================================================
            Copyright (c) 2010  Siemens PLM Software
             Unpublished - All rights reserved 
 
====================================================================================================
*/



package utils;
import java.io.PrintStream;
import java.util.Arrays;

import nxopen.*;

/** Contains methods for printing information on the contents of a sketch */
public class SketchPrinter extends NXPrinter
{
    private GeometryPrinter m_geomPrinter;
    
    public SketchPrinter(PrintStream out_)
    {
        super(out_);
        m_geomPrinter = new GeometryPrinter(out_);
    }
    
    /** Prints geometry contained in a sketch */
    public void printGeometry(NXObject geoms[], Sketch owningSketch, String indent) throws Throwable
    {
        Arrays.sort(geoms, ComparerByName.instance());
        for( int ii=0; ii < geoms.length; ++ii )
        {
            SmartObject geom = (SmartObject)geoms[ii];
            m_geomPrinter.printGeometry(geom, indent);
            SketchConstraint [] constraints = owningSketch.getConstraintsForGeometry(geom, Sketch.ConstraintClass.ANY);
            out.println(indent + "   Constraints associated with the geometry: ");
            printConstraints(constraints, owningSketch, indent + "      ");
        }
        
    }
    
    /** Prints sketch constraints */
    public void printConstraints(SketchConstraint [] constraints, Sketch owningSketch, String indent) throws Throwable
    {
        for (int ii = 0; ii < constraints.length; ii++) 
        {
            printConstraint(constraints[ii], owningSketch, indent);
        }
    }
    
    /** Prints a sketch constraint */
    public void printConstraint(SketchConstraint constraint, Sketch owningSketch, String indent) throws Throwable
    {
        Sketch.ConstraintType type = constraint.constraintType();
        out.println(indent + getClassName(constraint) + " " + type);
        if ( constraint instanceof SketchDimensionalConstraint)
        {
            SketchDimensionalConstraint dimConstraint = (SketchDimensionalConstraint)constraint;
            if ( type != Sketch.ConstraintType.PERIMETER_DIM )
            {
                out.println(indent + "   assoc dim origin = " + toString(dimConstraint.associatedDimension().annotationOrigin()));
            }
            if(dimConstraint.associatedExpression() != null)
            {
                out.println(indent + "   associated expression = " + dimConstraint.associatedExpression().equation());
                out.println(indent + "   value = " + dimConstraint.associatedExpression().value());
            }
            else
            {
                out.println(indent + "   No expression associated with this constraint.");
            }
            Sketch.DimensionGeometry [] dimGeoms = dimConstraint.getDimensionGeometry();
            for ( int ii = 0; ii < dimGeoms.length; ++ii)
            {
                Sketch.DimensionGeometry dimGeom = dimGeoms[ii];
                out.println(indent + "      geometry = " + getClassName(dimGeom.geometry) +
                        " " + getIdentifier(dimGeom.geometry));
                out.println(indent + "      assoc type = " + dimGeom.assocType);
                out.println(indent + "      assoc value = " + dimGeom.assocValue);
            }
       }
       else if ( constraint instanceof SketchGeometricConstraint &&
            type != Sketch.ConstraintType.ASSOC_TRIM && type != Sketch.ConstraintType.ASSOC_OFFSET )
       {
               SketchGeometricConstraint cnstrt = (SketchGeometricConstraint)constraint;
            out.println(indent + "   Geometry:");
            Sketch.ConstraintGeometry [] cntGeoms = cnstrt.getGeometry();
             for ( int ii=0; ii < cntGeoms.length; ++ii )
            {
                Sketch.ConstraintGeometry cntGeom = cntGeoms[ii];
                out.println(indent + "       geometry = " + getClassName(cntGeom.geometry) + " " + getIdentifier(cntGeom.geometry));
                out.println(indent + "       point type = " + cntGeom.pointType);
                if ( cntGeom.pointType == Sketch.ConstraintPointType.SPLINE_DEFINING_POINT)
                    out.println(indent + "       spline defining point = " + cntGeom.splineDefiningPointIndex);               
            }
        
       }
    }
    
    /** Prints a single sketch 
     * @param theSession      A Session object
     * @param sketch          The sketch to be printed
     * @param indent          Indentation to be placed at the beginning of each line 
     * @param doActivation    Whether to activate the sketch if it is not active.  
     *                        The status and degrees of freedom cannot be queried unless the sketch is active */
    public void printSketch(Session theSession, Sketch sketch, String indent, boolean doActivation) throws Throwable
    {        
        out.println("name = " + sketch.name());
        out.println("local coordinate system origin = " + toString(sketch.origin()));
        out.println("local coordinate system orientation = " + toString(sketch.orientation().element()));
        out.println("attached to " + getIdentifier(sketch.attachPlane()));
        
        Sketch.ReferenceDirectionData refDirData = sketch.getReferenceDirection();
        Vector3d refDir= refDirData.referenceDirection;
        NXObject refAxis = (NXObject)refDirData.referenceAxis;
        AxisOrientation refAxisOrientation = refDirData.referenceAxisOrientation;
        Sense refAxisSense = refDirData.referenceAxisSense;
        if (refAxis == null )
        {
            out.println("reference axis = null");
        }
        else
        {
            out.println("reference axis = " + getClassName(refAxis) + " " + getIdentifier(refAxis));
        }
        out.println("reference axis orientation = " + refAxisOrientation);
        out.println("reference axis sense = " + refAxisSense);
        out.println("reference vector = " + toString(refDir));
        Sketch oldActiveSketch= theSession.activeSketch();
        boolean sketchIsActive = sketch.equals(oldActiveSketch);
        boolean doDeactivate = false;
        if ( !sketchIsActive && doActivation )
        {
            sketch.activate(Sketch.ViewReorient.FALSE);
            doDeactivate = true;
            sketchIsActive = true;
        }
        if ( sketchIsActive )
        {
            Integer dof_needed;
            Sketch.StatusData statusData = sketch.getStatus();
            out.println("status = " + statusData.status);
            out.println("degrees of freedom remaining in sketch = " + statusData.dofNeeded);
        }
        if ( doDeactivate )
        {
            if (oldActiveSketch == null )
            {
                sketch.deactivate(Sketch.ViewReorient.FALSE, Sketch.UpdateLevel.SKETCH_ONLY);
            }
            else
            {
                oldActiveSketch.activate(Sketch.ViewReorient.FALSE);
            }
        }

        NXObject [] geoms= sketch.getAllGeometry();
        out.println("Number of geometric items in sketch = " + geoms.length);
        printGeometry(geoms, sketch, "   ");
        SketchConstraint [] constraints= sketch.getAllConstraintsOfType(Sketch.ConstraintClass.ANY, Sketch.ConstraintType.NO_CON);
        out.println("*******************************");
        out.println("Number of constraints in sketch = " + constraints.length);
        printConstraints(constraints, sketch, "   ");
        out.println("----------------------------------------------\n");
    }

    /** Prints an array of sketches
     * @param theSession      A Session object
     * @param sketches        The sketches to be printed
     * @param doActivation    Whether to activate a sketch if it is not active.  
     *                        The status and degrees of freedom cannot be queried unless the sketch is active */
    public void printSketches(Session theSession, Sketch [] sketches, boolean doActivation) throws Throwable
    {
        if (theSession.activeSketch() == null )
        {
            out.println("No active sketch");
        }
        else
        {
            out.println("The active sketch is " + theSession.activeSketch().name());
        }
        Arrays.sort(sketches, ComparerByName.instance());
        Sketch sketch;
        for( int ii=0; ii < sketches.length; ++ii )
        {
            sketch = sketches [ii];
            printSketch(theSession, sketch, "", doActivation);
        }
    }

    
 
}
