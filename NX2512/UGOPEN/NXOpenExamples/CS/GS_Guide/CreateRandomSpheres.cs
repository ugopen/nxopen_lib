/*==================================================================================================
  
                      Copyright (c) 2022 Siemens PLM 
                   Unpublished - All rights reserved

==================================================================================================*/

using NXOpen; 
using NXOpenUI;
using System;
using System.Drawing;
using System.Windows.Forms;

public class NXJournal
{
    static Button myButton;                   //A variable to hold a button 
    static Session theSession;                //A variable to hold the NX Session
    static Random rand;                       //A variable to hold a random number generator
    
    public static void Main()
    {
        theSession = Session.GetSession();             //Get the NX Session
        rand = new Random();                           //Create a random number generator 
        Form myForm = new Form();                      //Create a Windows form
        myForm.Text = "Create Random Spheres";
        FormUtilities.SetApplicationIcon(myForm);      //Use an NX icon for the application icon
        FormUtilities.ReparentForm(myForm);            //Set NX as the parent of our form
        myButton = new Button();                       //Create a button
        myButton.BackColor = Color.Yellow;             //Color it yellow
        myButton.Text = "Click me";                    //Put some text on it
        myButton.Click += Handler;
        myForm.Controls.Add(myButton);                 //Add it to our form
        myForm.ShowDialog();                           //Display our form
    }
    static void Handler(Object sender, EventArgs e)
    {
        double x = 100 * rand.NextDouble();   //Get a random x-coordinate between 0 and 100
        double y = 100 * rand.NextDouble();   //Get a random y-coordinate between 0 and 100
        double z = 100 * rand.NextDouble();   //Get a random z-coordinate between 0 and 100
        Guide.CreateSphere(x, y, z, 10);      //Create a sphere at (x,y,z) with diameter 10
    }
}
