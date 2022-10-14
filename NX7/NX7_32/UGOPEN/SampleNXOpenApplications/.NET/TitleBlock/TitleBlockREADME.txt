This example performs the following steps:

1) Queries the user for Part Name and Author Name.
2) Inserts a custom symbol for the title block.
3) Inserts the labels in the title block, and the user entered data.
   The date field is determined by the system's date.


HOW TO RUN THE EXAMPLE

- Open the example part that contains a drawing sheet.  
- Run  Generate_title_block.vb.  
- Fill in Part Name and Author Name fields, and hit OK on form.
- The title block will be generated.  The title block can then be moved 
  to another location on the sheet.  Notice that all the text is 
  associative to the framing title block.
  
USING OTHER PARTS
 - A part other than the example part can be used.  However, there are 
   two issues that will need to be taken care of.
   1) The file special.sbf, must be at the same file location as the 
   part you want to use.
   2) The preferences related to lettering size may be set in the part
   may cause the title block text to not show optimally.  

 







