import datetime
import random
from django.core.management.base import BaseCommand
from events.models import Event, Sangha, Location, Category, Event_Creator


locations = [
    'Mahindarama Temple',
    'Sariputta Community Centre',
    'Mahindarama Meditation Centre'
]

images = [
    'https://res.cloudinary.com/njhan/image/upload/c_crop,h_1950,w_2600/v1575251146/samples/landscapes/nature-mountains.jpg',
    'https://res.cloudinary.com/njhan/image/upload/v1575251142/samples/landscapes/beach-boat.jpg',
    'https://res.cloudinary.com/njhan/image/upload/c_crop,h_1950,w_2600/v1575251140/samples/landscapes/architecture-signs.jpg'
]

categories = [
    'Dhamma Talk',
    'Guided Meditation',
    'Sutta Study'
]

sangha = [
    'Buddha Gunhah',
    'Ajahn Brahm',
    'Ajahn Fa Le',
    'Ajahn Yiu',
    'Ajahn Brahmali',
    'Venerable Dhammaratana',
    'Venerable Indraratana',
    'Venerable Canda',
    'Ajahn Song Bun',
    'Ajahn Nissarano'
]

media_types = [
    'Article',
    'Video',
    'Audio'
]

publish_by = [
    'Blane Edward',
    'Roger Smith',
    'Cookie Yu',
    'Nellie Roche',
    'Milton Hawkins',
    'Tannie Hill',
    'Cherish More',
    'Frida Yamil'
]


def generate_location():
    index = random.randint(0, 2)
    return locations[index]


def generate_image():
    index = random.randint(0, 2)
    return images[index]


def generate_category_name():
    index = random.randint(0, 2)
    return categories[index]


def generate_sangha_name():
    index = random.randint(0, 9)
    return sangha[index]


def generate_media_types():
    index = random.randint(0, 2)
    return media_types[index]


def generate_start_date():
    year = random.randint(2020, 2021)
    month = random.randint(1, 6)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)


def generate_end_date():
    year = random.randint(2020, 2021)
    month = random.randint(7, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)


def generate_start_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime.time(hour, minute, second)


def generate_end_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime.time(hour, minute, second)


def generate_publish_date():
    year = random.randint(2020, 2021)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)


def generate_publish_by():
    index = random.randint(0, 7)
    return publish_by[index]


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', type=str, help='The txt file that contains the event titles.')

    def handle(self, *args, **kwargs):
        file_name = kwargs['file_name']
        with open(f'{file_name}.txt') as file:
            for row in file:
                title = row
                location = generate_location()
                image = generate_image()
                category_name = generate_category_name()
                sangha_name = generate_sangha_name()
                media_type = generate_media_types()
                start_date = generate_start_date()
                end_date = generate_end_date()
                start_time = generate_start_time()
                end_time = generate_end_time()
                publish_date = generate_publish_date()
                publish_by = generate_publish_by()

                publishBy = Event_Creator.objects.get_or_create(
                    name=publish_by)

                event = Event(
                    title=title,
                    image=image,
                    start_date=start_date,
                    end_date=end_date,
                    start_time=start_time,
                    end_time=end_time,
                    publish_date=publish_date,
                    publish_by=Event_Creator.objects.get(name=publish_by),
                )

                event.save()

                locate = Location.objects.get_or_create(name=location)
                category = Category.objects.get_or_create(name=category_name)
                sangha = Sangha.objects.get_or_create(name=sangha_name)

                event.location.add(
                    Location.objects.get(name=location))
                event.categories.add(
                    Category.objects.get(name=category_name))
                event.sangha_name.add(
                    Sangha.objects.get(name=sangha_name))

        self.stdout.write(self.style.SUCCESS('Event imported successfully'))
