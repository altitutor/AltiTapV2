---
SACE_or_IB: PreSACE
Student_name: Rianne Nithyananth
Current: Current
School: Saint Ignatius colle
Student_year_level: Year 9
Student_email: lisa.nith@proton.me
Student_mobile: +41412156863
Parent_name: Alice Mathuram
Parent_email: alicesam2509@yahoo.com
Parent_mobile: +61423669222
Monday: I can make myself available
Tuesday: I can make myself available
Wednesday: I can make myself available
Thursday: I can make myself available
Friday: I can make myself available
Saturday_AM: Definitely unavailable
Saturday_PM: I can make myself available
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
Subjects:
  - PreSACE Maths
---
Classes:: [[9MATH B2|9MATH B2]]

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
> where icontains(file.name,"Alice Mathuram")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Alice Mathuram")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Alice Mathuram")
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,"Alice Mathuram")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Alice Mathuram")
> 



## Trial session questions to ask
### 1. How did you hear about us?
- rianne
- Classmates coming Kemi and recommend
### 2. **Student details** - year level, school, subjects
- Year level: 9
- Subjects: Maths, sciences, english

- 9 general? not really clear about the streams since st ignatius does things a little weirdly
- depending on student results they can shuffle around
### 3. **Motivation** - why do you want tutoring?
- Improving her grades, math pathways and knowledge gaps,
- Studying in India til y6 and moved recently curriculum here is a lot more easier
- St Ignatius
### 4.  What do you want to do after you leave school?
- Doesn't know at moment
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Mainly mathematics
### 6. **Grades** - what grades are you currently on for each of these subjects?
- B in semester 2 and semester 1, A+ ideally
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Index laws

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

