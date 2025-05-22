Type	         Example	         Ordered?	  Mutable?	 Key-Value?    Duplicates

List	         [1, 2, 3]	          ✅	        ✅	        ❌        ✅	      
Dictionary	 {'a': 1, 'b': 2}	      ✅	        ✅	        ✅        ❌ (keys)
Set	          {1, 2, 3}	            ❌	        ✅	        ❌        ❌
Tuple        	(1, 2, 3)	            ✅	        ❌	        ❌        ✅

------------------------------------------------------------------------------------

Type	                  Example             	              Has :?	  Ordered?	  Good for DataFrame?
List of Dicts	 [{'name': 'Ashu', 'age': 24},{...}]	          ✅ Yes	   ✅ Yes	       ✅ Yes
List of Sets  	[{'Ashu', 24}, {'keshu', 19}]	                ❌ No      ❌ No	         ❌ No





#list of tuples 
data = [("Ashu",24),("keshu",19)]
col = ["Name","age"]
df = spark.createDataFrame(data,col)
df.show()


#list of dictionaries.
data = [{'id':1,'name':"Ashu"},{'id':2,'name':"keshu"}]
df = spark.createDataFrame(data)
df.show()

#we cannot use list of sets with dataFrame. its only take value not key.  (error occurs)


# Example: Tuple containing two lists
tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'])
