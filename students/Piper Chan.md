---
Student_name: Piper Chan
Current: Current
School: St Ignatius
Student_year_level: Year 11
Student_email: piperchan07@gmail.com
Student_mobile: 61433569687
Parent_name: Peter Chan
Parent_email: peter@pandaca.biz
Parent_mobile: 61410578356
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: I can make myself available
Friday: Definitely unavailable
Saturday_AM: I can make myself available
Saturday_PM: Currently available
Sunday_AM: Definitely unavailable
Sunday_PM: Currently available
Subjects:
  - SACE 12METH
SACE_or_IB: SACE
---
Classes:: [[1.2 Classes/12METH A2.md|12METH A2]]
```button
name Insert student details
type line(100) template
action Student details template
```
> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,"Piper Chan")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Piper Chan")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Piper Chan")
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,"Piper Chan")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Piper Chan")
> 



## Trial session questions to ask
### 1. How did you hear about us?
- AACC
### 2. **Student details** - year level, school, subjects
- Year level: 11
- Subjects: Chem Stage 1 and Methods (Stage 2)
- 
### 3. **Motivation** - why do you want tutoring?
- For better grades, don't understand things fast in methods, wants to consolidate her learning.
### 4.  What do you want to do after you leave school?
- Doesn't know yet, might take a gap year
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Methods atm
### 6. **Grades** - what grades are you currently on for each of these subjects?
- A+
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Started differential calculus

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview
type append template
action Subsidy questions template
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

