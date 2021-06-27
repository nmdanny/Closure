from django.core.management import BaseCommand, CommandError
from django.core.management.base import CommandParser
from rest_api import huji_loader
from pathlib import Path
from typing import Any, Optional

class Command(BaseCommand):
    help = "Loads HUJI course and track data"

    def add_arguments(self, parser: CommandParser) -> None:

        mutex_group = parser.add_mutually_exclusive_group()
        mutex_group.add_argument("-f", "--from-zip-file", type=Path, metavar="PARSED_DATA.ZIP",
                            help="Path to .zip file containing data")

        mutex_group.add_argument("-u", "--from-zip-url", type=str, metavar="PARSED_DATA_URL",
                            help="URL to .zip file containing data")
    

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        print(options)
        if "from_zip_file" in options:
            huji_loader.load_from_zip(options['from_zip_file'])
        elif "from_zip_url" in options:
            huji_loader.load_from_internet(options['from_zip_url'])
        else:
            raise CommandError("Must specify either a file or a URL to the parsed data .zip")