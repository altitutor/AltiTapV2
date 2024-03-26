---
SACE_or_IB: SACE
Student_name: Anagha Abhilash
Current: Current
School: GlHS
Student_year_level: Year 12
Student_email: anaghabhi13@gmail.com
Student_mobile: +61421892566
Parent_name: Anjana Abhilash
Parent_email: anjanathumbi@gmail.com
Parent_mobile: +61469055358
Monday: I can make myself available
Tuesday: Definitely unavailable
Wednesday: I can make myself available
Thursday: Currently available
Friday: Currently available
Saturday_AM: I can make myself available
Saturday_PM: Currently available
Sunday_AM: I can make myself available
Sunday_PM: Currently available
Subjects:
  - SACE English Lit
---
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
> where icontains(file.name,"Anagha Abhilash")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Anagha Abhilash")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Anagha Abhilash")
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,"Anagha Abhilash")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Anagha Abhilash")
> 



## Trial session questions to ask
### 1. How did you hear about us?
- Through a friend 
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: English Lit
- Creative arts, english lit, maths methods, IB geography 
### 3. **Motivation** - why do you want tutoring?
- Have a second person to have a look at your work
### 4.  What do you want to do after you leave school?
- Interior architecture (NSW)
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- English literature
### 6. **Grades** - what grades are you currently on for each of these subjects?
- English lit - As/A+s 
- Now on A-s (need feedback in fluency)
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Film study (three billboards outside ebbing missouri)

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

