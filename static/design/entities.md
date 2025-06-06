# entities

## Resume

| property | type | description |
| --- | --- | --- |
| name | str | Your name |
| subtitle | str | Title or tagline under name |
| contact_info | list | List of ContactItems |
| objective | str | Career objectives |
| skills_qualifications | list | List of strings representing main skill areas |
| work_experience | list | List of ExperienceItem |
| projects | list | List of ExperienceItem |
| education | list | List of ExperienceItem |
| about | str | More details about yourself |

## CoverLetter

| property | type | description |
| --- | --- | --- |
| ting | str | ... |

## ContactItem

| property | type | description |
| --- | --- | --- |
| contact_type | str | Contact type (email/phone/website/linkedin/github) |
| contact_info | str | Actual info |

## ExperienceItem

| property | type | description |
| --- | --- | --- |
| org_name | str | Name of employer/school |
| org_location | str | Location of employer/school |
| exp_type | str | Experience type (work/school/project) |
| exp_role | str | Job title or role |
| start_date | datetime | Start date |
| end_date | datetime | End date |
| skills | list | List of strings describing skills that were gained |
| highlights | list | List of strings describing the role/program |
| education_cred | str | Education credential (for `education` type) |
| project_name | str | Project name (for `project` type) |
