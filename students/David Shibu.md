---
SACE_or_IB: SACE
Student_name: David Shibu
Current: Current
School: Adelaide High School
Student_year_level: Year 12
Student_email: david.shibu6769@gmail.com
Student_mobile: 61481353578
Parent_name: Shibu Joseph
Parent_email: shibujmavelil@yahoo.co.in
Parent_mobile: 61425530525
Monday: Definitely unavailable
Tuesday: Currently available
Wednesday: Currently available
Thursday: Currently available
Friday: Definitely unavailable
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Currently available
Sunday_PM: Definitely unavailable
Subjects:
  - SACE 12PHYS
  - SACE 12CHEM
  - SACE 12METH
---

Classes:: [[1.2 Classes/12CHEM A1.md|12CHEM A1]], [[12METH D1|12METH D1]], [[12PHYS D1|12PHYS D1]]

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

Coming in with Breonna Jijo
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


[Click to message student](sms:61481353578)



[Click to message parent](sms:61425530525)

Hi Shibu Joseph, 

This message is just to confirm that your child David Shibu has registered to be a student with us at Altitutor. We have organised the following session times for them:

- SACE 12PHYS Thursday 4:15, starting on Thursday, 22 February
- SACE 12METH Thursday 5:45, starting on Thursday, 22 February
- SACE 12CHEM Wednesday 4:15, starting on Wednesday, 21 February

Before David Shibu’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get David Shibu to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 18 February before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin