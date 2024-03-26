---
Student_name: Campbell Smith
Current: Current
School: Christian Brothers
Student_year_level:
  - Year 9
Student_email: campbells77@icloud.com
Student_mobile: 61435388790
Parent_name: Jess Smith
Parent_email: jjsmith@adam.com.au
Parent_mobile: 61423632211
Monday: Currently available
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: I can make myself available
Saturday_AM: I can make myself available
Saturday_PM: I can make myself available
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
Subjects:
  - PreSACE Maths
SACE_or_IB: SACE
---
Classes:: [[1.2 Classes/9MATH + SCI B1.md|9MATH + SCI B1]]

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


## Trial session
1.  **Motivation** - why do you want tutoring?
	- mum feels like he is falling behind in maths - discussion with teacher
	- wants to do tutoring before he gets too far behind
	- Campbell maybe wants to do physio
1.  **Topic** - which topic are you up to for each subject?
	- percentages
2. **Grades** - what grades are you currently on for each subject?
	- B/B+ in the normal class (nonadvanced)


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

