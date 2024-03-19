---
Student_name: Johnny Turner
Current: Current
School: St Peter’s College
Student_year_level:
  - Year 12
Student_email: 75764@stpeters.sa.edu.au
Student_mobile: 61452564505
Parent_name: Dimi Turner
Parent_email: dimisimatos@yahoo.com
Parent_mobile: 61405350300
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: I can make myself available
Sunday_AM: I can make myself available
Sunday_PM: I can make myself available
SACE_or_IB: IB
Subjects:
  - IB ECO
---
Classes:: [[1.2 Classes/12IB ECO SL.md|12IB ECO SL]], [[1.2 Classes/6.Saturday PM/12IB MATH AA SL.md|12IB MATH AA SL]], [[12IB MATH AA SL|12IB MATH AA SL]]
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
	- st peters
	- ib
	- year `11`
1. **Motivation** - why do you want tutoring?
	- a bit behind on economics, not the grades he wants
2.  What do you want to do after you leave school?
	- combined degree bio + music
3. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- economics SL
	- maths IA
1. **Grades** - what grades are you currently on for each of these subjects?
	- 7s and 6s
2.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- 

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

