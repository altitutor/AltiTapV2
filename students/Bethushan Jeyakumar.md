---
Current: Current
Student_name: Bethushan
Subsidy: $25.00
School: The Heights School
SACE_or_IB: SACE
Subjects:
  - UCAT
  - UCAT
Student_year_level:
  - Year 11
Student_email: bethushan.jeyakumar668@schools.sa.edu.au
Student_mobile: "0432844980"
Parent_name: Jeyakumar Selvanayagam
Parent_email: sjaya_kumar@ymail.com
Parent_mobile: "0469747085"
Sunday_AM: Currently available
Sunday_PM: Definitely unavailable
Saturday_PM: Definitely unavailable
Saturday_AM: Definitely unavailable
Friday: Definitely unavailable
Thursday: Definitely unavailable
Wednesday: Definitely unavailable
Tuesday: Definitely unavailable
Monday: Definitely unavailable
---
Classes:: [[1.2 Classes/UCAT A.md|UCAT A]]
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




## Trial session questions to ask
### 1. How did you hear about us?
- Google, wanted UCAT tutoring
### 2. **Student details** - year level, school, subjects
- Year level: 11
- Subjects: UCAT
- Year level: 11
- School: the Heights
- Subjects: Bio, Chem, Psych, Methods, Eng Lit, UCAT
### 3. **Motivation** - why do you want tutoring?
- UCAT tutoring is important
- Wants help with Math and Sciences
### 4.  What do you want to do after you leave school?
- Medicine - Looking to be a GP?
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Methods, Bio, Chem and UCAT, English 
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Science: A-, B+
- Math: A
- English: B+
- Cutting Edge Science: A
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Biology
- Chem
- Methods
- English

**Subsidy application**
Email: [sjaya_kumar@ymail.com](mailto:sjaya_kumar@ymail.com)  
Phone number: 0469747085  
Which course would you like to apply for? Select all that apply.: UCAT preparation course  
Which days are you available to meet for a subsidy interview? Select all that apply.: Saturday morning, Saturday afternoon, Sunday morning  
Why are you applying for the subsidy program?: To hopefully get a reduced price so i can send my son to tutoring for UCAT

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview
type append template
action Subsidy questions template
```

- Only one income - too many extracurriculars 
- Bills and mortgage 
- Four boys 
- $25/week 

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

