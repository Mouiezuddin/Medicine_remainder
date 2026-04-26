from django.core.management.base import BaseCommand
from medicines.models import Medicine


class Command(BaseCommand):
    help = 'Add 50 tablets to all existing medicines'

    def add_arguments(self, parser):
        parser.add_argument(
            '--quantity',
            type=int,
            default=50,
            help='Number of tablets to add (default: 50)'
        )

    def handle(self, *args, **options):
        quantity = options['quantity']
        medicines = Medicine.objects.all()
        
        if not medicines.exists():
            self.stdout.write(
                self.style.WARNING('No medicines found in the database.')
            )
            return
        
        updated_count = 0
        for medicine in medicines:
            medicine.quantity += quantity
            medicine.save()
            updated_count += 1
            self.stdout.write(
                f'Added {quantity} tablets to {medicine.name} '
                f'(Total: {medicine.quantity})'
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully added {quantity} tablets to {updated_count} medicines.'
            )
        )