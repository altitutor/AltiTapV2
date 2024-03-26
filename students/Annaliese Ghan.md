---
Student_name: Annaliese Ghan
Current: Current
School: Pembroke
Student_year_level: Year 9
Student_email: annaliese.g09@gmail.com
Student_mobile: 61490331126
Parent_name: Caroline De Sousa
Parent_email: cazdesousa@icloud.com
Parent_mobile: 61403503582
Monday: Definitely unavailable
Tuesday: Currently available
Wednesday: Currently available
Thursday: I can make myself available
Friday: I can make myself available
Saturday_AM: Definitely unavailable
Saturday_PM: I can make myself available
Sunday_AM: Definitely unavailable
Sunday_PM: I can make myself available
SACE_or_IB: SACE
Subjects:
  - PreSACE Maths
Subsidy: $40
---
Classes:: [[1.2 Classes/10MATH A1.md|10MATH A1]]
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
> where icontains(file.name,"Annaliese Ghan")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Annaliese Ghan")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Annaliese Ghan")
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,"Annaliese Ghan")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Annaliese Ghan")
> 



## Trial session questions to ask
### 1. How did you hear about us?
- sibling came here
### 2. **Student details** - year level, school, subjects
- yr 9
- pembroke
### 3. **Motivation** - why do you want tutoring?
- med
### 4.  What do you want to do after you leave school?
- med
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- 10A maths
### 6. **Grades** - what grades are you currently on for each of these subjects?
- A/A-
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview
type append template
action Subsidy questions template
```

Name of student applying: Annaliese Ghan  
Email: [cazdesousa@icloud.com](mailto:cazdesousa@icloud.com)  
Phone number: 0403503582  
Which course would you like to apply for? Select all that apply.: Pre-SACE Mathematics  
Why are you applying for the subsidy program?: From my parents:  
Siblings enrolled into multiple subjects so we are seeking a multi-enrolment deduction please.

Impromptu subsidy interview - no email available


### Interview

1. **About** - tell me about yourself and your family
    - Mum of 3
    - Noah, Annaliese and a younger kid (Y4)
    - Wants to increase number of subjects as the year progresses
    - Also wants to sign Y4 kid up for tutoring
1. **Income** - what are all of the income sources for your family?
    - Parents
2. **Expenses** - what are all the sources of expenses for your family?
    - School, living expenses...
3. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
	- Mum negotiated $40 per session FINAL


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

