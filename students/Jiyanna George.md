---
Subjects:
  - PreSACE Maths
Current: Current
SACE_or_IB: SACE
Student_year_level:
  - Year 9
Parent_name: Sherin Mathew
Parent_mobile: "+61415852473"
Parent_email: sherinnkmathew@gmail.com
Student_mobile: "+61415852473"
---
Classes:: [[9MATH B4|9MATH B4]]

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

Daughter's name is Jiyanna?

### 1. How did you hear about us?
- Family friends word of mouth
### 2. **Student details** - year level, school, subjects
- Adelaide high, y9
	- dance, food tech, spanish, core subjects
### 3. **Motivation** - why do you want tutoring?
- good grades :D
### 4.  What do you want to do after you leave school?
- not sure
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Maths - one big class no extention available, english, and science
### 6. **Grades** - what grades are you currently on for each of these subjects?
- maths - A
- english - A
- sciences - A
- , dance B food tech A
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- maths- finished indices, eng book analysis, science - bio

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
