---
SACE_or_IB: SACE
Student_name: Charlotte Chung
Current: Current
School: Scotch college
Student_year_level: Year 11
Student_email: cchung2505@gmail.com
Student_mobile: 61478925058
Parent_name: Jing Lim
Parent_email: miloholic79@hotmail.com
Parent_mobile: 61421218083
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Currently available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
Subjects:
  - SACE 11METH
  - UCAT
---
Classes:: [[1.2 Classes/11METH A2.md|11METH A2]], [[UCAT B|UCAT B]]
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
- 
### 2. **Student details** - year level, school, subjects
- Year level: 11
- Subjects: Methods
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

[Click to message student](sms:61478925058)

Hi Charlotte Chung, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- 11METH: 1:15 Saturday PM, starting on Saturday, 3 February

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 28 January so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

[Click to message parent](sms:61421218083)

Hi Jing, 

This message is just to confirm that your child Charlotte Chung has registered to be a student with us at Altitutor. We have organised the following session times for them:

- 11METH: 1:15 Saturday PM, starting on Saturday, 3 February

Before Charlotte Chung’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin


