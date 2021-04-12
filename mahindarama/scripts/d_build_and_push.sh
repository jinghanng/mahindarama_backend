# host -> gcr.io/mahindaramatemple-310008/mahindarama

docker build -t mahindarama -f Dockerfile .

docker tag mahindarama gcr.io/mahindaramatemple-310008/mahindarama

docker push gcr.io/mahindaramatemple-310008/mahindarama