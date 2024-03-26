---
Student_name: Vishnu Patel
Current: Current
School: Norwood Internationa
Student_year_level: Year 12
Student_email: vis.patel07d@gmail.com
Student_mobile: 61448056019
Parent_name: Dipen Patel
Parent_email: dipenarchie@gmail.com
Parent_mobile: 61470589998
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: Definitely unavailable
Sunday_PM: Currently available
Subjects:
  - SACE 12SPEC
  - SACE 12CHEM
  - SACE 12METH
SACE_or_IB: SACE
---
Classes:: [[1.2 Classes/12METH A2.md|12METH A2]], [[1.2 Classes/12CHEM A2.md|12CHEM A2]], [[12SPEC A2|12SPEC A2]]
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
- His dad's colleague's child came here
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: 12METH 12SPEC 12CHEM, potentially 12BIO
- 
### 3. **Motivation** - why do you want tutoring?
- Didn't know if he could complete Y12 on his own
- Found chem and spec slightly hard in year 11
### 4.  What do you want to do after you leave school?
- Medicine
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- As above
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Spec B+/A-, Methods A-/A, Chem A-, Bio A
- Ideally wants an A+ across all subjects
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Hasn't started school, did 1.1 Chem for sample tutoring

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
