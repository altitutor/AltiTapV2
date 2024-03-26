---
Current: Current
School: St Peters College
SACE_or_IB: SACE
Subjects:
  - SACE 12METH
  - SACE 12BIO
Student_year_level:
  - Year 11
Student_email: Aisukich@outlook.com
Student_mobile: "+61433454787"
Parent_name: Lisa Tang
Parent_email: lisa_t94@hotmail.com
Parent_mobile: "+61426827749"
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Definitely unavailable
Saturday_PM: Currently available
Sunday_AM: Definitely unavailable
Sunday_PM: Currently available
Student_name: Alex Nguyen
---
Classes:: [[12METH A2|12METH A2]], [[12BIO A1|12BIO A1]]
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
	- 
2. **Motivation** - why do you want tutoring?
	- 
3.  What do you want to do after you leave school?
	- 
4. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- 
5. **Grades** - what grades are you currently on for each of these subjects?
	- 
6.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
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

[Click to message student](sms:+61433454787)

Hi Alex Nguyen, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- 12METH: 2:45 Saturday PM, starting on Saturday, 27 January
- 12BIO: 4:15 Thursday, starting on Thursday, 25 January

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 21 January so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin


```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

[Click to message parent](sms:+61426827749)

Hi Lisa Tang, 

This message is just to confirm that your child Alex Nguyen has registered to be a student with us at Altitutor. We have organised the following session times for them:

- 12METH: 2:45 Saturday PM, starting on Saturday, 27 January
- 12BIO: 4:15 Thursday, starting on Thursday, 25 January

Before Alex Nguyen’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get Alex Nguyen to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 21 January before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards, 
Altitutor Admin

