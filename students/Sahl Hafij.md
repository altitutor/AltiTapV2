---
SACE_or_IB: PreSACE
Student_name: Sahl Tajdeed Bin Hafij
Current: Current
School: Marryatville high
Student_year_level: Year 10
Student_email: rumakhanam1981@gmail.com
Student_mobile: 61474443907
Parent_name: Ruma Khanam
Parent_email: ruma_hafij@yahoo.com
Parent_mobile: 61474443907
Monday: Definitely unavailable
Tuesday: Definitely unavailable
Wednesday: Definitely unavailable
Thursday: Definitely unavailable
Friday: Definitely unavailable
Saturday_AM: Currently available
Saturday_PM: Definitely unavailable
Sunday_AM: Definitely unavailable
Sunday_PM: Definitely unavailable
Subjects:
  - PreSACE English
  - PreSACE Science
  - SACE 11METH
Subsidy: $10 per subject
---
Classes:: [[1.2 Classes/11METH B2.md|11METH B2]], [[1.2 Classes/10SCI A1.md|10SCI A1]]
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
> where icontains(file.name,"Hafij Ullah")
> ```
> 
> ## Meetings
> ```dataview
> table Meeting_type AS "Meeting type", Meeting_date AS Date, Meeting_time as Time
> from "1.4 Admin logs/Meetings" 
> where icontains(file.name,"Hafij Ullah")
> ```
> 
> ## English drafting sessions
> ```dataview
> table Date_of_session AS Date, Time_of_session AS Time
> from "1.4 Admin logs/English drafting sessions"
> where icontains(file.name,"Hafij Ullah")
> ```
> 
> ## Permanent class changes
> ```dataview
> table Subject, Old_class_date AS "Old class date", New_class_date AS "New class date", New_class_time as "New class time"
> from "1.4 Admin logs/Permanent class changes"
> where icontains(file.name,"Hafij Ullah")
> ```


## Trial session questions to ask
### 1. How did you hear about us?
- 
### 2. **Student details** - year level, school, subjects
- Year level: 10
- Subjects: 11 Methods (accelerated student), English and Science
- 
### 3. **Motivation** - why do you want tutoring?
- Wants to get a grasp on the curriculum (came to Aus from England)
### 4.  What do you want to do after you leave school?
- Computer science
### 5. **Subjects** - which subjects would you get tutoring for if you came to Altitutor?
- As above
### 6. **Grades** - what grades are you currently on for each of these subjects?
- On A's at the moment
### 7.  **Topic** - which topic are you up to for each of these subjects? Which topic(s) have you completed already?
- 

> [!Info]- Trial session guide
![[1.2.1 Trial sessions#General format]]

```button
name Insert subsidy interview
type append template
action Subsidy questions template
```

## Subsidy
### Application email

Name of student applying: Sahl Tajdeed Bin Hafij  
Email: [rumakhanam1981@gmail.com](mailto:rumakhanam1981@gmail.com)  
Phone number: 0474443907  
Which course would you like to apply for? Select all that apply.: SACE Mathematical Methods, SACE Physics, SACE Chemistry, SACE Biology, SACE English General, SACE English Literature  
Why are you applying for the subsidy program?: His mum is currently unemployed and dad is the only working person in the family of five. So it would be very difficult for him to pay the full fees for Maths, Science and English. It would be greatly appreciated if you consider Sahl a new student with subsidised fees.
### Interview
1. **About** - tell me about yourself and your family
	- Sahl has other two sisters 
	- Mum is not working 
1. **Income** - what are all of the income sources for your family?
	- Only dad's income
2.  **Expenses** - what are all the sources of expenses for your family?
	- Mortgage (high interest rates)
3. **Subsidy level** - how much can you afford to pay for tutoring (per class)?
	- $30.00 a week ($10.00/per subject)



# Messages
```button
name Generate student message
type append template
action MESSAGE - new student message
```

[Click to message student](sms:<% tp.frontmatter.Student_mobile %>)

Hi <% tp.frontmatter.Student_name %>, 

Thank you for registering to be a student with us at Altitutor. We have organised the following session times for you:

<%*
// Function to calculate the next available class date
function getNextClassDate(dayNumber, dayFormatted) {
    const dayOfWeekMap = {
        '1': 1, // Monday
        '2': 2, // Tuesday
        '3': 3, // Wednesday
        '4': 4, // Thursday
        '5': 5, // Friday
        '6': 6, // Saturday
        '7': 0  // Sunday
    };
    const today = new Date();
    let nextAvailable = new Date();
    let dayOfWeek = dayOfWeekMap[dayNumber]; // Get the day of week as a number

    // Calculate the difference between today and the next occurrence of the class day
    let diff = dayOfWeek - today.getDay();
    if (diff <= 0) {
        diff += 7; // If it's already past or today, get the next week's day
    }
    
    // Set the next available date to the next occurrence of the class day
    nextAvailable.setDate(today.getDate() + diff);
    
    // Format the date as "Sunday, 7 January"
    return nextAvailable.toLocaleDateString('en-UK', { weekday: 'long', day: 'numeric', month: 'long' });
}

// Function to clean and extract course names
function extractCourseNames(classesStr) {
    let coursesArray = classesStr.split("]], [[");
    return coursesArray.map(course => {
        course = course.replace(/[\[\]]/g, '').trim();
        let parts = course.split("|");
        let courseName = parts.length > 1 ? parts[1].trim() : parts[0].trim();
        // Remove .md extension and any folder paths if present
        courseName = courseName.replace(/\.md/g, '').split('/').pop();
        return courseName;
    });
}
// Function to fetch class details from another file
async function fetchClassDetails(courseName) {
    const classData = this.app.plugins.plugins.dataview.api.page(`1.2 Classes/${courseName}`);
    if (classData && classData.Day && classData.Time) {
        // Fetch the "Subject" from the linked file's frontmatter
        const subject = classData.Subject ? classData.Subject : "Subject not found";

        // Strip the first two characters from "Day"
        let dayFormatted = classData.Day.substring(2);

        // Calculate the next available class date
        let startDate = getNextClassDate(classData.Day.substring(0, 1), dayFormatted);

        return `${subject}: ${classData.Time} ${dayFormatted}, starting on ${startDate}`;
    } else {
        return "Class time, day, or subject not found";
    }
}

// Get the 'Classes' value from the current file's inline metadata
const classesValue = tp.user.fields(tp).Classes;

// Use the function to extract course names
const courseNames = extractCourseNames(classesValue);

// Initialize the message variable to an empty string
let message = "";

// Loop through each course name, fetch details, and append to message
for (let courseName of courseNames) {
    const details = await fetchClassDetails(courseName);
    message += `- ${details}\n`;
}

// Output the final message
tR += message;
%>
Before your first session, please do the following things
1. Add a credit card to the study portal by clicking https://student.altitutor.com/my-account/payment-methods/
2. Download our app by searching "Altitutor" in the app store / play store
3. Come to the homework help session anytime between 1pm-4pm on Sunday <%*
// Function to calculate the next Sunday, or Sunday in one week's time if today is Sunday
function getNextSunday() {
    const today = new Date();
    let nextSunday = new Date();

    // Calculate the difference to the next Sunday (always at least 7 days away)
    let diff = 7 - today.getDay(); // Days until next Sunday

    // Set the date to the next Sunday
    nextSunday.setDate(today.getDate() + diff);

    // Format the date as "Sunday, 7 January"
    return nextSunday.toLocaleDateString('en-UK', { weekday: 'long', day: 'numeric', month: 'long' });
}

// Call the function and output the date of the next Sunday or the Sunday in one week's time if today is Sunday
tR += getNextSunday();
%> so we can catch you up on content

Please let us know if you have any questions by email (admin@altitutor.com) or text/phone call (0483 849 842). 

Kindly note that we have implemented a 24-hour policy for managing absences. If you are unable to attend a session, we kindly request that you inform us at least 24 hours in advance for circumstances that can be reasonably foreseen. We will aim to reschedule the missed session at a convenient time for you. In the event rescheduling is not feasible, we will credit your account accordingly.

Kind regards,

Altitutor Admin



```button
name Generate parent message
type append template
action MESSAGE - new parent message
```





<%*
// Function to replace the current YAML frontmatter content
function replaceYAML(newContent, app) {
    // Get the current active file
    const file = app.workspace.getActiveFile();
    
    // Read the content of the file
    let content = app.vault.read(file);
    
    // Define a regular expression to find YAML frontmatter
    const yamlRegex = /^---\n[\s\S]*?\n---/gm;

    // Wait for the content to be read
    content.then(data => {
        // Replace the current YAML frontmatter with the new content
        const newData = data.replace(yamlRegex, `---\n${newContent}\n---`);

        // Write the updated content back to the file
        app.vault.modify(file, newData);
    });
}

// Function to translate subject codes to names and determine SACE_or_IB
function translateSubjectsAndDetermineType(subjectsStr) {
    const subjectMap = {
        "15069": "SACE 12SPEC",
        "8553": "SACE 12METH",
        "9931": "SACE 12PHYS",
        "9837": "SACE 12CHEM",
        "9880": "SACE 12BIO",
        "15208": "SACE 11SPEC",
        "15154": "SACE 11METH",
        "21135": "SACE 11PHYS",
        "20921": "SACE 11CHEM",
        "21177": "SACE 11BIO",
        "21187": "SACE English Lit",
        "21185": "SACE English",
        "8709": "UCAT",
        "21189": "Medicine interview course",
        "21179": "PreSACE Maths",
        "21181": "PreSACE Science",
        "21183": "PreSACE English",
        "24994": "IB MATH AA",
        "24996": "IB MATH AI",
        "25000": "IB PHYS",
        "24998": "IB CHEM",
        "25002": "IB BIO",
        "25004": "IB ENG",
        // Add all other mappings here
    };

    let saceOrIb = '';
    const translatedSubjects = subjectsStr.split(',').map(code => {
        const subjectName = subjectMap[code.trim()];
        if (!saceOrIb) {
            if (subjectName.startsWith("SACE")) saceOrIb = 'SACE';
            else if (subjectName.startsWith("IB")) saceOrIb = 'IB';
            else if (subjectName.startsWith("PreSACE")) saceOrIb = 'PreSACE';
            // UCAT and Medicine interview course will leave saceOrIb as blank
        }
        return `  - ${subjectName}`;
    }).join('\n');

    return { translatedSubjects, saceOrIb };
}

// Prompt the user to paste something
const userInput = await tp.system.prompt("Paste your text here:");

// Replace double spaces with line breaks in user input
let formattedInput = userInput.split("  ").join("\n");

// Check for Subjects field and format it if present
const subjectsRegex = /Subjects:\s*([0-9,]+)/;
const match = formattedInput.match(subjectsRegex);
let saceOrIbValue = '';
if (match) {
    const subjectsStr = match[1];
    const { translatedSubjects, saceOrIb } = translateSubjectsAndDetermineType(subjectsStr);
    formattedInput = formattedInput.replace(subjectsRegex, `Subjects:\n${translatedSubjects}`);
    saceOrIbValue = saceOrIb;
}

// Insert the SACE_or_IB field
formattedInput = `SACE_or_IB: ${saceOrIbValue}\n${formattedInput}`;

// Replace the YAML metadata with the user's input
replaceYAML(formattedInput, this.app);

// Get the current active file
const file = this.app.workspace.getActiveFile();

// Delete the script itself
deleteScript(this.app, file);
%>




