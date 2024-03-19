---
Subjects:
  - SACE 12METH
Current: Potential
---

Classes:: [[12METH B1|12METH B1]]

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
- Friend comes here
### 2. **Student details** - year level, school, subjects
- 12
- Mercedes
- Physics Methods Accounting Chem Spirituality VET
### 3. **Motivation** - why do you want tutoring?
- Engineering
- Wants to do well in phys and methods
### 4.  What do you want to do after you leave school?
- Engineering
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Physics
- Methods
### 6. **Grades** - what grades are you currently on for each of these subjects?
- RP B+
- Methods As
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Physics - just started 1.3
- Methods - Calculus (halfway through chapter 2)f

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


[Click to message student](sms:undefined)

Hi there, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- SACE 12METH Monday 5:45, starting on Monday, 18 March

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin

[Click to message parent](sms:undefined)

Hi undefined, 

This message is just to confirm that your child undefined has registered to be a student with us at Altitutor. We have organised the following session times for them:

- SACE 12METH Monday 5:45, starting on Monday, 18 March

Before undefined’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get undefined to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 17 March before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin