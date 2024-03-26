---
Student_name: Khai Tran
Current?: Current
School: Glenunga High School
Student_year_level:
  - Year 11
Student_email: k.mtran191107@gmail.com
Student_mobile: 61451911726
Parent_name: Danni Ha
Parent_email: dannihoang.ha@gmail.com
Parent_mobile: 61430223996
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: I can make myself available
Thursday: Definitely unavailable
Friday: I can make myself available
Saturday_AM: I can make myself available
Saturday_PM: Currently available
Sunday_AM: 
Sunday_PM: I can make myself available
Current: Current
SACE_or_IB: SACE
Subjects:
  - SACE 11METH
Day: 6. Saturday PM, 6. Saturday PM
ClassTime: 1:00, 2:30
Subsidy: $50
---
Classes:: [[11METH B1|11METH B1]]
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


## Trial session
### Motivation - why do you want tutoring?
- Parents
- Y10
- Wants to accelerate to Y11 methods
- Has finished all Y10 topics - can start from the start of Y11 methods
- Put in 11METH with Hannah C and Salwa
### Topic - which topic are you up to?
- Has finished all Y10 topics - can start from the start of Y11 methods
### Grades - what grades are you currently on for each subject?
- B/B+ grade student
- Wants A grades in Y10 and Y11

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

