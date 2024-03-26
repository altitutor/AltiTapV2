---
SACE_or_IB: SACE
Student_name: Katerina Antonas
Current: Current
School: The Heights School
Student_year_level: Year 12
Student_email: katerinaantonas06@gmail.com
Student_mobile: +61456190394
Parent_name: Mary Antonas
Parent_email: marybantonas@gmail.com
Parent_mobile: +61407559392
Monday: Currently available
Tuesday: Definitely unavailable
Wednesday: Currently available
Thursday: Definitely unavailable
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
Subjects:
  - SACE 12SPEC
  - SACE 12METH
---

Classes:: [[12SPEC A1|12SPEC A1]], [[12METH B1|12METH B1]]

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
- Through friends, Ajin, Nishtha
### 2. **Student details** - year level, school, subjects
- Year 12
- The Heights
- Methods, Spec, Visual Art
- Last years: Physics, English Lit
### 3. **Motivation** - why do you want tutoring?
- Get a good ATAR - to get into Engineering
### 4.  What do you want to do after you leave school?
- Engineering - Aerospace, Astrophysics
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Methods and Spec
### 6. **Grades** - what grades are you currently on for each of these subjects?
- A's and a few B's
- Spec topics were a bit difficult
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Methods - Calculus
- Spec - Finishing Induction

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


[Click to message student](sms:61456190394)

Hi Katerina Antonas, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- SACE 12SPEC Monday 4:15, starting on Monday, 19 February
- SACE 12METH Monday 5:45, starting on Monday, 19 February
Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 18 February so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin

[Click to message parent](sms:61407559392)

Hi Mary Antonas, 

This message is just to confirm that your child Katerina Antonas has registered to be a student with us at Altitutor. We have organised the following session times for them:

- SACE 12SPEC Monday 4:15, starting on Monday, 19 February
- SACE 12METH Monday 5:45, starting on Monday, 19 February

Before Katerina Antonas’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get Katerina Antonas to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 18 February before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin