---
SACE_or_IB: SACE
Student_name: Jia Wang
Current: Current
School: Mercedes College
Student_year_level: Year 11
Student_email: lachlan.wang2008@gmail.com
Student_mobile: 61420923016
Parent_name: Yuan Lu
Parent_email: luxinqiding@gmail.com
Parent_mobile: 61423403663
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Currently available
Friday: Currently available
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Currently available
Sunday_PM: Currently available
Subjects:
  - SACE 12BIO
  - SACE 12METH
Subsidy: $20 per subject
---
Classes:: [[12METH A3|12METH A3]], [[1.2 Classes/12BIO A1.md|12BIO A1]]
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
> where icontains(file.name,"Jia Wang")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Jia Wang")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Jia Wang")
> ```
> 
> ## Subject registrations
> ```dataview
> table Subject, Start_date_for_this_subject AS "Start date"
> from "1.4 Admin logs/New students"
> where icontains(file.name,"Jia Wang")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Jia Wang")
> 



## Trial session questions to ask
### 1. How did you hear about us?
- Through GRIP - knows Matt
### 2. **Student details** - year level, school, subjects
- Year level: 12
- Subjects: Methods, Chem, Bio, English
- 
### 3. **Motivation** - why do you want tutoring?
- Wants to get better grades for med 
### 4.  What do you want to do after you leave school?
- Medicine or dentistry
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- Year 12 Bio and methods
### 6. **Grades** - what grades are you currently on for each of these subjects?
- A/A+
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- 12BIO (DNA and Proteins - Week 8) 
- 
- 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview
type append template
action Subsidy questions template
```
Name of student applying: Jia Wang  
Email: [lachlan.wang2008@gmail.com](mailto:lachlan.wang2008@gmail.com)  
Phone number: 0420923016  
Which course would you like to apply for? Select all that apply.: SACE Mathematical Methods, SACE Chemistry, SACE Biology, SACE English General  
Which days are you available to meet for a subsidy interview? Select all that apply.: Thursday, Friday, Sunday morning, Sunday afternoon  
Why are you applying for the subsidy program?: I'm currently caught in a tough spot where my parents have split, and most of the money for my extracurricular stuff comes from my mother. This has really affected our financial status. Dad's also out of work and we're all on a concession card, and currently under centre link carer concession. On top of that, my parents are juggling the care of both sets of grandparents, making sure they're happy and healthy. Even with all that on our plate, I'd be very grateful for a shot at joining your school. Getting to learn there would mean the world to me. I want to understand things better so I can chase my dream of becoming a dentist or a doctor, and hopefully make things easier for my family down the line. In return I hope I can help provide more support to the children similar to my current situation in the future.

Subjects: Methods, Biology 

Subsidy:
- Parents aren't together (mum only pays for extracurricular)
- Mum is a librarian 

$20.00 per subject ($40.00 for two subjects)

Thursday 4.15pm - 12BIO with Justin Le
Thursday 5.45pm - 12METH with Yuhan 
# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```

