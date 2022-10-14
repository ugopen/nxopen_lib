Option Explicit Off
Imports Snap, Snap.Create

Module SnapSample

   Public Sub Main()
      
      pixels = New System.Drawing.Bitmap("C:\sammie.jpg")      ' Reads the file. Change this !!

      width = System.Math.Min(pixels.Width,   200)             ' Limit the width to 200
      height = System.Math.Min(pixels.Height, 200)             ' Limit the height to 200

      For x = 1 To width - 1                          ' Loop over the pixels in the image
         For y = 1 To height - 1
            pixelColor = pixels.GetPixel(x, y)        ' Read the pixel color at location (x,y)
            brightness = pixelColor.GetBrightness()   ' Measure the brightness of the color      
            If brightness < 0.4 Then Point(x, -y)     ' If dark, create a point (but flip y)
         Next y
      Next x

   End Sub

End Module
