---
Student_name: Diya Shrestha
Current: Current
School: OLSH
Student_year_level: Year 11
Student_email: diya.shrestha0325@gmail.com
Student_mobile: 61450883972
Parent_name: Anita Shrestha
Parent_email: anita_shrestha81@gmail.com
Parent_mobile: 61406622008
Monday: Definitely unavailable
Tuesday: Currently available
Wednesday: Currently available
Thursday: Currently available
Friday: Currently available
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - SACE 11CHEM
  - UCAT
SACE_or_IB: SACE
---
Classes:: [[1.2 Classes/11CHEM A2.md|11CHEM A2]], [[1.2 Classes/UCAT C.md|UCAT C]]
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
- Sumaya introduced
### 2. **Student details** - year level, school, subjects
- Year level: 11
- Subjects: Chemistry
- 
### 3. **Motivation** - why do you want tutoring?
- Last year chem grades improvement
- Maths elements of Chem
### 4.  What do you want to do after you leave school?
- Study med or dent
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Chemistry
- Maybe Bio
- UCAT
### 6. **Grades** - what grades are you currently on for each of these subjects?
- High B band to A/A-
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- From the start

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

