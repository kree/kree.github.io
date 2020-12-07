####################################
## SCRIPT: Mod6_kb157.py     
## NAME: Kristin Berry       
## CONTACT: kb157@students.uwf.edu
## DATE: 05/09/2020       
## DESCRIPTION:
##   This script opens a shapefile located at: S:\GIS5103\Mod6_Data\rivers.shp
##   and writes out the FID, vertex number, x-coordinate, y-coordinate, and
##   feature name for each point to an output file, kb157_rivers.txt
##   Subsequent runs will overwrite the output file.
##             
####################################

import arcpy

# Overwrite pre-existing output file
arcpy.env.overwriteOutput = True

# Set the workspace environment 
arcpy.env.workspace = "S:\GIS5103\Mod6_Data"

# Define the feature class variable
feature_class = r"S:\GIS5103\Mod6_Data\rivers.shp"

# Set up the output file to write to
filename = "rivers_kb157.txt"
print("Opening " + filename + " for writing.\n")
output_file = open(filename, "w")

# Create search cursor for rivers.shp that returns FID, SHAPE geometry object, and NAME.
cursor = arcpy.da.SearchCursor(feature_class, ['FID', 'SHAPE@', 'NAME'])

print("Writing FID, vertex number, x-coordinate, y-coordinate, and feature name from " + feature_class + \
      " to " + filename + ":")
# Iterate over the cursor to obtain and then write out the following information for each vertex:
# FID, vertex number, x-coordinate, y-coordinate, and feature name
for row in cursor:
    vertex_id = 0
    for point in row[1].getPart(0):
        vertex_id += 1
        output_line = str(row[0]) + " " + str(vertex_id) + " " + str(point.X) + " " + str(point.Y) + " " + row[2] +  "\n"
        print(output_line)
        output_file.write(output_line)

print("Information written successfully to " + filename + "! Closing " + filename + ".")

# Cleanup: close the .txt file and delete row and cursor variables outside of all loops.
output_file.close()
del cursor
del row
