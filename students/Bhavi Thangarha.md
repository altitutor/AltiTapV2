---
SACE_or_IB: SACE
Student_name: Bhavi Thangaraj
Current: Past
School: Glenunga
Student_year_level: Year 11
Student_email: bhavithangaraj14@gmail.com
Student_mobile: 61424962116
Parent_name: Menaka Thangaraj
Parent_email: menakathangaraj2005@gmail.com
Parent_mobile: 61452605722
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - UCAT
---
Classes:: 
```button
name Insert student details
type line(100) template
action Student details template
```
> [!Abstract]+ Session history
> ## Absences
> ```dataview
> table Subject, Absence_date AS Date, Absence_reason AS Reason
> from "1.4 Admin logs/Absences - planned" OR "1.4 Admin logs/Absences - unexplained"
> where icontains(file.name,"Bhavi Thangarha")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Bhavi Thangarha")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Bhavi Thangarha")
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,"Bhavi Thangarha")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Bhavi Thangarha")
> 



## Trial session questions to ask
### 1. How did you hear about us?
- Friends from school told her
### 2. **Student details** - year level, school, subjects
- Year level: 11
- Subjects: Bio, Chem, General Math, English, Nutrition, UCAT
### 3. **Motivation** - why do you want tutoring?
- Learn how to do the UCAT before next year
- 
### 4.  What do you want to do after you leave school?
- Medicine
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- UCAT
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
type line (1000) template
action MESSAGE - class times student
```



```button
name Generate parent message
type line (1000) template
action MESSAGE - class times parent
```



[Click to message student](sms:61424962116)

Hi Bhavi Thangaraj

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:


Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 11 February so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards

Altitutor Admin

[Click to message parent](sms:61452605722)

Hi Menaka Thangaraj

This message is just to confirm that your child Bhavi Thangaraj has registered to be a student with us at Altitutor. We have organised the following session times for them:



Before Bhavi Thangaraj’s first session, please add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/

We’ll get Bhavi Thangaraj to come to homework help anytime on between 1pm-4pm on Sunday Sunday, 11 February before their first session so we can catch them up on content.

Kindly note that we have implemented a 24-hour policy for managing absences. If your child is unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for your child. In the event rescheduling is not feasible, we will credit your account accordingly.

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kind regards 
Altitutor Admin