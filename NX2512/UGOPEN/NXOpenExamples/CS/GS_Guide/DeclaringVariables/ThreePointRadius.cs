/*=================================================================================================
                      Copyright (c) 2022 Siemens PLM 

                    Unpublished - All rights reserved

==================================================================================================*/
using NXOpen;
using System;

public class Program
{
    // class members
    private static Session theSession;


    public static Program theProgram;
    public static bool isDisposeCalled;
    //------------------------------------------------------------------------------
    // Constructor
    //------------------------------------------------------------------------------
    public Program()
    {
        try
        {
            theSession = Session.GetSession();


            isDisposeCalled = false;
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----
            // UI.GetUI().NXMessageBox.Show("Message", NXMessageBox.DialogType.Error, ex.Message);
        }
    }


    //------------------------------------------------------------------------------
    //  Explicit Activation
    //      This entry point is used to activate the application explicitly
    //------------------------------------------------------------------------------
    public static int Main(string[] args)
    {
        int retValue = 0;
        try
        {
            theProgram = new Program();

            //TODO: Add your application code here 
            var selUI = NXOpen.UI.GetUI();
            var sel = selUI.SelectionManager;
            View myView = null;
            Point3d p1, p2, p3;
            sel.SelectScreenPosition("Specify first point", out myView, out p1);  // Get first point from user
            sel.SelectScreenPosition("Specify second point", out myView, out p2); // Get second point
            sel.SelectScreenPosition("Specify third point", out myView, out p3);  // Get third point

            Vector3d u = new Vector3d(p2.X - p1.X, p2.Y - p1.Y, p2.Z - p1.Z);  // Vector3d from p1 to p2
            Vector3d v = new Vector3d(p3.X - p1.X, p3.Y - p1.Y, p3.Z - p1.Z);  // Vector3d from p1 to p3
            var uu = u.X * u.X + u.Y * u.Y + u.Z * u.Z;      // Dot product of vectors
            var uv = u.X * v.X + u.Y * v.Y + u.Z * v.Z;
            var vv = v.X * v.X + v.Y * v.Y + v.Z * v.Z;
            var det = uu * vv - uv * uv;                     // Determinant for solving linear equations
            var alpha = (uu * vv - uv * vv) / (2 * det);     // Bad code !! Should check that det is not zero
            var beta = (uu * vv - uu * uv) / (2 * det);
            var rx = alpha * u.X + beta * v.X;               // Radius vector components
            var ry = alpha * u.Y + beta * v.Y;
            var rz = alpha * u.Z + beta * v.Z;
            var radius = Math.Sqrt(rx * rx + ry * ry + rz * rz);   // Radius is length (norm) of this vector

            // Guide.InfoWriteLine(radius);                 // Output to Info window


            theProgram.Dispose();
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----

        }
        return retValue;
    }


    //------------------------------------------------------------------------------
    // Following method disposes all the class members
    //------------------------------------------------------------------------------
    public void Dispose()
    {
        try
        {
            if (isDisposeCalled == false)
            {
                //TODO: Add your application code here 
            }
            isDisposeCalled = true;
        }
        catch (NXOpen.NXException ex)
        {
            // ---- Enter your exception handling code here -----

        }
    }


    public static int GetUnloadOption(string arg)
    {
        //Unloads the image explicitly, via an unload dialog
        //return System.Convert.ToInt32(Session.LibraryUnloadOption.Explicitly);

        //Unloads the image immediately after execution within NX
        // return System.Convert.ToInt32(Session.LibraryUnloadOption.Immediately);

        //Unloads the image when the NX session terminates
        return System.Convert.ToInt32(Session.LibraryUnloadOption.AtTermination);


    }

}
