---
Student_name: Ajin Lee
Current: Current
School: The Heights School
Student_year_level:
  - Year 12
Student_email: ajin5016@gmail.com
Student_mobile: 61424262127
Parent_name: Jaehyuk LEE
Parent_email: xxhyuk@hotmail.com
Parent_mobile: 61403716394
Monday: Currently available
Tuesday: Definitely unavailable
Wednesday: I can make myself available
Thursday: I can make myself available
Friday: I can make myself available
Saturday_AM: Definitely unavailable
Saturday_PM: Currently available
Sunday_AM: Currently available
Sunday_PM: Currently available
SACE_or_IB: SACE
Subjects:
  - SACE 12PHYS
  - SACE 12METH
  - SACE 12SPEC
---
Classes:: [[1.2 Classes/12PHYS A1.md|12PHYS A1]], [[1.2 Classes/12METH A4.md|12METH A4]], [[1.2 Classes/12SPEC A1.md|12SPEC A1]]
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
1. **Student details** - year level, school, subjects 
	- Year level: 11
	- Subjects: Stage 2 Chemistry
	- 
2. **Motivation** - why do you want tutoring?
	- 
3.  What do you want to do after you leave school?
	- 
4. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 12CHEM
5. **Grades** - what grades are you currently on for each of these subjects?
	- 
6.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- Finishing off topic 3

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

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



[Click to message student](sms:61424262127)

Hi Ajin Lee, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- SACE 12PHYS Monday 5:45, starting on Monday, 12 February
- SACE 12SPEC Thursday 5:45, starting on Thursday, 8 February
- SACE 12METH Saturday AM 9:30, starting on Saturday, 10 February
Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 11 February so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin

[Click to message parent](sms:61403716394)

Hi Jaehyuk LEE, 

This message is just to confirm that your child Ajin Lee has registered to be a student with us at Altitutor. We have organised the following session times for them:

- SACE 12PHYS Monday 5:45, starting on Monday, 12 February
- SACE 12SPEC Thursday 5:45, starting on Thursday, 8 February
- SACE 12METH Saturday AM 9:30, starting on Saturday, 10 February

Before Ajin Lee’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get Ajin Lee to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 11 February before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin

[Click to message student](sms:61424262127)

Hi Ajin Lee, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- SACE 12PHYS Monday 5:45, starting on Monday, 12 February
- SACE 12SPEC Thursday 5:45, starting on Thursday, 8 February
- SACE 12METH Saturday AM 9:30, starting on Saturday, 10 February
Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 11 February so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin

[Click to message student](sms:61424262127)

Hi Ajin Lee, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- SACE 12PHYS Monday 5:45, starting on Monday, 12 February
- SACE 12SPEC Thursday 5:45, starting on Thursday, 8 February
- SACE 12METH Saturday AM 9:30, starting on Saturday, 10 February
Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 11 February so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin

[Click to message parent](sms:61403716394)

Hi Jaehyuk LEE, 

This message is just to confirm that your child Ajin Lee has registered to be a student with us at Altitutor. We have organised the following session times for them:

- SACE 12PHYS Monday 5:45, starting on Monday, 12 February
- SACE 12SPEC Thursday 5:45, starting on Thursday, 8 February
- SACE 12METH Saturday AM 9:30, starting on Saturday, 10 February

Before Ajin Lee’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get Ajin Lee to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 11 February before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin