score = 85

if score > 90:
      print("Excellent")
elif score >=70:
      print("good")
else:
    print("Bad")

-------------

tools = ["python","Sql","Airflow"]
for tool in tools:
    print(f"I am learning {tool}")

OUTPUT-
I am learning python
I am learning Sql
I am learning Airflow

tools = ["Python", "SQL", "Airflow"]
This creates a list called tools.
print(f"I am learning {tool}")
This prints a message.
f"" is an f-string, which lets you plug variables into strings.
{tool} gets replaced by the actual tool name in the loop.

--------------
#While Loop

i = 0
while i < 3:
    print("Love")
    i += 1

#Love
#Love
#Love
-------------
age = 20
if(age>18):
    print("Adult")
else:
    print("Not Adult")
