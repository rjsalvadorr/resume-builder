# entities

## Resume

| property | type | description |
| --- | --- | --- |
| subtitle | str | Title or tagline under name |
| contact_info | list | List of ContactItems |
| objective | str | Career objectives |
| skills_qualifications | list | List of strings representing main skill areas |
| work_experience | list | List of ExpEduItems |
| projects | list | List of ExpEduItems |
| education | list | List of ExpEduItems |
| about | str | More details about yourself |

## ContactItem

| property | type | description |
| --- | --- | --- |
| contact_type | str | Contact type (email/phone/website/linkedin/github) |
| contact_info | str | Actual info |

## ExpEduItem

| property | type | description |
| --- | --- | --- |
| org_name | str | Name of employer/school |
| org_location | str | Location of employer/school |
| start_date | datetime | Start date |
| end_date | datetime | End date |
| skills | list | List of strings describing skills that were gained |
| highlights | list | List of strings describing the role/program |
