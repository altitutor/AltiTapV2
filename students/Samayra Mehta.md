---
SACE_or_IB: 
Student_name: Samayra Mehta
Current: Current
School: Cedar College
Student_year_level: Year 11
Student_email: samayramehta9@gmail.com
Student_mobile: +61480365692
Parent_name: Rahul Mehta
Parent_email: rahul_mehta@live.com.au
Parent_mobile: +61410809287
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: Currently available
Friday: Currently available
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - UCAT
---

Classes:: [[UCAT B|UCAT B]]

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
- Friend
### 2. **Student details** - year level, school, subjects
- Y11
- Bio Chem Methods Legal English RP
### 3. **Motivation** - why do you want tutoring?
- Wants to do med
### 4.  What do you want to do after you leave school?
- Med
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- UCAT
- Methods
- Chem
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Mostly As
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Methods - unit circle and radians
- Chem - topic 1

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


[Click to message student](sms:61480365692)

Hi Samayra Mehta, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- UCAT Sunday AM 9:30, starting on Sunday, 25 February
Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 25 February so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin

[Click to message parent](sms:61410809287)

Hi Rahul Mehta, 

This message is just to confirm that your child Samayra Mehta has registered to be a student with us at Altitutor. We have organised the following session times for them:

- UCAT Sunday AM 9:30, starting on Sunday, 25 February

Before Samayra Mehta’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get Samayra Mehta to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 25 February before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin