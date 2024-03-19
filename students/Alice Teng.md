---
Current: Potential
---

> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,"Alice Teng")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Alice Teng")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Alice Teng")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Alice Teng")
> ```


## Trial session questions to ask
1. **Student details** - year level, school, subjects 
	- Year level: 11
	- Subjects: bio, PE, english, methods
	- Next year planning to do 12BIO, english, nutrition, general maths, RP (B+)
2. **Motivation** - why do you want tutoring?
	- Wants an A+ in bio, currently on B+/A-
3.  What do you want to do after you leave school?
	- Physio
4. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 12BIO
5. **Grades** - what grades are you currently on for each of these subjects?
	- B+/A-
6.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- Just starting Y12 bio

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

