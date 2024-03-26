---
Student_name: Serene Deng
Current: Current
School: University Senior C
Student_year_level: Year 11
Student_email: serenedengg@gmail.com
Student_mobile: 61480347891
Parent_name: May Taing
Parent_email: maymay123@live.com
Parent_mobile: 61411383699
Monday: Definitely unavailable
Tuesday: Currently available
Wednesday: Currently available
Thursday: Currently available
Friday: Currently available
Saturday_AM: Currently available
Saturday_PM: Definitely unavailable
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - UCAT
SACE_or_IB: SACE
---
Classes:: [[1.2 Classes/UCAT C.md|UCAT C]]

> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,"Serene Deng")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Serene Deng")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Serene Deng")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Serene Deng")
> ```


## Trial session questions to ask
### 1. How did you hear about us?
- found online
### 2. **Student details** - year level, school, subjects
- Year level: 11
- Subjects: UCAT
- 
### 3. **Motivation** - why do you want tutoring?
- Wants to get into dent
### 4.  What do you want to do after you leave school?
- Dent
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- UCAT
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Straight As
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Used to go to Northshore UCAT tutoring

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
undefined



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

