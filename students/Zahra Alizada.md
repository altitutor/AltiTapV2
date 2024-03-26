---
Student_name: Zahra Alizada
Current?: Current
School: OLSH
Student_year_level:
  - Year 10
Student_email: zahra.alizada3458@gmail.com
Student_mobile: 61470565973
Parent_name: Shafiqa alizada
Parent_email: shafiqa.alizada@icloud.com
Parent_mobile: 61421525177
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - PreSACE Maths
  - PreSACE Science
  - 10SCI
SACE_or_IB: PreSACE
Current: Current
Day: 3. Wednesday
ClassTime: 4:15
Subsidy: ---
Student_name: Zahra Alizada
Current?: Current
School: OLSH
Student_year_level:
  - Year 10
Student_email: zahra.alizada3458@gmail.com
Student_mobile: 61470565973
Parent_name: Shafiqa alizada
Parent_email: shafiqa.alizada@icloud.com
Parent_mobile: 61421525177
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - PreSACE Maths
  - PreSACE Science
SACE_or_IB: PreSACE
Current: Current
Day: 3. Wednesday
ClassTime: 4:15
Subsidy: $10
---0
---
Classes:: [[1.2 Classes/10MATH A1.md|10MATH A1]], [[10SCI B4|10SCI B4]]
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

