---
Student_name: Mah Rukh Fatima
Current: Current
School: The Heights School
Student_year_level: Year 12
Student_email: mahrukhfatima@hotmail.com
Student_mobile: 61412151180
Parent_name: Mah Rukh Fatima
Parent_email: uzma.baber.majid@gmail.com
Parent_mobile: 61403310887
Monday: Currently available
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: I can make myself available
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: I can make myself available
Subjects:
  - UCAT
SACE_or_IB: SACE
---
Classes:: [[UCAT B|UCAT B]]

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
> where icontains(file.name,"Mah Rukh Fatima")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Mah Rukh Fatima")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Mah Rukh Fatima")
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,"Mah Rukh Fatima")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Mah Rukh Fatima")
> 



## Trial session questions to ask
### 1. How did you hear about us?
- She has friends here 
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: UCAT
- Schools: The Heights
### 3. **Motivation** - why do you want tutoring?
- Needs help with UCAT as it is in five months time
### 4.  What do you want to do after you leave school?
- Medicine
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- UCAT
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

