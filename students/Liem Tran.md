---
Student_name: Liem Tran
Current?: Current
School: Glenunga High School
Student_year_level:
  - Year 12
Student_email: liemtran1408@gmail.com
Student_mobile: 61450156286
Parent_name: Danni Ha
Parent_email: dannihoang.ha@gmail.com
Parent_mobile: 61430223996
Monday: I can make myself available
Tuesday: I can make myself available
Wednesday: I can make myself available
Thursday: I can make myself available
Friday: Definitely unavailable
Saturday_AM: I can make myself available
Saturday_PM: Currently available
Sunday_AM: I can make myself available
Sunday_PM: Currently available
Subjects:
  - SACE 11METH
  - SACE 11PHYS
SACE_or_IB: SACE
Current: Current
Subsidy: $50
Day: 6. Saturday PM
ClassTime: 2:30
---
Classes:: [[12PHYS A1|12PHYS A1]], [[12METH A2|12METH A2]]

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
### Motivation - why do you want tutoring?
- Parents
- B -> A
- Y11
### Topic - which topic are you up to?
- Physics
	- Topic 1
- Psych
- Methods
- AIF
- English general
- VET course - fitness
### Grades - what grades are you currently on for each subject?
- B grade student


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

