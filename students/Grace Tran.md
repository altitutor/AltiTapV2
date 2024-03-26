---
Student_name: Grace Tran
Current: Current
School: USC
Student_year_level:
  - Year 12
Student_email: grace.tran2006@gmail.com
Student_mobile: 61452390108
Parent_name: Anh-Thu Nguyen
Parent_email: nat@ihug.com.au
Parent_mobile: 61418803683
Monday: Currently available
Tuesday: Currently available
Wednesday: Definitely unavailable
Thursday: Currently available
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: I can make myself available
Sunday_AM: Definitely unavailable
Sunday_PM: Currently available
SACE_or_IB: SACE
Subjects:
  - SACE 11PHYS
  - SACE 11CHEM
Subsidy: $40
---
Classes:: [[1.2 Classes/12CHEM A2.md|12CHEM A2]], [[1.2 Classes/12BIO A3.md|12BIO A3]]
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
	- not doing as well in physics as she wants to
	- not great at physics tests, doesnt know when to apply concepts and interpret questions
1.  **Topic** - which topic are you up to for each subject?
	- 11Physics - Newtons laws
	- 11Chem - Bonding
2. **Grades** - what grades are you currently on for each subject?
	- 11Physics - B
	- 11Chemistry - A
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

