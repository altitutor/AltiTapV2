---
Student_name: Kylie Tang
Current: Current
School: USC
Student_year_level:
  - Year 12
Student_email: tangkylie819@gmail.com
Student_mobile: 61452162127
Parent_name: Wan Tang
Parent_email: wanchiew@msn.com
Parent_mobile: 61422121619
Monday: Currently available
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
SACE_or_IB: SACE
Subjects:
  - SACE 11PHYS
---
Classes:: [[12PHYS A1|12PHYS A1]]
```button
name Insert student details
type command
action Templater: Insert Templates/Student details template.md
```

> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,this.file.name)
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,this.file.name)
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,this.file.name)
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,this.file.name)
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,this.file.name)
> 


## Trial session questions to ask
1. **Student details** - year level, school, subjects 
	- Year level: Year 11
	- Subjects: Physics
	- Put in same class as Grace (Monday 5:45pm for 11PHYS)
1. **Motivation** - why do you want tutoring?
	- Get better grades in physics - want to get an A- by the end of the year
2.  What do you want to do after you leave school?
	- Computer science
3. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- Stage 1 Physics
4. **Grades** - what grades are you currently on for each of these subjects?
	- Currently on a B
5.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- Topic 5 Waves 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview questions
type command
action QuickAdd: Insert subsidy interview questions
```



# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

