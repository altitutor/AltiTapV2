---
Student_name: Julie Huang
Current: Current
School: Seymour
Student_year_level:
  - Year 11
Student_email: julie.hhh0109@gmail.com
Student_mobile: 61416806915
Parent_name: Vivian Zou
Parent_email: vivian.w.zou@gmail.com
Parent_mobile: 61451321720
Monday: Definitely unavailable
Tuesday: Currently available
Wednesday: I can make myself available
Thursday: Currently available
Friday: Definitely unavailable
Saturday_AM: I can make myself available
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
Subjects:
  - SACE 11METH
SACE_or_IB: SACE
---
Classes:: [[12METH A4|12METH A4]]
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
	- Subjects: 11METH
	- 
2. **Motivation** - why do you want tutoring?
	- Wants to do well in stage 2 methods
	- 
1.  What do you want to do after you leave school?
	- Medical / health care industry 
		- Oral health, dentistry
	- Keen to do the UCAT
	- 
1. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- Methods
	- Biology
	- Chemistry
	- 
1. **Grades** - what grades are you currently on for each of these subjects?
	- Got a B+ in her last test
	- Ideally wants A+s for all subjects
	- 
1.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- Currently, calculus
	- Next, exponentials and logs (growth and decay)

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

