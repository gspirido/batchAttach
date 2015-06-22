##################################################################################
## ArcGIS 10.3																	##
##################################################################################
#	Author: Greg Spiridonov
#	Contact: greg.spiridonov@county-lambton.on.ca
#	Date: 2015-06-22
#
#
# 	Batch Attachments
#
#	Batch attachment script takes a series of selected features (can be
#	different layers) and asks for a list of files to attach to them. A temp 
#	csv table is created, and the AddAttachment tool is run to attach the files
#	to each selected feature. Script should also enable attachments if layer has
# 	not already been enabled, but I haven't tested it
#
##################################################################################
import os
import arcpy
import traceback

# get files to add
files = arcpy.GetParameterAsText(0).split(";")
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd,"*")[0]

# dir to save temporary csvs
dir = os.path.join(os.path.dirname(__file__))

arcpy.AddMessage("Temporary Path:");
arcpy.AddMessage(dir);

# for each layer
for l in arcpy.mapping.ListLayers(mxd, "", df):
	try:
		desc = arcpy.Describe(l)
		# get layer workspace
		path = desc.Path + "\\" + l.name
		
		arcpy.AddMessage("For " + l.name + ":");
		arcpy.AddMessage("  Layer path: " + path);
		
		# create temporary match table
		matchTable = dir + "\\" + l.name + ".csv"
		csv = open(matchTable, "w")
		
		arcpy.AddMessage("  Create table: " + matchTable)
		
		aa = arcpy.Describe(l.name)
		ss = aa.FIDset
		tt = ss.split("; ")
		
		# write field titles into csv
		csv.write("OBJECTID," + "Asset\n")
		
		for oid in tt:
			if oid <> "":
				for file in files:
					# get file path from file
					filename = file.replace("'", "")
					
					arcpy.AddMessage("  Add Attachment: " + filename)
					
					# write objectid and filename to csv
					csv.write(oid + ',' + filename + "\n")

		csv.close()
		
		# run addattachments using created csv
		arcpy.AddMessage("  Running AddAttachment Tool on... " + matchTable)
		arcpy.AddAttachments_management(path, "OBJECTID", matchTable, "OBJECTID", "Asset", None)
		
		# delete csv
		arcpy.AddMessage("  Removing temporary table: " + matchTable)
		os.remove(matchTable);
	except:
		print "Something went wrong handling " + str(l) + ". Here's a traceback:"
        traceback.print_exc()
        continue
	
	arcpy.AddMessage("Completed Script!")
del mxd