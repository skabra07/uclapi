from django.core.management.base import BaseCommand

from workspaces.occupeye.cache import OccupeyeCache


class Command(BaseCommand):
    help = (
        'Feeds the OccupEye data into Redis so that response times are quicker'
    )

    def handle(self, *args, **options):
        print("Running Mini OccupEye Caching Operation")
        print("[+] Feeding Cache")
        cache = OccupeyeCache()
        cache.feed_cache(full=False)
        print("Done!")
