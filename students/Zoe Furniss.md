---
Current: Potential
---

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

# Trial session
> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]
### 1. How did you hear about us?
- 
### 2. **Student details** - year level, school, subjects
- Year level: University
- Subjects: UCAT
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


*Whoever takes this trial session, please do the subsidy interview at the same time.*
**Subsidy email:**
Name of student applying: Zoe Furniss  
Email: [zoe.furniss@icloud.com](mailto:zoe.furniss@icloud.com)  
Phone number: 0490446095  
Which course would you like to apply for? Select all that apply.: UCAT preparation course  
Which days are you available to meet for a subsidy interview? Select all that apply.: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday morning, Saturday afternoon, Sunday morning, Sunday afternoon  
Why are you applying for the subsidy program?: I am currently studying law and accounting at university and wanting to get into medicine in interstate universities. I live out of home as my family live in the country. I currently receive Centrelink and are a concession card holder.

# Messages
```button
name Generate student message
type line (1000) template
action MESSAGE - class times student
```
```button
name Generate parent message
type line (1000) template
action MESSAGE - class times parent
```
