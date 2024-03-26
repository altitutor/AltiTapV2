---
Current: Current
Student_name: Hoorad Nejad
School: AHS
SACE_or_IB: SACE
Subjects:
  - SACE 12CHEM
Student_year_level:
  - Year 12
Student_email: hoorad.nejad@gmail.com
Student_mobile: "+61490761051"
Parent_name: Hoorad Nejad
Parent_email: alinejad50@gmail.com
Parent_mobile: "+61451663754"
Monday: Currently available
Tuesday: I can make myself available
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Currently available
Saturday_AM: I can make myself available
Saturday_PM: Definitely unavailable
Sunday_AM: I can make myself available
Sunday_PM: I can make myself available
---

Classes:: [[12CHEM B1|12CHEM B1]]

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
- 
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: Chem
- 
### 3. **Motivation** - why do you want tutoring?
- 
### 4.  What do you want to do after you leave school?
- 
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- 
### 6. **Grades** - what grades are you currently on for each of these subjects?
- 
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- 

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
