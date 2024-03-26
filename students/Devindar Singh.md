---
Subsidy: $50 for all subjects
File: Devindar Singh
Current: Current
Subjects:
  - SACE 12CHEM
  - SACE 12METH
Student_year_level:
  - Year 12
Student_email: devhere0000@gmail.com
Student_mobile: 61430910710
Parent_name: Seeta Kaur
Parent_mobile: 61430910710
Parent_email: hsrhere@gmail.com
Monday: Definitely unavailable
Tuesday: Currently available
Wednesday: Definitely unavailable
Thursday: Currently available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Currently available
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
School: Trinity College
SACE_or_IB: SACE
Day: 1. Monday, 6. Saturday PM
ClassTime: 4:15, 1:00
Student_name: Devindar Singh
---
Classes:: [[12CHEM B1|12CHEM B1]], [[1.2 Classes/12METH B1.md|12METH B1]]
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
	- 
2. **Motivation** - why do you want tutoring?
	- 
3.  What do you want to do after you leave school?
	- 
4. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 
5. **Grades** - what grades are you currently on for each of these subjects?
	- 
6.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview questions
type command
action QuickAdd: Insert subsidy interview questions
```
## Subsidy
### Application email

### About family
- 
### Income sources for family
- 
### Expenses sources for family
- 
### Agreed subsidy
- $50 for all subjects - multi subject discount (also his sis is coming to us so)


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

