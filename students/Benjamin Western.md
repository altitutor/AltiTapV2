---
Student_name: Benjamin Western
Current: Current
School: Pembroke high school
Student_year_level: Year 12
Student_email: benjaminwestern10@outlook.com
Student_mobile: 61478479823
Parent_name: Anthony Western
Parent_email: anthony.western@santos.com
Parent_mobile: 61418107330
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: Currently available
Friday: Currently available
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: Currently available
SACE_or_IB: SACE
Subjects:
  - SACE 12PHYS
  - SACE 12SPEC
  - SACE 12CHEM
---
Classes:: [[1.2 Classes/12PHYS A3.md|12PHYS A3]], [[1.2 Classes/12SPEC A2.md|12SPEC A2]], [[1.2 Classes/12CHEM A7.md|12CHEM A7]]
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
> where icontains(file.name,"Benjamin Western")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Benjamin Western")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Benjamin Western")
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,"Benjamin Western")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Benjamin Western")
> 



## Trial session questions to ask
### 1. How did you hear about us?
- 
### 2. **Student details** - year level, school, subjects
- Year level: Yes
- Subjects: Blahblah
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

