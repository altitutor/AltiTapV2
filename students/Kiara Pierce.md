---
Student_name: Kiara Pierce
Current: Current
School: Mercedes college
Student_year_level: Year 12
Student_email: kpierce1211@gmail.com
Student_mobile: 61452570903
Parent_name: Pippa Pierce
Parent_email: pipskijo@gmail.com
Parent_mobile: 61477753628
Monday: Currently available
Tuesday: I can make myself available
Wednesday: Currently available
Thursday: Currently available
Friday: I can make myself available
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: Currently available
SACE_or_IB: SACE
Subjects:
  - SACE 12METH
  - SACE 12CHEM
---
Classes:: [[1.2 Classes/UCAT A.md|UCAT A]], [[1.2 Classes/12BIO A2.md|12BIO A2]]
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
- Brother did it
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: Methods and UCAT, Nutrition, health and English
### 3. **Motivation** - why do you want tutoring?
- UCAT: Prep for UCAT
- Methods: High ATAR
### 4.  What do you want to do after you leave school?
- Medicine
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Methods and UCAT
### 6. **Grades** - what grades are you currently on for each of these subjects?
- 1st Sem B-
- 2nd Sem C+
- A for the folio in Year 11
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Has lesson plan for the year

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

[Click to message student](sms:61452570903)

Hi Kiara Pierce, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- 12METH: 5:45 Monday, starting on Monday, 5 February
- UCAT: 9:30 Sunday AM, starting on Sunday, 4 February

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 4 February so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

[Click to message parent](sms:undefined)

Hi undefined, 

This message is just to confirm that your child undefined has registered to be a student with us at Altitutor. We have organised the following session times for them:

- 12METH: 5:45 Monday, starting on Monday, 5 February
- UCAT: 9:30 Sunday AM, starting on Sunday, 4 February

Before undefined’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get undefined to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 4 February before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin

