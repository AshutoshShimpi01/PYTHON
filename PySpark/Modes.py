Mode	                                Description
"PERMISSIVE"      (default)	Loads all data, puts corrupt rows in a special column _corrupt_record
"DROPMALFORMED" 	Skips corrupted rows
"FAILFAST"	      Fails immediately when a corrupted row is found




Write Mode	                         Description
"overwrite"      	Overwrites the existing data at the path
"append"	        Adds the data to existing files
"ignore"	        If data already exists at path, do nothing (no error, no overwrite)
"error" or "errorifexists"	Fails if data already exists at path (default mode)
