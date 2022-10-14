//
//          Copyright (c) 2005 UGS Corp.
//              All rights reserved
//               Written by V.A.L.
package utils;

import java.io.PrintStream;

import nxopen.*;

/** Contains methods for printing data about various types of curves and 
 * datum geometry */
public class GeometryPrinter extends NXPrinter
{
    public GeometryPrinter(PrintStream out_)
    {
        super(out_);
    }
    
    void printGeometry(NXObject obj, String indent ) throws Throwable
    {
        if (obj instanceof Line )
        {
            Line line= (Line)obj;
            out.println(indent + "line name is " + obj.name());
            out.println(indent + "   start point = " + toString(line.startPoint()));
            out.println(indent + "   end point = " + toString(line.endPoint()));    
        }
        else if (obj instanceof Arc )
        {
            Arc arc= (Arc)obj;
            out.println(indent + "arc name is " + obj.name());
            out.println(indent + "   radius = " + arc.radius());
            out.println(indent + "   start angle = " + arc.startAngle());
            out.println(indent + "   end angle = " + arc.endAngle());
            out.println(indent + "   center = " + toString(arc.centerPoint()));
            out.println(indent + "   rotation angle = " + arc.rotationAngle());
            out.println(indent + "   matrix is " + toString(arc.matrix().element()));    
        }
        else if (obj instanceof Point )
        {
            Point point= (Point)obj;
            out.println(indent + "point name is " + obj.name());
            out.println(indent + "   coords = " + toString(point.coordinates()));   
        }
        else if (obj instanceof Ellipse )
        {
            Ellipse ellipse= (Ellipse)obj;
            out.println(indent + "ellipse name is " + obj.name());
            out.println(indent + "  center = " + toString(ellipse.centerPoint()));
            out.println(indent + "  major radius = " + ellipse.majorRadius());
            out.println(indent + "  minor radius = " + ellipse.minorRadius());
            out.println(indent + "  start angle = " + ellipse.startAngle());
            out.println(indent + "  end angle = " + ellipse.endAngle());
            out.println(indent + "  rotation angle = " + ellipse.rotationAngle());
            out.println(indent + "  matrix = " + toString(ellipse.matrix().element()));
    
        }
        else if (obj instanceof Hyperbola )
        {
            Hyperbola hyperbola= (Hyperbola)obj;
            out.println(indent + "hyperbola name is " + obj.name());
            out.println(indent + "  center = " + toString(hyperbola.centerPoint()));
            out.println(indent + "  semi-transverse length = " + hyperbola.semiTransverseLength());
            out.println(indent + "  semi-conjugate length = " + hyperbola.semiConjugateLength());
            out.println(indent + "  minimum DY width = " + hyperbola.minimumDY());
            out.println(indent + "  maximum DY width = " + hyperbola.maximumDY());
            out.println(indent + "  rotation angle = " + hyperbola.rotationAngle());
            out.println(indent + "  matrix = " + toString(hyperbola.matrix().element()));    
        }
        else if (obj instanceof Parabola )
        {
            Parabola parabola= (Parabola)obj;
            out.println(indent + "parabola name is " + obj.name());
            out.println(indent + "  center = " + parabola.centerPoint());
            out.println(indent + "  focal length = " + parabola.focalLength());
            out.println(indent + "  minimum DY width = " + parabola.minimumDY());
            out.println(indent + "  maximum DY width = " + parabola.maximumDY());
            out.println(indent + "  rotation angle = " + parabola.rotationAngle());
            out.println(indent + "  matrix = " + toString(parabola.matrix().element()));    
        }
        else if (obj instanceof DatumAxis )
        {
            DatumAxis theDaxis= (DatumAxis)obj;
            out.println(indent + "datum axis " + obj.name());
            out.println(indent + "  origin = " + toString(theDaxis.origin()));
            out.println(indent + "  direction = " + toString(theDaxis.direction()));            
        }
        else if (obj instanceof DatumPlane )
        {
            DatumPlane theDplane= (DatumPlane)obj;
            out.println(indent + "datum plane " + obj.name());
            out.println(indent + "  origin = " + toString(theDplane.origin()));
            out.println(indent + "  normal = " + toString(theDplane.normal()));
        }
        else
        {
            out.println(indent + getClassName(obj) + " name is " + getIdentifier(obj));    
        }

}

    void printGeometry(NXObject [] geometry, String indent) throws Throwable
    {
        NXObject obj;
        for( int ii=0; ii < geometry.length; ++ii )
        {
            obj = geometry [ii];
            printGeometry(obj, indent);
        }
    }

}
