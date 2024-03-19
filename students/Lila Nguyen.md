---
SACE_or_IB: SACE
Student_name: Lila Nguyen
Current: Current
School: St Peter’s Girls
Student_year_level: Year 11
Student_email: lila2503@icloud.com
Student_mobile: 61431938877
Parent_name: Phuong Truong
Parent_email: atruong07@gmail.com
Parent_mobile: 61401002079
Monday: Definitely unavailable
Tuesday: I can make myself available
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: I can make myself available
Sunday_PM: I can make myself available
Subjects:
  - SACE English
  - SACE 11CHEM
  - SACE 12BIO
  - UCAT
Subsidy: ---
SACE_or_IB: SACE
Student_name: Lila Nguyen
Current: Current
School: St Peter’s Girls
Student_year_level: Year 11
Student_email: lila2503@icloud.com
Student_mobile: 61431938877
Parent_name: Phuong Truong
Parent_email: atruong07@gmail.com
Parent_mobile: 61401002079
Monday: Definitely unavailable
Tuesday: I can make myself available
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: I can make myself available
Sunday_PM: I can make myself available
Subjects:
  - SACE English
  - SACE 11CHEM
  - SACE 12BIO
Subsidy: $100 for three subjects
---00 for three subjects
---
Classes:: [[1.2 Classes/11ENG A1.md|11ENG A1]], [[1.2 Classes/11CHEM A1.md|11CHEM A1]], [[11BIO A1|11BIO A1]], [[UCAT C|UCAT C]]


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



# Subsidy
## Application email
asdfasdf

## Subsidy interview
### 1. **About** - tell me about yourself and your family
- 
### 2. **Income** - what are all of the income sources for your family?
- 
### 3. **Expenses** - what are all the sources of expenses for your family?
- 
### 4. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
- 

# Trial session
### 1. How did you hear about us?
- Matthew Chua from GRIP
### 2. **Student details** - year level, school, subjects
- Year level: 11
- Subjects: Chemistry, Biology and English
- 
### 3. **Motivation** - why do you want tutoring?
- See if this tutoring place suits her 
- Improve grades
### 4.  What do you want to do after you leave school?
- Med or dentistry 
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Chemistry, Biology and English
- 12BIO, 11CHEM and 11ENGLISH 
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Science - average (in year 10)
- English - not too great 
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Not started the school year yet
- Doing 12BIO at Marden 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview
type append template
action Subsidy questions template
```

## Subsidy
### Application email

Name of student applying: Lila Nguyen  
Email: [lila2503@icloud.com](mailto:lila2503@icloud.com)  
Phone number: 0431938877  
Which course would you like to apply for? Select all that apply.: SACE Chemistry  
Why are you applying for the subsidy program?: I am extremely keen to attend your tuition, however the total amount for 3 subjects that I require assistance is quite expensive for my parents as I have two other siblings who are currently at school. Any form of discount would be much appreciated.  
  
Thank you for your consideration   
  
Lila Nguyen

### Interview
1. **About** - tell me about yourself and your family
	- Family of five (two parents + three children)
	- Very keen to start tutoring with us
1. **Income** - what are all of the income sources for your family?
	- Parents work full-time
2.  **Expenses** - what are all the sources of expenses for your family?
	- Three kids (their tuition fee for school; and other associated expenses)
3. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
	- $100 for three subjects
	- Can do ($40, $40, $20 on stripe?) Just make sure to credit $33.3 for each subject if she is absent) 



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
