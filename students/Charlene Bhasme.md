---
Student_name: Charlene Bhasme
Current: Current
School: Emmaus Christian Col
Student_year_level:
  - Year 12
Student_email: crbhasme1@gmail.com
Student_mobile: 61449616618
Parent_name: Cecil Bhasme
Parent_email: cbhasme@gmail.com
Parent_mobile: 61418850283
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: Currently available
Friday: Definitely unavailable
Saturday_AM: I can make myself available
Saturday_PM: Currently available
Sunday_AM: Definitely unavailable
Sunday_PM: I can make myself available
Subjects:
  - SACE 12PHYS
SACE_or_IB: SACE
---
Classes:: [[1.2 Classes/12PHYS A1.md|12PHYS A1]]
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
1.  **Motivation** - why do you want tutoring?
	- Want to get into the airforce in Canberra 
	- Want to get better grades and be more confident in the topics 
1.  **Topic** - which topic are you up to for each subject?
	- 11METHODS - Finished relations and functions
	- 11PHYSICS - Finished energy 
	- 11CHEM - ??? 
1. **Grades** - what grades are you currently on for each subject?
	- All in the B/B- band for all subjects 

## Subsidy
### Application email

### Interview
1. **About** - tell me about yourself and your family
	- 
2. **Income** - what are all of the income sources for your family?
	- 
3.  **Expenses** - what are all the sources of expenses for your family?
	- 
4. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
	- 


> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,"Charlene Bhasme")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Charlene Bhasme")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Charlene Bhasme")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Charlene Bhasme")
> ```


## Trial session questions to ask
1. **Student details** - year level, school, subjects 
	- 
2. **Motivation** - why do you want tutoring?
	- 
3.  What do you want to do after you leave school?
	- 
4. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 
5. **Grades** - what grades are you currently on for each of these subjects?
	- 
6.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- 

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

