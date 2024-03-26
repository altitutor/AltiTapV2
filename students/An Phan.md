---
Subjects:
  - SACE 12BIO
SACE_or_IB: SACE
Current: Past
School: USC
Student_email: an.phan@usc.adelaide.edu.au
Student_mobile: "0433748884"
Student_year_level:
  - Year 12
Saturday_PM: Currently available
Monday: Currently available
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
Student_name: An
---
Classes:: 

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
- Minah Cho 
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: Biology
- Chem, methods, psych, headstart (anatomy)
- Doing pretty good at school
### 3. **Motivation** - why do you want tutoring?
- Just want to get good grades for Year 12
### 4.  What do you want to do after you leave school?
- Medicine 
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- 12BIO and potentially 12CHEM, 12METH
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Straight As for subjects
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Bio - DNA and Proteins (Topic 1)
- Chem - Managing the environment 

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
