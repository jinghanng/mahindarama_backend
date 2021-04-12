instance_id = 'mahindarama'
postgres username = 'postgres'
postgres_user_pw = 'D2nr7cbmL8Mn2IlO'

local_db username = 'dblocaluser'
local_db pw = 'D2nr7cbmL8Mn2IlO'

dbproduser username = 'dbproduser'
dbproduser pw = 'D2nr7cbmL8Mn2IlO'

db_connection_name = 'mahindaramatemple-310008:us-west1:mahindarama'

<project_id>:<region>:<instance-id>

/Users/jinghanng/MyDocuments/dev/2021mahindaramabackend/mahindarama/db/key.json

Push to GitHub repository
Sync cloud source repositories from GitHub
Run cloud build trigger
Check cloud run for link to deployed app

Future Considerations

1)Setup Git & Cloud Source Repository DONE

2)Create Trigger for Git Pushes to: DONE

Build Project's Container Image
Deploy Project
Add Service Account Permissions for Triggers to do Build/Deploy via Repo

3)Create a cloudbuild.yaml to: NOT NEEDED

Improve build speed via caching

4)Setup Django Staticfiles via Google Cloud Storage and django-storages TODO

5)Map a custom domain to a Cloud Run Service NOT NEEDED

6)Implement Sendgrid to have transactional emails in our project NOT NEEDED

7)Build pre-push (or build) end-to-end tests in Django to ensure valid deploys NOT NEEDED

8)Review the Django Deployment Checklist NOT NEEDED

9)Knative on Kubernetes -> Cloud Run <- App Engine NOT NEEDED
