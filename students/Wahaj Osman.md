---
Student_name: Wahaj Osman
Current: Past
School: Islamic College, SA
Student_year_level:
  - Year 12
Student_email: wahajosman22@gmail.com
Student_mobile: 61468487971
Parent_name: Idris Osman
Parent_email: abofaris.sat@gmail.com
Parent_mobile: 61413656882
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: I can make myself available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Currently available
Sunday_AM: Definitely unavailable
Sunday_PM: I can make myself available
SACE_or_IB: SACE
Subjects:
  - SACE English
  - SACE 12CHEM
Subsidy: $25/session
---

Classes:: 

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
	- Year level: 12
	- Subjects: Chemistry, English
	- 
2. **Motivation** - why do you want tutoring?
	- better grades
	- 
1.  What do you want to do after you leave school?
	- med or allied health
2. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 
3. **Grades** - what grades are you currently on for each of these subjects?
	- As and Bs
4.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- starting year 12 this term (term 4)
	- His school starts the following year content in term 4 of the previous year - so need to be in a class by himself 

Extra notes:
- Wahaj is now enrolled in the online subscription for $15/month 

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

