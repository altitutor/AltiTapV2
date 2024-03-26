---
Student_name: Hariraj Nadar
Current: Current
School: Adelaide High School
Student_year_level: Year 12
Student_email: harivnadar@gmail.com
Student_mobile: 61414227962
Parent_name: Vella Nadar
Parent_email: vella.nadar@gmail.com
Parent_mobile: 61490237772
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Currently available
Friday: Currently available
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - SACE 12SPEC
  - SACE 12PHYS
  - SACE 12METH
SACE_or_IB: SACE
---
Classes:: [[1.2 Classes/12PHYS A3.md|12PHYS A3]], [[1.2 Classes/12METH A4.md|12METH A4]], [[12SPEC A2|12SPEC A2]]
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
### 1. How did you hear about us?
- Friends - Isaak ung, Hoorad
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: 12SPEC 12METH 12PHYS
- Also doing general english, done VET, RP
### 3. **Motivation** - why do you want tutoring?
- Wants to do really well 
### 4.  What do you want to do after you leave school?
- Compsci
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- 12SPEC 12METH 12PHYS
### 6. **Grades** - what grades are you currently on for each of these subjects?
- A for all
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Start of each

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

