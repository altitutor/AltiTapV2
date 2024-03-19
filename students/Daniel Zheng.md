---
SACE_or_IB: SACE
Student_name: Daniel Zheng
Current: Current
School: Glenunga
Student_year_level: Year 11
Student_email: dazhy12@gmail.com
Student_mobile: 61450810309
Parent_name: Daniel Zheng
Parent_email: huang.ruifang@hotmail.com
Parent_mobile: 61430528768
Monday: Currently available
Tuesday: I can make myself available
Wednesday: I can make myself available
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Definitely unavailable
Saturday_PM: I can make myself available
Sunday_AM: I can make myself available
Sunday_PM: I can make myself available
Subjects:
  - SACE 12BIO
  - SACE 12METH
---
Classes:: [[1.2 Classes/12BIO A2.md|12BIO A2]], [[1.2 Classes/12METH B1.md|12METH B1]]
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

# Trial session
> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]
### 1. How did you hear about us?
- Family friend referred them here.
### 2. **Student details** - year level, school, subjects
- Year 11, Glenunga, Ignite, General, AIF, 12 BIO, 12 METH, 11 SPEC, 11 11CHEM
### 3. **Motivation** - why do you want tutoring?
- Better grades, teacher isn't that great at teaching at school
### 4.  What do you want to do after you leave school?
- Medicine
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- 12 Methods, 12 Biology
### 6. **Grades** - what grades are you currently on for each of these subjects?
- A+
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Differential Equations & DNA and Proteins

# Subsidy interview
```button
name Insert subsidy interview
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
