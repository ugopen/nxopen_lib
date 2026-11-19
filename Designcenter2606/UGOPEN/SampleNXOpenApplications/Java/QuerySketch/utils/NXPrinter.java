/*==================================================================================================
                               Copyright 2026 Siemens
====================================================================================================

    NOTE:  Designcenter Development provides programming examples for illustration only.
    Designcenter Development assumes you are familiar with the programming language
    demonstrated in these examples, and the tools used to create and debug NXOpen
    programs. GTAC support professionals can help explain the functionality of
    a particular procedure, but neither GTAC nor Designcenter Development will modify
    these examples to provide added functionality or construction procedures.

File description:

    A Java class that implements an example of printing the data of the NX Objects

==================================================================================================*/

package utils;

import java.util.Comparator;
import java.io.PrintStream;

import nxopen.*;

/** Contains common utilities for use in printing data about NX objects */
public class NXPrinter 
{
    protected PrintStream out;
    public NXPrinter(PrintStream out_)
    {
        out = out_;
    }
    
    static public String toString(Point3d pnt) { 
        return "{ " + pnt.x + ", " + pnt.y + ", " + pnt.z + " }";
    }
    
    static public String toString(Vector3d pnt) { 
        return "{ " + pnt.x + ", " + pnt.y + ", " + pnt.z + " }";
    }
    
    static public String toString(Matrix3x3 mm) { 
        return "{ {" + mm.xx + ", " + mm.xy + ", " + mm.xz + " }, " +
        "{" + mm.yx + ", " + mm.yy + ", " + mm.yz + " }, " +
        "{" + mm.zx + ", " + mm.zy + ", " + mm.zz + " } }";
    }
    
    /** Returns a user-friendly string that identifies the specified INXObject */
    static public String getIdentifier(INXObject obj) throws NXException, java.rmi.RemoteException
    {
        String id;
        if ( obj instanceof nxopen.features.Feature || 
                obj instanceof Face || obj instanceof Edge ||
                obj instanceof DatumAxis || obj instanceof DatumPlane )
        {
            id = obj.journalIdentifier();
            String name = obj.name();
            if ( name != null && name.length() > 0 )
            {
                id += ":";
                id += name;
            }
            return id;
        }
        else if ( obj instanceof CoordinateSystem &&
                obj.owningPart().wcs().coordinateSystem().equals(obj) )
        {
            id = "WCS coordinate system";
        }
        else
        {
            id = obj.name();
            if ( id == null || id.length() == 0)
            {
                id = obj.journalIdentifier();
            }
        }
        return id;        
    }
    
    /** Returns a user-friendly string representing the class name for the specified INXObject */
    static public String getClassName(INXObject obj) throws NXException, java.rmi.RemoteException
    {
        String name = obj.getClass().getName();
        // Remove "_impl" from the end of the name
        if ( name.endsWith("_impl") )
            name = name.substring(0, name.length() - 5);
        return name;
    }
    
    /** Compares two NX objects based on their names */
    public static class ComparerByName implements Comparator<NXObject>
    {
        public int compare(NXObject nx, NXObject ny)
        {
            try
            {
                String nxName = nx.name();
                if ( nxName == null )
                    return ny.name() == null ? 0 : -1;
                return nxName.compareTo(ny.name());
            }
            catch ( Exception e )
            {
                throw new RuntimeException(e);
            }
        }
        
        /** Returns an instance of ComparerByName */
        static public ComparerByName instance() 
        { 
            if ( m_instance == null ) m_instance = new ComparerByName();
            return m_instance;
        }
        
        static private ComparerByName m_instance;
        private ComparerByName() {}
        
    }
    
}
