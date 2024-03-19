---
SACE_or_IB: SACE
Student_name: Maddison Jeffrey
Current: Current
School: Muirden Senior Colle
Student_year_level: Year 11
Student_email: mjeffrey4u@outlook.com
Student_mobile: 61452603279
Parent_name: Megan Jeffrey
Parent_email: mjeffrey4u@outlook.com
Parent_mobile: 61452614017
Monday: Currently available
Tuesday: Currently available
Wednesday: Currently available
Thursday: Definitely unavailable
Friday: Currently available
Saturday_AM: Currently available
Saturday_PM: I can make myself available
Sunday_AM: I can make myself available
Sunday_PM: I can make myself available
Subjects:
  - SACE English
  - SACE 11BIO
  - SACE 11CHEM
  - SACE 11METH
Subsidy: $25 per subject
---
Classes:: [[1.2 Classes/11BIO A1.md|11BIO A1]], [[1.2 Classes/11METH B2.md|11METH B2]], [[1.2 Classes/11CHEM A1.md|11CHEM A1]], [[1.2 Classes/11ENG B2.md|11ENG B2]]

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
- Through a friend referral (Diya)
### 2. **Student details** - year level, school, subjects
- Year 11
- Chemistry, Bio, Methods, English General (+ UCAT later on) + AIF (RP)
### 3. **Motivation** - why do you want tutoring?
- Get better grades to get into medicine 
### 4.  What do you want to do after you leave school?
- Medicine 
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Chemistry, Bio, Methods, English General (+ UCAT later on)
- **Do English every week (not per drafting)**
### 6. **Grades** - what grades are you currently on for each of these subjects?
- Chemistry - B/A
- Biology - B/A
- English - B
- Methods - B
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- Chemistry - Types of Materials 
- Methods - Statistics folio - but starting functions to graphs (non-calc) 
- English - Ladybird movie 
- Biology - Osmosis (+ design and deconstruct)

Subsidy Stuff
Name of student applying: Maddison Jeffrey  
Email: [mjeffrey4u@outlook.com](mailto:mjeffrey4u@outlook.com)  
Phone number: 0452603279  
Which course would you like to apply for? Select all that apply.: SACE Mathematical Methods, SACE Chemistry, SACE Biology, SACE English General, UCAT preparation course, Medicine interview course  
Which days are you available to meet for a subsidy interview? Select all that apply.: Monday, Wednesday, Friday  
Why are you applying for the subsidy program?: I come from a low income family and want to be the first to graduate from high school and first to go to university! I want to be a radiologist and I used to be a gifted child who burnt out very quickly, now, I’m serious about my studies and I’m dropping behind in my maths and need to get ahead in other subjects :)) I’m really in need of tutoring and work a part time job but recently it’s been super hard due to school so I’m applying from this grant - my family is on centrelink and my mother is mentally sick - my dad is working outer state but doesn’t make much to cover my whole family - I hope to see you if i get the interview!

- Income - one shift a week, Centrelink, dad working outer state (parents are financially separated)

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


[Click to message student](sms:61452603279)

Hi Maddison Jeffrey, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- SACE English Monday 5:45, starting on Monday, 4 March 
- SACE 11CHEM Saturday AM 9:30, starting on Saturday, 9 March
- SACE 11METH Saturday AM 11:00, starting on Saturday, 9 March
- SACE 11BIO PM 2:45, starting on Saturday, 9 March

Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin