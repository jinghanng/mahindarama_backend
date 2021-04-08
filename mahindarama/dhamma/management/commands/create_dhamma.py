import datetime
import random
from django.core.management.base import BaseCommand
from dhamma.models import Dhamma, Sangha, Location, Category, MediaType, Language

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

language = [
    'Pali',
    'English',
    'Chinese',
    'Thai',
    'Hindi',
    'Spanish',
    'French',
    'Italian'
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


def generate_record_date():
    year = random.randint(2020, 2021)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime.date(year, month, day)


def generate_media_types():
    index = random.randint(0, 2)
    return media_types[index]


def generate_duration():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    return datetime.time(hour, minute)    


def generate_language():
    index = random.randint(0, 7)
    return language[index]


def generate_sadhu():
    random_no = random.randint(1000, 3000)
    return random_no


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
                record_date = generate_record_date()
                media_type = generate_media_types()
                duration = generate_duration()
                language = generate_language()
                sadhu = generate_sadhu()

                dhamma = Dhamma(
                    title=title,
                    image=image,
                    record_date=record_date,
                    duration=duration,
                    sadhu=sadhu,
                )

                dhamma.save()

                _location = Location.objects.get_or_create(name=location)
                _category = Category.objects.get_or_create(name=category_name)
                _sangha = Sangha.objects.get_or_create(name=sangha_name)
                _mediatype = MediaType.objects.get_or_create(name=media_type)
                _language = Language.objects.get_or_create(name=language)

                dhamma.location.add(
                    Location.objects.get(name=location))
                dhamma.categories.add(
                    Category.objects.get(name=category_name))
                dhamma.sangha_name.add(
                    Sangha.objects.get(name=sangha_name))
                dhamma.media_type.add(
                    MediaType.objects.get(name=media_type))
                dhamma.language.add(
                    Language.objects.get(name=language))
                    

        self.stdout.write(self.style.SUCCESS('Dhamma imported successfully'))
