---
Student_name: Raneesya Kanniason
Current: Current
School: Glenunga high school
Student_year_level: Year 12
Student_email: raneesya18@gmail.com
Student_mobile: 61480279164
Parent_name: Kanniason Govindasamy
Parent_email: captkg@hotmail.com
Parent_mobile: 61422017889
Monday: Definitely unavailable
Tuesday: Currently available
Wednesday: Currently available
Thursday: Currently available
Friday: Currently available
Saturday_AM: Currently available
Saturday_PM: Definitely unavailable
Sunday_AM: I can make myself available
Sunday_PM: I can make myself available
Subjects:
  - SACE 12CHEM
SACE_or_IB: SACE
---
Classes:: [[1.2 Classes/12CHEM A1.md|12CHEM A1]]
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
### How did you hear about us?
- Friend at Altitutor - Renee
### **Student details** - year level, school, subjects 
	- Year level: 12
	- Subjects: 12CHEM
	- Chem, methods, english, health, done VET
3. **Motivation** - why do you want tutoring?
	- Get into med
4.  What do you want to do after you leave school?
	- Med
5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 12CHEM
6. **Grades** - what grades are you currently on for each of these subjects?
	- AIF A
7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- Start from start of 12CHEM

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

