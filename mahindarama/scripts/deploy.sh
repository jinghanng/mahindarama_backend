gcloud run deploy mahindarama \
--image gcr.io/mahindaramatemple-310008/mahindarama \
--platform managed \
--region us-west1 \
--allow-unauthenticated \
--project mahindaramatemple-310008 \
--service-account mahindarama-serverless@mahindaramatemple-310008.iam.gserviceaccount.com