Imports NXOpen, NXOpenUI
Imports System, System.Drawing.Color, System.Windows.Forms

' NX Open Windows Form example that creates random spheres in
' the current work part
Module NXOpenSample
  Dim WithEvents myButton As Button       'A variable to hold a button
  Dim theSession As Session               'A variable to hold the NX Session
  Dim rand As Random                      'A variable to hold a random number generator

  Sub Main ()
    theSession = Session.GetSession()           'Get the NX Session
    rand = New Random()                         'Create a random number generator
    Dim myForm = New Form()                     'Create a Windows form
    myForm.Text = "Create Random Spheres"
    FormUtilities.SetApplicationIcon(myForm)    'Use an NX icon for the application icon
    FormUtilities.ReparentForm(myForm)          'Set NX as the parent of our form
    myButton = New Button()                     'Create a button
    myButton.BackColor = Yellow                 'Color it yellow
    myButton.Text = "Click me"                  'Put some text on it
    myForm.Controls.Add(myButton)               'Add it to our form
    myForm.ShowDialog()                         'Display our form
  End Sub

  Sub Handler(sender As Object, e As EventArgs) Handles myButton.Click
    Dim x = 100 * rand.NextDouble()  'Get a random x coordinate between 0 and 100
    Dim y = 100 * rand.NextDouble()  'Get a random y coordinate between 0 and 100
    Dim z = 100 * rand.NextDouble()  'Get a random z coordinate between 0 and 100
    Guide.CreateSphere(x, y, z, 10)        'Create a sphere centered at (x,y,z) with diameter 10
  End Sub

 End Module



