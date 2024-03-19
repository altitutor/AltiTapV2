---
Current: Current
Student_name: Parson
School: USC
SACE_or_IB: SACE
Subjects:
  - SACE English
  - SACE 12METH
  - SACE 12BIO
  - UCAT
Student_year_level:
  - Year 12
Student_email: parsonso.ps@gmail.com
Student_mobile: "0478540178"
Parent_name: Samuel So
Parent_email: samuelsyk.@gmail.com
Parent_mobile: +852 97775935
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Friday: Currently available
Thursday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: Currently available
Sunday_PM: Currently available
Sunday_AM: Currently available
---
Classes:: [[1.2 Classes/12METH D1.md|12METH D1]], [[1.2 Classes/UCAT C.md|UCAT C]], [[12BIO A4|12BIO A4]]

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
> [!Info] Trial session guide
![[1.2.1 Trial sessions#General format]]
### 1. How did you hear about us?
- Homestay family son girlfriend Ect jot
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: 12BIO, 12METH, 12EAL
- 
### 3. **Motivation** - why do you want tutoring?
- Get into dentistry, 
### 4.  What do you want to do after you leave school?
- Dentistry -> physiotherapy or OT as back-up
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- UCAT, 12BIO, 12METHODS, EAL
EAL sessions only for drafting
### 6. **Grades** - what grades are you currently on for each of these subjects?
- 11
	- bio -> A
	- Methods -> B+
	- English -> A-
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Bio: DNA + Protein => practical report right now
- Methods: Applications of calculus
- English -> advertisement
**School**
 University senior college



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


[Click to message student](sms:0478540178)

Hi Parson, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- 12METH Monday 4:15, starting on Monday, 11 March (today)
- UCAT Sunday 9:30am-12:30pm, starting Sunday 17 March

When you come in for Methods today, we can finalise the details of your biology classes, including scheduling a time that works for you and matching you with the right tutor.

I have also read through your English draft and it is looking very good. Well done!

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday Sunday, 17 March so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,
Samantha, Altitutor Admin