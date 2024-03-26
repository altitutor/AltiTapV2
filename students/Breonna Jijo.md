---
Student_name: Breonna Jijo
Current: Current
School: Marden Senior Colleg
Student_year_level: Year 12
Student_email: breonnajijo2@gmail.com
Student_mobile: 61478474815
Parent_name: Jijo George
Parent_email: jijocherumuzhi@yahoo.co.in
Parent_mobile: 61401947786
Monday: Currently available
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Currently available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
SACE_or_IB: SACE
Subjects:
  - SACE 12BIO
  - SACE 12CHEM
  - SACE 12BIO
  - SACE 12CHEM
---

Classes:: [[12BIO A4|12BIO A4]], [[12CHEM B2|12CHEM B2]]

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

Coming in with David Shibu

### 1. How did you hear about us?
- DS; Friend - Jayden Nguyen
- BJ; David
### 2. **Student details** - year level, school, subjects
- DS; Year 12 Adelaide - General Eng, Method, Physics, Chem, Accounting
- BJ; Marden Stage 2 - General Eng , Chem, Bio, Essential
### 3. **Motivation** - why do you want tutoring?
- DS; Good grade
- BJ; Good grades
### 4.  What do you want to do after you leave school?
- DS; Dentistry
- BJ; Dentistry
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- DS; Methods, Physics and Chem
- BJ; Chem, Bio maybe, Essential MAYBE
### 6. **Grades** - what grades are you currently on for each of these subjects?
- DS; Straights As // 100% A+
- BJ; Bio A, Chem B, Maths A, Eng A // A+s
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- DS; Maths Diff Calc Started Chain, physics projectile motion
- BJ; Don't know, Chem greenhouse TOPIC 1, Bio DNA proteins

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


[Click to message student](sms:61478474815)

Hi Breonna Jijo

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- SACE 12BIO Monday 4:15, starting on Monday, 19 February
- SACE 12CHEM Wednesday 4:15, starting on Wednesday, 21 February
Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 18 February so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards

Altitutor Admin

[Click to message parent](sms:61401947786)

Hi Jijo George

This message is just to confirm that your child Breonna Jijo has registered to be a student with us at Altitutor. We have organised the following session times for them:

- SACE 12BIO Monday 4:15, starting on Monday, 19 February
- SACE 12CHEM Wednesday 4:15, starting on Wednesday, 21 February

Before Breonna Jijo’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get Breonna Jijo to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 18 February before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards 
Altitutor Admin