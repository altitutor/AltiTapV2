---
SACE_or_IB: SACE
Student_name: Chantelle Hill
Current: Current
School: Adelaide University
Student_year_level:
  - Year 12
Student_email: chantellejh1@gmail.com
Student_mobile: 61448736057
Parent_name: Chantelle Hill
Parent_email: chantellejh1@gmail.com
Parent_mobile: 61448736057
Monday: I can make myself available
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: I can make myself available
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - UCAT
Subsidy: $40 per subject
---
Classes:: [[UCAT C|UCAT C]]
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
> where icontains(file.name,"Chantelle Hill")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Chantelle Hill")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Chantelle Hill")
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,"Chantelle Hill")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Chantelle Hill")
> 



## Trial session questions to ask
### 1. How did you hear about us?
- Through Google 
- Knows Matt 
### 2. **Student details** - year level, school, subjects
- Year level: Undergrad 
- Subjects: UCAT
- 
### 3. **Motivation** - why do you want tutoring?
- Trying to get into dentistry so trying to get her GPA up 
### 4.  What do you want to do after you leave school?
- Dentistry
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- UCAT 
### 6. **Grades** - what grades are you currently on for each of these subjects?
- 
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- UCAT

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview
type append template
action Subsidy questions template
```

Name of student applying: Chantelle Hill  
Email: [chantellejh1@gmail.com](mailto:chantellejh1@gmail.com)  
Phone number: 0448736057  
Which course would you like to apply for? Select all that apply.: UCAT preparation course  
Which days are you available to meet for a subsidy interview? Select all that apply.: Monday  
Why are you applying for the subsidy program?: Struggling to afford cost of tuition as most of my money is used on rent, food, bills, etc. but would like to receive support to succeed in the UCAT.

- Not living at home
- Work casual 
- Struggle to have $50 by the end of each pay period 
- Groceries, rent, bills, petrol - need to pay for these herself 
- **$40/week (UCAT)** 

# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```

Hi Chantelle,

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- UCAT: Sundays from 9:30am - 12:30pm (starting 18 February)

Before your first session, please do the following things:

Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
Download our app by searching "Altitutor" in the app store / play store
Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842).

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,
Samantha

```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

