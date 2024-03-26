---
Student_name: Saira Ali qasemy
Current: Current
School: OLSH
Student_year_level:
  - Year 10
Student_email: sairaqasemy@gmail.com
Student_mobile: 61417660801
Parent_name: Zahra Ali qasemy
Parent_email: zahraaliqasemy@yahoo.com.au
Parent_mobile: 61450872357
Monday: Currently available
Tuesday: Definitely unavailable
Wednesday: Currently available
Thursday: I can make myself available
Friday: I can make myself available
Saturday_AM: Definitely unavailable
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: I can make myself available
SACE_or_IB: PreSACE
Subjects:
  - PreSACE Maths
  - PreSACE English
Subsidy: $10
---
Classes:: [[1.2 Classes/10ENG.md|10ENG]], [[1.2 Classes/10MATH A1.md|10MATH A1]]
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
	- Year level: 9
	- Subjects: maths, english, psych, business, arts, outdoor ed
	- OLSH
2. **Motivation** - why do you want tutoring?
	- Improve grades
1.  What do you want to do after you leave school?
	- Uncertain about career path, leaning towards university
2. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
	- Maths, english
3. **Grades** - what grades are you currently on for each of these subjects?
	- Bs
	- Up and down
	- Hoping to get to A level
	- Assignments is main struggle
1.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
	- Data collecting and graphs, measurement

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview questions
type command
action QuickAdd: Insert subsidy interview questions
```

## Subsidy
### Application email
Name of student applying: Saira Ali qasemy 
Email: sairaqasemy@gmail.com 
Phone number: 0417660801 
Which course would you like to apply for? Select all that apply.: Pre-SACE Mathematics, Pre-SACE English 
Why are you applying for the subsidy program?: Within the last year, my younger brother and I both had surgeries that was paid for by our family. Both surgeries was done by private surgeons without concession.

### Interview
1. **About** - tell me about yourself and your family
	- From Afghanistan, arrived in 2015, moved because the country isn't safe
	- 4 kids, all at school
	- Husband works in construction, moved in 2011
	- Mum Zahra is a stay at home mum, was a language teacher in Afghanistan
	- Own the house they're living in, Mortgage 
1. **Income** - what are all of the income sources for your family?
	- Husband's salary 
2.  **Expenses** - what are all the sources of expenses for your family?
	- Mortgage, bills
	- School fees - 9-10k/year
	- Son's tuition - 500/year
	- Daughter kindy - 40/term
	- Son had an ear operation
	- Saira had teeth surgery last year + braces + dental etc
1. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
	- $10 per subject = $6.67/hour for ALL subjects 



# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```

[Click to message student](sms:61417660801)

Hi Saira Ali qasemy, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

- Class time, day, or subject not found
- Class time, day, or subject not found

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

