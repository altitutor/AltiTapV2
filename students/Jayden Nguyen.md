---
Student_name: Jayden Nguyen
Current: Current
School: Adelaide High School
Student_year_level: Year 12
Student_email: jaydennguyen2424@gmail.com
Student_mobile: 61434802658
Parent_name: Loan Tran
Parent_email: loanthikim@outlook.com
Parent_mobile: 61423464365
Monday: Currently available
Tuesday: I can make myself available
Wednesday: I can make myself available
Thursday: I can make myself available
Friday: I can make myself available
Saturday_AM: I can make myself available
Saturday_PM: I can make myself available
Sunday_AM: I can make myself available
Sunday_PM: I can make myself available
Subjects:
  - SACE 12CHEM
SACE_or_IB: SACE
---

Classes:: [[12CHEM B1|12CHEM B1]], [[12BIO A1|12BIO A1]]

> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,"Jayden Nguyen")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Jayden Nguyen")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Jayden Nguyen")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Jayden Nguyen")
> ```


## Trial session questions to ask
1. **Student details** - year level, school, subjects 
	- Year level: Year 11
	- Subjects: Chemistry, Math Methods, Biology, English, Physics, Japanese
	- School: Adelaide High
2. **Motivation** - why do you want tutoring?
	- Maximise Grades
	- Enjoys Chem, Bio
1.  What do you want to do after you leave school?
	- Dentistry, Medicine
2. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- Chem, Bio, Method, 
3. **Grades** - what grades are you currently on for each of these subjects?
	- Chem: A
	- Bio: A
	- Method: A
1.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- Chem: Topic 5, Acids and Bases
	- Bio: 
	- Methods: DRV

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

