---
Student_name: Marissa Tee
Current: Current
School: Wilderness
Student_year_level: Year 11
Student_email: mezzytt07@gmail.com
Student_mobile: 61481905349
Parent_name: Olivia Chen
Parent_email: oliviayychen@gmail.com
Parent_mobile: 61401768916
Monday: Definitely unavailable
Tuesday: Currently available
Wednesday: Definitely unavailable
Thursday: Currently available
Friday: Definitely unavailable
Saturday_AM: I can make myself available
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
SACE_or_IB: SACE
Subjects:
  - SACE 11CHEM
---
Classes:: [[11CHEM A13|11CHEM A13]]
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
### 1. How did you hear about us?
- Just googling and then found our website 
### 2. **Student details** - year level, school, subjects
- Year level: 11
- Subjects: Biology, physics, chemistry
### 3. **Motivation** - why do you want tutoring?
- Better grades
### 4.  What do you want to do after you leave school?
- Either physics or psychology 
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Put into a year 12 bio class (not year 11)
### 6. **Grades** - what grades are you currently on for each of these subjects?
- As/A+s in Year 10
- She already did Stage 2 Biology in Year 10 but is going to do it again this year 
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Topic 1 for all of them (most likely)
- 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview
type append template
action Subsidy questions template
```


# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```

[Click to message student](sms:61481905349)

Hi Marissa

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- 11PHYS: 1:15 Saturday PM, starting on Saturday, 3 February
- 11CHEM: 5:45 Thursday, starting on Thursday, 1 February
- 12BIO: 4:15 Thursday, starting on Thursday, 1 February

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards
Altitutor Admin



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

