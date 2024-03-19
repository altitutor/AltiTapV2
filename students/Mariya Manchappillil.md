---
Student_name: Mariya Manchappillil
Current: Current
School: St Dominic's Priory
Student_year_level:
  - Year 11
Student_email: mariya.mancha@gmail.com
Student_mobile: 61491719972
Parent_name: Giji Mathew
Parent_email: gijimancha@gmail.com
Parent_mobile: 61421845280
Monday: Definitely unavailable
Tuesday: I can make myself available
Wednesday: Definitely unavailable
Thursday: I can make myself available
Friday: Definitely unavailable
Saturday_AM: I can make myself available
Saturday_PM: Definitely unavailable
Sunday_AM: Currently available
Sunday_PM: I can make myself available
Subjects:
  - UCAT
SACE_or_IB: SACE
---
Classes:: [[UCAT B|UCAT B]]
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
	- Year level: 10 
2. **Motivation** - why do you want tutoring?
	- Better grades
3.  What do you want to do after you leave school?
	- Dentistry 
4. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	-  UCAT, Stage 1 Bio and Stage 1 Physics
5. **Grades** - what grades are you currently on for each of these subjects?
	- Stage 1 Physics - A
6.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
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

